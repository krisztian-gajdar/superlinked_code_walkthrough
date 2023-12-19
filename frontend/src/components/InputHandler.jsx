import { React, useState } from 'react';
import axios from 'axios';
import UrlInput from './UrlInput';
import ParsingResult from './ParsingResult';
import UrlConvertButton from './UrlConvertButton';
import arrow from '../img/arrow.svg';

const InputHandler = () => {
    const [shortUrl, setShortUrl] = useState('');
    const [longUrl, setLongUrl] = useState('');
    const [actionName, setActionName] = useState('Shorten');
    const [displayMessage, setDisplayMessage] = useState('');
    const [isError, setError] = useState(false);
    const [rotation, setRotation] = useState(false);

    const handleUrlChange = (value, isLong) => {
        setLongUrl(isLong ? value : '');
        setShortUrl(isLong ? '' : value);
        setRotation(isLong ? 180 : 0);
        setDisplayMessage('');
        setActionName(isLong ? 'Shorten' : 'Decode');
    };

    const copyToClipBoard = (value) => {
        navigator.clipboard.writeText(value);
    };

    const handleClick = async () => {
        const isLong = longUrl.length;
        let req;
        if (isLong) {
            req = axios.post(`http://localhost:8080/encode_url?url=${longUrl}`);
        } else {
            req = axios.get(`http://localhost:8080/decode_url?url=${shortUrl}`);
        }
        req.then((res) => {
            const result = res.data.message;
            setError(false);
            handleUrlChange(result, !isLong);
            setDisplayMessage('Copied to clipboard');
            copyToClipBoard(result);
        }).catch((err) => {
            setDisplayMessage(err.response.data.detail);
            setError(true);
        });
    };

    return (
        <div className="inputContainer">
            <div className="mt-1">
                <UrlInput
                    handleUrlChange={handleUrlChange}
                    url={longUrl}
                    type="Long"
                />
            </div>
            <img
                className="arrow"
                src={arrow}
                alt="arrow"
                style={{
                    transform: `translateY(-2.4rem) rotate(${rotation}deg)`,
                }}
            />
            <div className="mb-1">
                <UrlInput
                    handleUrlChange={handleUrlChange}
                    url={shortUrl}
                    type="Short"
                />
            </div>
            <ParsingResult displayMessage={displayMessage} isError={isError} />
            <UrlConvertButton
                actionName={actionName}
                handleClick={handleClick}
            />
        </div>
    );
};

export default InputHandler;
