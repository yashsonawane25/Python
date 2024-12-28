import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TotalConsumption = () => {
  const [totalConsumption, setTotalConsumption] = useState(0);

  useEffect(() => {
    axios.get('/api/total-consumption')
      .then(response => {
        setTotalConsumption(response.data.total);
      })
      .catch(error => {
        console.error('Error fetching the total consumption:', error);
      });
  }, []);

  return (
    <div className="container mt-5">
      <h1 className="text-center">Total Electricity Consumption</h1>
      <div className="alert alert-primary text-center">
        {totalConsumption} kWh
      </div>
    </div>
  );
};

export default TotalConsumption;
