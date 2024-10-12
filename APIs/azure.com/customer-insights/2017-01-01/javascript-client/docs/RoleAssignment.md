# CustomerInsightsManagementClient.RoleAssignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignmentName** | **String** | The name of the metadata object. | [optional] [readonly] 
**conflationPolicies** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**connectors** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**description** | **{String: String}** | Localized description for the metadata. | [optional] 
**displayName** | **{String: String}** | Localized display names for the metadata. | [optional] 
**interactions** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**kpis** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**links** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**principals** | [**[AssignmentPrincipal]**](AssignmentPrincipal.md) | The principals being assigned to. | 
**profiles** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**relationshipLinks** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**relationships** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**role** | **String** | Type of roles. | 
**roleAssignments** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**sasPolicies** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**segments** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**tenantId** | **String** | The hub name. | [optional] [readonly] 
**views** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 
**widgetTypes** | [**ResourceSetDescription**](ResourceSetDescription.md) |  | [optional] 



## Enum: RoleEnum


* `Admin` (value: `"Admin"`)

* `Reader` (value: `"Reader"`)

* `ManageAdmin` (value: `"ManageAdmin"`)

* `ManageReader` (value: `"ManageReader"`)

* `DataAdmin` (value: `"DataAdmin"`)

* `DataReader` (value: `"DataReader"`)




