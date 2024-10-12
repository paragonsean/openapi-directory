

# Product

A Products resource represents an app in the Google Play store that is available to at least some users in the enterprise. (Some apps are restricted to a single enterprise, and no information about them is made available outside that enterprise.) The information provided for each product (localized name, icon, link to the full Google Play details page) is intended to allow a basic representation of the product within an EMM user interface.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appRestrictionsSchema** | [**AppRestrictionsSchema**](AppRestrictionsSchema.md) |  |  [optional] |
|**appTracks** | [**List&lt;TrackInfo&gt;**](TrackInfo.md) | The tracks visible to the enterprise. |  [optional] |
|**appVersion** | [**List&lt;AppVersion&gt;**](AppVersion.md) | App versions currently available for this product. |  [optional] |
|**authorName** | **String** | The name of the author of the product (for example, the app developer). |  [optional] |
|**availableCountries** | **List&lt;String&gt;** | The countries which this app is available in. |  [optional] |
|**availableTracks** | [**List&lt;AvailableTracksEnum&gt;**](#List&lt;AvailableTracksEnum&gt;) | Deprecated, use appTracks instead. |  [optional] |
|**category** | **String** | The app category (e.g. RACING, SOCIAL, etc.) |  [optional] |
|**contentRating** | [**ContentRatingEnum**](#ContentRatingEnum) | The content rating for this app. |  [optional] |
|**description** | **String** | The localized promotional description, if available. |  [optional] |
|**detailsUrl** | **String** | A link to the (consumer) Google Play details page for the product. |  [optional] |
|**distributionChannel** | [**DistributionChannelEnum**](#DistributionChannelEnum) | How and to whom the package is made available. The value publicGoogleHosted means that the package is available through the Play store and not restricted to a specific enterprise. The value privateGoogleHosted means that the package is a private app (restricted to an enterprise) but hosted by Google. The value privateSelfHosted means that the package is a private app (restricted to an enterprise) and is privately hosted. |  [optional] |
|**features** | [**List&lt;FeaturesEnum&gt;**](#List&lt;FeaturesEnum&gt;) | Noteworthy features (if any) of this product. |  [optional] |
|**fullDescription** | **String** | The localized full app store description, if available. |  [optional] |
|**iconUrl** | **String** | A link to an image that can be used as an icon for the product. This image is suitable for use at up to 512px x 512px. |  [optional] |
|**lastUpdatedTimestampMillis** | **String** | The approximate time (within 7 days) the app was last published, expressed in milliseconds since epoch. |  [optional] |
|**minAndroidSdkVersion** | **Integer** | The minimum Android SDK necessary to run the app. |  [optional] |
|**permissions** | [**List&lt;ProductPermission&gt;**](ProductPermission.md) | A list of permissions required by the app. |  [optional] |
|**productId** | **String** | A string of the form *app:&lt;package name&gt;*. For example, app:com.google.android.gm represents the Gmail app. |  [optional] |
|**productPricing** | [**ProductPricingEnum**](#ProductPricingEnum) | Whether this product is free, free with in-app purchases, or paid. If the pricing is unknown, this means the product is not generally available anymore (even though it might still be available to people who own it). |  [optional] |
|**recentChanges** | **String** | A description of the recent changes made to the app. |  [optional] |
|**requiresContainerApp** | **Boolean** | Deprecated. |  [optional] |
|**screenshotUrls** | **List&lt;String&gt;** | A list of screenshot links representing the app. |  [optional] |
|**signingCertificate** | [**ProductSigningCertificate**](ProductSigningCertificate.md) |  |  [optional] |
|**smallIconUrl** | **String** | A link to a smaller image that can be used as an icon for the product. This image is suitable for use at up to 128px x 128px. |  [optional] |
|**title** | **String** | The name of the product. |  [optional] |
|**workDetailsUrl** | **String** | A link to the managed Google Play details page for the product, for use by an Enterprise admin. |  [optional] |



## Enum: List&lt;AvailableTracksEnum&gt;

| Name | Value |
|---- | -----|
| APP_TRACK_UNSPECIFIED | &quot;appTrackUnspecified&quot; |
| PRODUCTION | &quot;production&quot; |
| BETA | &quot;beta&quot; |
| ALPHA | &quot;alpha&quot; |



## Enum: ContentRatingEnum

| Name | Value |
|---- | -----|
| RATING_UNKNOWN | &quot;ratingUnknown&quot; |
| ALL | &quot;all&quot; |
| PRE_TEEN | &quot;preTeen&quot; |
| TEEN | &quot;teen&quot; |
| MATURE | &quot;mature&quot; |



## Enum: DistributionChannelEnum

| Name | Value |
|---- | -----|
| PUBLIC_GOOGLE_HOSTED | &quot;publicGoogleHosted&quot; |
| PRIVATE_GOOGLE_HOSTED | &quot;privateGoogleHosted&quot; |
| PRIVATE_SELF_HOSTED | &quot;privateSelfHosted&quot; |



## Enum: List&lt;FeaturesEnum&gt;

| Name | Value |
|---- | -----|
| FEATURE_UNKNOWN | &quot;featureUnknown&quot; |
| VPN_APP | &quot;vpnApp&quot; |



## Enum: ProductPricingEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| FREE | &quot;free&quot; |
| FREE_WITH_IN_APP_PURCHASE | &quot;freeWithInAppPurchase&quot; |
| PAID | &quot;paid&quot; |



