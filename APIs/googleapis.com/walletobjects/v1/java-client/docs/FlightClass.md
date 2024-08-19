

# FlightClass


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowMultipleUsersPerObject** | **Boolean** | Deprecated. Use &#x60;multipleDevicesAndHoldersAllowedStatus&#x60; instead. |  [optional] |
|**boardingAndSeatingPolicy** | [**BoardingAndSeatingPolicy**](BoardingAndSeatingPolicy.md) |  |  [optional] |
|**callbackOptions** | [**CallbackOptions**](CallbackOptions.md) |  |  [optional] |
|**classTemplateInfo** | [**ClassTemplateInfo**](ClassTemplateInfo.md) |  |  [optional] |
|**countryCode** | **String** | Country code used to display the card&#39;s country (when the user is not in that country), as well as to display localized content when content is not available in the user&#39;s locale. |  [optional] |
|**destination** | [**AirportInfo**](AirportInfo.md) |  |  [optional] |
|**enableSmartTap** | **Boolean** | Identifies whether this class supports Smart Tap. The &#x60;redemptionIssuers&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. |  [optional] |
|**flightHeader** | [**FlightHeader**](FlightHeader.md) |  |  [optional] |
|**flightStatus** | [**FlightStatusEnum**](#FlightStatusEnum) | Status of this flight. If unset, Google will compute status based on data from other sources, such as FlightStats, etc. Note: Google-computed status will not be returned in API responses. |  [optional] |
|**heroImage** | [**Image**](Image.md) |  |  [optional] |
|**hexBackgroundColor** | **String** | The background color for the card. If not set the dominant color of the hero image is used, and if no hero image is set, the dominant color of the logo is used. The format is #rrggbb where rrggbb is a hex RGB triplet, such as &#x60;#ffcc00&#x60;. You can also use the shorthand version of the RGB triplet which is #rgb, such as &#x60;#fc0&#x60;. |  [optional] |
|**homepageUri** | [**Uri**](Uri.md) |  |  [optional] |
|**id** | **String** | Required. The unique identifier for a class. This ID must be unique across all classes from an issuer. This value should follow the format issuer ID. identifier where the former is issued by Google and latter is chosen by you. Your unique identifier should only include alphanumeric characters, &#39;.&#39;, &#39;_&#39;, or &#39;-&#39;. |  [optional] |
|**imageModulesData** | [**List&lt;ImageModuleData&gt;**](ImageModuleData.md) | Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level. |  [optional] |
|**infoModuleData** | [**InfoModuleData**](InfoModuleData.md) |  |  [optional] |
|**issuerName** | **String** | Required. The issuer name. Recommended maximum length is 20 characters to ensure full string is displayed on smaller screens. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#flightClass\&quot;&#x60;. |  [optional] |
|**languageOverride** | **String** | If this field is present, boarding passes served to a user&#39;s device will always be in this language. Represents the BCP 47 language tag. Example values are \&quot;en-US\&quot;, \&quot;en-GB\&quot;, \&quot;de\&quot;, or \&quot;de-AT\&quot;. |  [optional] |
|**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  |  [optional] |
|**localBoardingDateTime** | **String** | The boarding time as it would be printed on the boarding pass. This is an ISO 8601 extended format date/time without an offset. Time may be specified up to millisecond precision. eg: &#x60;2027-03-05T06:30:00&#x60; This should be the local date/time at the airport (not a UTC time). Google will reject the request if UTC offset is provided. Time zones will be calculated by Google based on departure airport. If this is not set, Google will set it based on data from other sources. |  [optional] |
|**localEstimatedOrActualArrivalDateTime** | **String** | The estimated time the aircraft plans to reach the destination gate (not the runway) or the actual time it reached the gate. This field should be set if at least one of the below is true: - It differs from the scheduled time. Google will use it to calculate the delay. - The aircraft already arrived at the gate. Google will use it to inform the user that the flight has arrived at the gate. This is an ISO 8601 extended format date/time without an offset. Time may be specified up to millisecond precision. eg: &#x60;2027-03-05T06:30:00&#x60; This should be the local date/time at the airport (not a UTC time). Google will reject the request if UTC offset is provided. Time zones will be calculated by Google based on arrival airport. If this is not set, Google will set it based on data from other sources. |  [optional] |
|**localEstimatedOrActualDepartureDateTime** | **String** | The estimated time the aircraft plans to pull from the gate or the actual time the aircraft already pulled from the gate. Note: This is not the runway time. This field should be set if at least one of the below is true: - It differs from the scheduled time. Google will use it to calculate the delay. - The aircraft already pulled from the gate. Google will use it to inform the user when the flight actually departed. This is an ISO 8601 extended format date/time without an offset. Time may be specified up to millisecond precision. eg: &#x60;2027-03-05T06:30:00&#x60; This should be the local date/time at the airport (not a UTC time). Google will reject the request if UTC offset is provided. Time zones will be calculated by Google based on departure airport. If this is not set, Google will set it based on data from other sources. |  [optional] |
|**localGateClosingDateTime** | **String** | The gate closing time as it would be printed on the boarding pass. Do not set this field if you do not want to print it in the boarding pass. This is an ISO 8601 extended format date/time without an offset. Time may be specified up to millisecond precision. eg: &#x60;2027-03-05T06:30:00&#x60; This should be the local date/time at the airport (not a UTC time). Google will reject the request if UTC offset is provided. Time zones will be calculated by Google based on departure airport. |  [optional] |
|**localScheduledArrivalDateTime** | **String** | The scheduled time the aircraft plans to reach the destination gate (not the runway). Note: This field should not change too close to the flight time. For updates to departure times (delays, etc), please set &#x60;localEstimatedOrActualArrivalDateTime&#x60;. This is an ISO 8601 extended format date/time without an offset. Time may be specified up to millisecond precision. eg: &#x60;2027-03-05T06:30:00&#x60; This should be the local date/time at the airport (not a UTC time). Google will reject the request if UTC offset is provided. Time zones will be calculated by Google based on arrival airport. If this is not set, Google will set it based on data from other sources. |  [optional] |
|**localScheduledDepartureDateTime** | **String** | Required. The scheduled date and time when the aircraft is expected to depart the gate (not the runway) Note: This field should not change too close to the departure time. For updates to departure times (delays, etc), please set &#x60;localEstimatedOrActualDepartureDateTime&#x60;. This is an ISO 8601 extended format date/time without an offset. Time may be specified up to millisecond precision. eg: &#x60;2027-03-05T06:30:00&#x60; This should be the local date/time at the airport (not a UTC time). Google will reject the request if UTC offset is provided. Time zones will be calculated by Google based on departure airport. |  [optional] |
|**localizedIssuerName** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**locations** | [**List&lt;LatLongPoint&gt;**](LatLongPoint.md) | Note: This field is currently not supported to trigger geo notifications. |  [optional] |
|**messages** | [**List&lt;Message&gt;**](Message.md) | An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10. |  [optional] |
|**multipleDevicesAndHoldersAllowedStatus** | [**MultipleDevicesAndHoldersAllowedStatusEnum**](#MultipleDevicesAndHoldersAllowedStatusEnum) | Identifies whether multiple users and devices will save the same object referencing this class. |  [optional] |
|**origin** | [**AirportInfo**](AirportInfo.md) |  |  [optional] |
|**redemptionIssuers** | **List&lt;String&gt;** | Identifies which redemption issuers can redeem the pass over Smart Tap. Redemption issuers are identified by their issuer ID. Redemption issuers must have at least one Smart Tap key configured. The &#x60;enableSmartTap&#x60; and object level &#x60;smartTapRedemptionLevel&#x60; fields must also be set up correctly in order for a pass to support Smart Tap. |  [optional] |
|**review** | [**Review**](Review.md) |  |  [optional] |
|**reviewStatus** | [**ReviewStatusEnum**](#ReviewStatusEnum) | Required. The status of the class. This field can be set to &#x60;draft&#x60; or &#x60;underReview&#x60; using the insert, patch, or update API calls. Once the review state is changed from &#x60;draft&#x60; it may not be changed back to &#x60;draft&#x60;. You should keep this field to &#x60;draft&#x60; when the class is under development. A &#x60;draft&#x60; class cannot be used to create any object. You should set this field to &#x60;underReview&#x60; when you believe the class is ready for use. The platform will automatically set this field to &#x60;approved&#x60; and it can be immediately used to create or migrate objects. When updating an already &#x60;approved&#x60; class you should keep setting this field to &#x60;underReview&#x60;. |  [optional] |
|**securityAnimation** | [**SecurityAnimation**](SecurityAnimation.md) |  |  [optional] |
|**textModulesData** | [**List&lt;TextModuleData&gt;**](TextModuleData.md) | Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class. |  [optional] |
|**version** | **String** | Deprecated |  [optional] |
|**viewUnlockRequirement** | [**ViewUnlockRequirementEnum**](#ViewUnlockRequirementEnum) | View Unlock Requirement options for the boarding pass. |  [optional] |
|**wordMark** | [**Image**](Image.md) |  |  [optional] |



## Enum: FlightStatusEnum

| Name | Value |
|---- | -----|
| FLIGHT_STATUS_UNSPECIFIED | &quot;FLIGHT_STATUS_UNSPECIFIED&quot; |
| SCHEDULED | &quot;SCHEDULED&quot; |
| SCHEDULED2 | &quot;scheduled&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| ACTIVE2 | &quot;active&quot; |
| LANDED | &quot;LANDED&quot; |
| LANDED2 | &quot;landed&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| CANCELLED2 | &quot;cancelled&quot; |
| REDIRECTED | &quot;REDIRECTED&quot; |
| REDIRECTED2 | &quot;redirected&quot; |
| DIVERTED | &quot;DIVERTED&quot; |
| DIVERTED2 | &quot;diverted&quot; |



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



## Enum: ViewUnlockRequirementEnum

| Name | Value |
|---- | -----|
| VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED | &quot;VIEW_UNLOCK_REQUIREMENT_UNSPECIFIED&quot; |
| UNLOCK_NOT_REQUIRED | &quot;UNLOCK_NOT_REQUIRED&quot; |
| UNLOCK_REQUIRED_TO_VIEW | &quot;UNLOCK_REQUIRED_TO_VIEW&quot; |



