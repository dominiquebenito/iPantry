import React from 'react';
import Login from './Login';

class NavBar extends React.Component {
  render() {
    let isLoggedIn;
    if (false) {
      isLoggedIn = (
        <ul className="nav navbar-nav navbar-right">
          <li><a><span className="glyphicon glyphicon-shopping-cart"></span> Pantry</a></li>
          <li><a><span className="glyphicon glyphicon-user"></span> Logout</a></li>
        </ul>
      );
    } else {
      isLoggedIn = <Login />;
    }

    return (
      <nav className="navbar navbar-default">
        <div className="container-fluid">
          <div>
            <a className="navbar-brand" href="index.html">iPantry</a>
          </div>
          <div>
            { isLoggedIn }
          </div>
        </div>
      </nav>
    );
  }
}

export default NavBar;