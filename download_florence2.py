from huggingface_hub import snapshot_download
import os
import sys

def download_florence2_model():
    # ComfyUI models dizinini bul
    try:
        # ComfyUI'nin folder_paths modülünü import et
        sys.path.append('.')
        import folder_paths
        
        # Model adı
        model_name = "thwri/CogFlorence-2.2-Large"
        
        # ComfyUI'nin models dizini altında LLM klasörü
        model_directory = os.path.join(folder_paths.models_dir, "LLM", "CogFlorence-2.2-Large")
        
        # Dizini oluştur
        os.makedirs(model_directory, exist_ok=True)
        
        print(f"Florence2 modeli indiriliyor: {model_name}")
        print(f"İndirme dizini: {model_directory}")
        
        try:
            # Modeli indir
            snapshot_download(
                repo_id=model_name,
                local_dir=model_directory,
                local_dir_use_symlinks=False
            )
            print("Model başarıyla indirildi!")
            
        except Exception as e:
            print(f"Model indirilirken bir hata oluştu: {str(e)}")
            
    except ImportError:
        print("Hata: ComfyUI folder_paths modülü bulunamadı. Script'i ComfyUI ana dizininde çalıştırdığınızdan emin olun.")
        sys.exit(1)

if __name__ == "__main__":
    download_florence2_model() 