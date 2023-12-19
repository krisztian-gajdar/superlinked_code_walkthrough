import { React } from 'react';
import PropTypes from 'prop-types';

const UrlInput = ({ handleUrlChange, url, type }) => (
    <input
        type="text"
        placeholder={`${type} URL`}
        value={url}
        onChange={(e) => handleUrlChange(e.target.value, type === 'Long')}
    />
);

UrlInput.propTypes = {
    handleUrlChange: PropTypes.func.isRequired,
    url: PropTypes.string.isRequired,
    type: PropTypes.string.isRequired,
};

export default UrlInput;
