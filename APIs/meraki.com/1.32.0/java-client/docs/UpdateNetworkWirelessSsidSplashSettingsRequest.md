

# UpdateNetworkWirelessSsidSplashSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowSimultaneousLogins** | **Boolean** | Whether or not to allow simultaneous logins from different devices. |  [optional] |
|**billing** | [**UpdateNetworkWirelessSsidSplashSettingsRequestBilling**](UpdateNetworkWirelessSsidSplashSettingsRequestBilling.md) |  |  [optional] |
|**blockAllTrafficBeforeSignOn** | **Boolean** | How restricted allowing traffic should be. If true, all traffic types are blocked until the splash page is acknowledged. If false, all non-HTTP traffic is allowed before the splash page is acknowledged. |  [optional] |
|**controllerDisconnectionBehavior** | [**ControllerDisconnectionBehaviorEnum**](#ControllerDisconnectionBehaviorEnum) | How login attempts should be handled when the controller is unreachable. Can be either &#39;open&#39;, &#39;restricted&#39;, or &#39;default&#39;. |  [optional] |
|**guestSponsorship** | [**UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship**](UpdateNetworkWirelessSsidSplashSettingsRequestGuestSponsorship.md) |  |  [optional] |
|**redirectUrl** | **String** | The custom redirect URL where the users will go after the splash page. |  [optional] |
|**sentryEnrollment** | [**UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment**](UpdateNetworkWirelessSsidSplashSettingsRequestSentryEnrollment.md) |  |  [optional] |
|**splashImage** | [**UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage**](UpdateNetworkWirelessSsidSplashSettingsRequestSplashImage.md) |  |  [optional] |
|**splashLogo** | [**UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo**](UpdateNetworkWirelessSsidSplashSettingsRequestSplashLogo.md) |  |  [optional] |
|**splashPrepaidFront** | [**UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront**](UpdateNetworkWirelessSsidSplashSettingsRequestSplashPrepaidFront.md) |  |  [optional] |
|**splashTimeout** | **Integer** | Splash timeout in minutes. This will determine how often users will see the splash page. |  [optional] |
|**splashUrl** | **String** | [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see &#39;useSplashUrl&#39; |  [optional] |
|**useRedirectUrl** | **Boolean** | The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page. A custom redirect URL must be set if this is true. |  [optional] |
|**useSplashUrl** | **Boolean** | [optional] Boolean indicating whether the users will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID&#39;s access control settings, it may not be possible to use the custom splash URL. |  [optional] |
|**welcomeMessage** | **String** | The welcome message for the users on the splash page. |  [optional] |



## Enum: ControllerDisconnectionBehaviorEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| OPEN | &quot;open&quot; |
| RESTRICTED | &quot;restricted&quot; |



