import Weekday from "./Weekday";
import './styles/Week.css'
function Week({formData}) {
	const Weekdays = [];
	for (let i = 0; i < 7; i++) {
		Weekdays.push(<Weekday key={i} dayName={i} list={formData!=null && formData[i]}/>);
	}
	return <div className="week">{Weekdays}</div>;


}

export default Week