# Implementação de uma arquitetura de nuvem utilizando a AWS.

### Matheus Castellucci

## Descrição do Projeto

O projeto consiste na criação de uma arquitetura de nuvem utilizando AWS. A arquitetura inclui uma aplicação web que será executada em uma instância EC2, que estará dentro de um Auto Scaling Group (ASG) e um Application Load Balancer (ALB) para distribuir a carga entre as instâncias EC2. Além disso, temos uma aplicação simples para comprovar o funcionamento do DynamoDB, que é um banco de dados NoSQL totalmente gerenciado pela AWS.

## Arquitetura da Solução
Os componentes principais da arquitetura da solução são:

1. **EC2**: A instância EC2 é uma máquina virtual na nuvem da AWS que será responsável por executar a aplicação web. Ela estará dentro de um Auto Scaling Group (ASG) para garantir alta disponibilidade e escalabilidade automática.

2. **Auto Scaling Group (ASG)**: O Auto Scaling Group é um grupo de instâncias EC2 que podem ser gerenciadas como uma unidade lógica para fins de dimensionamento automático e aplicação de políticas. Ele garante que o número especificado de instâncias do EC2 esteja sempre em execução.

3. **CloudWatch**: O Amazon CloudWatch é um serviço de monitoramento e observabilidade da AWS para recursos em nuvem e aplicativos executados na AWS. Ele será utilizado para monitorar o status do ASG e das instâncias EC2, além de criar novas instâncias automaticamente quando o uso da CPU ultrapassar um determinado limite.


