# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **[String]** | Optional. If set, only return changes that match one or more of these types of actions. | [optional] 
**actorEmail** | **[String]** | Optional. If set, only return changes if they are made by a user in this list. | [optional] 
**earliestChangeTime** | **String** | Optional. If set, only return changes made after this time (inclusive). | [optional] 
**latestChangeTime** | **String** | Optional. If set, only return changes made before this time (inclusive). | [optional] 
**pageSize** | **Number** | Optional. The maximum number of ChangeHistoryEvent items to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 items will be returned. The maximum value is 200 (higher values will be coerced to the maximum). | [optional] 
**pageToken** | **String** | Optional. A page token, received from a previous &#x60;SearchChangeHistoryEvents&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;SearchChangeHistoryEvents&#x60; must match the call that provided the page token. | [optional] 
**property** | **String** | Optional. Resource name for a child property. If set, only return changes made to this property or its child resources. Format: properties/{propertyId} Example: \&quot;properties/100\&quot; | [optional] 
**resourceType** | **[String]** | Optional. If set, only return changes if they are for a resource that matches at least one of these types. | [optional] 



## Enum: [ActionEnum]


* `ACTION_TYPE_UNSPECIFIED` (value: `"ACTION_TYPE_UNSPECIFIED"`)

* `CREATED` (value: `"CREATED"`)

* `UPDATED` (value: `"UPDATED"`)

* `DELETED` (value: `"DELETED"`)





## Enum: [ResourceTypeEnum]


* `CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED` (value: `"CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED"`)

* `ACCOUNT` (value: `"ACCOUNT"`)

* `PROPERTY` (value: `"PROPERTY"`)

* `FIREBASE_LINK` (value: `"FIREBASE_LINK"`)

* `GOOGLE_ADS_LINK` (value: `"GOOGLE_ADS_LINK"`)

* `GOOGLE_SIGNALS_SETTINGS` (value: `"GOOGLE_SIGNALS_SETTINGS"`)

* `CONVERSION_EVENT` (value: `"CONVERSION_EVENT"`)

* `MEASUREMENT_PROTOCOL_SECRET` (value: `"MEASUREMENT_PROTOCOL_SECRET"`)

* `DATA_RETENTION_SETTINGS` (value: `"DATA_RETENTION_SETTINGS"`)

* `DISPLAY_VIDEO_360_ADVERTISER_LINK` (value: `"DISPLAY_VIDEO_360_ADVERTISER_LINK"`)

* `DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL` (value: `"DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL"`)

* `DATA_STREAM` (value: `"DATA_STREAM"`)

* `ATTRIBUTION_SETTINGS` (value: `"ATTRIBUTION_SETTINGS"`)




