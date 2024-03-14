import Weekday from "./Weekday";
import './styles/Week.css'
function Week() {
	return (
		<div className="week">
			<Weekday dayName="Mon"></Weekday>
			<Weekday dayName="Tue"></Weekday>
			<Weekday dayName="Wed"></Weekday>
			<Weekday dayName="Thu"></Weekday>
			<Weekday dayName="Fri"></Weekday>
			<Weekday dayName="Sat"></Weekday>
			<Weekday dayName="Sun"></Weekday>
		</div>
	)
}

export default Week