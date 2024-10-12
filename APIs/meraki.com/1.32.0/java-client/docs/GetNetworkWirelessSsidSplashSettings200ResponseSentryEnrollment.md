

# GetNetworkWirelessSsidSplashSettings200ResponseSentryEnrollment

Systems Manager sentry enrollment splash settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enforcedSystems** | **List&lt;String&gt;** | The system types that the Sentry enforces. |  [optional] |
|**strength** | [**StrengthEnum**](#StrengthEnum) | The strength of the enforcement of selected system types. |  [optional] |
|**systemsManagerNetwork** | [**GetNetworkWirelessSsidSplashSettings200ResponseSentryEnrollmentSystemsManagerNetwork**](GetNetworkWirelessSsidSplashSettings200ResponseSentryEnrollmentSystemsManagerNetwork.md) |  |  [optional] |



## Enum: StrengthEnum

| Name | Value |
|---- | -----|
| CLICK_THROUGH | &quot;click-through&quot; |
| FOCUSED | &quot;focused&quot; |
| STRICT | &quot;strict&quot; |



