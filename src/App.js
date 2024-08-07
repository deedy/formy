import React, { useState, useEffect } from 'react';
import { JsonForms } from '@jsonforms/react';
import { materialRenderers, materialCells } from '@jsonforms/material-renderers';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { 
  CssBaseline, Container, Typography, TextField, Button, Paper, 
  Snackbar, CircularProgress, Box, AppBar, Toolbar
} from '@mui/material';
import { Alert } from '@mui/material';
import axios from 'axios';

// Create a dark theme
const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#90caf9',
    },
    secondary: {
      main: '#f48fb1',
    },
    background: {
      default: '#303030',
      paper: '#424242',
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    h4: {
      fontWeight: 600,
    },
    h5: {
      fontWeight: 500,
    },
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 8,
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 12,
        },
      },
    },
  },
});

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8080',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

function App() {
  const [description, setDescription] = useState('');
  const [formSchema, setFormSchema] = useState(null);
  const [formData, setFormData] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  useEffect(() => {
    testConnection();
  }, []);

  const testConnection = async () => {
    try {
      const response = await axiosInstance.get('/test');
      setSuccess('Connected to server successfully');
    } catch (error) {
      setError(`Error connecting to server: ${error.message}`);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setSuccess('');
    try {
      const response = await axiosInstance.post('/generate-form', { description });
      setFormSchema(JSON.parse(response.data.form_structure));
      setSuccess('Form generated successfully');
    } catch (error) {
      console.error('Error generating form:', error);
      setError(error.response?.data?.error || error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AppBar position="static" color="primary" elevation={0}>
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Formy
          </Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
        <Paper elevation={3} sx={{ p: 4, mb: 4 }}>
          <Typography variant="h4" gutterBottom>
            Generate Your Form
          </Typography>
          <form onSubmit={handleSubmit}>
            <TextField
              fullWidth
              label="Describe your form"
              variant="outlined"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              margin="normal"
              multiline
              rows={4}
            />
            <Box sx={{ mt: 2, position: 'relative' }}>
              <Button 
                type="submit" 
                variant="contained" 
                color="primary" 
                disabled={loading}
                fullWidth
              >
                Generate Form
              </Button>
              {loading && (
                <CircularProgress
                  size={24}
                  sx={{
                    position: 'absolute',
                    top: '50%',
                    left: '50%',
                    marginTop: '-12px',
                    marginLeft: '-12px',
                  }}
                />
              )}
            </Box>
          </form>
        </Paper>
        
        {formSchema && (
          <Paper elevation={3} sx={{ p: 4 }}>
            <Typography variant="h5" gutterBottom>
              Generated Form
            </Typography>
            <JsonForms
              schema={formSchema.schema}
              uischema={formSchema.uischema}
              data={formData}
              renderers={materialRenderers}
              cells={materialCells}
              onChange={({ data }) => setFormData(data)}
            />
          </Paper>
        )}
      </Container>
      <Snackbar open={!!error} autoHideDuration={6000} onClose={() => setError('')}>
        <Alert onClose={() => setError('')} severity="error" sx={{ width: '100%' }}>
          {error}
        </Alert>
      </Snackbar>
      <Snackbar open={!!success} autoHideDuration={6000} onClose={() => setSuccess('')}>
        <Alert onClose={() => setSuccess('')} severity="success" sx={{ width: '100%' }}>
          {success}
        </Alert>
      </Snackbar>
    </ThemeProvider>
  );
}

export default App;