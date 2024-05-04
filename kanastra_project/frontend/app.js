import React, { useState } from 'react';

function App() {
  // Estado para armazenar a resposta da solicitação
  const [response, setResponse] = useState(null);
  
  const handleButtonClick = () => {
    // Dados para serem enviados na solicitação POST
    const data = {
      "name": "Kanastra",
      "governmentId": "Olá, mundo!",
      "email": "example@kanastra.com.br",
      "debtAmount": "990.00",
      "debtDueDate": "26/01/2025"
    };

    // Envio da solicitação POST
    fetch('https://api.exemplo.com/endpoint', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Erro na requisição: ${response.statusText}`);
        }
        return response.json();  
      })
      .then((data) => {
        setResponse(data); 
      })
      .catch((error) => {
        console.error('Erro ao enviar a requisição:', error);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>Hello Kanastra!</p>
        <button onClick={handleButtonClick}>Enviar POST</button>
        {response && (
          <div>
            <p>Resposta do servidor:</p>
            <pre>{JSON.stringify(response, null, 2)}</pre>  
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
