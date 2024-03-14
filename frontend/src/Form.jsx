import { useState } from 'react'
import axios from 'axios';
export default function Form() {
	const [username, setUsername] = useState("");
  
	const handleSubmit = (event) => {
		event.preventDefault();
		// let getstring = `http://localhost:8000/anime?username=${username}`;
		axios.get("http://localhost:8000/")
		.then(function (response) {
		  // handle success

		  console.log("success");
		  console.log(response);
		})
		.catch(function (error) {
		  // handle error
		  console.log("failed");
		  console.log(error);
		})
		.finally(function () {
		  // always executed
		});


	}
  
	return (
	  <form onSubmit={handleSubmit}>
		<label>Enter your name:
		  <input 
			type="text" 
			value={username}
			onChange={(e) => setUsername(e.target.value)}
		  />
		</label>
		<input type="submit" />
	  </form>
	)
  }