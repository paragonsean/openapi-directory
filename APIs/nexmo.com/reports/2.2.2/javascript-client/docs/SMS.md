# ReportsApi.SMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountRef** | **String** | Search for messages with this &#x60;account_ref&#x60;. | [optional] 
**clientRef** | **String** | Search for messages with this &#x60;client_ref&#x60;. | [optional] 
**direction** | [**Direction**](Direction.md) |  | 
**from** | **String** | Request from this number. | [optional] 
**includeMessage** | **Boolean** | Include the text of messages in the report. | [optional] [default to false]
**network** | **String** | Network used to send the request. | [optional] 
**product** | [**ProductSms**](ProductSms.md) |  | 
**showConcatenated** | **Boolean** | Indicates whether the SMS was split up into multiple parts (due to its length). | [optional] [default to false]
**status** | [**SmsStatus**](SmsStatus.md) |  | [optional] 
**to** | **String** | Request to this number. | [optional] 


