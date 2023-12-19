import React from 'react';
import PropTypes from 'prop-types';

const UrlConvertButton = ({ actionName, handleClick }) =>
    actionName && (
        <input
            type="button"
            value={`${actionName} and copy URL`}
            onClick={handleClick}
        />
    );

UrlConvertButton.propTypes = {
    actionName: PropTypes.string.isRequired,
    handleClick: PropTypes.func.isRequired,
};

export default UrlConvertButton;
