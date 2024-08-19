# AdyenTerminalApi.SaleData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerOrderID** | **String** | Additional and optional identification of a customer order. | [optional] 
**customerOrderReq** | **[String]** |  | [optional] 
**operatorID** | **String** |  | [optional] 
**operatorLanguage** | **String** | if different from the Login. | [optional] 
**saleReferenceID** | **String** | If payment reservation. | [optional] 
**saleTerminalData** | [**SaleTerminalData**](SaleTerminalData.md) |  | [optional] 
**saleToAcquirerData** | **String** | Send to the Acquirer if present. | [optional] 
**saleToIssuerData** | [**SaleToIssuerData**](SaleToIssuerData.md) |  | [optional] 
**saleToPOIData** | **String** | Stored with the transaction. | [optional] 
**saleTransactionID** | [**TransactionIDType**](TransactionIDType.md) |  | 
**shiftNumber** | **String** | if different from the Login and  see Login .SaleData. | [optional] 
**tokenRequestedType** | [**TokenRequestedType**](TokenRequestedType.md) |  | [optional] 



## Enum: [CustomerOrderReqEnum]


* `Both` (value: `"Both"`)

* `Closed` (value: `"Closed"`)

* `Open` (value: `"Open"`)




