

# FloodlightActivity

A single Floodlight activity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserIds** | **List&lt;String&gt;** | Output only. IDs of the advertisers that have access to the parent Floodlight group. Only advertisers under the provided partner ID will be listed in this field. |  [optional] [readonly] |
|**displayName** | **String** | Required. The display name of the Floodlight activity. |  [optional] |
|**floodlightActivityId** | **String** | Output only. The unique ID of the Floodlight activity. Assigned by the system. |  [optional] [readonly] |
|**floodlightGroupId** | **String** | Required. Immutable. The ID of the parent Floodlight group. |  [optional] |
|**name** | **String** | Output only. The resource name of the Floodlight activity. |  [optional] [readonly] |
|**remarketingConfigs** | [**List&lt;RemarketingConfig&gt;**](RemarketingConfig.md) | Output only. A list of configuration objects designating whether remarketing for this Floodlight Activity is enabled and available for a specifc advertiser. If enabled, this Floodlight Activity generates a remarketing user list that is able to be used in targeting under the advertiser. |  [optional] [readonly] |
|**servingStatus** | [**ServingStatusEnum**](#ServingStatusEnum) | Optional. Whether the Floodlight activity is served. |  [optional] |
|**sslRequired** | **Boolean** | Output only. Whether tags are required to be compliant. |  [optional] [readonly] |



## Enum: ServingStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;FLOODLIGHT_ACTIVITY_SERVING_STATUS_UNSPECIFIED&quot; |
| ENABLED | &quot;FLOODLIGHT_ACTIVITY_SERVING_STATUS_ENABLED&quot; |
| DISABLED | &quot;FLOODLIGHT_ACTIVITY_SERVING_STATUS_DISABLED&quot; |



