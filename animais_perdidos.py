# Sistema de Cadastro de Animais Perdidos e Encontrados
# Utiliza listas, dicionários, laços de repetição (while/for) e condicionais (if/elif/else)

animais = []

print("=" * 55)
print("🐾 SISTEMA DE ANIMAIS PERDIDOS E ENCONTRADOS 🐾")
print("=" * 55)

while True:
    print("\nEscolha uma opção:")
    print("1 - Cadastrar animal (Perdido ou Encontrado)")
    print("2 - Listar todos os animais")
    print("3 - Buscar por espécie ou bairro")
    print("4 - Verificar possíveis reencontros (Cruzar dados)")
    print("0 - Sair")

    opcao = input("\nDigite o número da opção: ")

    # 1. CADASTRAR
    if opcao == "1":
        print("\n--- NOVO CADASTRO ---")
        status = input("Status (Perdido / Encontrado): ").strip().capitalize()
        especie = input("Espécie (ex: Cachorro, Gato): ").strip().capitalize()
        porte = input("Porte (Pequeno / Médio / Grande): ").strip().capitalize()
        cor = input("Cor predominante: ").strip().capitalize()
        bairro = input("Bairro onde foi perdido/encontrado: ").strip().capitalize()
        data = input("Data (dd/mm/aaaa): ").strip()
        contato = input("Seu nome e telefone/WhatsApp: ").strip()

        registro = {
            "status": status,
            "especie": especie,
            "porte": porte,
            "cor": cor,
            "bairro": bairro,
            "data": data,
            "contato": contato
        }

        animais.append(registro)
        print("\n✅ Registro cadastrado com sucesso!")

    # 2. LISTAR TODOS
    elif opcao == "2":
        print("\n--- MURAL DE ANIMAIS ---")
        if len(animais) == 0:
            print("Nenhum animal cadastrado ainda.")
        else:
            for i, pet in enumerate(animais, start=1):
                print(f"{i}. [{pet['status']}] {pet['especie']} | Porte: {pet['porte']} | Cor: {pet['cor']} | Bairro: {pet['bairro']} | Data: {pet['data']} | Contato: {pet['contato']}")

    # 3. BUSCAR COM FILTRO
    elif opcao == "3":
        print("\n--- BUSCA FILTRADA ---")
        termo = input("Digite a espécie ou o bairro que deseja procurar: ").strip().capitalize()
        encontrados = 0

        for pet in animais:
            if termo in pet["especie"] or termo in pet["bairro"]:
                print(f"-> [{pet['status']}] {pet['especie']} ({pet['cor']}, {pet['porte']}) - Bairro: {pet['bairro']} | Contato: {pet['contato']}")
                encontrados += 1

        if encontrados == 0:
            print("Nenhum registro encontrado com esse filtro.")

    # 4. CRUZAR DADOS (PERDIDOS X ENCONTRADOS)
    elif opcao == "4":
        print("\n--- POSSÍVEIS COMBINAÇÕES ---")
        combinacoes = 0

        for p1 in animais:
            for p2 in animais:
                if p1["status"] == "Perdido" and p2["status"] == "Encontrado":
                    if p1["especie"] == p2["especie"] and p1["bairro"] == p2["bairro"]:
                        print(f"🔔 ALERTA DE REENCONTRO ({p1['especie']} no bairro {p1['bairro']}):")
                        print(f"   Perdido: Cor {p1['cor']}, Porte {p1['porte']} -> Contato: {p1['contato']}")
                        print(f"   Encontrado: Cor {p2['cor']}, Porte {p2['porte']} -> Contato: {p2['contato']}\n")
                        combinacoes += 1

        if combinacoes == 0:
            print("Nenhuma combinação encontrada no momento.")

    # 0. SAIR
    elif opcao == "0":
        print("\nEncerrando o sistema. Obrigado por ajudar os animais! 🐶🐱")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("\n❌ Opção inválida! Tente novamente.")
