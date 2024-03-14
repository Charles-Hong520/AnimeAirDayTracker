import { useState } from 'react'
import axios from 'axios';
export default function Form({onSubmit}) {
	const [username, setUsername] = useState("");
  
	const handleSubmit = (event) => {
		event.preventDefault();
		let getURL = `http://localhost:8000/anime?username=${username}`;
		axios.get(getURL)
		.then(function (response) {
		  // handle success

			console.log("success");
			console.log(response["data"]);
			onSubmit(response["data"]);
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