import React, { useEffect, useState } from 'react';
import axios from 'axios';

function HomePage() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/news/')
      .then(response => {
        setNews(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the transfer news!', error);
      });
  }, []);

  return (
    <div>
      <h1>Welcome to Football Transfer News</h1>
      <ul>
        {news.map(item => (
          <li key={item.id}>{item.headline}</li>
        ))}
      </ul>
    </div>
  );
}

export default HomePage;
