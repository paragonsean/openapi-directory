# AgcoApi.GlobalResourcesSharedModelsTranslationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvalUserId** | **Number** | The ID of the user from which approval for the request is required | [optional] 
**cCEmailAddresses** | **[String]** | Additional email addresses to CC on emails pertaining to the request | 
**chargeToAccount** | **String** | The account to charge for the request | 
**deadline** | **Date** | The date by which the translations in the request are needed. Defaults to 30 days from the current date | 
**id** | **Number** | The ID of the request | [optional] 
**localeIds** | **[Number]** | Locale IDs to which these strings are requested to be translated | 
**notes** | **String** | Additional notes or comments about the request | 
**questionsUserId** | **Number** | The ID of the user to which to address questions regarding the request | [optional] 
**state** | **String** | The state of the request | 
**submittedBy** | **Number** | The ID of the User that submitted the request | [optional] 
**translatorEmail** | **String** | The email address for the translator | [optional] 
**translatorName** | **String** | The name of the translator | [optional] 



## Enum: StateEnum


* `NotSubmitted` (value: `"NotSubmitted"`)

* `Submitted` (value: `"Submitted"`)

* `Cancelled` (value: `"Cancelled"`)

* `Completed` (value: `"Completed"`)




