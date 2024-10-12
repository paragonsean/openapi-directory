

# GoogleAppsCloudidentityDevicesV1ClientState

Represents the state associated with an API client calling the Devices API. Resource representing ClientState and supports updates from API users

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetTags** | **List&lt;String&gt;** | The caller can specify asset tags for this resource |  [optional] |
|**complianceState** | [**ComplianceStateEnum**](#ComplianceStateEnum) | The compliance state of the resource as specified by the API client. |  [optional] |
|**createTime** | **String** | Output only. The time the client state data was created. |  [optional] [readonly] |
|**customId** | **String** | This field may be used to store a unique identifier for the API resource within which these CustomAttributes are a field. |  [optional] |
|**etag** | **String** | The token that needs to be passed back for concurrency control in updates. Token needs to be passed back in UpdateRequest |  [optional] |
|**healthScore** | [**HealthScoreEnum**](#HealthScoreEnum) | The Health score of the resource. The Health score is the callers specification of the condition of the device from a usability point of view. For example, a third-party device management provider may specify a health score based on its compliance with organizational policies. |  [optional] |
|**keyValuePairs** | [**Map&lt;String, GoogleAppsCloudidentityDevicesV1CustomAttributeValue&gt;**](GoogleAppsCloudidentityDevicesV1CustomAttributeValue.md) | The map of key-value attributes stored by callers specific to a device. The total serialized length of this map may not exceed 10KB. No limit is placed on the number of attributes in a map. |  [optional] |
|**lastUpdateTime** | **String** | Output only. The time the client state data was last updated. |  [optional] [readonly] |
|**managed** | [**ManagedEnum**](#ManagedEnum) | The management state of the resource as specified by the API client. |  [optional] |
|**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the ClientState in format: &#x60;devices/{device}/deviceUsers/{device_user}/clientState/{partner}&#x60;, where partner corresponds to the partner storing the data. For partners belonging to the \&quot;BeyondCorp Alliance\&quot;, this is the partner ID specified to you by Google. For all other callers, this is a string of the form: &#x60;{customer}-suffix&#x60;, where &#x60;customer&#x60; is your customer ID. The *suffix* is any string the caller specifies. This string will be displayed verbatim in the administration console. This suffix is used in setting up Custom Access Levels in Context-Aware Access. Your organization&#39;s customer ID can be obtained from the URL: &#x60;GET https://www.googleapis.com/admin/directory/v1/customers/my_customer&#x60; The &#x60;id&#x60; field in the response contains the customer ID starting with the letter &#39;C&#39;. The customer ID to be used in this API is the string after the letter &#39;C&#39; (not including &#39;C&#39;) |  [optional] [readonly] |
|**ownerType** | [**OwnerTypeEnum**](#OwnerTypeEnum) | Output only. The owner of the ClientState |  [optional] [readonly] |
|**scoreReason** | **String** | A descriptive cause of the health score. |  [optional] |



## Enum: ComplianceStateEnum

| Name | Value |
|---- | -----|
| COMPLIANCE_STATE_UNSPECIFIED | &quot;COMPLIANCE_STATE_UNSPECIFIED&quot; |
| COMPLIANT | &quot;COMPLIANT&quot; |
| NON_COMPLIANT | &quot;NON_COMPLIANT&quot; |



## Enum: HealthScoreEnum

| Name | Value |
|---- | -----|
| HEALTH_SCORE_UNSPECIFIED | &quot;HEALTH_SCORE_UNSPECIFIED&quot; |
| VERY_POOR | &quot;VERY_POOR&quot; |
| POOR | &quot;POOR&quot; |
| NEUTRAL | &quot;NEUTRAL&quot; |
| GOOD | &quot;GOOD&quot; |
| VERY_GOOD | &quot;VERY_GOOD&quot; |



## Enum: ManagedEnum

| Name | Value |
|---- | -----|
| MANAGED_STATE_UNSPECIFIED | &quot;MANAGED_STATE_UNSPECIFIED&quot; |
| MANAGED | &quot;MANAGED&quot; |
| UNMANAGED | &quot;UNMANAGED&quot; |



## Enum: OwnerTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;OWNER_TYPE_UNSPECIFIED&quot; |
| CUSTOMER | &quot;OWNER_TYPE_CUSTOMER&quot; |
| PARTNER | &quot;OWNER_TYPE_PARTNER&quot; |



