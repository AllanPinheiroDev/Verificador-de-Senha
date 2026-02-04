# 🔐 Password Strength Checker

Projeto educacional desenvolvido para estudo de **Segurança da Informação**, com foco na análise da força de senhas e na verificação de vazamentos conhecidos, seguindo boas práticas recomendadas pela **OWASP**.

---

## 🎯 Objetivo
Avaliar a robustez de uma senha com base em critérios de segurança e verificar se ela já foi exposta em vazamentos públicos, utilizando a API **Have I Been Pwned** de forma segura (k-Anonymity).

---

## 🛠️ Tecnologias Utilizadas
- Python  
- Regex (Expressões Regulares)  
- Flask (interface web)  
- API Have I Been Pwned  
- HTML5 e CSS3  

---

## ⚙️ Funcionalidades
- Classificação da senha como **Fraca**, **Média** ou **Forte**
- Verificação de exposição da senha em vazamentos públicos
- Uso de hashing **SHA-1** sem envio da senha em texto puro
- Interface web simples e moderna
- Opção de exibir ou ocultar a senha (checkbox)

---

## 🔐 Conceitos de Segurança Aplicados
- Boas práticas de criação de senhas
- Hashing de credenciais
- k-Anonymity
- Vazamento de credenciais
- Uso ético de APIs públicas

---

## 🚀 Como Executar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/SEUUSUARIO/password-strength-checker.git
cd password-strength-checker
