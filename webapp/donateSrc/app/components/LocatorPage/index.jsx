import React, { useState } from 'react';
import Locator from '../Locator/index.jsx';

const DEFAULT_GENDER = 'female';
const ORIENTATIONS = ['front', 'right', 'back', 'left'];

const LocatorPage = () => {
  const [orientation, setOrientation] = useState(0);
  const [gender, setGender] = useState(DEFAULT_GENDER);
  const isFemale = gender === 'female';
  const isFront = orientation === 'front';

  const nextOrientation = () => {
    if (orientation === ORIENTATIONS.length - 1) {
      setOrientation(0);
    } else {
      setOrientation(orientation + 1);
    }
  }

  const prevOrientation = () => {
    if (orientation === 0) {
      setOrientation(ORIENTATIONS.length - 1);
    } else {
      setOrientation(orientation - 1);
    }
  }

  const toggleGender = () => {
    setGender(isFemale ? 'male' : 'female');
  }

  return (
    <div>
      <div className="locatorFlex">
        <button className="ui primary button bodyori" onClick={prevOrientation}>
          Spin Left
        </button>
        <div className="locDiv">
          <Locator orientation={ORIENTATIONS[orientation]} gender={gender} />
        </div>
        <button className="ui primary button bodyori" onClick={nextOrientation}>
          Spin Right
        </button>
      </div>
      <br></br>
      <button className="ui primary fluid button" onClick={toggleGender}>
        Swap Gender
      </button>
    </div>
  );
}

LocatorPage.propTypes = {};

LocatorPage.defaultProps = {};

export default LocatorPage;
