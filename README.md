# Implementação de uma arquitetura de nuvem utilizando a AWS.

### Matheus Castellucci

## Descrição do Projeto

O projeto consiste na criação de uma arquitetura de nuvem utilizando AWS. A arquitetura inclui uma aplicação web que será executada em uma instância EC2, que estará dentro de um Auto Scaling Group (ASG) e um Application Load Balancer (ALB) para distribuir a carga entre as instâncias EC2. A aplicação web será uma API RESTful com funcionalidades CRUD simples, acessando um banco de dados DynamoDB, um serviço NoSQL da AWS que oferece alta escalabilidade e desempenho.

## Arquitetura da Solução
A arquitetura da solução é composta por 5 componentes principais:

1. **EC2**: A instância EC2 é uma máquina virtual na nuvem da AWS que será responsável por executar a aplicação web. A instância EC2 estará dentro de um Auto Scaling Group (ASG) para garantir alta disponibilidade e escalabilidade automática.

2. **Auto Scaling Group (ASG)**: O Auto Scaling Group é um grupo de instâncias EC2 que podem ser gerenciadas como uma unidade lógica para fins de dimensionamento automático e aplicação de políticas. O ASG garante que o número especificado de instâncias do EC2 esteja sempre em execução.

3. **CloudWatch**: O Amazon CloudWatch é um serviço de monitoramento e observabilidade da AWS para recursos em nuvem e aplicativos executados na AWS. O CloudWatch será utilizado para monitorar o status do ASG e das instâncias EC2, além de criar novas instâncias automaticamente quando o uso da CPU ultrapassar um determinado limite.


<p align="center"><b style="font-size: 24px;"><u>Topologia da solução</u></b></p>
<p align="center">
  <img src="imgs\cloud_roteiro.drawio.png" alt="Topologia"/>
  <p align="center"><style="font-size: 14px;">Algumas imagens foram retiradas do site da AWS (Fonte: https://aws.amazon.com/pt/elasticloadbalancing/ )</p>
</p>


<p align="center"><b style="font-size: 24px;"><u>Diagrama da Arquitetura AWS</u></b></p>
<p align="center">
  <img src="imgs\cloud_roteiro.drawio.png" alt="Topologia"/>
  <p align="center"><style="font-size: 14px;">Algumas imagens foram retiradas do site da AWS (Fonte: https://aws.amazon.com/pt/elasticloadbalancing/ )</p>
</p>


## Tecnologias usadas

### AWS
* A Amazon Web Services (AWS) é uma plataforma de computação em nuvem oferecida pela Amazon.com, composta por diversos serviços de computação. Esses serviços são disponibilizados em várias regiões geográficas ao redor do mundo.

### AWS CLI
* O AWS Command Line Interface (AWS CLI) é uma ferramenta unificada para gerenciar serviços da AWS. Com uma única ferramenta para download e configuração, você pode controlar vários serviços da AWS a partir da linha de comando e automatizar tarefas por meio de scripts.

### AWS EC2
* O Amazon Elastic Compute Cloud (Amazon EC2) é um serviço web que oferece capacidade de computação redimensionável na nuvem. Foi projetado para facilitar a computação em nuvem em escala web para desenvolvedores.

### AWS ALB
* O Application Load Balancer (ALB) é um balanceador de carga gerenciado pela AWS, projetado para aplicativos HTTP e HTTPS. Operando na camada 7, o ALB roteia o tráfego de entrada para alvos como instâncias do Amazon EC2, contêineres do Amazon ECS e funções do AWS Lambda, com base nas regras definidas pelo usuário. Neste projeto, o ALB também foi configurado com "Health Checks" para verificar a integridade das instâncias EC2 e removê-las do balanceamento de carga se estiverem inativas.

### AWS ASG
* O Auto Scaling Group (ASG) é um grupo de instâncias do Amazon EC2 que podem ser gerenciadas como uma unidade lógica para fins de dimensionamento automático e aplicação de políticas. Um ASG garante que o número especificado de instâncias do EC2 esteja sempre em execução.

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

Para executar o projeto, também é necessário criar um par de chaves SSH. Acesse o console da AWS, vá para o serviço EC2, clique em "Key Pairs" no menu lateral esquerdo e crie um novo par de chaves. O arquivo .pem gerado deve ser salvo na pasta raiz do projeto. O nome do par de chaves no arquivo .yaml é "MyKeyPair". Caso queira usar outro nome, altere-o no arquivo .yaml.

![Alt text](imgs\key_pair.jpg)

## Execução do Projeto

Com tudo configurado, acesse o serviço de CloudFormation da AWS e crie um novo stack. Selecione o arquivo .yaml presente na pasta raiz do projeto e siga as instruções para criar o stack.

```bash
aws cloudformation create-stack --stack-name nome_da_stack --template-body file://projeto_aws.yaml --capabilities CAPABILITY_IAM
```

```bash
aws cloudformation delete-stack --stack-name nome_da_stack
```








## Escolha da região
A região escolhida para a execução do projeto foi SA-east-1. A seleção foi baseada na latência e no custo dos serviços. A região SA-east-1 é a mais próxima do Brasil, proporcionando menor latência para os usuários brasileiros, além de possuir preços competitivos em relação a outras regiões.

## Calculo de custos
Para estimar os custos associados à arquitetura proposta, utilizamos o AWS Cost Calculator. Esta ferramenta permite modelar e comparar os custos de diferentes configurações de serviços AWS, ajudando a tomar decisões informadas sobre escalabilidade e custo-benefício.
Os principais custos são associados ao DynamoDB e ao Elastic Load Balancer, que são os serviços mais caros da aplicação. Abaixo estão os custos estimados para a aplicação proposta:

1. **DynamoDB**:
2. **Elastic Load Balancer**:

**Obs**: Para reduzir custos, consideramos possíveis melhorias como a utilização de instâncias reservadas ou instâncias spot, que são mais econômicas do que as instâncias sob demanda, além da substituição do DynamoDB por um banco de dados RDS, que é mais barato.

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