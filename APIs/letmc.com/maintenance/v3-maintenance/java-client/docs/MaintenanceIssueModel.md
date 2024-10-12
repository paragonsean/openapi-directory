

# MaintenanceIssueModel

Submission Model - Handles all fields required to submit an online maintenance job

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documents** | [**List&lt;MaintenanceDocumentModel&gt;**](MaintenanceDocumentModel.md) | Documents linked to a submitted maintenance job |  [optional] |
|**externalID** | **String** | ID used externally to manage jobs before sending to the system. This has a 10 character limit. |  [optional] |
|**issueFault** | **String** | The fault title if applicable |  [optional] |
|**issueNotes** | **String** | Fault notes |  [optional] |
|**issuePriority** | [**IssuePriorityEnum**](#IssuePriorityEnum) | The priority of the job (Defaults to &#39;Low&#39; if incorrect value or empty) |  [optional] |
|**issueTitle** | **String** | The title of the issue |  [optional] |
|**propertyAddress1** | **String** | The first line of the property address |  [optional] |
|**propertyAddress2** | **String** | The second line of the property address |  [optional] |
|**propertyAddress3** | **String** | The third line of the property address |  [optional] |
|**propertyAddress4** | **String** | The forth line of the property address |  [optional] |
|**propertyCountry** | **String** | The country the property is located |  [optional] |
|**propertyPostcode** | **String** | The property postcode |  [optional] |
|**reportedAt** | **OffsetDateTime** | The date the job was reported |  [optional] |
|**tenantEMailAddress** | **String** | The email address of the Tenant |  [optional] |
|**tenantForename** | **String** | The forename of the Tenant |  [optional] |
|**tenantPhonePrimary** | **String** | The primary phone number of the Tenant |  [optional] |
|**tenantPhoneSecondary** | **String** | The secondary phone number of the Tenant |  [optional] |
|**tenantPresenceRequested** | **Boolean** | Is the Tenant’s presence requested during the maintenance visit? (Defaults to “false” if incorrect value or empty) |  [optional] |
|**tenantSurname** | **String** | The surname of the Tenant |  [optional] |
|**tenantTitle** | **String** | The title of the Tenant |  [optional] |



## Enum: IssuePriorityEnum

| Name | Value |
|---- | -----|
| LOW | &quot;Low&quot; |
| MEDIUM | &quot;Medium&quot; |
| HIGH | &quot;High&quot; |



