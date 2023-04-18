import React from 'react';
import { Link } from 'react-router-dom';

export default function Esqueci (){
    
    return (
        <div style={{backgroundColor: '#d9d9d9', position: 'absolute', top: '0', display:'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', width: '100vw', height: '100vh'}} >
            <p>Parece que você esqueceu sua senha...</p>
            <p>O link para redefinição será enviado.</p>
            <Link to="/"><button>Entendi</button></Link>
        </div>
    );
}
