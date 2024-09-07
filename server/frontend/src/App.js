import LoginPanel from "./components/Login/Login";
import { Routes, Route } from "react-router-dom";
import Register from "./components/Register/Register";

/* changed path='login' to path='register' and 
element={<LoginPanel />} to element={<Register />}
to render the register page when regsiter button is clicked. */
function App() {
  return (
    <Routes>
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}
export default App;
