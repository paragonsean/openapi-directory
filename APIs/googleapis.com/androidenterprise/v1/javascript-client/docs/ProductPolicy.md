# GooglePlayEmmApi.ProductPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoInstallPolicy** | [**AutoInstallPolicy**](AutoInstallPolicy.md) |  | [optional] 
**autoUpdateMode** | **String** | The auto-update mode for the product. When autoUpdateMode is used, it always takes precedence over the user&#39;s choice. So when a user makes changes to the device settings manually, these changes are ignored. | [optional] 
**enterpriseAuthenticationAppLinkConfigs** | [**[EnterpriseAuthenticationAppLinkConfig]**](EnterpriseAuthenticationAppLinkConfig.md) | An authentication URL configuration for the authenticator app of an identity provider. This helps to launch the identity provider&#39;s authenticator app during the authentication happening in a private app using Android WebView. Authenticator app should already be the default handler for the authentication url on the device. | [optional] 
**managedConfiguration** | [**ManagedConfiguration**](ManagedConfiguration.md) |  | [optional] 
**productId** | **String** | The ID of the product. For example, \&quot;app:com.google.android.gm\&quot;. | [optional] 
**trackIds** | **[String]** | Grants the device visibility to the specified product release track(s), identified by trackIds. The list of release tracks of a product can be obtained by calling Products.Get. | [optional] 
**tracks** | **[String]** | Deprecated. Use trackIds instead. | [optional] 



## Enum: AutoUpdateModeEnum


* `autoUpdateModeUnspecified` (value: `"autoUpdateModeUnspecified"`)

* `autoUpdateDefault` (value: `"autoUpdateDefault"`)

* `autoUpdatePostponed` (value: `"autoUpdatePostponed"`)

* `autoUpdateHighPriority` (value: `"autoUpdateHighPriority"`)





## Enum: [TracksEnum]


* `appTrackUnspecified` (value: `"appTrackUnspecified"`)

* `production` (value: `"production"`)

* `beta` (value: `"beta"`)

* `alpha` (value: `"alpha"`)




