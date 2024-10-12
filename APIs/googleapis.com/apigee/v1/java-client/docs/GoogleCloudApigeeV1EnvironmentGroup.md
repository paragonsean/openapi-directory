

# GoogleCloudApigeeV1EnvironmentGroup

EnvironmentGroup configuration. An environment group is used to group one or more Apigee environments under a single host name.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | Output only. The time at which the environment group was created as milliseconds since epoch. |  [optional] [readonly] |
|**hostnames** | **List&lt;String&gt;** | Required. Host names for this environment group. |  [optional] |
|**lastModifiedAt** | **String** | Output only. The time at which the environment group was last updated as milliseconds since epoch. |  [optional] [readonly] |
|**name** | **String** | ID of the environment group. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the environment group. Values other than ACTIVE means the resource is not ready to use. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |



