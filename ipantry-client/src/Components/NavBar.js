import React from 'react';

class NavBar extends React.Component {
    render(){
        return (
            <nav className="navbar navbar-default">
                <div className="container-fluid">
                    <div>
                        <a className="navbar-brand" href="index.html">iPantry</a>
                    </div>
                    <div>
                        <ul className="nav navbar-nav navbar-right">
                            <li>
                                <a>
                                    <span className="glyphicon glyphicon-user"></span> Login
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        );
    }
}

export default NavBar;