const express = require('express');
const axios = require('axios');
const _ = require('lodash');

const app = express();
const PORT = 3000;
const API_URL = 'http://localhost:5000/api';

app.use(express.json());
app.use(express.static('public'));

// Proxy endpoint to backend API
app.get('/api/users', async (req, res) => {
    try {
        const response = await axios.get(`${API_URL}/users`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch users' });
    }
});

app.get('/api/users/:id', async (req, res) => {
    try {
        // Validate that id is a positive integer to prevent SSRF
        const userId = parseInt(req.params.id, 10);
        if (isNaN(userId) || userId < 1) {
            return res.status(400).json({ error: 'Invalid user ID' });
        }
        const response = await axios.get(`${API_URL}/users/${userId}`);
        res.json(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).json({ 
            error: 'Failed to fetch user' 
        });
    }
});

app.post('/api/users', async (req, res) => {
    try {
        const response = await axios.post(`${API_URL}/users`, req.body);
        res.status(201).json(response.data);
    } catch (error) {
        res.status(400).json({ error: 'Failed to create user' });
    }
});

// Helper function using lodash
function processUsers(users) {
    return _.orderBy(users, ['name'], ['asc']);
}

app.listen(PORT, () => {
    console.log(`Frontend server running on port ${PORT}`);
});

module.exports = app;
