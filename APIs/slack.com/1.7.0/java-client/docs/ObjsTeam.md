

# ObjsTeam


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archived** | **Boolean** |  |  [optional] |
|**avatarBaseUrl** | **URI** |  |  [optional] |
|**created** | **Integer** |  |  [optional] |
|**dateCreate** | **Integer** |  |  [optional] |
|**deleted** | **Boolean** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**discoverable** | [**List&lt;ObjsTeamDiscoverableInner&gt;**](ObjsTeamDiscoverableInner.md) |  |  [optional] |
|**domain** | **String** |  |  |
|**emailDomain** | **String** |  |  |
|**enterpriseId** | **String** |  |  [optional] |
|**enterpriseName** | **String** |  |  [optional] |
|**externalOrgMigrations** | [**ObjsExternalOrgMigrations**](ObjsExternalOrgMigrations.md) |  |  [optional] |
|**hasComplianceExport** | **Boolean** |  |  [optional] |
|**icon** | [**ObjsIcon**](ObjsIcon.md) |  |  |
|**id** | **String** |  |  |
|**isAssigned** | **Boolean** |  |  [optional] |
|**isEnterprise** | **Integer** |  |  [optional] |
|**isOverStorageLimit** | **Boolean** |  |  [optional] |
|**limitTs** | **Integer** |  |  [optional] |
|**locale** | **String** |  |  [optional] |
|**messagesCount** | **Integer** |  |  [optional] |
|**msgEditWindowMins** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**overIntegrationsLimit** | **Boolean** |  |  [optional] |
|**overStorageLimit** | **Boolean** |  |  [optional] |
|**payProdCur** | **String** |  |  [optional] |
|**plan** | [**PlanEnum**](#PlanEnum) |  |  [optional] |
|**primaryOwner** | [**ObjsPrimaryOwner**](ObjsPrimaryOwner.md) |  |  [optional] |
|**ssoProvider** | [**ObjsTeamSsoProvider**](ObjsTeamSsoProvider.md) |  |  [optional] |



## Enum: PlanEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| STD | &quot;std&quot; |
| PLUS | &quot;plus&quot; |
| COMPLIANCE | &quot;compliance&quot; |
| ENTERPRISE | &quot;enterprise&quot; |



