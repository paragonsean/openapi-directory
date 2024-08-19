# RudderApi.Directive

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Human readable name of the directive | [optional] 
**enabled** | **Boolean** | Is the directive enabled | [optional] 
**id** | **String** | Directive id | [optional] 
**longDescription** | **String** | Description of the technique (rendered as markdown) | [optional] 
**parameters** | **Object** | Directive parameters (depends on the source technique) | [optional] 
**policyMode** | **String** | Policy mode of the directive | [optional] 
**priority** | **Number** | Directive priority. &#x60;0&#x60; has highest priority. | [optional] 
**shortDescription** | **String** | One line directive description | [optional] 
**system** | **Boolean** | If true it is an internal Rudder directive | [optional] 
**tags** | [**[DirectiveTagsInner]**](DirectiveTagsInner.md) |  | [optional] 
**techniqueName** | **String** | Directive id | [optional] 
**techniqueVersion** | **String** | Directive id | [optional] 



## Enum: PolicyModeEnum


* `enforce` (value: `"enforce"`)

* `audit` (value: `"audit"`)




