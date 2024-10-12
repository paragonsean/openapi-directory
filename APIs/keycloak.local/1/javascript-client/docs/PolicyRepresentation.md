# KeycloakAdminRestApi.PolicyRepresentation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **{String: Object}** |  | [optional] 
**decisionStrategy** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**id** | **String** |  | [optional] 
**logic** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**owner** | **String** |  | [optional] 
**policies** | **[String]** |  | [optional] 
**resources** | **[String]** |  | [optional] 
**resourcesData** | [**[ResourceRepresentation]**](ResourceRepresentation.md) |  | [optional] 
**scopes** | **[String]** |  | [optional] 
**scopesData** | [**[ScopeRepresentation]**](ScopeRepresentation.md) |  | [optional] 
**type** | **String** |  | [optional] 



## Enum: DecisionStrategyEnum


* `AFFIRMATIVE` (value: `"AFFIRMATIVE"`)

* `UNANIMOUS` (value: `"UNANIMOUS"`)

* `CONSENSUS` (value: `"CONSENSUS"`)





## Enum: LogicEnum


* `POSITIVE` (value: `"POSITIVE"`)

* `NEGATIVE` (value: `"NEGATIVE"`)




