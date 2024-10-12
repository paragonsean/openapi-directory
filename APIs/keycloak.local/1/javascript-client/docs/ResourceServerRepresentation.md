# KeycloakAdminRestApi.ResourceServerRepresentation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowRemoteResourceManagement** | **Boolean** |  | [optional] 
**clientId** | **String** |  | [optional] 
**decisionStrategy** | **String** |  | [optional] 
**id** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**policies** | [**[PolicyRepresentation]**](PolicyRepresentation.md) |  | [optional] 
**policyEnforcementMode** | **String** |  | [optional] 
**resources** | [**[ResourceRepresentation]**](ResourceRepresentation.md) |  | [optional] 
**scopes** | [**[ScopeRepresentation]**](ScopeRepresentation.md) |  | [optional] 



## Enum: DecisionStrategyEnum


* `AFFIRMATIVE` (value: `"AFFIRMATIVE"`)

* `UNANIMOUS` (value: `"UNANIMOUS"`)

* `CONSENSUS` (value: `"CONSENSUS"`)





## Enum: PolicyEnforcementModeEnum


* `ENFORCING` (value: `"ENFORCING"`)

* `PERMISSIVE` (value: `"PERMISSIVE"`)

* `DISABLED` (value: `"DISABLED"`)




