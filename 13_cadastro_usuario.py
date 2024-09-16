import difflib

class Usuario:
    #retirei "nacionalidade" da função contrutora.
    def __init__(self, nome, idade, cpf, especialidade):
        self.nome = nome
        self.idade = idade
        #self.nacionalidade = nacionalidade
        self.cpf = cpf
        self.especialidade = especialidade

    @classmethod
    def cadastrar_usuario(cls):
        while True:
            nome = input("Digite o nome do usuário: ").strip()
            print(f"Você digitou: {nome}")
            confirmacao = input("Está correto? (s/n): ").strip().lower()
            if confirmacao == 's':
                break
        
        while True:
            idade = int(input("Digite a idade do Usuario: "))
            print(f"Você digitou: {idade}")
            confirmacao = input("Está correto? (s/n): ").strip().lower()
            if confirmacao == 's':
                break


        while True:
            cpf = input("Digite o CPF do Usuario: ").strip()
            print(f"Você digitou: {cpf}")
            confirmacao = input("Está correto? (s/n): ").strip().lower()
            if confirmacao == 's':
                break

        #comentei esse bloco, poir retireu nacionalidade do cadastro.
        """while True:
            nacionalidade = input("Digite a nacionalidade do funcionário: ").strip()
            print(f"Você digitou: {nacionalidade}")
            confirmacao = input("Está correto? (s/n): ").strip().lower()
            if confirmacao == 's':
                break"""

        while True:
            especialidade = input("Digite a especialidade do Usuario: ").strip()
            print(f"Você digitou: {especialidade}")
            confirmacao = input("Está correto? (s/n): ").strip().lower()
            if confirmacao == 's':
                break
        
        return cls(nome, idade, cpf, especialidade)

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Especialidade: {self.especialidade})"


