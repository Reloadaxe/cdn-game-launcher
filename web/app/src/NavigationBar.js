import React from 'react';
import { Nav, Navbar } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { Component } from 'react';
import styled from 'styled-components';
import packageJson from '../package.json';

const Styles = styled.div`
    .navbar-custom {
        background-color: transparent;
        height: 40px;
        font-weight: bold;
    }

    .navbar-brand, .navbar-nav .nav-link {
        color: black;
    }

    .brand-image {
        max-width: 64px;
        height: 30px;
    }
`;

export class NavigationBar extends Component {
    render() {
        return (
            <Styles>
                <Nav className="navbar-custom">
                    <Navbar.Brand as={Link} to={'/'} style={{ whiteSpace: "pre-line" }}>
                        <img
                            alt="Logo Game Manager"
                            src={packageJson["homepage"] + "/logo.png"}
                            className="d-inline-block align-top brand-image"
                        />
                        {` Game Manager `}
                    </Navbar.Brand>
                </Nav>
            </Styles>
        )
    }

}