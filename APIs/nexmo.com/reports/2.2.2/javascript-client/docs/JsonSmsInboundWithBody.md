# ReportsApi.JsonSmsInboundWithBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account ID (API key) you wish to search for. This can differ from the API key in the authorization header because some accounts can request reports for other accounts, e.g. a primary account owner wants to create a report for one of its subaccounts. | [optional] 
**country** | **String** | Country where the request was sent. | [optional] 
**countryName** | **String** | Country name where the request was sent. | [optional] 
**currency** | **String** | Currency of the price of the request. | [optional] 
**dateReceived** | **Date** | Date of the request. | [optional] 
**direction** | [**Direction**](Direction.md) |  | [optional] 
**from** | **String** | Request from this number. | [optional] 
**messageId** | **String** | Id of the request. | [optional] 
**network** | **String** | Network used to send the request. | [optional] 
**networkName** | **String** | Name of the network used to send the request. | [optional] 
**to** | **String** | Request to this number. | [optional] 
**totalPrice** | **String** | Price of the request. | [optional] 
**messageBody** | **String** | Body of the message sent. Only present if include_message parameter is set to true. | [optional] 


