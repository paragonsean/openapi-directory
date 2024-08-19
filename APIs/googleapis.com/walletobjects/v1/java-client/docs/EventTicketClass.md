

# EventTicketClass


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowMultipleUsersPerObject** | **Boolean** | Deprecated. Use &#x60;multipleDevicesAndHoldersAllowedStatus&#x60; instead. |  [optional] |
|**callbackOptions** | [**CallbackOptions**](CallbackOptions.md) |  |  [optional] |
|**classTemplateInfo** | [**ClassTemplateInfo**](ClassTemplateInfo.md) |  |  [optional] |
|**confirmationCodeLabel** | [**ConfirmationCodeLabelEnum**](#ConfirmationCodeLabelEnum) | The label to use for the confirmation code value (&#x60;eventTicketObject.reservationInfo.confirmationCode&#x60;) on the card detail view. Each available option maps to a set of localized strings, so that translations are shown to the user based on their locale. Both &#x60;confirmationCodeLabel&#x60; and &#x60;customConfirmationCodeLabel&#x60; may not be set. If neither is set, the label will default to \&quot;Confirmation Code\&quot;, localized. If the confirmation code field is unset, this label will not be used. |  [optional] |
|**countryCode** | **String** | Country code used to display the card&#39;s country (when the user is not in that country), as well as to display localized content when content is not available in the user&#39;s locale. |  [optional] |
|**customConfirmationCodeLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customGateLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customRowLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customSeatLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customSectionLabel** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**dateTime** | [**EventDateTime**](EventDateTime.md) |  |  [optional] |
|**enableSmartTap** | **Boolean** | Identifies whether this class supports Smart Tap. The &#x60;redemptionIssuers&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. |  [optional] |
|**eventId** | **String** | The ID of the event. This ID should be unique for every event in an account. It is used to group tickets together if the user has saved multiple tickets for the same event. It can be at most 64 characters. If provided, the grouping will be stable. Be wary of unintentional collision to avoid grouping tickets that should not be grouped. If you use only one class per event, you can simply set this to the &#x60;classId&#x60; (with or without the issuer ID portion). If not provided, the platform will attempt to use other data to group tickets (potentially unstable). |  [optional] |
|**eventName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**finePrint** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**gateLabel** | [**GateLabelEnum**](#GateLabelEnum) | The label to use for the gate value (&#x60;eventTicketObject.seatInfo.gate&#x60;) on the card detail view. Each available option maps to a set of localized strings, so that translations are shown to the user based on their locale. Both &#x60;gateLabel&#x60; and &#x60;customGateLabel&#x60; may not be set. If neither is set, the label will default to \&quot;Gate\&quot;, localized. If the gate field is unset, this label will not be used. |  [optional] |
|**heroImage** | [**Image**](Image.md) |  |  [optional] |
|**hexBackgroundColor** | **String** | The background color for the card. If not set the dominant color of the hero image is used, and if no hero image is set, the dominant color of the logo is used. The format is #rrggbb where rrggbb is a hex RGB triplet, such as &#x60;#ffcc00&#x60;. You can also use the shorthand version of the RGB triplet which is #rgb, such as &#x60;#fc0&#x60;. |  [optional] |
|**homepageUri** | [**Uri**](Uri.md) |  |  [optional] |
|**id** | **String** | Required. The unique identifier for a class. This ID must be unique across all classes from an issuer. This value should follow the format issuer ID. identifier where the former is issued by Google and latter is chosen by you. Your unique identifier should only include alphanumeric characters, &#39;.&#39;, &#39;_&#39;, or &#39;-&#39;. |  [optional] |
|**imageModulesData** | [**List&lt;ImageModuleData&gt;**](ImageModuleData.md) | Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level. |  [optional] |
|**infoModuleData** | [**InfoModuleData**](InfoModuleData.md) |  |  [optional] |
|**issuerName** | **String** | Required. The issuer name. Recommended maximum length is 20 characters to ensure full string is displayed on smaller screens. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#eventTicketClass\&quot;&#x60;. |  [optional] |
|**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  |  [optional] |
|**localizedIssuerName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**locations** | [**List&lt;LatLongPoint&gt;**](LatLongPoint.md) | Note: This field is currently not supported to trigger geo notifications. |  [optional] |
|**logo** | [**Image**](Image.md) |  |  [optional] |
|**messages** | [**List&lt;Message&gt;**](Message.md) | An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10. |  [optional] |
|**multipleDevicesAndHoldersAllowedStatus** | [**MultipleDevicesAndHoldersAllowedStatusEnum**](#MultipleDevicesAndHoldersAllowedStatusEnum) | Identifies whether multiple users and devices will save the same object referencing this class. |  [optional] |
|**redemptionIssuers** | **List&lt;String&gt;** | Identifies which redemption issuers can redeem the pass over Smart Tap. Redemption issuers are identified by their issuer ID. Redemption issuers must have at least one Smart Tap key configured. The &#x60;enableSmartTap&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. |  [optional] |
|**review** | [**Review**](Review.md) |  |  [optional] |
|**reviewStatus** | [**ReviewStatusEnum**](#ReviewStatusEnum) | Required. The status of the class. This field can be set to &#x60;draft&#x60; or &#x60;underReview&#x60; using the insert, patch, or update API calls. Once the review state is changed from &#x60;draft&#x60; it may not be changed back to &#x60;draft&#x60;. You should keep this field to &#x60;draft&#x60; when the class is under development. A &#x60;draft&#x60; class cannot be used to create any object. You should set this field to &#x60;underReview&#x60; when you believe the class is ready for use. The platform will automatically set this field to &#x60;approved&#x60; and it can be immediately used to create or migrate objects. When updating an already &#x60;approved&#x60; class you should keep setting this field to &#x60;underReview&#x60;. |  [optional] |
|**rowLabel** | [**RowLabelEnum**](#RowLabelEnum) | The label to use for the row value (&#x60;eventTicketObject.seatInfo.row&#x60;) on the card detail view. Each available option maps to a set of localized strings, so that translations are shown to the user based on their locale. Both &#x60;rowLabel&#x60; and &#x60;customRowLabel&#x60; may not be set. If neither is set, the label will default to \&quot;Row\&quot;, localized. If the row field is unset, this label will not be used. |  [optional] |
|**seatLabel** | [**SeatLabelEnum**](#SeatLabelEnum) | The label to use for the seat value (&#x60;eventTicketObject.seatInfo.seat&#x60;) on the card detail view. Each available option maps to a set of localized strings, so that translations are shown to the user based on their locale. Both &#x60;seatLabel&#x60; and &#x60;customSeatLabel&#x60; may not be set. If neither is set, the label will default to \&quot;Seat\&quot;, localized. If the seat field is unset, this label will not be used. |  [optional] |
|**sectionLabel** | [**SectionLabelEnum**](#SectionLabelEnum) | The label to use for the section value (&#x60;eventTicketObject.seatInfo.section&#x60;) on the card detail view. Each available option maps to a set of localized strings, so that translations are shown to the user based on their locale. Both &#x60;sectionLabel&#x60; and &#x60;customSectionLabel&#x60; may not be set. If neither is set, the label will default to \&quot;Section\&quot;, localized. If the section field is unset, this label will not be used. |  [optional] |
|**securityAnimation** | [**SecurityAnimation**](SecurityAnimation.md) |  |  [optional] |
|**textModulesData** | [**List&lt;TextModuleData&gt;**](TextModuleData.md) | Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class. |  [optional] |
|**venue** | [**EventVenue**](EventVenue.md) |  |  [optional] |
|**version** | **String** | Deprecated |  [optional] |
|**viewUnlockRequirement** | [**ViewUnlockRequirementEnum**](#ViewUnlockRequirementEnum) | View Unlock Requirement options for the event ticket. |  [optional] |
|**wideLogo** | [**Image**](Image.md) |  |  [optional] |
|**wordMark** | [**Image**](Image.md) |  |  [optional] |



## Enum: ConfirmationCodeLabelEnum

| Name | Value |
|---- | -----|
| CONFIRMATION_CODE_LABEL_UNSPECIFIED | &quot;CONFIRMATION_CODE_LABEL_UNSPECIFIED&quot; |
| CONFIRMATION_CODE | &quot;CONFIRMATION_CODE&quot; |
| CONFIRMATION_CODE2 | &quot;confirmationCode&quot; |
| CONFIRMATION_NUMBER | &quot;CONFIRMATION_NUMBER&quot; |
| CONFIRMATION_NUMBER2 | &quot;confirmationNumber&quot; |
| ORDER_NUMBER | &quot;ORDER_NUMBER&quot; |
| ORDER_NUMBER2 | &quot;orderNumber&quot; |
| RESERVATION_NUMBER | &quot;RESERVATION_NUMBER&quot; |
| RESERVATION_NUMBER2 | &quot;reservationNumber&quot; |



## Enum: GateLabelEnum

| Name | Value |
|---- | -----|
| GATE_LABEL_UNSPECIFIED | &quot;GATE_LABEL_UNSPECIFIED&quot; |
| GATE | &quot;GATE&quot; |
| GATE2 | &quot;gate&quot; |
| DOOR | &quot;DOOR&quot; |
| DOOR2 | &quot;door&quot; |
| ENTRANCE | &quot;ENTRANCE&quot; |
| ENTRANCE2 | &quot;entrance&quot; |



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



## Enum: RowLabelEnum

| Name | Value |
|---- | -----|
| ROW_LABEL_UNSPECIFIED | &quot;ROW_LABEL_UNSPECIFIED&quot; |
| ROW | &quot;ROW&quot; |
| ROW2 | &quot;row&quot; |



## Enum: SeatLabelEnum

| Name | Value |
|---- | -----|
| SEAT_LABEL_UNSPECIFIED | &quot;SEAT_LABEL_UNSPECIFIED&quot; |
| SEAT | &quot;SEAT&quot; |
| SEAT2 | &quot;seat&quot; |



## Enum: SectionLabelEnum

| Name | Value |
|---- | -----|
| SECTION_LABEL_UNSPECIFIED | &quot;SECTION_LABEL_UNSPECIFIED&quot; |
| SECTION | &quot;SECTION&quot; |
| SECTION2 | &quot;section&quot; |
| THEATER | &quot;THEATER&quot; |
| THEATER2 | &quot;theater&quot; |



## Enum: ViewUnlockRequirementEnum

| Name | Value |
|---- | -----|
| VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED | &quot;VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED&quot; |
| UNLOCK_NOT_REQUIRED | &quot;UNLOCK_NOT_REQUIRED&quot; |
| UNLOCK_REQUIRED_TO_VIEW | &quot;UNLOCK_REQUIRED_TO_VIEW&quot; |



