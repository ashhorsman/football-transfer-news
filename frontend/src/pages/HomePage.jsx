import React, { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

const HomePage = () => {
    const [news, setNews] = useState([]);
    const [error, setError] = useState(null);
    const [nextPage, setNextPage] = useState(null);
    const [searchQuery, setSearchQuery] = useState('');

    useEffect(() => {
        fetchNews('http://localhost:8000/api/news/');
    }, []);

    const fetchNews = (url) => {
        axios.get(url)
            .then(response => {
                console.log('API Response:', response);
                const results = response.data.results;
                if (Array.isArray(results)) {
                    setNews(results);
                    setNextPage(response.data.next);
                } else {
                    setError('Unexpected API response format');
                }
            })
            .catch(error => {
                console.error("There was an error fetching the transfer news!", error);
                setError(error.message);
            });
    };

    const loadMore = () => {
        if (nextPage) {
            fetchNews(nextPage);
        }
    };

    const handleSearch = (event) => {
        event.preventDefault();
        const query = searchQuery.trim();
        if (query) {
            fetchNews(`http://localhost:8000/api/news/?search=${query}`);
        } else {
            fetchNews('http://localhost:8000/api/news/');
        }
    };

    if (error) {
        return <div className="alert alert-danger">There was an error fetching the transfer news! {error}</div>;
    }

    return (
        <div className="container">
            <h1 className="my-4">Latest Transfer News</h1>
            <form onSubmit={handleSearch} className="mb-4">
                <div className="input-group">
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Search for news..."
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                    />
                    <button className="btn btn-primary" type="submit">Search</button>
                </div>
            </form>
            <div className="row">
                {news.map(item => (
                    <div key={item.id} className="col-md-6 mb-4">
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">{item.headline}</h5>
                                <p className="card-text">{item.content}</p>
                                <p className="card-text"><small className="text-muted">Published at: {new Date(item.published_at).toLocaleString()}</small></p>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
            {nextPage && <button className="btn btn-primary my-4" onClick={loadMore}>Load More</button>}
        </div>
    );
};

export default HomePage;
