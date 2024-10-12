

# Organization

The root node in the resource hierarchy to which a particular entity's (a company, for example) resources belong.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp when the Organization was created. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. Timestamp when the Organization was requested for deletion. |  [optional] [readonly] |
|**directoryCustomerId** | **String** | Immutable. The G Suite / Workspace customer id used in the Directory API. |  [optional] |
|**displayName** | **String** | Output only. A human-readable string that refers to the organization in the Google Cloud Console. This string is set by the server and cannot be changed. The string will be set to the primary domain (for example, \&quot;google.com\&quot;) of the Google Workspace customer that owns the organization. |  [optional] [readonly] |
|**etag** | **String** | Output only. A checksum computed by the server based on the current value of the Organization resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of the organization. This is the organization&#39;s relative path in the API. Its format is \&quot;organizations/[organization_id]\&quot;. For example, \&quot;organizations/1234\&quot;. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The organization&#39;s current lifecycle state. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Timestamp when the Organization was last modified. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETE_REQUESTED | &quot;DELETE_REQUESTED&quot; |



