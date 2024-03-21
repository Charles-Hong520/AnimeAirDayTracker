import { useState } from 'react';
import axios from 'axios';
import './styles/Form.css';
export default function Form({onSubmit}) {
	const [username, setUsername] = useState("");
	const [isLoading, setIsLoading] = useState(false);
	
	const handleSubmit = (event) => {
		event.preventDefault();
		let getURL = `https://chuckchuck.duckdns.org/AnimeAirDayTracker?username=${username}`;
		// let getURL = `http://localhost:8000/AnimeAirDayTracker?username=${username}`;
		setIsLoading(true);
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
			setIsLoading(false);
		// always executed
		});


	}
  
	return (
		<>
		<form onSubmit={handleSubmit}>
		<label>Enter your MyAnimeList username:</label>
		<input 
			type="text" 
			value={username}
			onChange={(e) => setUsername(e.target.value)}
		  />
		<input type="submit" />
	  	</form>
		{isLoading ? <div className='loading'>Loading...</div> : null}
		</>
		)
  }