import React, { useEffect, useState } from 'react';
import axios from 'axios';

const HomePage = () => {
    const [news, setNews] = useState([]);
    const [clubs, setClubs] = useState([]);
    const [players, setPlayers] = useState([]);
    const [managers, setManagers] = useState([]);

    useEffect(() => {
        fetchItems();
    }, []);

    const fetchItems = async () => {
        try {
            const newsResponse = await axios.get('http://localhost:8000/api/news/');
            setNews(newsResponse.data);

            const clubsResponse = await axios.get('http://localhost:8000/api/clubs/');
            setClubs(clubsResponse.data);

            const playersResponse = await axios.get('http://localhost:8000/api/players/');
            setPlayers(playersResponse.data);

            const managersResponse = await axios.get('http://localhost:8000/api/managers/');
            setManagers(managersResponse.data);
        } catch (error) {
            console.error('There was an error fetching the items!', error);
        }
    };

    return (
        <div>
            <h1>Transfer News</h1>
            <ul>
                {news.map((item) => (
                    <li key={item.id}>{item.title}</li>
                ))}
            </ul>
            <h2>Clubs</h2>
            <ul>
                {clubs.map((club) => (
                    <li key={club.id}>{club.name}</li>
                ))}
            </ul>
            <h2>Players</h2>
            <ul>
                {players.map((player) => (
                    <li key={player.id}>{player.name}</li>
                ))}
            </ul>
            <h2>Managers</h2>
            <ul>
                {managers.map((manager) => (
                    <li key={manager.id}>{manager.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default HomePage;
