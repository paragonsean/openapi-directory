# KustoManagementClient.DatabasePrincipal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | Application id - relevant only for application principal type. | [optional] 
**email** | **String** | Database principal email if exists. | [optional] 
**fqn** | **String** | Database principal fully qualified name. | [optional] 
**name** | **String** | Database principal name. | 
**role** | **String** | Database principal role. | 
**tenantName** | **String** | The tenant name of the principal | [optional] [readonly] 
**type** | **String** | Database principal type. | 



## Enum: RoleEnum


* `Admin` (value: `"Admin"`)

* `Ingestor` (value: `"Ingestor"`)

* `Monitor` (value: `"Monitor"`)

* `User` (value: `"User"`)

* `UnrestrictedViewers` (value: `"UnrestrictedViewers"`)

* `Viewer` (value: `"Viewer"`)





## Enum: TypeEnum


* `App` (value: `"App"`)

* `Group` (value: `"Group"`)

* `User` (value: `"User"`)




