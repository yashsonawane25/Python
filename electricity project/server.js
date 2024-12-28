const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(cors());

// Replace with your MongoDB connection string
const mongoURI = 'mongodb://localhost:27017/electricityDB';

mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

const consumptionSchema = new mongoose.Schema({
  total: Number
});

const Consumption = mongoose.model('Consumption', consumptionSchema);

app.get('/api/total-consumption', async (req, res) => {
  try {
    const consumption = await Consumption.findOne({});
    res.json({ total: consumption ? consumption.total : 0 });
  } catch (err) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
