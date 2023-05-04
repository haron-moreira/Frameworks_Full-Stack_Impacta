import React from 'react';
import { Link } from 'react-router-dom';

export default function Menu (){
    
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('login');

    const getInfoApi = async () => {
        const response = await fetch(
            "http://localhost:9000/status",
        ).then((response) => response.json());

        // console.log(response.data)
        alert(response.status_api)

    };
    
    return (
        <div style={{backgroundColor: '#d9d9d9', position: 'absolute', top: '0', display:'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', width: '100vw', height: '100vh'}} >
            <p>Usuário logado! </p>
            <button onClick={getInfoApi}>Verificar Status da Api</button>
            <p>Nome do usuário: {username}</p>
            <Link to="/"><button>Deslogar</button></Link>
        </div>
    );
}
