
import React, { useState } from 'react';
import { Button, Container, TextField, Typography, Card, Grid } from '@mui/material';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [jobs, setJobs] = useState([]);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('resume', file);
    await axios.post('http://localhost:8001/upload_resume', formData);
    const res = await axios.get('http://localhost:8003/recommendations');
    setJobs(res.data);
  };

  return (
    <Container>
      <Typography variant="h3" align="center" gutterBottom>Job Recommendation System</Typography>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <Button variant="contained" onClick={handleUpload}>Upload & Find Jobs</Button>

      <Grid container spacing={2} style={{ marginTop: 20 }}>
        {jobs.map((job, index) => (
          <Grid item xs={12} md={6} key={index}>
            <Card style={{ padding: 20 }}>
              <Typography variant="h6">{job.title}</Typography>
              <Typography>Company: {job.company}</Typography>
              <Typography>Skills: {job.skills.join(', ')}</Typography>
              <Typography>Location: {job.location}</Typography>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}

export default App;
