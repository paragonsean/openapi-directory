# GooglePayPassesApi.EventTicketClass

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowMultipleUsersPerObject** | **Boolean** | Deprecated. Use &#x60;multipleDevicesAndHoldersAllowedStatus&#x60; instead. | [optional] 
**callbackOptions** | [**CallbackOptions**](CallbackOptions.md) |  | [optional] 
**classTemplateInfo** | [**ClassTemplateInfo**](ClassTemplateInfo.md) |  | [optional] 
**confirmationCodeLabel** | **String** | The label to use for the confirmation code value (&#x60;eventTicketObject.reservationInfo.confirmationCode&#x60;) on the card detail view. Each available option maps to a set of localized strings, so that translations are shown to the user based on their locale. Both &#x60;confirmationCodeLabel&#x60; and &#x60;customConfirmationCodeLabel&#x60; may not be set. If neither is set, the label will default to \&quot;Confirmation Code\&quot;, localized. If the confirmation code field is unset, this label will not be used. | [optional] 
**countryCode** | **String** | Country code used to display the card&#39;s country (when the user is not in that country), as well as to display localized content when content is not available in the user&#39;s locale. | [optional] 
**customConfirmationCodeLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customGateLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customRowLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customSeatLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customSectionLabel** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**dateTime** | [**EventDateTime**](EventDateTime.md) |  | [optional] 
**enableSmartTap** | **Boolean** | Identifies whether this class supports Smart Tap. The &#x60;redemptionIssuers&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. | [optional] 
**eventId** | **String** | The ID of the event. This ID should be unique for every event in an account. It is used to group tickets together if the user has saved multiple tickets for the same event. It can be at most 64 characters. If provided, the grouping will be stable. Be wary of unintentional collision to avoid grouping tickets that should not be grouped. If you use only one class per event, you can simply set this to the &#x60;classId&#x60; (with or without the issuer ID portion). If not provided, the platform will attempt to use other data to group tickets (potentially unstable). | [optional] 
**eventName** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**finePrint** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**gateLabel** | **String** | The label to use for the gate value (&#x60;eventTicketObject.seatInfo.gate&#x60;) on the card detail view. Each available option maps to a set of localized strings, so that translations are shown to the user based on their locale. Both &#x60;gateLabel&#x60; and &#x60;customGateLabel&#x60; may not be set. If neither is set, the label will default to \&quot;Gate\&quot;, localized. If the gate field is unset, this label will not be used. | [optional] 
**heroImage** | [**Image**](Image.md) |  | [optional] 
**hexBackgroundColor** | **String** | The background color for the card. If not set the dominant color of the hero image is used, and if no hero image is set, the dominant color of the logo is used. The format is #rrggbb where rrggbb is a hex RGB triplet, such as &#x60;#ffcc00&#x60;. You can also use the shorthand version of the RGB triplet which is #rgb, such as &#x60;#fc0&#x60;. | [optional] 
**homepageUri** | [**Uri**](Uri.md) |  | [optional] 
**id** | **String** | Required. The unique identifier for a class. This ID must be unique across all classes from an issuer. This value should follow the format issuer ID. identifier where the former is issued by Google and latter is chosen by you. Your unique identifier should only include alphanumeric characters, &#39;.&#39;, &#39;_&#39;, or &#39;-&#39;. | [optional] 
**imageModulesData** | [**[ImageModuleData]**](ImageModuleData.md) | Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level. | [optional] 
**infoModuleData** | [**InfoModuleData**](InfoModuleData.md) |  | [optional] 
**issuerName** | **String** | Required. The issuer name. Recommended maximum length is 20 characters to ensure full string is displayed on smaller screens. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#eventTicketClass\&quot;&#x60;. | [optional] 
**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  | [optional] 
**localizedIssuerName** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**locations** | [**[LatLongPoint]**](LatLongPoint.md) | Note: This field is currently not supported to trigger geo notifications. | [optional] 
**logo** | [**Image**](Image.md) |  | [optional] 
**messages** | [**[Message]**](Message.md) | An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10. | [optional] 
**multipleDevicesAndHoldersAllowedStatus** | **String** | Identifies whether multiple users and devices will save the same object referencing this class. | [optional] 
**redemptionIssuers** | **[String]** | Identifies which redemption issuers can redeem the pass over Smart Tap. Redemption issuers are identified by their issuer ID. Redemption issuers must have at least one Smart Tap key configured. The &#x60;enableSmartTap&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. | [optional] 
**review** | [**Review**](Review.md) |  | [optional] 
**reviewStatus** | **String** | Required. The status of the class. This field can be set to &#x60;draft&#x60; or &#x60;underReview&#x60; using the insert, patch, or update API calls. Once the review state is changed from &#x60;draft&#x60; it may not be changed back to &#x60;draft&#x60;. You should keep this field to &#x60;draft&#x60; when the class is under development. A &#x60;draft&#x60; class cannot be used to create any object. You should set this field to &#x60;underReview&#x60; when you believe the class is ready for use. The platform will automatically set this field to &#x60;approved&#x60; and it can be immediately used to create or migrate objects. When updating an already &#x60;approved&#x60; class you should keep setting this field to &#x60;underReview&#x60;. | [optional] 
**rowLabel** | **String** | The label to use for the row value (&#x60;eventTicketObject.seatInfo.row&#x60;) on the card detail view. Each available option maps to a set of localized strings, so that translations are shown to the user based on their locale. Both &#x60;rowLabel&#x60; and &#x60;customRowLabel&#x60; may not be set. If neither is set, the label will default to \&quot;Row\&quot;, localized. If the row field is unset, this label will not be used. | [optional] 
**seatLabel** | **String** | The label to use for the seat value (&#x60;eventTicketObject.seatInfo.seat&#x60;) on the card detail view. Each available option maps to a set of localized strings, so that translations are shown to the user based on their locale. Both &#x60;seatLabel&#x60; and &#x60;customSeatLabel&#x60; may not be set. If neither is set, the label will default to \&quot;Seat\&quot;, localized. If the seat field is unset, this label will not be used. | [optional] 
**sectionLabel** | **String** | The label to use for the section value (&#x60;eventTicketObject.seatInfo.section&#x60;) on the card detail view. Each available option maps to a set of localized strings, so that translations are shown to the user based on their locale. Both &#x60;sectionLabel&#x60; and &#x60;customSectionLabel&#x60; may not be set. If neither is set, the label will default to \&quot;Section\&quot;, localized. If the section field is unset, this label will not be used. | [optional] 
**securityAnimation** | [**SecurityAnimation**](SecurityAnimation.md) |  | [optional] 
**textModulesData** | [**[TextModuleData]**](TextModuleData.md) | Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class. | [optional] 
**venue** | [**EventVenue**](EventVenue.md) |  | [optional] 
**version** | **String** | Deprecated | [optional] 
**viewUnlockRequirement** | **String** | View Unlock Requirement options for the event ticket. | [optional] 
**wordMark** | [**Image**](Image.md) |  | [optional] 



## Enum: ConfirmationCodeLabelEnum


* `CONFIRMATION_CODE_LABEL_UNSPECIFIED` (value: `"CONFIRMATION_CODE_LABEL_UNSPECIFIED"`)

* `CONFIRMATION_CODE` (value: `"CONFIRMATION_CODE"`)

* `confirmationCode` (value: `"confirmationCode"`)

* `CONFIRMATION_NUMBER` (value: `"CONFIRMATION_NUMBER"`)

* `confirmationNumber` (value: `"confirmationNumber"`)

* `ORDER_NUMBER` (value: `"ORDER_NUMBER"`)

* `orderNumber` (value: `"orderNumber"`)

* `RESERVATION_NUMBER` (value: `"RESERVATION_NUMBER"`)

* `reservationNumber` (value: `"reservationNumber"`)





## Enum: GateLabelEnum


* `GATE_LABEL_UNSPECIFIED` (value: `"GATE_LABEL_UNSPECIFIED"`)

* `GATE` (value: `"GATE"`)

* `gate` (value: `"gate"`)

* `DOOR` (value: `"DOOR"`)

* `door` (value: `"door"`)

* `ENTRANCE` (value: `"ENTRANCE"`)

* `entrance` (value: `"entrance"`)





## Enum: MultipleDevicesAndHoldersAllowedStatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `MULTIPLE_HOLDERS` (value: `"MULTIPLE_HOLDERS"`)

* `multipleHolders` (value: `"multipleHolders"`)

* `ONE_USER_ALL_DEVICES` (value: `"ONE_USER_ALL_DEVICES"`)

* `oneUserAllDevices` (value: `"oneUserAllDevices"`)

* `ONE_USER_ONE_DEVICE` (value: `"ONE_USER_ONE_DEVICE"`)

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





## Enum: RowLabelEnum


* `ROW_LABEL_UNSPECIFIED` (value: `"ROW_LABEL_UNSPECIFIED"`)

* `ROW` (value: `"ROW"`)

* `row` (value: `"row"`)





## Enum: SeatLabelEnum


* `SEAT_LABEL_UNSPECIFIED` (value: `"SEAT_LABEL_UNSPECIFIED"`)

* `SEAT` (value: `"SEAT"`)

* `seat` (value: `"seat"`)





## Enum: SectionLabelEnum


* `SECTION_LABEL_UNSPECIFIED` (value: `"SECTION_LABEL_UNSPECIFIED"`)

* `SECTION` (value: `"SECTION"`)

* `section` (value: `"section"`)

* `THEATER` (value: `"THEATER"`)

* `theater` (value: `"theater"`)





## Enum: ViewUnlockRequirementEnum


* `VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED` (value: `"VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED"`)

* `UNLOCK_NOT_REQUIRED` (value: `"UNLOCK_NOT_REQUIRED"`)

* `UNLOCK_REQUIRED_TO_VIEW` (value: `"UNLOCK_REQUIRED_TO_VIEW"`)




