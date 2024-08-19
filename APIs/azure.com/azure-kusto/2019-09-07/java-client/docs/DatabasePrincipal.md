

# DatabasePrincipal

A class representing database principal entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | Application id - relevant only for application principal type. |  [optional] |
|**email** | **String** | Database principal email if exists. |  [optional] |
|**fqn** | **String** | Database principal fully qualified name. |  [optional] |
|**name** | **String** | Database principal name. |  |
|**role** | [**RoleEnum**](#RoleEnum) | Database principal role. |  |
|**tenantName** | **String** | The tenant name of the principal |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Database principal type. |  |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ADMIN | &quot;Admin&quot; |
| INGESTOR | &quot;Ingestor&quot; |
| MONITOR | &quot;Monitor&quot; |
| USER | &quot;User&quot; |
| UNRESTRICTED_VIEWERS | &quot;UnrestrictedViewers&quot; |
| VIEWER | &quot;Viewer&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| APP | &quot;App&quot; |
| GROUP | &quot;Group&quot; |
| USER | &quot;User&quot; |



