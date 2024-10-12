

# UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment

Systems Manager sentry enrollment splash settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enforcedSystems** | **List&lt;String&gt;** | The system types that the Sentry enforces. Must be included in: &#39;iOS, &#39;Android&#39;, &#39;macOS&#39;, and &#39;Windows&#39;. |  [optional] |
|**strength** | [**StrengthEnum**](#StrengthEnum) | The strength of the enforcement of selected system types. Must be one of: &#39;focused&#39;, &#39;click-through&#39;, and &#39;strict&#39;. |  [optional] |
|**systemsManagerNetwork** | [**UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollmentSystemsManagerNetwork**](UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollmentSystemsManagerNetwork.md) |  |  [optional] |



## Enum: StrengthEnum

| Name | Value |
|---- | -----|
| CLICK_THROUGH | &quot;click-through&quot; |
| FOCUSED | &quot;focused&quot; |
| STRICT | &quot;strict&quot; |



