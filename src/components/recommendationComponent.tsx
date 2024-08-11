interface RecommendationProps {
    recommendations: any[]
}

function GetListOfRecommendations(props: RecommendationProps) {
    return (
        <ul>
            {props.recommendations.map((recommendation) => (
          <li key={recommendation.malId}>{recommendation.english_title}</li>
        ))}
        </ul>
    )
}

export default GetListOfRecommendations