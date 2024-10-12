# CloudIdentityApi.ClientState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetTags** | **[String]** | The caller can specify asset tags for this resource | [optional] 
**complianceState** | **String** | The compliance state of the resource as specified by the API client. | [optional] 
**createTime** | **String** | Output only. The time the client state data was created. | [optional] [readonly] 
**customId** | **String** | This field may be used to store a unique identifier for the API resource within which these CustomAttributes are a field. | [optional] 
**etag** | **String** | The token that needs to be passed back for concurrency control in updates. Token needs to be passed back in UpdateRequest | [optional] 
**healthScore** | **String** | The Health score of the resource | [optional] 
**keyValuePairs** | [**{String: CustomAttributeValue}**](CustomAttributeValue.md) | The map of key-value attributes stored by callers specific to a device. The total serialized length of this map may not exceed 10KB. No limit is placed on the number of attributes in a map. | [optional] 
**lastUpdateTime** | **String** | Output only. The time the client state data was last updated. | [optional] [readonly] 
**managed** | **String** | The management state of the resource as specified by the API client. | [optional] 
**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the ClientState in format: &#x60;devices/{device_id}/deviceUsers/{device_user_id}/clientState/{partner_id}&#x60;, where partner_id corresponds to the partner storing the data. | [optional] [readonly] 
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




