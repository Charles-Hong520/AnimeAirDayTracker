import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import ReactDOM from 'react-dom/client';
import Week from './Week.jsx'
import Form from './Form.jsx'
function App() {
  const [formData, setFormData] = useState(null)

  const handleFormSubmit = (data) => {
    setFormData(data);
    console.log("setformdata func called");
  };

  return (
    <>
      <Form onSubmit={handleFormSubmit}/>
      <Week formData={formData}/>
    </>
  )
}

export default App
