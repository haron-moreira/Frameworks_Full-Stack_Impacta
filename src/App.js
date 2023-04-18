import React from 'react';
import {Switch, Route, Link} from 'react-router-dom';

import Esqueci from './Esqueci';
import Menu from './Menu';


export default function App() {
   return (
       <>
     <header>
     </header>
     <main>
     <form method='get' action='/menu/' style={{display:'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', width: '100vw', height: '100vh'} }>
            <h1>Área de Login</h1>
            <label for='login'>Login</label>
            <input name='login' id='login' type='text' required></input><br />
            <label for='senha'>Senha</label>
            <input id='senha' type='password' required></input><br /><br />
            
            <button type='submit'>Acessar</button><br />
            <p><Link to="/esqueci_senha">Esqueci minha senha</Link></p>
        </form>
            
         <Switch>
           <Route path='/menu/' component= {Menu}/>
           <Route path='/esqueci_senha' component= {Esqueci}/>
         </Switch>
       </main></>
   );
}
