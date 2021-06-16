import React, { Component } from "react";
import styled from "styled-components";
import { Container, Card, Col, Row } from "react-bootstrap";

const Styles = styled.div`
    
`;

export default class Home extends Component {
    constructor(props) {
        super(props)
        this.state = {
            games: []
        }
    }

    loadGames = () => {
        fetch("/api/game/")
        .then(res => res.json())
        .then(data => {
            if (data.error) {
                console.log(data.error)
                return
            }
            this.setState({games: data.details})
        })
    }

    render() {
        return (
            <Styles>
                <Container>
                    <Row>
                        {this.state.games.map((game, index) => {
                            return (
                                <Col xs={3} key={index} onClick={() => window.location = "/api/game/" + game.name + "/"}>
                                    <Card style={{cursor: "pointer"}}>
                                        <Card.Header>
                                            <Card.Title>{game.name} - {game.valid ? "" : "in"}valide</Card.Title>
                                        </Card.Header>
                                    </Card>
                                </Col>
                            )
                        })}
                    </Row>
                </Container>
            </Styles>
        )
    }

    componentDidMount() {
        this.loadGames();
    }
}