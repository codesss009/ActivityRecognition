import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
    const [file, setFile] = useState(null);
    const [name, setName] = useState('');
    const [result, setResult] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleNameChange = (e) => {
        setName(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('file', file);
        formData.append('name', name);

        try {
            const response = await axios.post('http://localhost:8000/api/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setResult(response.data.predictions.join('\n'));
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} />
                <input type="text" value={name} onChange={handleNameChange} placeholder="Enter your name" />
                <button type="submit">Upload and Predict</button>
            </form>
            <div>
                <h3>Predictions:</h3>
                <pre>{result}</pre>
            </div>
        </div>
    );
};

export default FileUpload;
