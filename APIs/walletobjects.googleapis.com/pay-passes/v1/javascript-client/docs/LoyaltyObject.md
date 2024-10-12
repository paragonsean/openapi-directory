# GooglePayPassesApi.LoyaltyObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The loyalty account identifier. Recommended maximum length is 20 characters. | [optional] 
**accountName** | **String** | The loyalty account holder name, such as \&quot;John Smith.\&quot; Recommended maximum length is 20 characters to ensure full string is displayed on smaller screens. | [optional] 
**appLinkData** | [**AppLinkData**](AppLinkData.md) |  | [optional] 
**barcode** | [**Barcode**](Barcode.md) |  | [optional] 
**classId** | **String** | Required. The class associated with this object. The class must be of the same type as this object, must already exist, and must be approved. Class IDs should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. | [optional] 
**classReference** | [**LoyaltyClass**](LoyaltyClass.md) |  | [optional] 
**disableExpirationNotification** | **Boolean** | Indicates if notifications should explicitly be suppressed. If this field is set to true, regardless of the &#x60;messages&#x60; field, expiration notifications to the user will be suppressed. By default, this field is set to false. Currently, this can only be set for offers. | [optional] 
**groupingInfo** | [**GroupingInfo**](GroupingInfo.md) |  | [optional] 
**hasLinkedDevice** | **Boolean** | Whether this object is currently linked to a single device. This field is set by the platform when a user saves the object, linking it to their device. Intended for use by select partners. Contact support for additional information. | [optional] 
**hasUsers** | **Boolean** | Indicates if the object has users. This field is set by the platform. | [optional] 
**heroImage** | [**Image**](Image.md) |  | [optional] 
**id** | **String** | Required. The unique identifier for an object. This ID must be unique across all objects from an issuer. This value should follow the format issuer ID.identifier where the former is issued by Google and latter is chosen by you. The unique identifier should only include alphanumeric characters, &#39;.&#39;, &#39;_&#39;, or &#39;-&#39;. | [optional] 
**imageModulesData** | [**[ImageModuleData]**](ImageModuleData.md) | Image module data. The maximum number of these fields displayed is 1 from object level and 1 for class object level. | [optional] 
**infoModuleData** | [**InfoModuleData**](InfoModuleData.md) |  | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#loyaltyObject\&quot;&#x60;. | [optional] 
**linkedOfferIds** | **[String]** | A list of offer objects linked to this loyalty card. The offer objects must already exist. Offer object IDs should follow the format issuer ID. identifier where the former is issued by Google and latter is chosen by you. | [optional] 
**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  | [optional] 
**locations** | [**[LatLongPoint]**](LatLongPoint.md) | Note: This field is currently not supported to trigger geo notifications. | [optional] 
**loyaltyPoints** | [**LoyaltyPoints**](LoyaltyPoints.md) |  | [optional] 
**messages** | [**[Message]**](Message.md) | An array of messages displayed in the app. All users of this object will receive its associated messages. The maximum number of these fields is 10. | [optional] 
**passConstraints** | [**PassConstraints**](PassConstraints.md) |  | [optional] 
**rotatingBarcode** | [**RotatingBarcode**](RotatingBarcode.md) |  | [optional] 
**secondaryLoyaltyPoints** | [**LoyaltyPoints**](LoyaltyPoints.md) |  | [optional] 
**smartTapRedemptionValue** | **String** | The value that will be transmitted to a Smart Tap certified terminal over NFC for this object. The class level fields &#x60;enableSmartTap&#x60; and &#x60;redemptionIssuers&#x60; must also be set up correctly in order for the pass to support Smart Tap. Only ASCII characters are supported. If this value is not set but the class level fields &#x60;enableSmartTap&#x60; and &#x60;redemptionIssuers&#x60; are set up correctly, the &#x60;barcode.value&#x60; or the &#x60;accountId&#x60; fields are used as fallback if present. | [optional] 
**state** | **String** | Required. The state of the object. This field is used to determine how an object is displayed in the app. For example, an &#x60;inactive&#x60; object is moved to the \&quot;Expired passes\&quot; section. | [optional] 
**textModulesData** | [**[TextModuleData]**](TextModuleData.md) | Text module data. If text module data is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from the object and 10 from the class. | [optional] 
**validTimeInterval** | [**TimeInterval**](TimeInterval.md) |  | [optional] 
**version** | **String** | Deprecated | [optional] 



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




