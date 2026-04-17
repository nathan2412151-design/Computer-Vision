from deepface import DeepFace

registered_user = "database/usuario.jpg"
test_image = "test.jpg"

try:
    result = DeepFace.verify(
        img1_path=registered_user,
        img2_path=test_image
    )

    if result["verified"]:
        print("✅ Acceso concedido")
    else:
        print("❌ Acceso denegado")

except Exception as e:
    print("Error:", e)