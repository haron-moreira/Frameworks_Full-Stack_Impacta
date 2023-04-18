import React from 'react';
import { Link } from 'react-router-dom';

export default function Menu (){
    
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('login');
    
    return (
        <div style={{backgroundColor: '#d9d9d9', position: 'absolute', top: '0', display:'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', width: '100vw', height: '100vh'}} >
            <p>Usuário logado! </p>
            <p>Nome do usuário: {username}</p>
            <Link to="/"><button>Deslogar</button></Link>
        </div>
    );
}
