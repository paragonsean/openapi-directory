# LinQr.MeCardData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthday** | **Date** | Birthday. | [optional] 
**city** | **String** | Address information: City. | [optional] 
**country** | **String** | Address information: Country. | [optional] 
**email** | [**Email**](Email.md) |  | [optional] 
**encoding** | **String** | &#x60;mecard&#x60; encoding. Data format created especially for saving contact details in the QR Code by Japanese company NTT DoCoMo. The resultant QR code is more compact than its &#x60;vcard&#x60; equivalent, but it can contain only limited number of data fields.  For more information please refer to: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/MeCard_(QR_code)\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;en.wikipedia.org&lt;/a&gt;. | [optional] [default to &#39;mecard&#39;]
**firstName** | **String** | First name. | [optional] 
**houseNumber** | **String** | Address information: House number. | [optional] 
**lastName** | **String** | Last name. | 
**memo** | **String** | Short notice. | [optional] 
**nickname** | **String** | Nickname. | [optional] 
**phone** | [**Phone**](Phone.md) |  | [optional] 
**poBox** | **String** | Address information: Post Office Box. | [optional] 
**prefecture** | **String** | Address information: Prefecture. | [optional] 
**reading** | **String** | Kana name. | [optional] 
**roomNumber** | **String** | Address information: Room number. | [optional] 
**url** | [**Url**](Url.md) |  | [optional] 
**videophone** | [**Videophone**](Videophone.md) |  | [optional] 
**zipCode** | **String** | Address information: ZIP code. | [optional] 



## Enum: EncodingEnum


* `mecard` (value: `"mecard"`)




