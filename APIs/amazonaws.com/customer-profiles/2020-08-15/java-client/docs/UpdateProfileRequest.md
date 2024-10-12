

# UpdateProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | The unique identifier of a customer profile. |  |
|**additionalInformation** | **String** | Any additional information relevant to the customer’s profile. |  [optional] |
|**accountNumber** | **String** | A unique account number that you have given to the customer. |  [optional] |
|**partyType** | [**PartyTypeEnum**](#PartyTypeEnum) | The type of profile used to describe the customer. |  [optional] |
|**businessName** | **String** | The name of the customer’s business. |  [optional] |
|**firstName** | **String** | The customer’s first name. |  [optional] |
|**middleName** | **String** | The customer’s middle name. |  [optional] |
|**lastName** | **String** | The customer’s last name. |  [optional] |
|**birthDate** | **String** | The customer’s birth date.  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) | The gender with which the customer identifies.  |  [optional] |
|**phoneNumber** | **String** | The customer’s phone number, which has not been specified as a mobile, home, or business number.  |  [optional] |
|**mobilePhoneNumber** | **String** | The customer’s mobile phone number. |  [optional] |
|**homePhoneNumber** | **String** | The customer’s home phone number. |  [optional] |
|**businessPhoneNumber** | **String** | The customer’s business phone number. |  [optional] |
|**emailAddress** | **String** | The customer’s email address, which has not been specified as a personal or business address.  |  [optional] |
|**personalEmailAddress** | **String** | The customer’s personal email address. |  [optional] |
|**businessEmailAddress** | **String** | The customer’s business email address. |  [optional] |
|**address** | [**UpdateProfileRequestAddress**](UpdateProfileRequestAddress.md) |  |  [optional] |
|**shippingAddress** | [**UpdateProfileRequestAddress**](UpdateProfileRequestAddress.md) |  |  [optional] |
|**mailingAddress** | [**UpdateProfileRequestAddress**](UpdateProfileRequestAddress.md) |  |  [optional] |
|**billingAddress** | [**UpdateProfileRequestAddress**](UpdateProfileRequestAddress.md) |  |  [optional] |
|**attributes** | **Map&lt;String, String&gt;** | A key value pair of attributes of a customer profile. |  [optional] |
|**partyTypeString** | **String** | An alternative to &lt;code&gt;PartyType&lt;/code&gt; which accepts any string as input. |  [optional] |
|**genderString** | **String** | An alternative to &lt;code&gt;Gender&lt;/code&gt; which accepts any string as input. |  [optional] |



## Enum: PartyTypeEnum

| Name | Value |
|---- | -----|
| INDIVIDUAL | &quot;INDIVIDUAL&quot; |
| BUSINESS | &quot;BUSINESS&quot; |
| OTHER | &quot;OTHER&quot; |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;MALE&quot; |
| FEMALE | &quot;FEMALE&quot; |
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |



