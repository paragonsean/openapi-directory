# SpendingPulse.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | This is the text description of the error. This is optional and will only be displayed if more information is available than is stored in the data identifier and reason code. | [optional] 
**reasonCode** | **String** | This will identify the reason for the error. | [optional] 
**recoverable** | **Boolean** | This is a true/false presentation to explain if the transaction was submitted again would it be successful or not. | [optional] 
**source** | **String** | Unique identifier that attempts to define the field in error when available.  If a specific field can&#39;t be identified System will be returned. | [optional] 


