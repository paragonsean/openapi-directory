

# RoleAssignment

The Role Assignment definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignmentName** | **String** | The name of the metadata object. |  [optional] [readonly] |
|**conflationPolicies** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**connectors** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**description** | **Map&lt;String, String&gt;** | Localized description for the metadata. |  [optional] |
|**displayName** | **Map&lt;String, String&gt;** | Localized display names for the metadata. |  [optional] |
|**interactions** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**kpis** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**links** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**principals** | [**List&lt;AssignmentPrincipal&gt;**](AssignmentPrincipal.md) | The principals being assigned to. |  |
|**profiles** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**relationshipLinks** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**relationships** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Type of roles. |  |
|**roleAssignments** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**sasPolicies** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**segments** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |
|**views** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |
|**widgetTypes** | [**ResourceSetDescription**](ResourceSetDescription.md) |  |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ADMIN | &quot;Admin&quot; |
| READER | &quot;Reader&quot; |
| MANAGE_ADMIN | &quot;ManageAdmin&quot; |
| MANAGE_READER | &quot;ManageReader&quot; |
| DATA_ADMIN | &quot;DataAdmin&quot; |
| DATA_READER | &quot;DataReader&quot; |