<p align="center"><b style="font-size: 24px;"><u>Topologia da solução</u></b></p>
<p align="center">
  <img src="imgs\cloud_roteiro.drawio.png" alt="Topologia"/>
  <p align="center"><style="font-size: 14px;">Algumas imagens foram retiradas do site da AWS (Fonte: https://aws.amazon.com/pt/elasticloadbalancing/ )</p>
</p>


<p align="center"><b style="font-size: 24px;"><u>Diagrama da Arquitetura AWS</u></b></p>
<p align="center">
  <img src="imgs\application-composer-template.yaml.png" alt="Topologia"/>
  <p align="center"><style="font-size: 14px;">Diagrama feito com uma das ferramentas disponibilizadas pela AWS(https://sa-east-1.console.aws.amazon.com/composer/canvas?mode=new&region=sa-east-1)</p>
</p>


## Tecnologias usadas

### AWS
* A Amazon Web Services (AWS) é uma plataforma de computação em nuvem oferecida pela Amazon.com, composta por diversos serviços de computação. Esses serviços são disponibilizados em várias regiões geográficas ao redor do mundo.

### AWS CLI
* O AWS Command Line Interface (AWS CLI) é uma ferramenta unificada que permite gerenciar os serviços da Amazon Web Services (AWS) por meio de comandos de linha de comando. Com o AWS CLI, é possível controlar vários serviços da AWS e automatizar tarefas, facilitando a interação com a plataforma de computação em nuvem da AWS.

### AWS EC2
* O Amazon Elastic Compute Cloud (Amazon EC2) é um serviço de computação em nuvem que oferece capacidade de computação redimensionável na nuvem. Ele permite que os usuários executem virtualmente qualquer tipo de aplicativo em servidores virtuais, conhecidos como instâncias EC2, proporcionando escalabilidade e flexibilidade para as cargas de trabalho.

### AWS ALB
* O Application Load Balancer (ALB) da AWS é um balanceador de carga gerenciado projetado para aplicativos HTTP e HTTPS. Ele opera na camada 7 do modelo OSI, roteando o tráfego de entrada para diferentes destinos, como instâncias do Amazon EC2, com base em regras definidas pelo usuário. O ALB também oferece recursos avançados, como "Health Checks" para verificar a integridade das instâncias e escalabilidade automática.

### AWS ASG
* O Auto Scaling Group (ASG) da AWS é um grupo de instâncias do Amazon EC2 que podem ser gerenciadas como uma única unidade para fins de dimensionamento automático e aplicação de políticas. O ASG garante que o número especificado de instâncias EC2 esteja sempre em execução, ajustando automaticamente a capacidade de acordo com a demanda, o que ajuda a garantir a disponibilidade e a otimizar os custos.

### AWS CloudWatch
* O Amazon CloudWatch é um serviço de monitoramento e observabilidade da AWS para recursos em nuvem e aplicativos executados na AWS. Ele permite coletar e rastrear métricas, monitorar arquivos de log e definir alarmes. Neste projeto, o CloudWatch foi utilizado para monitorar o status do ASG e das instâncias EC2. Além disso, o CloudWatch também foi configurado para criar novas instâncias automaticamente quando o uso da CPU ultrapassa 70%.

### AWS DynamoDB
* O Amazon DynamoDB é um serviço de banco de dados NoSQL totalmente gerenciado que oferece desempenho rápido e previsível com escalabilidade contínua. O DynamoDB é um banco de dados sem servidor, o que significa que não há servidores para gerenciar, provisionar ou manter, nem software para instalar, manter ou operar.

### AWS IAM
* O AWS Identity and Access Management (IAM) é um serviço da AWS que ajuda a controlar o acesso a recursos da AWS. Ele permite que você gerencie usuários e grupos de usuários e conceda permissões para permitir ou negar o acesso a recursos da AWS.

### AWS VPC
* O Amazon Virtual Private Cloud (Amazon VPC) permite que você crie uma rede virtual na AWS sem a necessidade de VPN, hardware ou datacenter físico. Você pode controlar sua própria rede virtual, incluindo a seleção do intervalo de endereços IP, criação de sub-redes e configuração de tabelas de roteamento e gateways de rede.


## Pré-requisitos

Para executar o projeto, é necessário ter o AWS CLI instalado. Para instalar o AWS CLI, siga as instruções no site oficial: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html.

Após a instalação do AWS CLI, configure-o com as credenciais de acesso da sua conta AWS usando o comando abaixo e siga as instruções:

```bash
aws configure
```

## Execução do Projeto

Com tudo configurado, acesse o serviço de CloudFormation da AWS e crie um novo stack. Selecione o arquivo .yaml presente na pasta raiz do projeto e siga as instruções para utilizar o template de criação da arquitetura.

### Criação do Stack

```bash
chmod +x criar_stack.sh
./criar_stack.sh
```
Com esses 2 comandos é possível deixar o script executável, e executar o script que cria a stack.

Após alguns minutos a stack estará criada e será possível acessar a aplicação através do link que será gerado no output da stack.

### Atualização da Stack

```bash
chmod +x atualizar_stack.sh
./atualizar_stack.sh
```
Esse comando atualiza a aplicação, caso seja necessário. Para usar esse comando é necessário que a stack já tenha sido criada. 

O comando também só funcionará se houver mudanças no .yaml, caso contrário, não haverá atualização.

### Exclusão da Stack

```bash
chmod +x destruir_stack.sh
./destruir_stack.sh
```
Esse comando exclui a stack criada. Para usar esse comando é necessário que a stack já tenha sido criada.

### Obtenção do DNS

```bash
chmod +x dns_finder.sh
./dns_finder.sh
```
Esse comando retorna o DNS do ALB. Para usar esse comando é necessário que a stack já tenha sido criada.

## Teste da Aplicação

Para testar a aplicação, você pode usar o comando curl para enviar requisições HTTP para a API RESTful. Abaixo estão alguns exemplos de comandos curl para testar as funcionalidades CRUD da aplicação:

1. **Já existe um script que faz todos os testes de forma automatica**

```bash
python3 aplicacao_aplicada.py
```
Esse comando executa um script que faz os testes de CRUD na aplicação. Para usar esse comando é necessário que a stack já tenha sido criada.

2. **Criar um novo item**:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id": "1", "name": "Matheus"}' <ALB-DNS>/add_user
```

3. **Obter um item existente**:

```bash
curl -X GET "<ALB-DNS>/get_user?user_id=1"
```

4. **Atualizar um item existente**:

```bash
curl -X PUT <ALB-DNS>/update_user -H "Content-Type: application/json" -d '{"id": "1", "name": "Matheus Castellucci"}' 
```

5. **Excluir um item existente**:

```bash
curl -X DELETE <ALB-DNS>/delete_user?user_id=1
```

Substitua `<ALB-DNS>` pelo DNS do Application Load Balancer (ALB) gerado após a criação da stack.

## Escolha da região
A região selecionada para a execução do projeto foi SA-east-1, a qual foi escolhida com base na latência e no custo dos serviços. SA-east-1 é a única região localizada no Brasil, o que garante menor latência para os usuários brasileiros. Além disso, essa região oferece preços competitivos em comparação com outras regiões.

## Projeção de custos do projeto
Para estimar os custos relacionaos à arquitetura proposta pelo projeto, utilizamos o AWS Cost Calculator. Esta ferramenta permite modelar e comparar os custos de diferentes configurações de serviços AWS, com base em fatores como região, tipo de instância, armazenamento, transferência de dados e outros.
Os principais custos da arquitetura do projeto são associados ao DynamoDB e ao Elastic Load Balancer. Abaixo estão os custos estimados para a aplicação proposta:

1. **DynamoDB**:DynamoDB: $26,39 por/mês (1 table with 1GB of storage)
2. **Elastic Load Balancer**: Elastic Load Balancer: $16,44 per/month (1 Application Load Balancer)

Para mais informações sobre os custos dos serviços AWS, consulte o arquivo : [Estimativa de Custos AWS](https://github.com/MatheusCastellucci/App-Cloud/blob/main/imgs/My%20Estimate%20-%20Calculadora%20de%20Pre%C3%A7os%20da%20AWS.pdf)

## Calculo real dos custos
Apesar de não termos acesso completo à todas as funcionalidades da AWS, podemos utilizar a aba de `Billing & Cost Management` para verificar um sumário dos custos do projeto.

<p align="center"><b style="font-size: 24px;"><u>Custos do Projeto</u></b></p>
<p align="center">
  <img src="imgs\custos.jpg" alt="Topologia"/>
  <p align="center"><style="font-size: 14px;">Foto tirada em  23/05/2024</p>
</p>  

Os valores apresentados na imagem acima são referentes ao período de 1 mês de execução do projeto. Claro que isto não apresenta o custo real do projeto, pois o mesmo foi executado por apenas alguns dias e o valor apresentado é referente a um mês de execução. Vale mencionar também que o valor apresentado não leva em consideração o porte que a aplicação precisaria ter para atender a demanda de usuários.

## Referências
As principais referências utilizadas foram:
- AWS: https://aws.amazon.com/pt/
- AWS CLI: https://aws.amazon.com/pt/cli/ 
- AWS EC2: https://aws.amazon.com/pt/ec2/ 
- AWS ALB: https://aws.amazon.com/pt/elasticloadbalancing/ 
- AWS ASG: https://aws.amazon.com/pt/autoscaling/ 
- AWS CloudWatch: https://aws.amazon.com/pt/cloudwatch/ 
- AWS IAM: https://aws.amazon.com/pt/iam/ 
- AWS VPC: https://aws.amazon.com/pt/vpc/ 
- AWS Pricing Calculator: https://calculator.aws/#/