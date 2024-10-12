

# GenericObject

Generic Object Next ID: 121

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appLinkData** | [**AppLinkData**](AppLinkData.md) |  |  [optional] |
|**barcode** | [**Barcode**](Barcode.md) |  |  [optional] |
|**cardTitle** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**classId** | **String** | Required. The class associated with this object. The class must be of the same type as this object, must already exist, and must be approved. Class IDs should follow the format &#x60;issuerID.identifier&#x60; where &#x60;issuerID&#x60; is issued by Google and &#x60;identifier&#x60; is chosen by you. |  [optional] |
|**genericType** | [**GenericTypeEnum**](#GenericTypeEnum) | Specify which &#x60;GenericType&#x60; the card belongs to. |  [optional] |
|**groupingInfo** | [**GroupingInfo**](GroupingInfo.md) |  |  [optional] |
|**hasUsers** | **Boolean** | Indicates if the object has users. This field is set by the platform. |  [optional] |
|**header** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**heroImage** | [**Image**](Image.md) |  |  [optional] |
|**hexBackgroundColor** | **String** | The background color for the card. If not set, the dominant color of the hero image is used, and if no hero image is set, the dominant color of the logo is used and if logo is not set, a color would be chosen by Google. |  [optional] |
|**id** | **String** | Required. The unique identifier for an object. This ID must be unique across all objects from an issuer. This value needs to follow the format &#x60;issuerID.identifier&#x60; where &#x60;issuerID&#x60; is issued by Google and &#x60;identifier&#x60; is chosen by you. The unique identifier can only include alphanumeric characters, &#x60;.&#x60;, &#x60;_&#x60;, or &#x60;-&#x60;. |  [optional] |
|**imageModulesData** | [**List&lt;ImageModuleData&gt;**](ImageModuleData.md) | Image module data. Only one of the image from class and one from object level will be rendered when both set. |  [optional] |
|**linksModuleData** | [**LinksModuleData**](LinksModuleData.md) |  |  [optional] |
|**logo** | [**Image**](Image.md) |  |  [optional] |
|**notifications** | [**Notifications**](Notifications.md) |  |  [optional] |
|**passConstraints** | [**PassConstraints**](PassConstraints.md) |  |  [optional] |
|**rotatingBarcode** | [**RotatingBarcode**](RotatingBarcode.md) |  |  [optional] |
|**smartTapRedemptionValue** | **String** | The value that will be transmitted to a Smart Tap certified terminal over NFC for this object. The class level fields &#x60;enableSmartTap&#x60; and &#x60;redemptionIssuers&#x60; must also be set up correctly in order for the pass to support Smart Tap. Only ASCII characters are supported. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the object. This field is used to determine how an object is displayed in the app. For example, an &#x60;inactive&#x60; object is moved to the \&quot;Expired passes\&quot; section. If this is not provided, the object would be considered &#x60;ACTIVE&#x60;. |  [optional] |
|**subheader** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**textModulesData** | [**List&lt;TextModuleData&gt;**](TextModuleData.md) | Text module data. If &#x60;textModulesData&#x60; is also defined on the class, both will be displayed. The maximum number of these fields displayed is 10 from class and 10 from object. |  [optional] |
|**validTimeInterval** | [**TimeInterval**](TimeInterval.md) |  |  [optional] |



## Enum: GenericTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;GENERIC_TYPE_UNSPECIFIED&quot; |
| SEASON_PASS | &quot;GENERIC_SEASON_PASS&quot; |
| UTILITY_BILLS | &quot;GENERIC_UTILITY_BILLS&quot; |
| PARKING_PASS | &quot;GENERIC_PARKING_PASS&quot; |
| VOUCHER | &quot;GENERIC_VOUCHER&quot; |
| GYM_MEMBERSHIP | &quot;GENERIC_GYM_MEMBERSHIP&quot; |
| LIBRARY_MEMBERSHIP | &quot;GENERIC_LIBRARY_MEMBERSHIP&quot; |
| RESERVATIONS | &quot;GENERIC_RESERVATIONS&quot; |
| AUTO_INSURANCE | &quot;GENERIC_AUTO_INSURANCE&quot; |
| HOME_INSURANCE | &quot;GENERIC_HOME_INSURANCE&quot; |
| ENTRY_TICKET | &quot;GENERIC_ENTRY_TICKET&quot; |
| RECEIPT | &quot;GENERIC_RECEIPT&quot; |
| OTHER | &quot;GENERIC_OTHER&quot; |



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



