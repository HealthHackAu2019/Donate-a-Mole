import React, { useRef, useState } from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import Pointer from '../Pointer/index.jsx';
import './locator.css';
import MaleFront from '../Svg/MaleFront.svg';
import FemaleFront from '../Svg/FemaleFront.svg';
import MaleBack from '../Svg/MaleBack.svg';
import FemaleBack from '../Svg/FemaleBack.svg';

const Locator = ({ gender, isFront }) => {
  const parentEl = useRef(null);
  const [pointerX, setPointerX] = useState(0);
  const [pointerY, setPointerY] = useState(0);

  const handleClick = (e) => {
    const relX = e.nativeEvent.pageX - parentEl.current.offsetLeft;
    const relY = e.nativeEvent.pageY - parentEl.current.offsetTop;

    setPointerX(relX);
    setPointerY(relY);

    console.log('mole X: ', relX - (parentEl.current.offsetWidth / 2));
    console.log('mole Y: ', relY - (parentEl.current.offsetHeight / 2));
  };

  return (
    <div className="locator" onClick={handleClick} ref={parentEl}>
      <div className="locatorImage">
        {gender === 'female' && isFront && <FemaleFront />}
        {gender === 'female' && !isFront && <FemaleBack />}
        {gender === 'male' && isFront && <MaleFront />}
        {gender === 'male' && !isFront && <MaleBack />}
      </div>
      <Pointer style={{ top: pointerY, left: pointerX }}/>
    </div>
  );
}

Locator.propTypes = {
  gender: PropTypes.oneOf(['male', 'female']),
  isFront: PropTypes.bool,
};

Locator.defaultProps = {
  gender: 'female',
  isFront: false,
};

export default Locator;
