# GooglePlayEmmApi.Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appRestrictionsSchema** | [**AppRestrictionsSchema**](AppRestrictionsSchema.md) |  | [optional] 
**appTracks** | [**[TrackInfo]**](TrackInfo.md) | The tracks visible to the enterprise. | [optional] 
**appVersion** | [**[AppVersion]**](AppVersion.md) | App versions currently available for this product. | [optional] 
**authorName** | **String** | The name of the author of the product (for example, the app developer). | [optional] 
**availableCountries** | **[String]** | The countries which this app is available in. | [optional] 
**availableTracks** | **[String]** | Deprecated, use appTracks instead. | [optional] 
**category** | **String** | The app category (e.g. RACING, SOCIAL, etc.) | [optional] 
**contentRating** | **String** | The content rating for this app. | [optional] 
**description** | **String** | The localized promotional description, if available. | [optional] 
**detailsUrl** | **String** | A link to the (consumer) Google Play details page for the product. | [optional] 
**distributionChannel** | **String** | How and to whom the package is made available. The value publicGoogleHosted means that the package is available through the Play store and not restricted to a specific enterprise. The value privateGoogleHosted means that the package is a private app (restricted to an enterprise) but hosted by Google. The value privateSelfHosted means that the package is a private app (restricted to an enterprise) and is privately hosted. | [optional] 
**features** | **[String]** | Noteworthy features (if any) of this product. | [optional] 
**fullDescription** | **String** | The localized full app store description, if available. | [optional] 
**iconUrl** | **String** | A link to an image that can be used as an icon for the product. This image is suitable for use at up to 512px x 512px. | [optional] 
**lastUpdatedTimestampMillis** | **String** | The approximate time (within 7 days) the app was last published, expressed in milliseconds since epoch. | [optional] 
**minAndroidSdkVersion** | **Number** | The minimum Android SDK necessary to run the app. | [optional] 
**permissions** | [**[ProductPermission]**](ProductPermission.md) | A list of permissions required by the app. | [optional] 
**productId** | **String** | A string of the form *app:&lt;package name&gt;*. For example, app:com.google.android.gm represents the Gmail app. | [optional] 
**productPricing** | **String** | Whether this product is free, free with in-app purchases, or paid. If the pricing is unknown, this means the product is not generally available anymore (even though it might still be available to people who own it). | [optional] 
**recentChanges** | **String** | A description of the recent changes made to the app. | [optional] 
**requiresContainerApp** | **Boolean** | Deprecated. | [optional] 
**screenshotUrls** | **[String]** | A list of screenshot links representing the app. | [optional] 
**signingCertificate** | [**ProductSigningCertificate**](ProductSigningCertificate.md) |  | [optional] 
**smallIconUrl** | **String** | A link to a smaller image that can be used as an icon for the product. This image is suitable for use at up to 128px x 128px. | [optional] 
**title** | **String** | The name of the product. | [optional] 
**workDetailsUrl** | **String** | A link to the managed Google Play details page for the product, for use by an Enterprise admin. | [optional] 



## Enum: [AvailableTracksEnum]


* `appTrackUnspecified` (value: `"appTrackUnspecified"`)

* `production` (value: `"production"`)

* `beta` (value: `"beta"`)

* `alpha` (value: `"alpha"`)





## Enum: ContentRatingEnum


* `ratingUnknown` (value: `"ratingUnknown"`)

* `all` (value: `"all"`)

* `preTeen` (value: `"preTeen"`)

* `teen` (value: `"teen"`)

* `mature` (value: `"mature"`)





## Enum: DistributionChannelEnum


* `publicGoogleHosted` (value: `"publicGoogleHosted"`)

* `privateGoogleHosted` (value: `"privateGoogleHosted"`)

* `privateSelfHosted` (value: `"privateSelfHosted"`)





## Enum: [FeaturesEnum]


* `featureUnknown` (value: `"featureUnknown"`)

* `vpnApp` (value: `"vpnApp"`)





## Enum: ProductPricingEnum


* `unknown` (value: `"unknown"`)

* `free` (value: `"free"`)

* `freeWithInAppPurchase` (value: `"freeWithInAppPurchase"`)

* `paid` (value: `"paid"`)




