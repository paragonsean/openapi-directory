

# GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest

Request message for SearchChangeHistoryEvents RPC.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**List&lt;ActionEnum&gt;**](#List&lt;ActionEnum&gt;) | Optional. If set, only return changes that match one or more of these types of actions. |  [optional] |
|**actorEmail** | **List&lt;String&gt;** | Optional. If set, only return changes if they are made by a user in this list. |  [optional] |
|**earliestChangeTime** | **String** | Optional. If set, only return changes made after this time (inclusive). |  [optional] |
|**latestChangeTime** | **String** | Optional. If set, only return changes made before this time (inclusive). |  [optional] |
|**pageSize** | **Integer** | Optional. The maximum number of ChangeHistoryEvent items to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 items will be returned. The maximum value is 200 (higher values will be coerced to the maximum). |  [optional] |
|**pageToken** | **String** | Optional. A page token, received from a previous &#x60;SearchChangeHistoryEvents&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;SearchChangeHistoryEvents&#x60; must match the call that provided the page token. |  [optional] |
|**property** | **String** | Optional. Resource name for a child property. If set, only return changes made to this property or its child resources. Format: properties/{propertyId} Example: \&quot;properties/100\&quot; |  [optional] |
|**resourceType** | [**List&lt;ResourceTypeEnum&gt;**](#List&lt;ResourceTypeEnum&gt;) | Optional. If set, only return changes if they are for a resource that matches at least one of these types. |  [optional] |



## Enum: List&lt;ActionEnum&gt;

| Name | Value |
|---- | -----|
| ACTION_TYPE_UNSPECIFIED | &quot;ACTION_TYPE_UNSPECIFIED&quot; |
| CREATED | &quot;CREATED&quot; |
| UPDATED | &quot;UPDATED&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: List&lt;ResourceTypeEnum&gt;

| Name | Value |
|---- | -----|
| CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED | &quot;CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED&quot; |
| ACCOUNT | &quot;ACCOUNT&quot; |
| PROPERTY | &quot;PROPERTY&quot; |
| FIREBASE_LINK | &quot;FIREBASE_LINK&quot; |
| GOOGLE_ADS_LINK | &quot;GOOGLE_ADS_LINK&quot; |
| GOOGLE_SIGNALS_SETTINGS | &quot;GOOGLE_SIGNALS_SETTINGS&quot; |
| CONVERSION_EVENT | &quot;CONVERSION_EVENT&quot; |
| MEASUREMENT_PROTOCOL_SECRET | &quot;MEASUREMENT_PROTOCOL_SECRET&quot; |
| CUSTOM_DIMENSION | &quot;CUSTOM_DIMENSION&quot; |
| CUSTOM_METRIC | &quot;CUSTOM_METRIC&quot; |
| DATA_RETENTION_SETTINGS | &quot;DATA_RETENTION_SETTINGS&quot; |
| DISPLAY_VIDEO_360_ADVERTISER_LINK | &quot;DISPLAY_VIDEO_360_ADVERTISER_LINK&quot; |
| DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL | &quot;DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL&quot; |
| SEARCH_ADS_360_LINK | &quot;SEARCH_ADS_360_LINK&quot; |
| DATA_STREAM | &quot;DATA_STREAM&quot; |
| ATTRIBUTION_SETTINGS | &quot;ATTRIBUTION_SETTINGS&quot; |
| EXPANDED_DATA_SET | &quot;EXPANDED_DATA_SET&quot; |
| CHANNEL_GROUP | &quot;CHANNEL_GROUP&quot; |
| ENHANCED_MEASUREMENT_SETTINGS | &quot;ENHANCED_MEASUREMENT_SETTINGS&quot; |
| DATA_REDACTION_SETTINGS | &quot;DATA_REDACTION_SETTINGS&quot; |
| SKADNETWORK_CONVERSION_VALUE_SCHEMA | &quot;SKADNETWORK_CONVERSION_VALUE_SCHEMA&quot; |
| ADSENSE_LINK | &quot;ADSENSE_LINK&quot; |
| AUDIENCE | &quot;AUDIENCE&quot; |
| EVENT_CREATE_RULE | &quot;EVENT_CREATE_RULE&quot; |
| CALCULATED_METRIC | &quot;CALCULATED_METRIC&quot; |



