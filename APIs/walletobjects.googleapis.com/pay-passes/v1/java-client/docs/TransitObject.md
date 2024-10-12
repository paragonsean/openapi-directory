

# TransitObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationStatus** | [**ActivationStatus**](ActivationStatus.md) |  |  [optional] |
|**appLinkData** | [**AppLinkData**](AppLinkData.md) |  |  [optional] |
|**barcode** | [**Barcode**](Barcode.md) |  |  [optional] |
|**classId** | **String** | Required. The class associated with this object. The class must be of the same type as this object, must already exist, and must be approved. Class IDs should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. |  [optional] |
|**classReference** | [**TransitClass**](TransitClass.md) |  |  [optional] |
|**concessionCategory** | [**ConcessionCategoryEnum**](#ConcessionCategoryEnum) | The concession category for the ticket. |  [optional] |
|**customConcessionCategory** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**customTicketStatus** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**deviceContext** | [**DeviceContext**](DeviceContext.md) |  |  [optional] |
|**disableExpirationNotification** | **Boolean** | Indicates if notifications should explicitly be suppressed. If this field is set to true, regardless of the &#x60;messages&#x60; field, expiration notifications to the user will be suppressed. By default, this field is set to false. Currently, this can only be set for offers. |  [optional] |
|**groupingInfo** | [**GroupingInfo**](GroupingInfo.md) |  |  [optional] |
|**hasLinkedDevice** | **Boolean** | Whether this object is currently linked to a single device. This field is set by the platform when a user saves the object, linking it to their device. Intended for use by select partners. Contact support for additional information. |  [optional] |
|**hasUsers** | **Boolean** | Indicates if the object has users. This field is set by the platform. |  [optional] |
|**heroImage** | [**Image**](Image.md) |  |  [optional] |
|**hexBackgroundColor** | **String** | The background color for the card. If not set the dominant color of the hero image is used, and if no hero image is set, the dominant color of the logo is used. The format is #rrggbb where rrggbb is a hex RGB triplet, such as &#x60;#ffcc00&#x60;. You can also use the shorthand version of the RGB triplet which is #rgb, such as &#x60;#fc0&#x60;. |  [optional] |
|**id** | **String** | Required. The unique identifier for an object. This ID must be unique across all objects from an issuer. This value should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. The unique identifier should only include alphanumeric characters, &#39;.&#39;, &#39;_&#39;, or &#39;-&#39;. |  [optional] |
|**imageModulesData** | [**List&lt;ImageModuleData&gt;**](ImageModuleData.md) | Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level. |  [optional] |
|**infoModuleData** | [**InfoModuleData**](InfoModuleData.md) |  |  [optional] |
|**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  |  [optional] |
|**locations** | [**List&lt;LatLongPoint&gt;**](LatLongPoint.md) | Note: This field is currently not supported to trigger geo notifications. |  [optional] |
|**messages** | [**List&lt;Message&gt;**](Message.md) | An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10. |  [optional] |
|**passConstraints** | [**PassConstraints**](PassConstraints.md) |  |  [optional] |
|**passengerNames** | **String** | The name(s) of the passengers the ticket is assigned to. The above &#x60;passengerType&#x60; field is meant to give Google context on this field. |  [optional] |
|**passengerType** | [**PassengerTypeEnum**](#PassengerTypeEnum) | The number of passengers. |  [optional] |
|**purchaseDetails** | [**PurchaseDetails**](PurchaseDetails.md) |  |  [optional] |
|**rotatingBarcode** | [**RotatingBarcode**](RotatingBarcode.md) |  |  [optional] |
|**smartTapRedemptionValue** | **String** | The value that will be transmitted to a Smart Tap certified terminal over NFC for this object. The class level fields &#x60;enableSmartTap&#x60; and &#x60;redemptionIssuers&#x60; must also be set up correctly in order for the pass to support Smart Tap. Only ASCII characters are supported. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Required. The state of the object. This field is used to determine how an object is displayed in the app. For example, an &#x60;inactive&#x60; object is moved to the \&quot;Expired passes\&quot; section. |  [optional] |
|**textModulesData** | [**List&lt;TextModuleData&gt;**](TextModuleData.md) | Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class. |  [optional] |
|**ticketLeg** | [**TicketLeg**](TicketLeg.md) |  |  [optional] |
|**ticketLegs** | [**List&lt;TicketLeg&gt;**](TicketLeg.md) | Each ticket may contain one or more legs. Each leg contains departure and arrival information along with boarding and seating information. If only one leg is to be specified then use the &#x60;ticketLeg&#x60; field instead. Both &#x60;ticketLeg&#x60; and &#x60;ticketLegs&#x60; may not be set. |  [optional] |
|**ticketNumber** | **String** | The number of the ticket. This is a unique identifier for the ticket in the transit operator&#39;s system. |  [optional] |
|**ticketRestrictions** | [**TicketRestrictions**](TicketRestrictions.md) |  |  [optional] |
|**ticketStatus** | [**TicketStatusEnum**](#TicketStatusEnum) | The status of the ticket. For states which affect display, use the &#x60;state&#x60; field instead. |  [optional] |
|**tripId** | **String** | This id is used to group tickets together if the user has saved multiple tickets for the same trip. |  [optional] |
|**tripType** | [**TripTypeEnum**](#TripTypeEnum) | Required. The type of trip this transit object represents. Used to determine the pass title and/or which symbol to use between the origin and destination. |  [optional] |
|**validTimeInterval** | [**TimeInterval**](TimeInterval.md) |  |  [optional] |
|**version** | **String** | Deprecated |  [optional] |



## Enum: ConcessionCategoryEnum

| Name | Value |
|---- | -----|
| CONCESSION_CATEGORY_UNSPECIFIED | &quot;CONCESSION_CATEGORY_UNSPECIFIED&quot; |
| ADULT | &quot;ADULT&quot; |
| ADULT2 | &quot;adult&quot; |
| CHILD | &quot;CHILD&quot; |
| CHILD2 | &quot;child&quot; |
| SENIOR | &quot;SENIOR&quot; |
| SENIOR2 | &quot;senior&quot; |



## Enum: PassengerTypeEnum

| Name | Value |
|---- | -----|
| PASSENGER_TYPE_UNSPECIFIED | &quot;PASSENGER_TYPE_UNSPECIFIED&quot; |
| SINGLE_PASSENGER | &quot;SINGLE_PASSENGER&quot; |
| SINGLE_PASSENGER2 | &quot;singlePassenger&quot; |
| MULTIPLE_PASSENGERS | &quot;MULTIPLE_PASSENGERS&quot; |
| MULTIPLE_PASSENGERS2 | &quot;multiplePassengers&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| ACTIVE2 | &quot;active&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| COMPLETED2 | &quot;completed&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| EXPIRED2 | &quot;expired&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| INACTIVE2 | &quot;inactive&quot; |



## Enum: TicketStatusEnum

| Name | Value |
|---- | -----|
| TICKET_STATUS_UNSPECIFIED | &quot;TICKET_STATUS_UNSPECIFIED&quot; |
| USED | &quot;USED&quot; |
| USED2 | &quot;used&quot; |
| REFUNDED | &quot;REFUNDED&quot; |
| REFUNDED2 | &quot;refunded&quot; |
| EXCHANGED | &quot;EXCHANGED&quot; |
| EXCHANGED2 | &quot;exchanged&quot; |



## Enum: TripTypeEnum

| Name | Value |
|---- | -----|
| TRIP_TYPE_UNSPECIFIED | &quot;TRIP_TYPE_UNSPECIFIED&quot; |
| ROUND_TRIP | &quot;ROUND_TRIP&quot; |
| ROUND_TRIP2 | &quot;roundTrip&quot; |
| ONE_WAY | &quot;ONE_WAY&quot; |
| ONE_WAY2 | &quot;oneWay&quot; |



