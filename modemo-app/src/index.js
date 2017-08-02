import React from 'react';
import ReactDOM from 'react-dom';
import logo from './logo.png';
import './index.css';

class Header extends React.Component {
  render() {
    return (
      <div className="header">
          <img src={logo} className="modemo-logo" alt="logo" />
          <h2 className="modemo-title">Modemo</h2>
      </div>
    );
  }
}

ReactDOM.render(
  (<div>
    <Header />
  </div>),
  document.getElementById('root')
);