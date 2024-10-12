

# PolicyRepresentation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**config** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**decisionStrategy** | [**DecisionStrategyEnum**](#DecisionStrategyEnum) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**logic** | [**LogicEnum**](#LogicEnum) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**owner** | **String** |  |  [optional] |
|**policies** | **List&lt;String&gt;** |  |  [optional] |
|**resources** | **List&lt;String&gt;** |  |  [optional] |
|**resourcesData** | [**List&lt;ResourceRepresentation&gt;**](ResourceRepresentation.md) |  |  [optional] |
|**scopes** | **List&lt;String&gt;** |  |  [optional] |
|**scopesData** | [**List&lt;ScopeRepresentation&gt;**](ScopeRepresentation.md) |  |  [optional] |
|**type** | **String** |  |  [optional] |



## Enum: DecisionStrategyEnum

| Name | Value |
|---- | -----|
| AFFIRMATIVE | &quot;AFFIRMATIVE&quot; |
| UNANIMOUS | &quot;UNANIMOUS&quot; |
| CONSENSUS | &quot;CONSENSUS&quot; |



## Enum: LogicEnum

| Name | Value |
|---- | -----|
| POSITIVE | &quot;POSITIVE&quot; |
| NEGATIVE | &quot;NEGATIVE&quot; |