class Residencia:
    PAISES_VALIDOS = [
        "Afeganistão", "África do Sul", "Albânia", "Alemanha", "Andorra", "Angola", "Antígua e Barbuda", "Arábia Saudita",
        "Argélia", "Argentina", "Armênia", "Austrália", "Áustria", "Azerbaijão", "Bahamas", "Bangladesh", "Barbados", 
        "Bélgica", "Belize", "Benin", "Bolívia", "Bósnia e Herzegovina", "Botsuana", "Brasil", "Brunei", "Bulgária", 
        "Burkina Faso", "Burundi", "Butão", "Cabo Verde", "Camarões", "Canadá", "Catar", "Chade", "Chile", "China", 
        "Chipre", "Colômbia", "Comores", "Congo", "Coreia do Norte", "Coreia do Sul", "Costa do Marfim", "Costa Rica", 
        "Croácia", "Cuba", "Dinamarca", "Dominica", "Egito", "El Salvador", "Emirados Árabes Unidos", "Equador", 
        "Eritreia", "Eslováquia", "Eslovênia", "Espanha", "Estados Unidos", "Estônia", "Eswatini", "Etiópia", 
        "Filipinas", "Finlândia", "França", "Gabão", "Gâmbia", "Gana", "Geórgia", "Grécia", "Granada", "Guatemala", 
        "Guiana", "Guiné", "Guiné-Bissau", "Guiné Equatorial", "Haiti", "Holanda", "Honduras", "Hungria", "Iémen", 
        "Ilhas Fiji", "Indonésia", "Irã", "Iraque", "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Japão", 
        "Jordânia", "Kuwait", "Laos", "Lesoto", "Letônia", "Líbano", "Libéria", "Líbia", "Liechtenstein", "Lituânia", 
        "Luxemburgo", "Madagascar", "Malásia", "Malawi", "Maldivas", "Mali", "Malta", "Marrocos", "Maurícia"
    ]

    ESTADOS_VALIDOS = {
        "Brasil": [
            "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", 
            "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", 
            "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", 
            "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", 
            "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
        ],
        "Estados Unidos": [
            "Alabama", "Alasca", "Arizona", "Arkansas", "Califórnia", "Carolina do Norte", 
            "Carolina do Sul", "Colorado", "Connecticut", "Dakota do Norte", "Dakota do Sul", 
            "Delaware", "Flórida", "Geórgia", "Havaí", "Idaho", "Illinois", "Indiana", "Iowa", 
            "Kansas", "Kentucky", "Luisiana", "Maine", "Maryland", "Massachusetts", 
            "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", 
            "Nevada", "Nova Hampshire", "Nova Jersey", "Nova York", "Novo México", 
            "Ohio", "Oklahoma", "Oregon", "Pensilvânia", "Rhode Island", "Tennessee", 
            "Texas", "Utah", "Vermont", "Virgínia", "Virgínia Ocidental", "Washington", 
            "Wisconsin", "Wyoming"
        ],
        "Canadá": [
            "Alberta", "Colúmbia Britânica", "Ilha do Príncipe Eduardo", "Manitoba", 
            "Nova Brunswick", "Nova Escócia", "Nunavut", "Ontário", "Quebec", 
            "Saskatchewan", "Terra Nova e Labrador", "Territórios do Noroeste", "Yukon"
        ],
        "Alemanha": [
            "Baden-Württemberg", "Baviera", "Berlim", "Brandemburgo", "Bremen", 
            "Hamburgo", "Hesse", "Mecklemburgo-Pomerânia Ocidental", "Baixa Saxônia", 
            "Renânia do Norte-Vestfália", "Renânia-Palatinado", "Sarre", "Saxônia", 
            "Saxônia-Anhalt", "Schleswig-Holstein", "Turíngia"
        ],
        # Adicione mais países e estados aqui
    }

    def __init__(self, pais, estado):
        self.pais = pais
        self.estado = estado

    @classmethod
    def cadastrar_residencia(cls):
        while True:
            pais = input("Digite o país de residência: ").strip()
            paises_validos_lower = [p.lower() for p in cls.PAISES_VALIDOS]
            
            if pais.lower() in paises_validos_lower:
                pais_correto = next(p for p in cls.PAISES_VALIDOS if p.lower() == pais.lower())
                print(f"Você digitou o país: {pais_correto}")
                #Retirei a confirmação pois estava muito cansativo o cadastro dessa maneira
                """confirmacao = input("Está correto? (s/n): ").strip().lower()
                if confirmacao == 's':
                    break
                else:
                    print("Por favor, tente novamente.")"""
            else:
                sugestoes = difflib.get_close_matches(pais.lower(), paises_validos_lower, n=1, cutoff=0.8)
                if sugestoes:
                    pais_sugerido = next(p for p in cls.PAISES_VALIDOS if p.lower() == sugestoes[0])
                    confirmacao = input(f"Você quis dizer '{pais_sugerido}'? (s/n): ").strip().lower()
                    if confirmacao == 's':
                        pais_correto = pais_sugerido
                        print(f"Você digitou o país: {pais_correto}")
                        confirmacao = input("Está correto? (s/n): ").strip().lower()
                        if confirmacao == 's':
                            break
                        else:
                            print("Por favor, tente novamente.")
                    else:
                        print("Por favor, tente novamente.")
                else:
                    print(f"Erro: '{pais}' não é um país válido. Por favor, insira um país válido.")

        estado_correto = "Estado não informado"  # Define um valor padrão para `estado_correto`
        
        while True:
            if pais_correto in cls.ESTADOS_VALIDOS:
                estado = input(f"Digite o estado de residência em {pais_correto} (ou deixe em branco para pular): ").strip()
                
                if not estado:
                    print(f"Estado definido como: {estado_correto}")
                    break

                estados_validos_lower = [e.lower() for e in cls.ESTADOS_VALIDOS[pais_correto]]
                
                if estado.lower() in estados_validos_lower:
                    estado_correto = next(e for e in cls.ESTADOS_VALIDOS[pais_correto] if e.lower() == estado.lower())
                    print(f"Você digitou o estado: {estado_correto}")
                    confirmacao = input("Está correto? (s/n): ").strip().lower()
                    if confirmacao == 's':
                        break
                    else:
                        print("Por favor, tente novamente.")
                else:
                    sugestoes = difflib.get_close_matches(estado.lower(), estados_validos_lower, n=1, cutoff=0.8)
                    if sugestoes:
                        estado_sugerido = next(e for e in cls.ESTADOS_VALIDOS[pais_correto] if e.lower() == sugestoes[0])
                        confirmacao = input(f"Você quis dizer '{estado_sugerido}'? (s/n): ").strip().lower()
                        if confirmacao == 's':
                            estado_correto = estado_sugerido
                            print(f"Você digitou o estado: {estado_correto}")
                            confirmacao = input("Está correto? (s/n): ").strip().lower()
                            if confirmacao == 's':
                                break
                            else:
                                print("Por favor, tente novamente.")
                        else:
                            print("Por favor, tente novamente.")
                    else:
                        print(f"Erro: '{estado}' não é um estado válido em {pais_correto}. Por favor, insira um estado válido.")
            else:
                print(f"Erro: Não há estados disponíveis para o país '{pais_correto}'. Por favor, insira um país com estados válidos.")
        
        return cls(pais_correto, estado_correto)

    def __str__(self):
        return f"Residencia (País: {self.pais}, Estado: {self.estado})"

def main():
    usuario = Usuario.cadastrar_usuario()
    residencia = Residencia.cadastrar_residencia()

    print("\nDados Cadastrados:")
    print(usuario)
    print(residencia)

if __name__ == "__main__":
    main()
