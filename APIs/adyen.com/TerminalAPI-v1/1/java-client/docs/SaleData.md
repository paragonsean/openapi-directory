

# SaleData

Data associated to the Sale System, with a particular value during the processing of the payment by the POI, including the cards acquisition. Data related to the Sale System.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerOrderID** | **String** | Additional and optional identification of a customer order. |  [optional] |
|**customerOrderReq** | [**List&lt;CustomerOrderReqEnum&gt;**](#List&lt;CustomerOrderReqEnum&gt;) |  |  [optional] |
|**operatorID** | **String** |  |  [optional] |
|**operatorLanguage** | **String** | if different from the Login. |  [optional] |
|**saleReferenceID** | **String** | If payment reservation. |  [optional] |
|**saleTerminalData** | [**SaleTerminalData**](SaleTerminalData.md) |  |  [optional] |
|**saleToAcquirerData** | **String** | Send to the Acquirer if present. |  [optional] |
|**saleToIssuerData** | [**SaleToIssuerData**](SaleToIssuerData.md) |  |  [optional] |
|**saleToPOIData** | **String** | Stored with the transaction. |  [optional] |
|**saleTransactionID** | [**TransactionIDType**](TransactionIDType.md) |  |  |
|**shiftNumber** | **String** | if different from the Login and  see Login .SaleData. |  [optional] |
|**tokenRequestedType** | **TokenRequestedType** |  |  [optional] |



## Enum: List&lt;CustomerOrderReqEnum&gt;

| Name | Value |
|---- | -----|
| BOTH | &quot;Both&quot; |
| CLOSED | &quot;Closed&quot; |
| OPEN | &quot;Open&quot; |



