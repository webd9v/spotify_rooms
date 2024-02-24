import React from "react";
import HomePage from "./HomePage";
import RoomCreatePage from "./RoomCreatePage";
import RoomJoinPage from "./RoomJoinPage";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
} from "react-router-dom";

const App = () => {
    return (
        <Router>
            <div
                style={{
                    display: "flex",
                    justifyContent: "center",
                }}
            >
                <h1>Spotify App</h1>
            </div>
            <Routes>
                <Route path="/" element={<HomePage />}>
                    Home
                </Route>
                <Route path="/join" element={<RoomJoinPage />}>
                    Join Room
                </Route>
                <Route path="/create" element={<RoomCreatePage />}>
                    Create Room
                </Route>
                <Route></Route>
            </Routes>
        </Router>
    );
};
export default App;
