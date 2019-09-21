import React from 'react';
import ReactDOM from 'react-dom';
import LocatorPage from './components/LocatorPage/index.jsx';

class App extends React.Component{
    render(){
        return(
            <LocatorPage />
        )
    }
}

ReactDOM.render(<App />, document.getElementById('donateRoot'))
