

# ViasPhoneNumber


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneCountryCode** | **String** | The two-character country code of the phone number. &gt;The permitted country codes are defined in ISO-3166-1 alpha-2 (e.g. &#39;NL&#39;). |  [optional] |
|**phoneNumber** | **String** | The phone number. &gt;The inclusion of the phone number country code is not necessary. |  [optional] |
|**phoneType** | [**PhoneTypeEnum**](#PhoneTypeEnum) | The type of the phone number. &gt;The following values are permitted: &#x60;Landline&#x60;, &#x60;Mobile&#x60;, &#x60;SIP&#x60;, &#x60;Fax&#x60;. |  [optional] |



## Enum: PhoneTypeEnum

| Name | Value |
|---- | -----|
| FAX | &quot;Fax&quot; |
| LANDLINE | &quot;Landline&quot; |
| MOBILE | &quot;Mobile&quot; |
| SIP | &quot;SIP&quot; |



