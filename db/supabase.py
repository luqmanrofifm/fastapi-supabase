from settings import (
    SUPABASE_URL,
    SUPABASE_KEY,
)
from supabase import create_client, Client

supabase_url = SUPABASE_URL
supabase_key = SUPABASE_KEY

def get_supabase() -> Client:
    """
    Create a Supabase client instance.
    """
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        print(f"Supabase client created with URL: {supabase_url}")
        
        return supabase
    except Exception as e:
        raise Exception(f"Failed to create Supabase client: {str(e)}")