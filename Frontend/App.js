import React, { useState, useEffect, useRef } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import * as Location from 'expo-location';
import axios from 'axios';

const API_URL_CREATE = 'http://192.168.1.75:8000/api/productos/';  // Para la primera inserción
const API_URL_UPDATE = 'http://192.168.1.75:8000/api/ubicacion/actualizar/';  // Para actualizaciones

const App = () => {
    const [ubicacion, setUbicacion] = useState(null);
    const [suscripcion, setSuscripcion] = useState(null);
    const ubicacionCreadaRef = useRef(false);

    useEffect(() => {
        const obtenerPermiso = async () => {
            const { status } = await Location.requestForegroundPermissionsAsync();
            if (status !== 'granted') {
                alert('Permiso de ubicación denegado');
                return;
            }
        };
        obtenerPermiso();
    }, []);
    
    const enviarUbicacion = async (coords) => {
        try {
            const url = ubicacionCreadaRef.current ? API_URL_UPDATE : API_URL_CREATE;
            const metodo = ubicacionCreadaRef.current ? axios.put : axios.post;
    
            console.log(`Enviando ${ubicacionCreadaRef.current ? 'PUT' : 'POST'} a ${url}`);
    
            await metodo(url, {
                latitud: coords.latitude,
                longitud: coords.longitude
            });
    
            console.log("Ubicación enviada:", coords);
            ubicacionCreadaRef.current = true;
        } catch (error) {
            console.error('Error al enviar la ubicación:', error);
        }
    };

    const iniciarSeguimiento = async () => {
        const sub = await Location.watchPositionAsync(
            {
                accuracy: Location.Accuracy.High,
                timeInterval: 5000,  // Obtiene la ubicación cada 5 segundos
            },
            (location) => {
                setUbicacion(location.coords);
                enviarUbicacion(location.coords);
            }
        );
        setSuscripcion(sub);
    };

    const detenerSeguimiento = () => {
        if (suscripcion) {
            suscripcion.remove();
            setSuscripcion(null);
            console.log("Seguimiento de ubicación detenido.");
        }
    };

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Ubicación en Tiempo Real</Text>
            <Button title="Iniciar Seguimiento" onPress={iniciarSeguimiento} />
            <Button title="Detener Seguimiento" onPress={detenerSeguimiento} />
            {ubicacion && (
                <Text style={styles.text}>Lat: {ubicacion.latitude}, Lon: {ubicacion.longitude}</Text>
            )}
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 20,
    },
    text: {
        marginTop: 10,
        fontSize: 16,
    }
});

export default App;

/*
Documentacion Basica:

View: representa el componente mas basico para un elemento en pantalla
Text: Es para poder colocar texto en la pantalla
Image: 
Local-
const icon = require('./assets/icon.png');
<Image source={icon} style={{
        width:100, 
        height:100,
        resizeMode: 'center'
      }}/>
Remota - 
      <Image source={{ uri: 'https://image.api.playstation.com/cdn/UP0700/CUSA03388_00/v8JlD8KcQUtTqaLBmpFnj1ESRR5zMkLk.png'}}
      style={{
        width:100,
        height:100
      }}
      />

StatusBar - Es algo que no es de react native

Button: Es un boton que puede cambiar te estilo dependiendo de el dispositivo
<Button title='Pulsa aqui' onPress={() => alert('Te amo helena')}/>

TouchableHighlight: Es un boton mas personalizado
        <TouchableHighlight
        underlayColor={"red"}
          onPress={() => alert('Te amo mucho amor')}
          style={{ width:100,height:100,justifyContent:'center' }}>
            <Text style={{color:'white'}}>Prueva para el movil</Text>
        </TouchableHighlight>
        
Pressable:

*/