import { React } from 'react';
import logo from '../img/tier-logo.svg';

const Header = () => (
    <header className="main-header">
        <a href="index.html">
            <img src={logo} alt="logo" />
        </a>
    </header>
);

export default Header;
