import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <Link className="navbar-brand" to="/">Transfer News</Link>
            <div className="collapse navbar-collapse">
                <ul className="navbar-nav ml-auto">
                    <li className="nav-item">
                        <Link className="nav-link" to="/accounts/login/">Login</Link>
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link" to="/accounts/signup/">Signup</Link>
                    </li>
                </ul>
            </div>
        </nav>
    );
};

export default Navbar;
