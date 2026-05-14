import json

def verificar():
    try:
        # Abrimos tu archivo JSON
        with open('test_localization.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        idiomas_requeridos = ['es', 'en', 'fr', 'it']
        idiomas_presentes = data.get('translations', {}).keys()
        
        faltan = [lang for lang in idiomas_requeridos if lang not in idiomas_presentes]
        
        if not faltan:
            print("✅ Localización completa. Todos los idiomas están presentes.")
        else:
            print(f"⚠️ Alerta: Faltan los siguientes idiomas: {', '.join(faltan)}")
            
    except FileNotFoundError:
        print("❌ Error: No encontré el archivo 'test_localization.json'. Asegúrate de que el nombre sea exacto.")

# ESTA LÍNEA ES LA QUE HACE QUE EL SCRIPT FUNCIONE
if __name__ == "__main__":
    verificar()