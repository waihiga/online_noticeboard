import React from 'react'
import {connect} from 'react-redux';
import {Route, Redirect} from 'react-router-dom';

const EditorRoute = ({component: Component, auth, ...rest}) => (
    <Route {...rest}
           render={props => {
               if (auth.isLoading) {
                   return <h2>Loading....</h2>
               } else if (!auth.isAuthenticated) {
                   return <Redirect to="/login"/>
               } else if (auth.user.role === 'Administrator' || auth.user.role === 'HOD' || auth.user.role === 'student_leader' || parseInt(auth.user.id)===1) {
                   return <Component {...props} />
               } else {
                   return <Redirect to="/" />
               }

           }}/>
);

const mapStateToProps = ({auth}) => ({
    auth
});
export default connect(mapStateToProps)(EditorRoute);
