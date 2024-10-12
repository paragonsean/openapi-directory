# AnchoreEngineApiServer.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The timestamp when the account was created | [optional] 
**email** | **String** | Optional email address associated with the account | [optional] 
**lastUpdated** | **Date** | The timestamp of the last update to the account metadata itself (not users or creds) | [optional] 
**name** | **String** | The account identifier, not updatable after creation | 
**state** | **String** | State of the account. Disabled accounts prevent member users from logging in, deleting accounts are disabled and pending deletion and will be removed once all owned resources are garbage collected by the system | [optional] 
**type** | **String** | The user type (admin vs user). If not specified in a POST request, &#39;user&#39; is default | [optional] 



## Enum: StateEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)

* `deleting` (value: `"deleting"`)





## Enum: TypeEnum


* `user` (value: `"user"`)

* `admin` (value: `"admin"`)

* `service` (value: `"service"`)




