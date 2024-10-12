

# BusinessCallsSettings

Business calls settings for a location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callsState** | [**CallsStateEnum**](#CallsStateEnum) | Required. The state of this location&#39;s enrollment in Business calls. |  [optional] |
|**consentTime** | **String** | Input only. Time when the end user provided consent to the API user to enable business calls. |  [optional] |
|**name** | **String** | Required. The resource name of the calls settings. Format: locations/{location}/businesscallssettings |  [optional] |



## Enum: CallsStateEnum

| Name | Value |
|---- | -----|
| CALLS_STATE_UNSPECIFIED | &quot;CALLS_STATE_UNSPECIFIED&quot; |
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |



