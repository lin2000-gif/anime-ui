import { useParams } from "react-router-dom"

function Recommendations() {

    const params = useParams()
    const malId = params.malId
    return (
            <h1>Helloooooo {malId}!</h1>
    )
}

export default Recommendations