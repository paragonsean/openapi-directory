# GooglePayPassesApi.GenericObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appLinkData** | [**AppLinkData**](AppLinkData.md) |  | [optional] 
**barcode** | [**Barcode**](Barcode.md) |  | [optional] 
**cardTitle** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**classId** | **String** | Required. The class associated with this object. The class must be of the same type as this object, must already exist, and must be approved. Class IDs should follow the format &#x60;issuerID.identifier&#x60; where &#x60;issuerID&#x60; is issued by Google and &#x60;identifier&#x60; is chosen by you. | [optional] 
**genericType** | **String** | Specify which &#x60;GenericType&#x60; the card belongs to. | [optional] 
**groupingInfo** | [**GroupingInfo**](GroupingInfo.md) |  | [optional] 
**hasUsers** | **Boolean** | Indicates if the object has users. This field is set by the platform. | [optional] 
**header** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**heroImage** | [**Image**](Image.md) |  | [optional] 
**hexBackgroundColor** | **String** | The background color for the card. If not set, the dominant color of the hero image is used, and if no hero image is set, the dominant color of the logo is used and if logo is not set, a color would be chosen by Google. | [optional] 
**id** | **String** | Required. The unique identifier for an object. This ID must be unique across all objects from an issuer. This value needs to follow the format &#x60;issuerID.identifier&#x60; where &#x60;issuerID&#x60; is issued by Google and &#x60;identifier&#x60; is chosen by you. The unique identifier can only include alphanumeric characters, &#x60;.&#x60;, &#x60;_&#x60;, or &#x60;-&#x60;. | [optional] 
**imageModulesData** | [**[ImageModuleData]**](ImageModuleData.md) | Image module data. Only one of the image from class and one from object level will be rendered when both set. | [optional] 
**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  | [optional] 
**logo** | [**Image**](Image.md) |  | [optional] 
**notifications** | [**Notifications**](Notifications.md) |  | [optional] 
**passConstraints** | [**PassConstraints**](PassConstraints.md) |  | [optional] 
**rotatingBarcode** | [**RotatingBarcode**](RotatingBarcode.md) |  | [optional] 
**smartTapRedemptionValue** | **String** | The value that will be transmitted to a Smart Tap certified terminal over NFC for this object. The class level fields &#x60;enableSmartTap&#x60; and &#x60;redemptionIssuers&#x60; must also be set up correctly in order for the pass to support Smart Tap. Only ASCII characters are supported. | [optional] 
**state** | **String** | The state of the object. This field is used to determine how an object is displayed in the app. For example, an &#x60;inactive&#x60; object is moved to the \&quot;Expired passes\&quot; section. If this is not provided, the object would be considered &#x60;ACTIVE&#x60;. | [optional] 
**subheader** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**textModulesData** | [**[TextModuleData]**](TextModuleData.md) | Text module data. If &#x60;textModulesData&#x60; is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from class and 10 from object. | [optional] 
**validTimeInterval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 



## Enum: GenericTypeEnum


* `TYPE_UNSPECIFIED` (value: `"GENERIC_TYPE_UNSPECIFIED"`)

* `SEASON_PASS` (value: `"GENERIC_SEASON_PASS"`)

* `UTILITY_BILLS` (value: `"GENERIC_UTILITY_BILLS"`)

* `PARKING_PASS` (value: `"GENERIC_PARKING_PASS"`)

* `VOUCHER` (value: `"GENERIC_VOUCHER"`)

* `GYM_MEMBERSHIP` (value: `"GENERIC_GYM_MEMBERSHIP"`)

* `LIBRARY_MEMBERSHIP` (value: `"GENERIC_LIBRARY_MEMBERSHIP"`)

* `RESERVATIONS` (value: `"GENERIC_RESERVATIONS"`)

* `AUTO_INSURANCE` (value: `"GENERIC_AUTO_INSURANCE"`)

* `HOME_INSURANCE` (value: `"GENERIC_HOME_INSURANCE"`)

* `ENTRY_TICKET` (value: `"GENERIC_ENTRY_TICKET"`)

* `RECEIPT` (value: `"GENERIC_RECEIPT"`)

* `OTHER` (value: `"GENERIC_OTHER"`)





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




