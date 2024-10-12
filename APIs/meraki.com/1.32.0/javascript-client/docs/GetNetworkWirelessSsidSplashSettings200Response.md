# MerakiDashboardApi.GetNetworkWirelessSsidSplashSettings200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowSimultaneousLogins** | **Boolean** | Whether or not to allow simultaneous logins from different devices. | [optional] 
**billing** | [**GetNetworkWirelessSsidSplashSettings200ResponseBilling**](GetNetworkWirelessSsidSplashSettings200ResponseBilling.md) |  | [optional] 
**blockAllTrafficBeforeSignOn** | **Boolean** | How restricted allowing traffic should be. If true, all traffic types are blocked until the splash page is acknowledged. If false, all non-HTTP traffic is allowed before the splash page is acknowledged. | [optional] 
**controllerDisconnectionBehavior** | **String** | How login attempts should be handled when the controller is unreachable. | [optional] 
**guestSponsorship** | [**GetNetworkWirelessSsidSplashSettings200ResponseGuestSponsorship**](GetNetworkWirelessSsidSplashSettings200ResponseGuestSponsorship.md) |  | [optional] 
**redirectUrl** | **String** | The custom redirect URL where the users will go after the splash page. | [optional] 
**selfRegistration** | [**GetNetworkWirelessSsidSplashSettings200ResponseSelfRegistration**](GetNetworkWirelessSsidSplashSettings200ResponseSelfRegistration.md) |  | [optional] 
**sentryEnrollment** | [**GetNetworkWirelessSsidSplashSettings200ResponseSentryEnrollment**](GetNetworkWirelessSsidSplashSettings200ResponseSentryEnrollment.md) |  | [optional] 
**splashImage** | [**GetNetworkWirelessSsidSplashSettings200ResponseSplashImage**](GetNetworkWirelessSsidSplashSettings200ResponseSplashImage.md) |  | [optional] 
**splashLogo** | [**GetNetworkWirelessSsidSplashSettings200ResponseSplashLogo**](GetNetworkWirelessSsidSplashSettings200ResponseSplashLogo.md) |  | [optional] 
**splashPage** | **String** | The type of splash page for this SSID | [optional] 
**splashPrepaidFront** | [**GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront**](GetNetworkWirelessSsidSplashSettings200ResponseSplashPrepaidFront.md) |  | [optional] 
**splashTimeout** | **Number** | Splash timeout in minutes. | [optional] 
**splashUrl** | **String** | The custom splash URL of the click-through splash page. | [optional] 
**ssidNumber** | **Number** | SSID number | [optional] 
**useRedirectUrl** | **Boolean** | The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page. | [optional] 
**useSplashUrl** | **Boolean** | Boolean indicating whether the users will be redirected to the custom splash url | [optional] 
**welcomeMessage** | **String** | The welcome message for the users on the splash page. | [optional] 


