# Id4iApi.Guid

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTimestamp** | **Number** | The UTC unix timestamp of when this GUID has been created | [optional] [readonly] 
**holderOrganizationId** | **String** | Organization namespace of the GUID holder | [optional] [readonly] 
**id4n** | **String** | The ID | [optional] [readonly] 
**ownerOrganizationId** | **String** | Organization namespace of the GUID owner | [optional] [readonly] 
**physicalState** | **String** | Physical attachment state of the GUID | [optional] 
**properties** | **{String: String}** | The properties of the organization | [optional] [readonly] 



## Enum: PhysicalStateEnum


* `UNATTACHED` (value: `"UNATTACHED"`)

* `ATTACHED` (value: `"ATTACHED"`)

* `DETACHED` (value: `"DETACHED"`)




