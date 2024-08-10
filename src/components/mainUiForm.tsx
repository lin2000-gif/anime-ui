import { ChangeEvent, SyntheticEvent, useState } from "react";

function MainUiForm() {
  const [malId, setMalId] = useState("");

  function handleTextareaChange(e: ChangeEvent<HTMLInputElement>): void {
    setMalId(e.target.value);
  }

  function handleClick(e: SyntheticEvent): void {
    e.preventDefault();
    console.log(e);
    console.log(malId);
  }

  return (
    <>
      <h1>Welcome to AniCompass!</h1>
      <h2>Enter your MAL username</h2>
      <form>
        <label>
          <input name="myInput" value={malId} onChange={handleTextareaChange} />
          <br></br>
        </label>
        <button type="submit" onClick={handleClick}>
          Submit
        </button>
      </form>
    </>
  );
}

export default MainUiForm;
