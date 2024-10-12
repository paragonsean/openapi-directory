# CloudIdentityApi.GoogleAppsCloudidentityDevicesV1ClientState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetTags** | **[String]** | The caller can specify asset tags for this resource | [optional] 
**complianceState** | **String** | The compliance state of the resource as specified by the API client. | [optional] 
**createTime** | **String** | Output only. The time the client state data was created. | [optional] [readonly] 
**customId** | **String** | This field may be used to store a unique identifier for the API resource within which these CustomAttributes are a field. | [optional] 
**etag** | **String** | The token that needs to be passed back for concurrency control in updates. Token needs to be passed back in UpdateRequest | [optional] 
**healthScore** | **String** | The Health score of the resource. The Health score is the callers specification of the condition of the device from a usability point of view. For example, a third-party device management provider may specify a health score based on its compliance with organizational policies. | [optional] 
**keyValuePairs** | [**{String: GoogleAppsCloudidentityDevicesV1CustomAttributeValue}**](GoogleAppsCloudidentityDevicesV1CustomAttributeValue.md) | The map of key-value attributes stored by callers specific to a device. The total serialized length of this map may not exceed 10KB. No limit is placed on the number of attributes in a map. | [optional] 
**lastUpdateTime** | **String** | Output only. The time the client state data was last updated. | [optional] [readonly] 
**managed** | **String** | The management state of the resource as specified by the API client. | [optional] 
**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the ClientState in format: &#x60;devices/{device}/deviceUsers/{device_user}/clientState/{partner}&#x60;, where partner corresponds to the partner storing the data. For partners belonging to the \&quot;BeyondCorp Alliance\&quot;, this is the partner ID specified to you by Google. For all other callers, this is a string of the form: &#x60;{customer}-suffix&#x60;, where &#x60;customer&#x60; is your customer ID. The *suffix* is any string the caller specifies. This string will be displayed verbatim in the administration console. This suffix is used in setting up Custom Access Levels in Context-Aware Access. Your organization&#39;s customer ID can be obtained from the URL: &#x60;GET https://www.googleapis.com/admin/directory/v1/customers/my_customer&#x60; The &#x60;id&#x60; field in the response contains the customer ID starting with the letter &#39;C&#39;. The customer ID to be used in this API is the string after the letter &#39;C&#39; (not including &#39;C&#39;) | [optional] [readonly] 
**ownerType** | **String** | Output only. The owner of the ClientState | [optional] [readonly] 
**scoreReason** | **String** | A descriptive cause of the health score. | [optional] 



## Enum: ComplianceStateEnum


* `COMPLIANCE_STATE_UNSPECIFIED` (value: `"COMPLIANCE_STATE_UNSPECIFIED"`)

* `COMPLIANT` (value: `"COMPLIANT"`)

* `NON_COMPLIANT` (value: `"NON_COMPLIANT"`)





## Enum: HealthScoreEnum


* `HEALTH_SCORE_UNSPECIFIED` (value: `"HEALTH_SCORE_UNSPECIFIED"`)

* `VERY_POOR` (value: `"VERY_POOR"`)

* `POOR` (value: `"POOR"`)

* `NEUTRAL` (value: `"NEUTRAL"`)

* `GOOD` (value: `"GOOD"`)

* `VERY_GOOD` (value: `"VERY_GOOD"`)





## Enum: ManagedEnum


* `MANAGED_STATE_UNSPECIFIED` (value: `"MANAGED_STATE_UNSPECIFIED"`)

* `MANAGED` (value: `"MANAGED"`)

* `UNMANAGED` (value: `"UNMANAGED"`)





## Enum: OwnerTypeEnum


* `UNSPECIFIED` (value: `"OWNER_TYPE_UNSPECIFIED"`)

* `CUSTOMER` (value: `"OWNER_TYPE_CUSTOMER"`)

* `PARTNER` (value: `"OWNER_TYPE_PARTNER"`)




