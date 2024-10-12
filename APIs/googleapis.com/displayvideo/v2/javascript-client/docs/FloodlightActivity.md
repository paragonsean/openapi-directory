# DisplayVideo360Api.FloodlightActivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiserIds** | **[String]** | Output only. IDs of the advertisers that have access to the parent Floodlight group. Only advertisers under the provided partner ID will be listed in this field. | [optional] [readonly] 
**displayName** | **String** | Required. The display name of the Floodlight activity. | [optional] 
**floodlightActivityId** | **String** | Output only. The unique ID of the Floodlight activity. Assigned by the system. | [optional] [readonly] 
**floodlightGroupId** | **String** | Required. Immutable. The ID of the parent Floodlight group. | [optional] 
**name** | **String** | Output only. The resource name of the Floodlight activity. | [optional] [readonly] 
**remarketingConfigs** | [**[RemarketingConfig]**](RemarketingConfig.md) | Output only. A list of configuration objects designating whether remarketing for this Floodlight Activity is enabled and available for a specifc advertiser. If enabled, this Floodlight Activity generates a remarketing user list that is able to be used in targeting under the advertiser. | [optional] [readonly] 
**servingStatus** | **String** | Optional. Whether the Floodlight activity is served. | [optional] 
**sslRequired** | **Boolean** | Output only. Whether tags are required to be compliant. | [optional] [readonly] 



## Enum: ServingStatusEnum


* `UNSPECIFIED` (value: `"FLOODLIGHT_ACTIVITY_SERVING_STATUS_UNSPECIFIED"`)

* `ENABLED` (value: `"FLOODLIGHT_ACTIVITY_SERVING_STATUS_ENABLED"`)

* `DISABLED` (value: `"FLOODLIGHT_ACTIVITY_SERVING_STATUS_DISABLED"`)




