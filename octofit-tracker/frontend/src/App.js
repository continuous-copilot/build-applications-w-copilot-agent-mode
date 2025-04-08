import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">OctoFit Tracker</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Features</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Pricing</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container mt-4">
        <h1 className="display-4 text-center">Welcome to OctoFit Tracker</h1>
        <p className="lead text-center">Track your fitness activities and compete with others!</p>

        <div className="card mt-4">
          <div className="card-body">
            <h5 className="card-title">Get Started</h5>
            <p className="card-text">Sign up or log in to start tracking your fitness journey.</p>
            <a href="#" className="btn btn-primary">Sign Up</a>
            <a href="#" className="btn btn-secondary ms-2">Log In</a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
