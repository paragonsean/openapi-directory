# AccountingApi.Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **String** | Name of city. | [optional] 
**contactName** | **String** | Name of the contact person at the address | [optional] 
**country** | **String** | country code according to ISO 3166-1 alpha-2. | [optional] 
**county** | **String** | Address field that holds a sublocality, such as a county | [optional] 
**email** | **String** | Email address of the address | [optional] 
**fax** | **String** | Fax number of the address | [optional] 
**id** | **String** | Unique identifier for the address. | [optional] 
**latitude** | **String** | Latitude of the address | [optional] 
**line1** | **String** | Line 1 of the address e.g. number, street, suite, apt #, etc. | [optional] 
**line2** | **String** | Line 2 of the address | [optional] 
**line3** | **String** | Line 3 of the address | [optional] 
**line4** | **String** | Line 4 of the address | [optional] 
**longitude** | **String** | Longitude of the address | [optional] 
**name** | **String** | The name of the address. | [optional] 
**notes** | **String** | Additional notes | [optional] 
**phoneNumber** | **String** | Phone number of the address | [optional] 
**postalCode** | **String** | Zip code or equivalent. | [optional] 
**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**salutation** | **String** | Salutation of the contact person at the address | [optional] 
**state** | **String** | Name of state | [optional] 
**streetNumber** | **String** | Street number | [optional] 
**string** | **String** | The address string. Some APIs don&#39;t provide structured address data. | [optional] 
**type** | **String** | The type of address. | [optional] 
**website** | **String** | Website of the address | [optional] 



## Enum: TypeEnum


* `primary` (value: `"primary"`)

* `secondary` (value: `"secondary"`)

* `home` (value: `"home"`)

* `office` (value: `"office"`)

* `shipping` (value: `"shipping"`)

* `billing` (value: `"billing"`)

* `other` (value: `"other"`)




