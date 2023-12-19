import { React } from 'react';
import bgField from '../img/bg-field.svg';
import bgCloud from '../img/bg-cloud.svg';

const BackgroundObjectContainer = () => (
    <>
        <img className="bg-field" src={bgField} alt="background object" />
        <img className="bg-cloud-left" src={bgCloud} alt="background object" />
        <img className="bg-cloud-right" src={bgCloud} alt="background object" />
    </>
);

export default BackgroundObjectContainer;
