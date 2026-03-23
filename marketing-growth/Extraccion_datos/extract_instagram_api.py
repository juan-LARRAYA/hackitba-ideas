import requests
import pandas as pd
import os

# --- CONFIGURACIÓN ---
# Debes obtener estos datos desde el portal de Facebook Developers
ACCESS_TOKEN = 'TU_USER_ACCESS_TOKEN'
INSTAGRAM_ACCOUNT_ID = 'TU_INSTAGRAM_BUSINESS_ACCOUNT_ID'
# ---------------------

def get_instagram_media_data():
    """
    Extrae datos de publicaciones usando la Instagram Graph API.
    """
    url = f"https://graph.facebook.com/v19.0/{INSTAGRAM_ACCOUNT_ID}/media"
    
    # Campos que queremos extraer de cada publicación
    fields = "id,caption,media_type,media_url,permalink,timestamp,like_count,comments_count"
    
    params = {
        'fields': fields,
        'access_token': ACCESS_TOKEN
    }

    try:
        print("Consultando la API de Instagram...")
        response = requests.get(url, params=params)
        data = response.json()

        if 'error' in data:
            print(f"Error de la API: {data['error']['message']}")
            return None

        posts = data.get('data', [])
        posts_list = []

        for post in posts:
            post_info = {
                "ID": post.get('id'),
                "Fecha": post.get('timestamp'),
                "Tipo": post.get('media_type'),
                "Likes": post.get('like_count'),
                "Comentarios": post.get('comments_count'),
                "Caption": post.get('caption', ''),
                "URL": post.get('permalink')
            }
            posts_list.append(post_info)

        # Crear DataFrame y guardar a CSV
        df = pd.DataFrame(posts_list)
        output_file = "instagram_api_data.csv"
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        print(f"Éxito! Se extrajeron {len(posts_list)} publicaciones.")
        print(f"Datos guardados en: {output_file}")
        return df

    except Exception as e:
        print(f"Error en la conexión: {e}")
        return None

if __name__ == "__main__":
    if ACCESS_TOKEN == 'TU_USER_ACCESS_TOKEN':
        print("POR FAVOR: Edita el script y coloca tu ACCESS_TOKEN e INSTAGRAM_ACCOUNT_ID.")
    else:
        get_instagram_media_data()
