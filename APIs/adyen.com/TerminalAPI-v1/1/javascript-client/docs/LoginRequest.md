# AdyenTerminalApi.LoginRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerOrderReq** | **[String]** |  | [optional] 
**dateTime** | **Date** | Date and Time. | 
**operatorID** | **String** | 4 conditions to send it: a) the Sale System wants the POI log it in the transaction log b) because of reconciliation. | [optional] 
**operatorLanguage** | **String** | Default value for Device type displays. | 
**pOISerialNumber** | **String** | If the login involve a POI Terminal and not the first Login to the POI System. | [optional] 
**saleSoftware** | [**SaleSoftware**](SaleSoftware.md) |  | 
**saleTerminalData** | [**SaleTerminalData**](SaleTerminalData.md) |  | [optional] 
**shiftNumber** | **String** | Same as OperatorID. | [optional] 
**tokenRequestedType** | [**TokenRequestedType**](TokenRequestedType.md) |  | [optional] 
**trainingModeFlag** | **Boolean** | The POI does not realise the transaction with the Acquirer. | [optional] [default to false]



## Enum: [CustomerOrderReqEnum]


* `Both` (value: `"Both"`)

* `Closed` (value: `"Closed"`)

* `Open` (value: `"Open"`)




