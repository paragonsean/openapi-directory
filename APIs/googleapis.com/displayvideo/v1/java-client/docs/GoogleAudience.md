

# GoogleAudience

Describes a Google audience resource. Includes Google audience lists.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Output only. The display name of the Google audience. . |  [optional] [readonly] |
|**googleAudienceId** | **String** | Output only. The unique ID of the Google audience. Assigned by the system. |  [optional] [readonly] |
|**googleAudienceType** | [**GoogleAudienceTypeEnum**](#GoogleAudienceTypeEnum) | Output only. The type of Google audience. . |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of the google audience. |  [optional] [readonly] |



## Enum: GoogleAudienceTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;GOOGLE_AUDIENCE_TYPE_UNSPECIFIED&quot; |
| AFFINITY | &quot;GOOGLE_AUDIENCE_TYPE_AFFINITY&quot; |
| IN_MARKET | &quot;GOOGLE_AUDIENCE_TYPE_IN_MARKET&quot; |
| INSTALLED_APPS | &quot;GOOGLE_AUDIENCE_TYPE_INSTALLED_APPS&quot; |
| NEW_MOBILE_DEVICES | &quot;GOOGLE_AUDIENCE_TYPE_NEW_MOBILE_DEVICES&quot; |
| LIFE_EVENT | &quot;GOOGLE_AUDIENCE_TYPE_LIFE_EVENT&quot; |
| EXTENDED_DEMOGRAPHIC | &quot;GOOGLE_AUDIENCE_TYPE_EXTENDED_DEMOGRAPHIC&quot; |



