import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './Home';
import { Layout } from './Layout';
import { NavigationBar } from './NavigationBar';
import { NotificationContainer } from 'react-notifications';

class App extends Component {
    render() {
        return (
            <React.Fragment>
                <Router basename={"/"}>
                    <NavigationBar/>
                    <Layout>
                        <Switch>
                            <Route exact path="/" render={() => {return(<Home />)}} />
                        </Switch>
                    </Layout>
                    <NotificationContainer/>
                </Router>
            </React.Fragment>
        );
    }
}

export default App;
