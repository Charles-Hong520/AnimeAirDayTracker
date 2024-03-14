import './styles/Weekday.css'

function Weekday({dayName, list}) {

	return (
		<>
		<div className='weekday'>
			{dayName}
			<ol>
				{list && list.map((item, index) => (
					<li key={index}>{item}</li>
				))}
    		</ol>
		</div>
		</>
	)
}


export default Weekday