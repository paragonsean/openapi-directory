

# Directive


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Human readable name of the directive |  [optional] |
|**enabled** | **Boolean** | Is the directive enabled |  [optional] |
|**id** | **UUID** | Directive id |  [optional] |
|**longDescription** | **String** | Description of the technique (rendered as markdown) |  [optional] |
|**parameters** | **Object** | Directive parameters (depends on the source technique) |  [optional] |
|**policyMode** | [**PolicyModeEnum**](#PolicyModeEnum) | Policy mode of the directive |  [optional] |
|**priority** | **Integer** | Directive priority. &#x60;0&#x60; has highest priority. |  [optional] |
|**shortDescription** | **String** | One line directive description |  [optional] |
|**system** | **Boolean** | If true it is an internal Rudder directive |  [optional] |
|**tags** | [**List&lt;DirectiveTagsInner&gt;**](DirectiveTagsInner.md) |  |  [optional] |
|**techniqueName** | **String** | Directive id |  [optional] |
|**techniqueVersion** | **String** | Directive id |  [optional] |



## Enum: PolicyModeEnum

| Name | Value |
|---- | -----|
| ENFORCE | &quot;enforce&quot; |
| AUDIT | &quot;audit&quot; |



