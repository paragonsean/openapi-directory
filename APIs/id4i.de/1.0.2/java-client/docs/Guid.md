

# Guid


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTimestamp** | **Long** | The UTC unix timestamp of when this GUID has been created |  [optional] [readonly] |
|**holderOrganizationId** | **String** | Organization namespace of the GUID holder |  [optional] [readonly] |
|**id4n** | **String** | The ID |  [optional] [readonly] |
|**ownerOrganizationId** | **String** | Organization namespace of the GUID owner |  [optional] [readonly] |
|**physicalState** | [**PhysicalStateEnum**](#PhysicalStateEnum) | Physical attachment state of the GUID |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | The properties of the organization |  [optional] [readonly] |



## Enum: PhysicalStateEnum

| Name | Value |
|---- | -----|
| UNATTACHED | &quot;UNATTACHED&quot; |
| ATTACHED | &quot;ATTACHED&quot; |
| DETACHED | &quot;DETACHED&quot; |



