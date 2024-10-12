# ReportsApi.CsvMessagesInbound

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account ID (API key) you wish to search for. This can differ from the API key in the authorization header because some accounts can request reports for other accounts, e.g. a primary account owner wants to create a report for one of its subaccounts. | [optional] 
**currency** | **String** | Currency of the price of the request. | [optional] 
**dateReceived** | **Date** | Date of the request. | [optional] 
**direction** | [**Direction**](Direction.md) |  | [optional] 
**from** | **String** | Request from this number. | [optional] 
**messageBody** | **String** | Body of the message sent. Only present if include_message parameter is set to true. | [optional] 
**messageId** | **String** | Id of the request. | [optional] 
**provider** | **String** | Provider of the message. | [optional] 
**to** | **String** | Request to this number. | [optional] 
**totalPrice** | **String** | Total price of the request. | [optional] 


