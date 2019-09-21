import React, { useState } from 'react';
import Locator from '../Locator/index.jsx';

const DEFAULT_GENDER = 'female';
const DEFAULT_ORIENTATION = 'front';

const LocatorPage = () => {
  const [orientation, setOrientation] = useState(DEFAULT_ORIENTATION);
  const [gender, setGender] = useState(DEFAULT_GENDER);
  const isFemale = gender === 'female';
  const isFront = orientation === 'front';

  const toggleFrontOrientation = () => {
    setOrientation(isFront ? 'back' : 'front');
  };

  const toggleLeft = () => {
    setOrientation('left');
  };

  const toggleRight = () => {
    setOrientation('right');
  };

  const toggleGender = () => {
    setGender(isFemale ? 'male' : 'female');
  }

  return (
    <div className="locatorPage">
      <button className="left floated ui primary button bodyori" onClick={toggleLeft}>
        Spin Left
      </button>
      <button className="right floated ui primary button bodyori" onClick={toggleRight}>
        Spin Right
      </button>
      <div className="locDiv">
        <Locator orientation={orientation} gender={gender} />
      </div>
      <button className="ui primary fluid button" onClick={toggleFrontOrientation}>
        Change to {orientation === 'front' ? 'back' : 'front'}
      </button>
      <br></br>
      <button className="ui primary fluid button" onClick={toggleGender}>
        Swap Avatar
      </button>
    </div>
  );
}

LocatorPage.propTypes = {};

LocatorPage.defaultProps = {};

export default LocatorPage;
