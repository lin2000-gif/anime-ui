import { ChangeEvent, SyntheticEvent, useState } from "react";
import Button from 'react-bootstrap/Button';
import { useNavigate } from "react-router-dom";

function MainUiForm() {
  const [malId, setMalId] = useState("");

  const navigate = useNavigate();

  function handleTextareaChange(e: ChangeEvent<HTMLInputElement>): void {
    setMalId(e.target.value);
  }

  function handleClick(e: SyntheticEvent): void {
    e.preventDefault();
    navigate(`/recommendations/${malId}`)
  }

  return (
    <>
      <h1 className="glow">Welcome to AniCompass!</h1>
      <h2>Enter your MAL username</h2>
      <form>
        <label>
          <input name="myInput" value={malId} onChange={handleTextareaChange} />
          <br></br>
        </label>
        <Button type="submit" onClick={handleClick}>
          Submit
        </Button>
      </form>
    </>
  );
}

export default MainUiForm;
