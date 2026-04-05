import pywhatkit as kit
import pyautogui
import time

# --- Configurações ---
numero = "+558182029414"
mensagem = "Oi?"
repeticoes = 500

try:
    print("Abrindo o chat do WhatsApp...")
    # Abre o chat mas NÃO envia ainda (espera 15 segundos para carregar)
    kit.sendwhatmsg_instantly(numero, mensagem, wait_time=5, tab_close=False)
    
    # Aguarda mais 1 segundo extra para garantir que o cursor está no campo de texto
    time.sleep(1)
    
    print(f"Iniciando envio de {repeticoes} mensagens...")
    
    for i in range(repeticoes):
        # Escreve a mensagem com maiúsculas corretas
        for char in mensagem:
            if char.isupper():
                pyautogui.keyDown('shift')
                pyautogui.press(char.lower())
                pyautogui.keyUp('shift')
            elif char == '?':
                pyautogui.keyDown('shift')
                pyautogui.press('/')
                pyautogui.keyUp('shift')
            else:
                pyautogui.press(char)
        
        # Aperta a tecla Enter
        pyautogui.press("enter")
        
        # Pequena pausa entre as mensagens para não travar o WhatsApp
        time.sleep(0.0) 
        
    print("Processo concluído!")

except Exception as e:
    print(f"Erro: {e}")

# Mantém o script aberto até o usuário pressionar Enter
input("Pressione Enter para fechar o programa...")