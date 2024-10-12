

# FlightObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appLinkData** | [**AppLinkData**](AppLinkData.md) |  |  [optional] |
|**barcode** | [**Barcode**](Barcode.md) |  |  [optional] |
|**boardingAndSeatingInfo** | [**BoardingAndSeatingInfo**](BoardingAndSeatingInfo.md) |  |  [optional] |
|**classId** | **String** | Required. The class associated with this object. The class must be of the same type as this object, must already exist, and must be approved. Class IDs should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. |  [optional] |
|**classReference** | [**FlightClass**](FlightClass.md) |  |  [optional] |
|**disableExpirationNotification** | **Boolean** | Indicates if notifications should explicitly be suppressed. If this field is set to true, regardless of the &#x60;messages&#x60; field, expiration notifications to the user will be suppressed. By default, this field is set to false. Currently, this can only be set for Flights. |  [optional] |
|**groupingInfo** | [**GroupingInfo**](GroupingInfo.md) |  |  [optional] |
|**hasLinkedDevice** | **Boolean** | Whether this object is currently linked to a single device. This field is set by the platform when a user saves the object, linking it to their device. Intended for use by select partners. Contact support for additional information. |  [optional] |
|**hasUsers** | **Boolean** | Indicates if the object has users. This field is set by the platform. |  [optional] |
|**heroImage** | [**Image**](Image.md) |  |  [optional] |
|**hexBackgroundColor** | **String** | The background color for the card. If not set the dominant color of the hero image is used, and if no hero image is set, the dominant color of the logo is used. The format is #rrggbb where rrggbb is a hex RGB triplet, such as &#x60;#ffcc00&#x60;. You can also use the shorthand version of the RGB triplet which is #rgb, such as &#x60;#fc0&#x60;. |  [optional] |
|**id** | **String** | Required. The unique identifier for an object. This ID must be unique across all objects from an issuer. This value should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. The unique identifier should only include alphanumeric characters, &#39;.&#39;, &#39;_&#39;, or &#39;-&#39;. |  [optional] |
|**imageModulesData** | [**List&lt;ImageModuleData&gt;**](ImageModuleData.md) | Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level. |  [optional] |
|**infoModuleData** | [**InfoModuleData**](InfoModuleData.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#flightObject\&quot;&#x60;. |  [optional] |
|**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  |  [optional] |
|**locations** | [**List&lt;LatLongPoint&gt;**](LatLongPoint.md) | Note: This field is currently not supported to trigger geo notifications. |  [optional] |
|**messages** | [**List&lt;Message&gt;**](Message.md) | An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10. |  [optional] |
|**passConstraints** | [**PassConstraints**](PassConstraints.md) |  |  [optional] |
|**passengerName** | **String** | Required. Passenger name as it would appear on the boarding pass. eg: \&quot;Dave M Gahan\&quot; or \&quot;Gahan/Dave\&quot; or \&quot;GAHAN/DAVEM\&quot; |  [optional] |
|**reservationInfo** | [**ReservationInfo**](ReservationInfo.md) |  |  [optional] |
|**rotatingBarcode** | [**RotatingBarcode**](RotatingBarcode.md) |  |  [optional] |
|**securityProgramLogo** | [**Image**](Image.md) |  |  [optional] |
|**smartTapRedemptionValue** | **String** | The value that will be transmitted to a Smart Tap certified terminal over NFC for this object. The class level fields &#x60;enableSmartTap&#x60; and &#x60;redemptionIssuers&#x60; must also be set up correctly in order for the pass to support Smart Tap. Only ASCII characters are supported. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Required. The state of the object. This field is used to determine how an object is displayed in the app. For example, an &#x60;inactive&#x60; object is moved to the \&quot;Expired passes\&quot; section. |  [optional] |
|**textModulesData** | [**List&lt;TextModuleData&gt;**](TextModuleData.md) | Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class. |  [optional] |
|**validTimeInterval** | [**TimeInterval**](TimeInterval.md) |  |  [optional] |
|**version** | **String** | Deprecated |  [optional] |



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



