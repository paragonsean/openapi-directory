

# ServiceProjectAttachment

ServiceProjectAttachment represents an attachment from a service project to a host project. Service projects contain the underlying cloud infrastructure resources, and expose these resources to the host project through a ServiceProjectAttachment. With the attachments, the host project can provide an aggregated view of resources across all service projects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Create time. |  [optional] [readonly] |
|**name** | **String** | Identifier. The resource name of a ServiceProjectAttachment. Format: \&quot;projects/{host-project-id}/locations/global/serviceProjectAttachments/{service-project-id}.\&quot; |  [optional] |
|**serviceProject** | **String** | Required. Immutable. Service project name in the format: \&quot;projects/abc\&quot; or \&quot;projects/123\&quot;. As input, project name with either project id or number are accepted. As output, this field will contain project number. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. ServiceProjectAttachment state. |  [optional] [readonly] |
|**uid** | **String** | Output only. A globally unique identifier (in UUID4 format) for the &#x60;ServiceProjectAttachment&#x60;. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |



