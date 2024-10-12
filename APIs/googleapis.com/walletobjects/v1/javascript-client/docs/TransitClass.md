# GoogleWalletApi.TransitClass

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationOptions** | [**ActivationOptions**](ActivationOptions.md) |  | [optional] 
**allowMultipleUsersPerObject** | **Boolean** | Deprecated. Use &#x60;multipleDevicesAndHoldersAllowedStatus&#x60; instead. | [optional] 
**callbackOptions** | [**CallbackOptions**](CallbackOptions.md) |  | [optional] 
**classTemplateInfo** | [**ClassTemplateInfo**](ClassTemplateInfo.md) |  | [optional] 
**countryCode** | **String** | Country code used to display the card&#39;s country (when the user is not in that country), as well as to display localized content when content is not available in the user&#39;s locale. | [optional] 
**customCarriageLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customCoachLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customConcessionCategoryLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customConfirmationCodeLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customDiscountMessageLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customFareClassLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customFareNameLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customOtherRestrictionsLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customPlatformLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customPurchaseFaceValueLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customPurchasePriceLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customPurchaseReceiptNumberLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customRouteRestrictionsDetailsLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customRouteRestrictionsLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customSeatLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customTicketNumberLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customTimeRestrictionsLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customTransitTerminusNameLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customZoneLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**enableSingleLegItinerary** | **Boolean** | Controls the display of the single-leg itinerary for this class. By default, an itinerary will only display for multi-leg trips. | [optional] 
**enableSmartTap** | **Boolean** | Identifies whether this class supports Smart Tap. The &#x60;redemptionIssuers&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. | [optional] 
**heroImage** | [**Image**](Image.md) |  | [optional] 
**hexBackgroundColor** | **String** | The background color for the card. If not set the dominant color of the hero image is used, and if no hero image is set, the dominant color of the logo is used. The format is #rrggbb where rrggbb is a hex RGB triplet, such as &#x60;#ffcc00&#x60;. You can also use the shorthand version of the RGB triplet which is #rgb, such as &#x60;#fc0&#x60;. | [optional] 
**homepageUri** | [**Uri**](Uri.md) |  | [optional] 
**id** | **String** | Required. The unique identifier for a class. This ID must be unique across all classes from an issuer. This value should follow the format issuer ID. identifier where the former is issued by Google and latter is chosen by you. Your unique identifier should only include alphanumeric characters, &#39;.&#39;, &#39;_&#39;, or &#39;-&#39;. | [optional] 
**imageModulesData** | [**[ImageModuleData]**](ImageModuleData.md) | Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level. | [optional] 
**infoModuleData** | [**InfoModuleData**](InfoModuleData.md) |  | [optional] 
**issuerName** | **String** | Required. The issuer name. Recommended maximum length is 20 characters to ensure full string is displayed on smaller screens. | [optional] 
**languageOverride** | **String** | If this field is present, transit tickets served to a user&#39;s device will always be in this language. Represents the BCP 47 language tag. Example values are \&quot;en-US\&quot;, \&quot;en-GB\&quot;, \&quot;de\&quot;, or \&quot;de-AT\&quot;. | [optional] 
**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  | [optional] 
**localizedIssuerName** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**locations** | [**[LatLongPoint]**](LatLongPoint.md) | Note: This field is currently not supported to trigger geo notifications. | [optional] 
**logo** | [**Image**](Image.md) |  | [optional] 
**messages** | [**[Message]**](Message.md) | An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10. | [optional] 
**multipleDevicesAndHoldersAllowedStatus** | **String** | Identifies whether multiple users and devices will save the same object referencing this class. | [optional] 
**redemptionIssuers** | **[String]** | Identifies which redemption issuers can redeem the pass over Smart Tap. Redemption issuers are identified by their issuer ID. Redemption issuers must have at least one Smart Tap key configured. The &#x60;enableSmartTap&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. | [optional] 
**review** | [**Review**](Review.md) |  | [optional] 
**reviewStatus** | **String** | Required. The status of the class. This field can be set to &#x60;draft&#x60; or &#x60;underReview&#x60; using the insert, patch, or update API calls. Once the review state is changed from &#x60;draft&#x60; it may not be changed back to &#x60;draft&#x60;. You should keep this field to &#x60;draft&#x60; when the class is under development. A &#x60;draft&#x60; class cannot be used to create any object. You should set this field to &#x60;underReview&#x60; when you believe the class is ready for use. The platform will automatically set this field to &#x60;approved&#x60; and it can be immediately used to create or migrate objects. When updating an already &#x60;approved&#x60; class you should keep setting this field to &#x60;underReview&#x60;. | [optional] 
**securityAnimation** | [**SecurityAnimation**](SecurityAnimation.md) |  | [optional] 
**textModulesData** | [**[TextModuleData]**](TextModuleData.md) | Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class. | [optional] 
**transitOperatorName** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**transitType** | **String** | Required. The type of transit this class represents, such as \&quot;bus\&quot;. | [optional] 
**version** | **String** | Deprecated | [optional] 
**viewUnlockRequirement** | **String** | View Unlock Requirement options for the transit ticket. | [optional] 
**watermark** | [**Image**](Image.md) |  | [optional] 
**wideLogo** | [**Image**](Image.md) |  | [optional] 
**wordMark** | [**Image**](Image.md) |  | [optional] 



## Enum: MultipleDevicesAndHoldersAllowedStatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `MULTIPLE_HOLDERS` (value: `"MULTIPLE_HOLDERS"`)

* `ONE_USER_ALL_DEVICES` (value: `"ONE_USER_ALL_DEVICES"`)

* `ONE_USER_ONE_DEVICE` (value: `"ONE_USER_ONE_DEVICE"`)

* `multipleHolders` (value: `"multipleHolders"`)

* `oneUserAllDevices` (value: `"oneUserAllDevices"`)

* `oneUserOneDevice` (value: `"oneUserOneDevice"`)





## Enum: ReviewStatusEnum


* `REVIEW_STATUS_UNSPECIFIED` (value: `"REVIEW_STATUS_UNSPECIFIED"`)

* `UNDER_REVIEW` (value: `"UNDER_REVIEW"`)

* `underReview` (value: `"underReview"`)

* `APPROVED` (value: `"APPROVED"`)

* `approved` (value: `"approved"`)

* `REJECTED` (value: `"REJECTED"`)

* `rejected` (value: `"rejected"`)

* `DRAFT` (value: `"DRAFT"`)

* `draft` (value: `"draft"`)





## Enum: TransitTypeEnum


* `TRANSIT_TYPE_UNSPECIFIED` (value: `"TRANSIT_TYPE_UNSPECIFIED"`)

* `BUS` (value: `"BUS"`)

* `bus` (value: `"bus"`)

* `RAIL` (value: `"RAIL"`)

* `rail` (value: `"rail"`)

* `TRAM` (value: `"TRAM"`)

* `tram` (value: `"tram"`)

* `FERRY` (value: `"FERRY"`)

* `ferry` (value: `"ferry"`)

* `OTHER` (value: `"OTHER"`)

* `other` (value: `"other"`)





## Enum: ViewUnlockRequirementEnum


* `VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED` (value: `"VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED"`)

* `UNLOCK_NOT_REQUIRED` (value: `"UNLOCK_NOT_REQUIRED"`)

* `UNLOCK_REQUIRED_TO_VIEW` (value: `"UNLOCK_REQUIRED_TO_VIEW"`)




