

# TransitClass


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationOptions** | [**ActivationOptions**](ActivationOptions.md) |  |  [optional] |
|**allowMultipleUsersPerObject** | **Boolean** | Deprecated. Use &#x60;multipleDevicesAndHoldersAllowedStatus&#x60; instead. |  [optional] |
|**callbackOptions** | [**CallbackOptions**](CallbackOptions.md) |  |  [optional] |
|**classTemplateInfo** | [**ClassTemplateInfo**](ClassTemplateInfo.md) |  |  [optional] |
|**countryCode** | **String** | Country code used to display the card&#39;s country (when the user is not in that country), as well as to display localized content when content is not available in the user&#39;s locale. |  [optional] |
|**customCarriageLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customCoachLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customConcessionCategoryLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customConfirmationCodeLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customDiscountMessageLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customFareClassLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customFareNameLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customOtherRestrictionsLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customPlatformLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customPurchaseFaceValueLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customPurchasePriceLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customPurchaseReceiptNumberLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customRouteRestrictionsDetailsLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customRouteRestrictionsLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customSeatLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customTicketNumberLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customTimeRestrictionsLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customTransitTerminusNameLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customZoneLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**enableSingleLegItinerary** | **Boolean** | Controls the display of the single-leg itinerary for this class. By default, an itinerary will only display for multi-leg trips. |  [optional] |
|**enableSmartTap** | **Boolean** | Identifies whether this class supports Smart Tap. The &#x60;redemptionIssuers&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. |  [optional] |
|**heroImage** | [**Image**](Image.md) |  |  [optional] |
|**hexBackgroundColor** | **String** | The background color for the card. If not set the dominant color of the hero image is used, and if no hero image is set, the dominant color of the logo is used. The format is #rrggbb where rrggbb is a hex RGB triplet, such as &#x60;#ffcc00&#x60;. You can also use the shorthand version of the RGB triplet which is #rgb, such as &#x60;#fc0&#x60;. |  [optional] |
|**homepageUri** | [**Uri**](Uri.md) |  |  [optional] |
|**id** | **String** | Required. The unique identifier for a class. This ID must be unique across all classes from an issuer. This value should follow the format issuer ID. identifier where the former is issued by Google and latter is chosen by you. Your unique identifier should only include alphanumeric characters, &#39;.&#39;, &#39;_&#39;, or &#39;-&#39;. |  [optional] |
|**imageModulesData** | [**List&lt;ImageModuleData&gt;**](ImageModuleData.md) | Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level. |  [optional] |
|**infoModuleData** | [**InfoModuleData**](InfoModuleData.md) |  |  [optional] |
|**issuerName** | **String** | Required. The issuer name. Recommended maximum length is 20 characters to ensure full string is displayed on smaller screens. |  [optional] |
|**languageOverride** | **String** | If this field is present, transit tickets served to a user&#39;s device will always be in this language. Represents the BCP 47 language tag. Example values are \&quot;en-US\&quot;, \&quot;en-GB\&quot;, \&quot;de\&quot;, or \&quot;de-AT\&quot;. |  [optional] |
|**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  |  [optional] |
|**localizedIssuerName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**locations** | [**List&lt;LatLongPoint&gt;**](LatLongPoint.md) | Note: This field is currently not supported to trigger geo notifications. |  [optional] |
|**logo** | [**Image**](Image.md) |  |  [optional] |
|**messages** | [**List&lt;Message&gt;**](Message.md) | An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10. |  [optional] |
|**multipleDevicesAndHoldersAllowedStatus** | [**MultipleDevicesAndHoldersAllowedStatusEnum**](#MultipleDevicesAndHoldersAllowedStatusEnum) | Identifies whether multiple users and devices will save the same object referencing this class. |  [optional] |
|**redemptionIssuers** | **List&lt;String&gt;** | Identifies which redemption issuers can redeem the pass over Smart Tap. Redemption issuers are identified by their issuer ID. Redemption issuers must have at least one Smart Tap key configured. The &#x60;enableSmartTap&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. |  [optional] |
|**review** | [**Review**](Review.md) |  |  [optional] |
|**reviewStatus** | [**ReviewStatusEnum**](#ReviewStatusEnum) | Required. The status of the class. This field can be set to &#x60;draft&#x60; or &#x60;underReview&#x60; using the insert, patch, or update API calls. Once the review state is changed from &#x60;draft&#x60; it may not be changed back to &#x60;draft&#x60;. You should keep this field to &#x60;draft&#x60; when the class is under development. A &#x60;draft&#x60; class cannot be used to create any object. You should set this field to &#x60;underReview&#x60; when you believe the class is ready for use. The platform will automatically set this field to &#x60;approved&#x60; and it can be immediately used to create or migrate objects. When updating an already &#x60;approved&#x60; class you should keep setting this field to &#x60;underReview&#x60;. |  [optional] |
|**securityAnimation** | [**SecurityAnimation**](SecurityAnimation.md) |  |  [optional] |
|**textModulesData** | [**List&lt;TextModuleData&gt;**](TextModuleData.md) | Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class. |  [optional] |
|**transitOperatorName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**transitType** | [**TransitTypeEnum**](#TransitTypeEnum) | Required. The type of transit this class represents, such as \&quot;bus\&quot;. |  [optional] |
|**version** | **String** | Deprecated |  [optional] |
|**viewUnlockRequirement** | [**ViewUnlockRequirementEnum**](#ViewUnlockRequirementEnum) | View Unlock Requirement options for the transit ticket. |  [optional] |
|**watermark** | [**Image**](Image.md) |  |  [optional] |
|**wideLogo** | [**Image**](Image.md) |  |  [optional] |
|**wordMark** | [**Image**](Image.md) |  |  [optional] |



## Enum: MultipleDevicesAndHoldersAllowedStatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| MULTIPLE_HOLDERS | &quot;MULTIPLE_HOLDERS&quot; |
| ONE_USER_ALL_DEVICES | &quot;ONE_USER_ALL_DEVICES&quot; |
| ONE_USER_ONE_DEVICE | &quot;ONE_USER_ONE_DEVICE&quot; |
| MULTIPLE_HOLDERS2 | &quot;multipleHolders&quot; |
| ONE_USER_ALL_DEVICES2 | &quot;oneUserAllDevices&quot; |
| ONE_USER_ONE_DEVICE2 | &quot;oneUserOneDevice&quot; |



## Enum: ReviewStatusEnum

| Name | Value |
|---- | -----|
| REVIEW_STATUS_UNSPECIFIED | &quot;REVIEW_STATUS_UNSPECIFIED&quot; |
| UNDER_REVIEW | &quot;UNDER_REVIEW&quot; |
| UNDER_REVIEW2 | &quot;underReview&quot; |
| APPROVED | &quot;APPROVED&quot; |
| APPROVED2 | &quot;approved&quot; |
| REJECTED | &quot;REJECTED&quot; |
| REJECTED2 | &quot;rejected&quot; |
| DRAFT | &quot;DRAFT&quot; |
| DRAFT2 | &quot;draft&quot; |



## Enum: TransitTypeEnum

| Name | Value |
|---- | -----|
| TRANSIT_TYPE_UNSPECIFIED | &quot;TRANSIT_TYPE_UNSPECIFIED&quot; |
| BUS | &quot;BUS&quot; |
| BUS2 | &quot;bus&quot; |
| RAIL | &quot;RAIL&quot; |
| RAIL2 | &quot;rail&quot; |
| TRAM | &quot;TRAM&quot; |
| TRAM2 | &quot;tram&quot; |
| FERRY | &quot;FERRY&quot; |
| FERRY2 | &quot;ferry&quot; |
| OTHER | &quot;OTHER&quot; |
| OTHER2 | &quot;other&quot; |



## Enum: ViewUnlockRequirementEnum

| Name | Value |
|---- | -----|
| VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED | &quot;VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED&quot; |
| UNLOCK_NOT_REQUIRED | &quot;UNLOCK_NOT_REQUIRED&quot; |
| UNLOCK_REQUIRED_TO_VIEW | &quot;UNLOCK_REQUIRED_TO_VIEW&quot; |



