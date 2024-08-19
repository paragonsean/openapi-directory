

# MediationGroupMediationGroupLine

Settings for an ad network used by a mediation group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adSourceId** | **String** | The ID of the ad source this mediation line is associated with. |  [optional] |
|**adUnitMappings** | **Map&lt;String, String&gt;** | References of the ad unit mappings for each ad unit associated with this mediation line. Key is the ad unit ID, value is resource name of the ad unit mapping. For mediation lines where the ad source id is the AdMob Network, ad unit mappings will be ignored. |  [optional] |
|**cpmMicros** | **String** | The CPM for this allocation line. $0.01 is the minimum allowed amount. For LIVE CPM modes, the default amount is $0.01. This value is ignored if &#x60;cpm_mode&#x60; is &#x60;LIVE&#x60;. **Warning:** \&quot;USD\&quot; is the only supported currency at the moment. The unit is in micros. |  [optional] |
|**cpmMode** | [**CpmModeEnum**](#CpmModeEnum) | Indicates how the CPM for this mediation line is provided. Note that &#x60;MANUAL&#x60; and &#x60;LIVE&#x60; are the only fully-supported mode at the moment. Please use the AdMob UI (https://admob.google.com) if you wish to create or update to other cpm modes. |  [optional] |
|**displayName** | **String** | User-provided label for this mediation line. The maximum length allowed is 255 characters. |  [optional] |
|**experimentVariant** | [**ExperimentVariantEnum**](#ExperimentVariantEnum) | Output only. The Mediation A/B experiment variant to which the mediation group line belongs to. |  [optional] [readonly] |
|**id** | **String** | The 16 digit ID for this mediation line e.g. 0123456789012345. When creating a new mediation group line, use a distinct negative integer as the ID place holder. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The status of the mediation group line. Only enabled mediation group lines will be served. |  [optional] |



## Enum: CpmModeEnum

| Name | Value |
|---- | -----|
| CPM_MODE_UNSPECIFIED | &quot;CPM_MODE_UNSPECIFIED&quot; |
| LIVE | &quot;LIVE&quot; |
| MANUAL | &quot;MANUAL&quot; |
| ANO | &quot;ANO&quot; |



## Enum: ExperimentVariantEnum

| Name | Value |
|---- | -----|
| VARIANT_UNSPECIFIED | &quot;VARIANT_UNSPECIFIED&quot; |
| VARIANT_A | &quot;VARIANT_A&quot; |
| VARIANT_B | &quot;VARIANT_B&quot; |
| ORIGINAL | &quot;ORIGINAL&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |



