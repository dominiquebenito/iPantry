import React from 'react';
import { Modal, ModalBody, ModalFooter } from 'react-modal-bootstrap';

import '../Styles/Login.css';

class Login extends React.Component {
  constructor() {
    super();

    this.state = {
      showModal: false
    };

    this.toggleShowModal = this.toggleShowModal.bind(this);
  }

  toggleShowModal() {
    this.setState({ showModal: !this.state.showModal });
  }

  render() {
    return (
      <div>
        <ul className="nav navbar-nav navbar-right">
          <li >
            <a onClick={ this.toggleShowModal }><span className="glyphicon glyphicon-user"></span> Login</a>
          </li>
        </ul>
        <Modal isOpen={ this.state.showModal } >
          <ModalBody>
            <div className="avatar">
              <img src="resources/login_avatar.png" alt="Avatar" className="avatar" />
            </div>

            <div>
              <input type="text" placeholder="Enter Username" name="uname" required />
              <input type="password" placeholder="Enter Password" name="psw" required />
              <button className="btn btn-success login" type="submit">Login</button>
            </div>
          </ModalBody>
          <ModalFooter>
            <button className='btn btn-default'> SignUp </button>
            <button className='btn btn-danger' onClick={ this.toggleShowModal }> Close </button>
          </ModalFooter>
        </Modal>
      </div>
    );
  }
}

export default Login;