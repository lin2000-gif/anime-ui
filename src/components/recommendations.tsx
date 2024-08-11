import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import GetListOfRecommendations from "./recommendationComponent"

function Recommendations() {
    const params = useParams()
    const malId = params.malId

    let [recommendations, setRecommendations] = useState(null)

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/recommendations/${malId}`)
        .then(response => response.json())
        .then(
            data => {
                console.log(data.recommendationList[0].english_title)
                setRecommendations(data.recommendationList)
            }
        )
        .catch(error => console.log("error", error))
    }, [])

    return (
        <>
            <h1>Helloooooo {malId}!</h1>
            {recommendations && <GetListOfRecommendations recommendations={recommendations}/>}
        </>
    )
}

export default Recommendations