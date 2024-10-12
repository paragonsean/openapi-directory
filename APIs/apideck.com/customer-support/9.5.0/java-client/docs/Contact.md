

# Contact


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** |  |  [optional] |
|**addresses** | [**List&lt;Address&gt;**](Address.md) |  |  [optional] |
|**birthday** | **String** |  |  [optional] |
|**companyId** | **String** |  |  [optional] |
|**companyName** | **String** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**currentBalance** | **BigDecimal** |  |  [optional] |
|**customFields** | [**List&lt;CustomField&gt;**](CustomField.md) |  |  [optional] |
|**department** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**emailDomain** | **String** |  |  [optional] |
|**emails** | [**List&lt;Email&gt;**](Email.md) |  |  [optional] |
|**fax** | **String** |  |  [optional] |
|**firstCallAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**firstEmailAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**firstName** | **String** |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) |  |  [optional] |
|**id** | **String** |  |  [optional] [readonly] |
|**image** | **String** |  |  [optional] |
|**language** | **String** | language code according to ISO 639-1. For the United States - EN |  [optional] |
|**lastActivityAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**lastName** | **String** |  |  [optional] |
|**leadId** | **String** |  |  [optional] |
|**leadSource** | **String** |  |  [optional] |
|**middleName** | **String** |  |  [optional] |
|**name** | **String** |  |  |
|**ownerId** | **String** |  |  [optional] |
|**phoneNumbers** | [**List&lt;PhoneNumber&gt;**](PhoneNumber.md) |  |  [optional] |
|**photoUrl** | **String** | The URL of the photo of a person. |  [optional] |
|**prefix** | **String** |  |  [optional] |
|**socialLinks** | [**List&lt;SocialLink&gt;**](SocialLink.md) |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**suffix** | **String** |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**websites** | [**List&lt;Website&gt;**](Website.md) |  |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |
| UNISEX | &quot;unisex&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER | &quot;customer&quot; |
| SUPPLIER | &quot;supplier&quot; |
| EMPLOYEE | &quot;employee&quot; |
| PERSONAL | &quot;personal&quot; |



