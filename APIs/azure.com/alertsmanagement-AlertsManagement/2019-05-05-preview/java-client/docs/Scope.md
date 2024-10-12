

# Scope

Target scope for a given action rule. By default scope will be the subscription. User can also provide list of resource groups or list of resources from the scope subscription as well.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scopeType** | [**ScopeTypeEnum**](#ScopeTypeEnum) | type of target scope |  [optional] |
|**values** | **List&lt;String&gt;** | list of ARM IDs of the given scope type which will be the target of the given action rule. |  [optional] |



## Enum: ScopeTypeEnum

| Name | Value |
|---- | -----|
| RESOURCE_GROUP | &quot;ResourceGroup&quot; |
| RESOURCE | &quot;Resource&quot; |



