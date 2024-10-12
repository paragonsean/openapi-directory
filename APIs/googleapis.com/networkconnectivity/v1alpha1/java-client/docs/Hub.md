

# Hub

Network Connectivity Center is a hub-and-spoke abstraction for network connectivity management in Google Cloud. It reduces operational complexity through a simple, centralized connectivity management model. Following is the resource message of a hub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Time when the Hub was created. |  [optional] |
|**description** | **String** | Short description of the hub resource. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels. |  [optional] |
|**name** | **String** | Immutable. The name of a Hub resource. |  [optional] |
|**spokes** | **List&lt;String&gt;** | Output only. A list of the URIs of all attached spokes. This field is deprecated and will not be included in future API versions. Call ListSpokes on each region instead. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current lifecycle state of this Hub. |  [optional] [readonly] |
|**uniqueId** | **String** | Output only. Google-generated UUID for this resource. This is unique across all Hub resources. If a Hub resource is deleted and another with the same name is created, it gets a different unique_id. |  [optional] [readonly] |
|**updateTime** | **String** | Time when the Hub was updated. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |



