import { Route, Routes } from "react-router-dom";
import "./App.css";
import MainUiForm from "./components/mainUiForm";
import Recommendations from "./components/recommendations";

function App() {
  return (
    <Routes> 
      <Route path="/" element={<MainUiForm />} />
      <Route path={`/recommendations/:malId`} element={<Recommendations/>} />
    </Routes>
  );
}

export default App;
