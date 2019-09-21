import React, { useState } from 'react';
import Locator from '../Locator/index.jsx';

const DEFAULT_GENDER = 'female';

const LocatorPage = () => {
  const [isFront, setIsFront] = useState(true);
  const [gender, setGender] = useState(DEFAULT_GENDER);
  const isFemale = gender === 'female';

  const toggleIsFront = () => {
    setIsFront(!isFront);
  };

  const toggleGender = () => {
    setGender(isFemale ? 'male' : 'female');
  }

  return (
    <div>
      <Locator isFront={isFront} gender={gender} />
      <button onClick={toggleIsFront}>
        Change to {isFront ? 'back' : 'front'}
      </button>
      <br/><br/>
      <button onClick={toggleGender}>
        Change to {gender === 'female' ? 'male' : 'female'}
      </button>
    </div>
  );
}

LocatorPage.propTypes = {};

LocatorPage.defaultProps = {};

export default LocatorPage;
