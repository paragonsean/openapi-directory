

# GoogleAnalyticsAdminV1alphaGoogleSignalsSettings

Settings values for Google Signals. This is a singleton resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consent** | [**ConsentEnum**](#ConsentEnum) | Output only. Terms of Service acceptance. |  [optional] [readonly] |
|**name** | **String** | Output only. Resource name of this setting. Format: properties/{property_id}/googleSignalsSettings Example: \&quot;properties/1000/googleSignalsSettings\&quot; |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Status of this setting. |  [optional] |



## Enum: ConsentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;GOOGLE_SIGNALS_CONSENT_UNSPECIFIED&quot; |
| CONSENTED | &quot;GOOGLE_SIGNALS_CONSENT_CONSENTED&quot; |
| NOT_CONSENTED | &quot;GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;GOOGLE_SIGNALS_STATE_UNSPECIFIED&quot; |
| ENABLED | &quot;GOOGLE_SIGNALS_ENABLED&quot; |
| DISABLED | &quot;GOOGLE_SIGNALS_DISABLED&quot; |



