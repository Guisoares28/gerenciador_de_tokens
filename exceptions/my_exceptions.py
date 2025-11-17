
class LoginInvalidoException(Exception):
    def __init__(self, mensagem="Login ou Senha inválidos"):
        super().__init__(mensagem)
        self.mensagem = mensagem

class UserNotFoundException(Exception):
    def __init__(self, mensagem="Usuário não encontrado"):
        super().__init__(mensagem)
        self.mensagem = mensagem

class TokenInvalidoException(Exception):
    def __init__(self, mensagem="Token inválido"):
        super().__init__(mensagem)
        self.mensagem = mensagem

class QuantidadeExcedidaException(Exception):
    def __init__(self, mensagem="Token inválido"):
        super().__init__(mensagem)
        self.mensagem = mensagem

class TokenNotFoundException(Exception):
    def __init__(self, mensagem="Token inválido"):
        super().__init__(mensagem)
        self.mensagem = mensagem