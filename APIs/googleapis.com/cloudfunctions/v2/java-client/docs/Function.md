

# Function

Describes a Cloud Function that contains user computation executed in response to an event. It encapsulates function and trigger configurations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buildConfig** | [**BuildConfig**](BuildConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. The create timestamp of a Cloud Function. This is only applicable to 2nd Gen functions. |  [optional] [readonly] |
|**description** | **String** | User-provided description of a function. |  [optional] |
|**environment** | [**EnvironmentEnum**](#EnvironmentEnum) | Describe whether the function is 1st Gen or 2nd Gen. |  [optional] |
|**eventTrigger** | [**EventTrigger**](EventTrigger.md) |  |  [optional] |
|**kmsKeyName** | **String** | [Preview] Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function resources. It must match the pattern &#x60;projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}&#x60;. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels associated with this Cloud Function. |  [optional] |
|**name** | **String** | A user-defined name of the function. Function names must be unique globally and match pattern &#x60;projects/_*_/locations/_*_/functions/_*&#x60; |  [optional] |
|**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**serviceConfig** | [**ServiceConfig**](ServiceConfig.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the function. |  [optional] [readonly] |
|**stateMessages** | [**List&lt;GoogleCloudFunctionsV2StateMessage&gt;**](GoogleCloudFunctionsV2StateMessage.md) | Output only. State Messages for this Cloud Function. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The last update timestamp of a Cloud Function. |  [optional] [readonly] |
|**upgradeInfo** | [**UpgradeInfo**](UpgradeInfo.md) |  |  [optional] |
|**url** | **String** | Output only. The deployed url for the function. |  [optional] [readonly] |



## Enum: EnvironmentEnum

| Name | Value |
|---- | -----|
| ENVIRONMENT_UNSPECIFIED | &quot;ENVIRONMENT_UNSPECIFIED&quot; |
| GEN_1 | &quot;GEN_1&quot; |
| GEN_2 | &quot;GEN_2&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| FAILED | &quot;FAILED&quot; |
| DEPLOYING | &quot;DEPLOYING&quot; |
| DELETING | &quot;DELETING&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



