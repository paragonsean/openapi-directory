# ReportsApi.CsvWebsockets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account ID (API key) you wish to search for. This can differ from the API key in the authorization header because some accounts can request reports for other accounts, e.g. a primary account owner wants to create a report for one of its subaccounts. | [optional] 
**callId** | **String** | UUID of the request. | [optional] 
**currency** | **String** | Currency of the price of the request. | [optional] 
**dateEnd** | **Date** | Date of the end of the call. | [optional] 
**dateStart** | **Date** | Date of the start of the call. | [optional] 
**duration** | **Number** | Duration of the call in seconds. | [optional] 
**price** | **String** | Price of the request. | [optional] 
**status** | **String** | Search only for WebSocket call with corresponding status. | [optional] 
**totalPrice** | **String** | Total price of the request. | [optional] 


