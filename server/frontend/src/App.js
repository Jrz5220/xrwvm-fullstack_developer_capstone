import LoginPanel from "./components/Login/Login";
import { Routes, Route } from "react-router-dom";
import Register from "./components/Register/Register";
import Dealers from './components/Dealers/Dealers';

/* changed path='login' to path='register' and 
element={<LoginPanel />} to element={<Register />}
to render the register page when regsiter button is clicked. */
function App() {
  return (
    <Routes>
      <Route path="/register" element={<Register />} />
      <Route path="/dealers" element={<Dealers />} />
    </Routes>
  );
}
export default App;
