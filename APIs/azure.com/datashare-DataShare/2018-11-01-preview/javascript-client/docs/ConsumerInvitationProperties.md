# DataShareManagementClient.ConsumerInvitationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSetCount** | **Number** | Number of data sets in a share | [optional] [readonly] 
**description** | **String** | Description shared when the invitation was created | [optional] [readonly] 
**invitationId** | **String** | Unique id of the invitation. | 
**invitationStatus** | **String** | The status of the invitation. | [optional] [readonly] 
**location** | **String** | invitation location | [optional] [readonly] 
**providerEmail** | **String** | Email of the provider who created the resource | [optional] [readonly] 
**providerName** | **String** | Name of the provider who created the resource | [optional] [readonly] 
**providerTenantName** | **String** | Tenant name of the provider who created the resource | [optional] [readonly] 
**respondedAt** | **Date** | The time the recipient responded to the invitation. | [optional] [readonly] 
**sentAt** | **Date** | Gets the time at which the invitation was sent. | [optional] [readonly] 
**shareName** | **String** | Gets the source share Name. | [optional] [readonly] 
**termsOfUse** | **String** | Terms of use shared when the invitation was created | [optional] [readonly] 
**userEmail** | **String** | Email of the user who created the resource | [optional] [readonly] 
**userName** | **String** | Name of the user who created the resource | [optional] [readonly] 



## Enum: InvitationStatusEnum


* `Pending` (value: `"Pending"`)

* `Accepted` (value: `"Accepted"`)

* `Rejected` (value: `"Rejected"`)

* `Withdrawn` (value: `"Withdrawn"`)




