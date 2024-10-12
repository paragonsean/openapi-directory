# ReportsApi.GetRecords200ResponseOneOf7

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ReportResponseTopLevelLinks**](ReportResponseTopLevelLinks.md) |  | [optional] 
**accountId** | **String** | The account ID (API key) you wish to search for. This can differ from the API key in the authorization header because some accounts can request reports for other accounts, e.g. a primary account owner wants to create a report for one of its subaccounts. | [optional] 
**currency** | **String** | Currency of the price of the request. | [optional] 
**idsNotFound** | **String** | If you request multiple records using a comma-separated list of UUIDs, then the UUIDs of any records not found are listed in this field. | [optional] 
**price** | **String** | Price of the request. | [optional] 
**receivedAt** | **Date** | Time at which the report request was received by the service. | [optional] 
**requestId** | **String** | UUID of the request. | [optional] 
**requestStatus** | [**RequestStatus**](RequestStatus.md) |  | [optional] 
**direction** | **String** | Direction of the communication, either &#x60;inbound&#x60; (received by our services), or &#x60;outbound&#x60; (originated from our services). Required for products &#x60;SMS&#x60; and &#x60;MESSAGES&#x60;. Optional for &#x60;VOICE-CALL&#x60;. Invalid for &#x60;IN-APP-VOICE&#x60;, &#x60;CONVERSATIONS&#x60;, &#x60;NUMBER-INSIGHT&#x60;, &#x60;VERIFY-API&#x60;. | [optional] 
**includeMessage** | **Boolean** | Include the text of messages in the report. | [optional] 
**itemsCount** | **Number** | The number of returned records | [optional] 
**product** | [**ProductMessages**](ProductMessages.md) |  | [optional] 
**records** | [**[CsvMessagesOutbound]**](CsvMessagesOutbound.md) | Records in JSON format | [optional] 
**showConcatenated** | **Boolean** | Indicates whether the SMS was split up into multiple parts (due to its length). | [optional] 



## Enum: DirectionEnum


* `inbound` (value: `"inbound"`)

* `outbound` (value: `"outbound"`)




