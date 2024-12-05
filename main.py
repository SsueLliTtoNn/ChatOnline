# ChatONline
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem


import flet as ft

def main(pagina):
    texto = ft.Text('ChatONline')

    chat = ft.Column() # Chat ira aparecer as mensagens, uma em baixo da outra

    nome_usuario = ft.TextField(label='Escreva seu nome')

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem['tipo']
        if tipo == 'mesagem':
            texto_mensagem = mensagem['texto']
            usuario_mensagem = mensagem['usuario']
            # adicionar a mensagem do chat
            chat.controls.append(ft.Text(f'{usuario_mensagem}: {texto_mensagem}'))
        else:
            usuario_mensagem = mensagem['usuario']
            chat.controls.append(ft.Text(f'{usuario_mensagem} entrou no chat'),
                                 size=12, italic=True, color=ft.colors.ORANGE_500)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        pagina.pubsub.send_all({'texto': campo_mensagem.value, 'usuario': nome_usuario.value,
                                'tipo': 'mensagem'})
        # limpar o campo de mensagem
        campo_mensagem.value = '' 
        pagina.update()

    campo_mensagem = ft.TextField(label='Digite uma mensagem', on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)

    def entrar_popup(evento):
        pagina.pubsub.send_all({'usuario': nome_usuario.value, 'tipo': 'entrada'})
        # adicionar o chat
        pagina.add(chat)
        # fechar o popup
        popup.open = False
        # remover o botao iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # Criar campo de mensagem do usuario
        # Criar o botao de enviar mensagem do usuario
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))  # ft.Row = Cria uma linha
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text('Bem vindo ao ChatONline'),
        content=nome_usuario,
        actions=[ft.ElevatedButton('Entrar', on_click=entrar_popup)],
        )

    def entrar_chat(evento):
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=entrar_chat)
    
    pagina.overlay.append(popup) # Esse overlay.append e da função ENTRAR_CHAT 

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8000)