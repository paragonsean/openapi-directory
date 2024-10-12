

# ProductPolicy

The policy for a product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoInstallPolicy** | [**AutoInstallPolicy**](AutoInstallPolicy.md) |  |  [optional] |
|**autoUpdateMode** | [**AutoUpdateModeEnum**](#AutoUpdateModeEnum) | The auto-update mode for the product. When autoUpdateMode is used, it always takes precedence over the user&#39;s choice. So when a user makes changes to the device settings manually, these changes are ignored. |  [optional] |
|**enterpriseAuthenticationAppLinkConfigs** | [**List&lt;EnterpriseAuthenticationAppLinkConfig&gt;**](EnterpriseAuthenticationAppLinkConfig.md) | An authentication URL configuration for the authenticator app of an identity provider. This helps to launch the identity provider&#39;s authenticator app during the authentication happening in a private app using Android WebView. Authenticator app should already be the default handler for the authentication url on the device. |  [optional] |
|**managedConfiguration** | [**ManagedConfiguration**](ManagedConfiguration.md) |  |  [optional] |
|**productId** | **String** | The ID of the product. For example, \&quot;app:com.google.android.gm\&quot;. |  [optional] |
|**trackIds** | **List&lt;String&gt;** | Grants the device visibility to the specified product release track(s), identified by trackIds. The list of release tracks of a product can be obtained by calling Products.Get. |  [optional] |
|**tracks** | [**List&lt;TracksEnum&gt;**](#List&lt;TracksEnum&gt;) | Deprecated. Use trackIds instead. |  [optional] |



## Enum: AutoUpdateModeEnum

| Name | Value |
|---- | -----|
| AUTO_UPDATE_MODE_UNSPECIFIED | &quot;autoUpdateModeUnspecified&quot; |
| AUTO_UPDATE_DEFAULT | &quot;autoUpdateDefault&quot; |
| AUTO_UPDATE_POSTPONED | &quot;autoUpdatePostponed&quot; |
| AUTO_UPDATE_HIGH_PRIORITY | &quot;autoUpdateHighPriority&quot; |



## Enum: List&lt;TracksEnum&gt;

| Name | Value |
|---- | -----|
| APP_TRACK_UNSPECIFIED | &quot;appTrackUnspecified&quot; |
| PRODUCTION | &quot;production&quot; |
| BETA | &quot;beta&quot; |
| ALPHA | &quot;alpha&quot; |



