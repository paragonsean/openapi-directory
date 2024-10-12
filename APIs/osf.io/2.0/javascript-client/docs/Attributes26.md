# OsfApiv2Documentation.Attributes26

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto** | **Boolean** | Bool of representing whether a user created the action. | [optional] [readonly] 
**comment** | **String** | A comment made explaining the reasoning of the action. | [optional] [readonly] 
**dateCreated** | **String** | The date the action was created. | [optional] [readonly] 
**fromState** | **String** | The name of the state of the Schema Response prior to the creation of the action. | [optional] 
**toState** | **String** | The name of the state of the Schema Response after the creation of the action | [optional] 
**trigger** | **String** | The name of the trigger that caused the action. | [optional] 
**visible** | **Boolean** | Bool of representing whether the action is visible. | [optional] [readonly] 



## Enum: FromStateEnum


* `initial` (value: `"initial"`)

* `in_progress` (value: `"in_progress"`)

* `approved` (value: `"approved"`)

* `pending_moderation` (value: `"pending_moderation"`)





## Enum: ToStateEnum


* `in_progress` (value: `"in_progress"`)

* `approved` (value: `"approved"`)

* `pending_moderation` (value: `"pending_moderation"`)





## Enum: TriggerEnum


* `submit` (value: `"submit"`)

* `approve` (value: `"approve"`)

* `accept` (value: `"accept"`)

* `admin_reject` (value: `"admin_reject"`)

* `moderator_reject` (value: `"moderator_reject"`)




