# LinQr.VCardData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthday** | **Date** | Birthday. | [optional] 
**cellPhone** | [**CellPhone**](CellPhone.md) |  | [optional] 
**city** | **String** | Address information: City. | [optional] 
**country** | **String** | Address information: Country. | [optional] 
**displayName** | **String** | Common name. By default, equals to concatenated &#x60;first_name&#x60; and &#x60;last_name&#x60;. | [optional] 
**email** | [**Email**](Email.md) |  | [optional] 
**encoding** | **String** | &#x60;vcard&#x60; encoding. Universal standard for electronic business cards, typically stored as &#x60;*.vcf&#x60; file. It allows you to encode more types of data compared to its &#x60;mecard&#x60; equivalent, but it results in a larger QR code.  For more information please refer to: &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/VCard\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; target&#x3D;\&quot;_blank\&quot; &gt;en.wikipedia.org&lt;/a&gt;. | [optional] [default to &#39;vcard&#39;]
**fax** | [**Fax**](Fax.md) |  | [optional] 
**firstName** | **String** | First name. | [optional] 
**homePhone** | [**HomePhone**](HomePhone.md) |  | [optional] 
**lastName** | **String** | Last name. | 
**latitude** | **Number** | Location latitude. | [optional] 
**longitude** | **Number** | Location longitude. | [optional] 
**memo** | **String** | Short notice. | [optional] 
**nickname** | **String** | Nickname. | [optional] 
**organization** | **String** | Organization/company name | [optional] 
**phone** | [**Phone**](Phone.md) |  | [optional] 
**photo** | [**Photo**](Photo.md) |  | [optional] 
**poBox** | **String** | Address information: Post Office Box. | [optional] 
**region** | **String** | Address information: Region. | [optional] 
**revision** | **Date** | vCard revision/last modification date. | [optional] 
**source** | **String** | URL pointing to vCard file itself. | [optional] 
**street** | **String** | Address information: Street. | [optional] 
**title** | [**Title**](Title.md) |  | [optional] 
**url** | [**Url**](Url.md) |  | [optional] 
**videophone** | [**Videophone**](Videophone.md) |  | [optional] 
**workPhone** | [**WorkPhone**](WorkPhone.md) |  | [optional] 
**zipCode** | **String** | Address information: ZIP code. | [optional] 



## Enum: EncodingEnum


* `vcard` (value: `"vcard"`)




