

# ClientState

Represents the state associated with an API client calling the Devices API. Resource representing ClientState and supports updates from API users

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetTags** | **List&lt;String&gt;** | The caller can specify asset tags for this resource |  [optional] |
|**complianceState** | [**ComplianceStateEnum**](#ComplianceStateEnum) | The compliance state of the resource as specified by the API client. |  [optional] |
|**createTime** | **String** | Output only. The time the client state data was created. |  [optional] [readonly] |
|**customId** | **String** | This field may be used to store a unique identifier for the API resource within which these CustomAttributes are a field. |  [optional] |
|**etag** | **String** | The token that needs to be passed back for concurrency control in updates. Token needs to be passed back in UpdateRequest |  [optional] |
|**healthScore** | [**HealthScoreEnum**](#HealthScoreEnum) | The Health score of the resource |  [optional] |
|**keyValuePairs** | [**Map&lt;String, CustomAttributeValue&gt;**](CustomAttributeValue.md) | The map of key-value attributes stored by callers specific to a device. The total serialized length of this map may not exceed 10KB. No limit is placed on the number of attributes in a map. |  [optional] |
|**lastUpdateTime** | **String** | Output only. The time the client state data was last updated. |  [optional] [readonly] |
|**managed** | [**ManagedEnum**](#ManagedEnum) | The management state of the resource as specified by the API client. |  [optional] |
|**name** | **String** | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the ClientState in format: &#x60;devices/{device_id}/deviceUsers/{device_user_id}/clientState/{partner_id}&#x60;, where partner_id corresponds to the partner storing the data. |  [optional] [readonly] |
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



