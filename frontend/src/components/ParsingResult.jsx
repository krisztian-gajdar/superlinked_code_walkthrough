import React from 'react';
import PropTypes from 'prop-types';

const ParsingResult = ({ displayMessage, isError }) => (
    <div
        className="result-holder"
        style={{
            backgroundColor: isError ? '#DC2121' : '#14B106',
            visibility: displayMessage ? 'visible' : 'hidden',
        }}
    >
        <span>{displayMessage}</span>
    </div>
);

ParsingResult.propTypes = {
    displayMessage: PropTypes.string.isRequired,
    isError: PropTypes.bool.isRequired,
};

export default ParsingResult;
