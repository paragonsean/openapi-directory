# ReportsApi.CsvVoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account ID (API key) you wish to search for. This can differ from the API key in the authorization header because some accounts can request reports for other accounts, e.g. a primary account owner wants to create a report for one of its subaccounts. | [optional] 
**callId** | **String** | UUID of the request. | [optional] 
**country** | **String** | Country where the request was sent. | [optional] 
**countryName** | **String** | Country name where the request was sent. | [optional] 
**currency** | **String** | Currency of the price of the request. | [optional] 
**dateEnd** | **Date** | Date of the end of the call. | [optional] 
**dateStart** | **Date** | Date of the start of the call. | [optional] 
**direction** | [**Direction**](Direction.md) |  | [optional] 
**duration** | **Number** | Duration of the call in seconds. | [optional] 
**from** | **String** | Request from this number. | [optional] 
**network** | **String** | Network used to send the request. | [optional] 
**networkName** | **String** | Name of the network used to send the request. | [optional] 
**price** | **String** | Price of the request. | [optional] 
**status** | [**VoiceStatus**](VoiceStatus.md) |  | [optional] 
**statusDescription** | **String** | Description of the status of the call. | [optional] 
**to** | **String** | Request to this number. | [optional] 
**totalPrice** | **String** | Total price of the request. | [optional] 


