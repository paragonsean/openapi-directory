# CnabOnline.OccurrenceAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency** | **String** | Retorna o número da agencia | [optional] 
**bankTax** | **Number** | Tarifa bancária | [optional] 
**chargedAgency** | **String** | Retorna a agencia cobradora (com o digito) | [optional] 
**code** | **String** | Código de Ocorrência conforme o padrão CNAB | [optional] 
**codeName** | **String** | Nome do código | [optional] 
**creditDate** | **String** | Retorna a data em que o dinheiro caiu na conta | [optional] 
**discountValue** | **Number** | Valor de desconto | [optional] 
**documentNumber** | **String** | Retorna o número do documento do boleto | [optional] 
**dueDate** | **String** | Retorna a data de vencimento de boleto | [optional] 
**iofTax** | **Number** | Retorna o valor do Imposto sobre operações financeiras (IOF) | [optional] 
**isDda** | **String** | Retorna de o boleto foi pago através do Débito Direto Autorizado | [optional] 
**isPayment** | **Boolean** | Retorna se é para dar baixa no boleto | [optional] 
**isRejectedPayment** | **Boolean** | Retorno se é uma baixa rejeitada (Ex: pedido de baixa foi rejeitado) | [optional] 
**liquidationCode** | **String** | Retorna o código de liquidação, normalmente usado para saber onde o cliente efetuou o pagamento | [optional] 
**liquidationDescription** | **String** | Retorna a descrição do código de liquidação | [optional] 
**mulctValue** | **String** | Retorna o valor de juros e mora | [optional] 
**occurrenceDate** | **String** | Retorna a data da ocorrencia, o dia do pagamento | [optional] 
**othersCreditsValue** | **Number** | Retorna o valor de outros creditos | [optional] 
**ourNumber** | **String** | Retorna o nosso número do boleto (sem o digito) | [optional] 
**payerAllegation** | **String** | Retorna a alegação do pagador (para erros) | [optional] 
**rebateValue** | **Number** | Retornna o valor dos abatimentos concedidos (depois da emissão) | [optional] 
**receivedValue** | **Number** | Valor recebido | [optional] 
**sequencialNumber** | **Number** | Retorna o numero sequencial da ocorrência no arquivo | [optional] 
**titleValue** | **Number** | Valor do título (valor do boleto) | [optional] 
**wallet** | **String** | Retorna o número da carteira do boleto | [optional] 


