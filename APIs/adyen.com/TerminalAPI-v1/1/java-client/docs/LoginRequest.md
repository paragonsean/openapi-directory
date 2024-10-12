

# LoginRequest

It conveys Information related to the session (period between a Login and the following Logout) to process. Content of the Login Request message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerOrderReq** | [**List&lt;CustomerOrderReqEnum&gt;**](#List&lt;CustomerOrderReqEnum&gt;) |  |  [optional] |
|**dateTime** | **OffsetDateTime** | Date and Time. |  |
|**operatorID** | **String** | 4 conditions to send it: a) the Sale System wants the POI log it in the transaction log b) because of reconciliation. |  [optional] |
|**operatorLanguage** | **String** | Default value for Device type displays. |  |
|**poISerialNumber** | **String** | If the login involve a POI Terminal and not the first Login to the POI System. |  [optional] |
|**saleSoftware** | [**SaleSoftware**](SaleSoftware.md) |  |  |
|**saleTerminalData** | [**SaleTerminalData**](SaleTerminalData.md) |  |  [optional] |
|**shiftNumber** | **String** | Same as OperatorID. |  [optional] |
|**tokenRequestedType** | **TokenRequestedType** |  |  [optional] |
|**trainingModeFlag** | **Boolean** | The POI does not realise the transaction with the Acquirer. |  [optional] |



## Enum: List&lt;CustomerOrderReqEnum&gt;

| Name | Value |
|---- | -----|
| BOTH | &quot;Both&quot; |
| CLOSED | &quot;Closed&quot; |
| OPEN | &quot;Open&quot; |



