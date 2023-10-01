from pytube import Playlist

def descargar_audio_playlist():
    # Solicitar la URL y el nombre de la carpeta
    url = input("Ingrese la URL de la lista de reproducción: ")
    carpeta = input("Ingrese el nombre de la carpeta donde guardar los archivos: ")
    
    # Crear la ruta de la carpeta si no existe
    output_path = f'descargas/{carpeta}'
    
    playlist = Playlist(url)
    
    # Inicializar contador y lista de errores
    contador = 1
    errores = []
    
    for video in playlist.videos:
        try:
            # Descargar sólo el audio
            audio_stream = video.streams.filter(only_audio=True).first()
            print(f"Descargando({contador}): {video.title}")
            audio_stream.download(output_path=output_path)
        except Exception as e:
            print(f"Error al descargar {video.title}: {e}")
            errores.append(video.title)
        
        contador += 1

    if errores:
        print("Los siguientes temas no se descargaron:")
        print(", ".join(errores))

# Iniciar la descarga
descargar_audio_playlist()
