import { React } from 'react';
import './css/App.css';
import Header from './components/Header';
import InputHandler from './components/InputHandler';
import BackgroundObjectContainer from './components/BackgroundObjectContainer';

const App = () => (
    <div className="App">
        <Header />
        <div className="centered">
            <h1 className="mt-3">Change mobility for good</h1>
            <div className="box mt-3 align-self-center">
                <h2>Shorten or decode your URL</h2>
                <b className="self-start">Paste your URL</b>
                <InputHandler />
            </div>
        </div>
        <BackgroundObjectContainer />
    </div>
);

export default App;
