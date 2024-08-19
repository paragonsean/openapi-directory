

# PhoneNumber


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneCountryCode** | **String** | The two-character ISO-3166-1 alpha-2 country code of the phone number. For example, **US** or **NL**. |  [optional] |
|**phoneNumber** | **String** | The phone number. The inclusion of the phone number country code is not necessary. |  [optional] |
|**phoneType** | [**PhoneTypeEnum**](#PhoneTypeEnum) | The type of the phone number. Possible values: **Landline**, **Mobile**, **SIP**, **Fax**. |  [optional] |



## Enum: PhoneTypeEnum

| Name | Value |
|---- | -----|
| FAX | &quot;Fax&quot; |
| LANDLINE | &quot;Landline&quot; |
| MOBILE | &quot;Mobile&quot; |
| SIP | &quot;SIP&quot; |



