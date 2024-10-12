# GooglePayPassesApi.TransitObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationStatus** | [**ActivationStatus**](ActivationStatus.md) |  | [optional] 
**appLinkData** | [**AppLinkData**](AppLinkData.md) |  | [optional] 
**barcode** | [**Barcode**](Barcode.md) |  | [optional] 
**classId** | **String** | Required. The class associated with this object. The class must be of the same type as this object, must already exist, and must be approved. Class IDs should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. | [optional] 
**classReference** | [**TransitClass**](TransitClass.md) |  | [optional] 
**concessionCategory** | **String** | The concession category for the ticket. | [optional] 
**customConcessionCategory** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**customTicketStatus** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**deviceContext** | [**DeviceContext**](DeviceContext.md) |  | [optional] 
**disableExpirationNotification** | **Boolean** | Indicates if notifications should explicitly be suppressed. If this field is set to true, regardless of the &#x60;messages&#x60; field, expiration notifications to the user will be suppressed. By default, this field is set to false. Currently, this can only be set for offers. | [optional] 
**groupingInfo** | [**GroupingInfo**](GroupingInfo.md) |  | [optional] 
**hasLinkedDevice** | **Boolean** | Whether this object is currently linked to a single device. This field is set by the platform when a user saves the object, linking it to their device. Intended for use by select partners. Contact support for additional information. | [optional] 
**hasUsers** | **Boolean** | Indicates if the object has users. This field is set by the platform. | [optional] 
**heroImage** | [**Image**](Image.md) |  | [optional] 
**hexBackgroundColor** | **String** | The background color for the card. If not set the dominant color of the hero image is used, and if no hero image is set, the dominant color of the logo is used. The format is #rrggbb where rrggbb is a hex RGB triplet, such as &#x60;#ffcc00&#x60;. You can also use the shorthand version of the RGB triplet which is #rgb, such as &#x60;#fc0&#x60;. | [optional] 
**id** | **String** | Required. The unique identifier for an object. This ID must be unique across all objects from an issuer. This value should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. The unique identifier should only include alphanumeric characters, &#39;.&#39;, &#39;_&#39;, or &#39;-&#39;. | [optional] 
**imageModulesData** | [**[ImageModuleData]**](ImageModuleData.md) | Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level. | [optional] 
**infoModuleData** | [**InfoModuleData**](InfoModuleData.md) |  | [optional] 
**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  | [optional] 
**locations** | [**[LatLongPoint]**](LatLongPoint.md) | Note: This field is currently not supported to trigger geo notifications. | [optional] 
**messages** | [**[Message]**](Message.md) | An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10. | [optional] 
**passConstraints** | [**PassConstraints**](PassConstraints.md) |  | [optional] 
**passengerNames** | **String** | The name(s) of the passengers the ticket is assigned to. The above &#x60;passengerType&#x60; field is meant to give Google context on this field. | [optional] 
**passengerType** | **String** | The number of passengers. | [optional] 
**purchaseDetails** | [**PurchaseDetails**](PurchaseDetails.md) |  | [optional] 
**rotatingBarcode** | [**RotatingBarcode**](RotatingBarcode.md) |  | [optional] 
**smartTapRedemptionValue** | **String** | The value that will be transmitted to a Smart Tap certified terminal over NFC for this object. The class level fields &#x60;enableSmartTap&#x60; and &#x60;redemptionIssuers&#x60; must also be set up correctly in order for the pass to support Smart Tap. Only ASCII characters are supported. | [optional] 
**state** | **String** | Required. The state of the object. This field is used to determine how an object is displayed in the app. For example, an &#x60;inactive&#x60; object is moved to the \&quot;Expired passes\&quot; section. | [optional] 
**textModulesData** | [**[TextModuleData]**](TextModuleData.md) | Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class. | [optional] 
**ticketLeg** | [**TicketLeg**](TicketLeg.md) |  | [optional] 
**ticketLegs** | [**[TicketLeg]**](TicketLeg.md) | Each ticket may contain one or more legs. Each leg contains departure and arrival information along with boarding and seating information. If only one leg is to be specified then use the &#x60;ticketLeg&#x60; field instead. Both &#x60;ticketLeg&#x60; and &#x60;ticketLegs&#x60; may not be set. | [optional] 
**ticketNumber** | **String** | The number of the ticket. This is a unique identifier for the ticket in the transit operator&#39;s system. | [optional] 
**ticketRestrictions** | [**TicketRestrictions**](TicketRestrictions.md) |  | [optional] 
**ticketStatus** | **String** | The status of the ticket. For states which affect display, use the &#x60;state&#x60; field instead. | [optional] 
**tripId** | **String** | This id is used to group tickets together if the user has saved multiple tickets for the same trip. | [optional] 
**tripType** | **String** | Required. The type of trip this transit object represents. Used to determine the pass title and/or which symbol to use between the origin and destination. | [optional] 
**validTimeInterval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**version** | **String** | Deprecated | [optional] 



## Enum: ConcessionCategoryEnum


* `CONCESSION_CATEGORY_UNSPECIFIED` (value: `"CONCESSION_CATEGORY_UNSPECIFIED"`)

* `ADULT` (value: `"ADULT"`)

* `adult` (value: `"adult"`)

* `CHILD` (value: `"CHILD"`)

* `child` (value: `"child"`)

* `SENIOR` (value: `"SENIOR"`)

* `senior` (value: `"senior"`)





## Enum: PassengerTypeEnum


* `PASSENGER_TYPE_UNSPECIFIED` (value: `"PASSENGER_TYPE_UNSPECIFIED"`)

* `SINGLE_PASSENGER` (value: `"SINGLE_PASSENGER"`)

* `singlePassenger` (value: `"singlePassenger"`)

* `MULTIPLE_PASSENGERS` (value: `"MULTIPLE_PASSENGERS"`)

* `multiplePassengers` (value: `"multiplePassengers"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `active` (value: `"active"`)

* `COMPLETED` (value: `"COMPLETED"`)

* `completed` (value: `"completed"`)

* `EXPIRED` (value: `"EXPIRED"`)

* `expired` (value: `"expired"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `inactive` (value: `"inactive"`)





## Enum: TicketStatusEnum


* `TICKET_STATUS_UNSPECIFIED` (value: `"TICKET_STATUS_UNSPECIFIED"`)

* `USED` (value: `"USED"`)

* `used` (value: `"used"`)

* `REFUNDED` (value: `"REFUNDED"`)

* `refunded` (value: `"refunded"`)

* `EXCHANGED` (value: `"EXCHANGED"`)

* `exchanged` (value: `"exchanged"`)





## Enum: TripTypeEnum


* `TRIP_TYPE_UNSPECIFIED` (value: `"TRIP_TYPE_UNSPECIFIED"`)

* `ROUND_TRIP` (value: `"ROUND_TRIP"`)

* `roundTrip` (value: `"roundTrip"`)

* `ONE_WAY` (value: `"ONE_WAY"`)

* `oneWay` (value: `"oneWay"`)




