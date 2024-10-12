# ReportsApi.CsvVerify

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account ID (API key) you wish to search for. This can differ from the API key in the authorization header because some accounts can request reports for other accounts, e.g. a primary account owner wants to create a report for one of its subaccounts. | [optional] 
**country** | **String** | Country where the request was sent. | [optional] 
**countryName** | **String** | Country name where the request was sent. | [optional] 
**currency** | **String** | Currency of the price of the request. | [optional] 
**dateFinalized** | **Date** | Date when the request was finalized. | [optional] 
**dateReceived** | **Date** | Date of the request. | [optional] 
**estimatedPrice** | **String** | Estimated price of the verify request. | [optional] 
**firstEventDate** | **Date** | Date of the first verify event. | [optional] 
**from** | **String** | Request from this number. | [optional] 
**lastEventDate** | **Date** | Date of the last verify event. | [optional] 
**locale** | **String** | Locale used for the TTS. | [optional] 
**network** | **String** | Network used to send the request. | [optional] 
**networkName** | **String** | Name of the network used to send the request. | [optional] 
**numberType** | **String** | Type of phone number to which requests are sent. | [optional] 
**price** | **String** | Price of the request. | [optional] 
**pricingModel** | **String** | Pricing model used for this request. | [optional] 
**requestId** | **String** | UUID of the request. | [optional] 
**smsEventCount** | **Number** | Number of sms sent for this verify request. | [optional] 
**to** | **String** | Request to this number. | [optional] 
**ttsEventCount** | **Number** | Number of tts sent for this verify request. | [optional] 
**verifyStatus** | **String** | Status of the verify request. | [optional] 


