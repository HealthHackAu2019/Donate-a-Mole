import React, { useRef, useState } from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import Pointer from '../Pointer/index.jsx';
import './locator.css';
import MaleFront from '../Svg/MaleFront.svg';
import FemaleFront from '../Svg/FemaleFront.svg';
import MaleBack from '../Svg/MaleBack.svg';
import FemaleBack from '../Svg/FemaleBack.svg';
import MaleLeft from '../Svg/MaleLeft.svg';
import FemaleLeft from '../Svg/FemaleLeft.svg';
import MaleRight from '../Svg/MaleRight.svg';
import FemaleRight from '../Svg/FemaleRight.svg';

const Locator = ({ gender, orientation }) => {
  const parentEl = useRef(null);
  const [pointerX, setPointerX] = useState(0);
  const [pointerY, setPointerY] = useState(0);
  const [pointerD, setPointerD] = useState('none');

  const handleClick = (e) => {
    const relX = e.nativeEvent.pageX - parentEl.current.offsetLeft;
    const relY = e.nativeEvent.pageY - parentEl.current.offsetTop;

    setPointerX(relX);
    setPointerY(relY);
    setPointerD('block')

    console.log('mole X: ', relX - (parentEl.current.offsetWidth / 2));
    console.log('mole Y: ', relY - (parentEl.current.offsetHeight / 2));

    // move the origin of the coordinates to be relative to the center
    // of the body image.
    const bodyX = relX - (parentEl.current.offsetWidth / 2);
    const bodyY = relY - (parentEl.current.offsetHeight / 2);

    // console.log('mole X: ', bodyX);
    // console.log('mole Y: ', bodyY);

    const bodyLocationField = document.getElementById('body_location');
    const bodyImageField = document.getElementById('body_image');

    if (bodyLocationField) bodyLocationField.value = `${bodyX}, ${bodyY}`;
    if (bodyImageField) bodyImageField.value = `${gender}-${orientation}`;
  };

  return (
    <div className="locator" onClick={handleClick} ref={parentEl}>
      <div className="locatorImage">
        {gender === 'female' && orientation == 'front' && <FemaleFront />}
        {gender === 'female' && orientation == 'back' && <FemaleBack />}
        {gender === 'female' && orientation == 'left' && <FemaleLeft />}
        {gender === 'female' && orientation == 'right' && <FemaleRight />}
        {gender === 'male' && orientation == 'front' && <MaleFront />}
        {gender === 'male' && orientation == 'back' && <MaleBack />}
        {gender === 'male' && orientation == 'left' && <MaleLeft />}
        {gender === 'male' && orientation == 'right' && <MaleRight />}
      </div>
      <Pointer className="locatorPointer" style={{ display: pointerD, top: pointerY, left: pointerX }}/>
    </div>
  );
}

Locator.propTypes = {
  gender: PropTypes.oneOf(['male', 'female']),
  orientation: PropTypes.oneOf(['front', 'back', 'left', 'right']),
};

Locator.defaultProps = {
  gender: 'female',
  orientation: 'front',
};

export default Locator;
