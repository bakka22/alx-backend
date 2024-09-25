import express from 'express';
import redis from 'ioredis';
import { promisify } from 'util';

const client = redis.createClient();

const listProducts = [
  {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {id: 4, name: 'Suitcase 1050', price: 550, stock: 5},];

function getItemById(id) {
  for (const item of listProducts) {
    if (item.id == id) {
      return item;
    }
  }
  return null;
}
//---------------redis----------------
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

function reserveStockById (itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById (itemId) {
  const getAsync = promisify(client.get).bind(client);
  const value = await getAsync(itemId);
  return value;
}

for (const item of listProducts) {
  reserveStockById(item.id, item.stock);
}
//------------------express-----------------

const app = express();
const port = 1245;

app.use(express.json());

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId);
  if (item === null) {
    return res.json({'status': 'Product not found'});
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  const payload = {itemId: item.id, itemName: item.name,
                   price: item.price,
	           initialAvailableQuantity: item.stock,
                   currentQuantity: currentStock,};
  return res.json(payload);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(itemId);
  if (item === null) {
    return res.json({'status': 'Product not found'});
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === '0') {
    return res.json({'status': 'Not enough stock available',
                     'itemId': item.id});
  }
  reserveStockById(item.id, currentStock - 1);
  return res.json({'status': 'Reservation confirmed', 'itemId': item.id});
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
