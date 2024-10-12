# Gitlab.PostV3ProjectsIdStatusesShaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **String** | The state of the status | 
**ref** | **String** | The ref | [optional] 
**targetUrl** | **String** | The target URL to associate with this status | [optional] 
**description** | **String** | A short description of the status | [optional] 
**name** | **String** | A string label to differentiate this status from the status of other systems. Default: \&quot;default\&quot; | [optional] 
**context** | **String** | A string label to differentiate this status from the status of other systems. Default: \&quot;default\&quot; | [optional] 



## Enum: StateEnum


* `pending` (value: `"pending"`)

* `running` (value: `"running"`)

* `success` (value: `"success"`)

* `failed` (value: `"failed"`)

* `canceled` (value: `"canceled"`)




