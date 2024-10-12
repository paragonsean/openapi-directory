

# ResourceServerRepresentation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowRemoteResourceManagement** | **Boolean** |  |  [optional] |
|**clientId** | **String** |  |  [optional] |
|**decisionStrategy** | [**DecisionStrategyEnum**](#DecisionStrategyEnum) |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**policies** | [**List&lt;PolicyRepresentation&gt;**](PolicyRepresentation.md) |  |  [optional] |
|**policyEnforcementMode** | [**PolicyEnforcementModeEnum**](#PolicyEnforcementModeEnum) |  |  [optional] |
|**resources** | [**List&lt;ResourceRepresentation&gt;**](ResourceRepresentation.md) |  |  [optional] |
|**scopes** | [**List&lt;ScopeRepresentation&gt;**](ScopeRepresentation.md) |  |  [optional] |



## Enum: DecisionStrategyEnum

| Name | Value |
|---- | -----|
| AFFIRMATIVE | &quot;AFFIRMATIVE&quot; |
| UNANIMOUS | &quot;UNANIMOUS&quot; |
| CONSENSUS | &quot;CONSENSUS&quot; |



## Enum: PolicyEnforcementModeEnum

| Name | Value |
|---- | -----|
| ENFORCING | &quot;ENFORCING&quot; |
| PERMISSIVE | &quot;PERMISSIVE&quot; |
| DISABLED | &quot;DISABLED&quot; |



