import axios from 'axios';
import { useState } from 'react';

export default async function Test() {
    const [data, setData] = useState(null);

    try {
        const response = await axios.get('http://localhost:8000/api');
        console.log(response.data.results.drug)
        setData(response.data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }

    return (
        <div>
            <h1>Test</h1>
            {data && <p>{JSON.stringify(data)}</p>}
        </div>
    );
}