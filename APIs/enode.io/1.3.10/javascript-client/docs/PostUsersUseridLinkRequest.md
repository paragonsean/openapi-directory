# EnodeApi.PostUsersUseridLinkRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forceLanguage** | **String** | BCP47 language code - Force the Link UI to prefer the specified language. If omitted, the UI will default to the user&#39;s browser default language. | [optional] 
**linkMultiple** | **Boolean** | Allow multiple car vendors to be linked during a single Link session. Automatically disabled if &#x60;vendor&#x60; is set. | [optional] [default to false]
**userImage** | **String** | Full URL to an image that the user would recognize as being their own. This URL is only stored for the duration of the Link session, and is displayed to the user to reduce the effectiveness of phishing attacks. | [optional] 
**userName** | **String** | The User&#39;s first name, full name, or other identifier that the user would recognize as being their own. This name is only stored for the duration of the Link session, and is displayed to the user to reduce the effectiveness of phishing attacks. | [optional] 
**vendor** | **String** | Automatically skip to the credential input screen for this vendor, skipping the Vendor selection menu. | [optional] 



## Enum: VendorEnum


* `TESLA` (value: `"TESLA"`)

* `BMW` (value: `"BMW"`)

* `AUDI` (value: `"AUDI"`)

* `VOLKSWAGEN` (value: `"VOLKSWAGEN"`)

* `HYUNDAI` (value: `"HYUNDAI"`)

* `PEUGEOT` (value: `"PEUGEOT"`)

* `NISSAN` (value: `"NISSAN"`)




