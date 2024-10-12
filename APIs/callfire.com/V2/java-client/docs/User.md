

# User

~

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**Account**](Account.md) |  |  [optional] |
|**accountHolder** | **Boolean** | ~ |  [optional] |
|**accountId** | **Long** | ~ |  [optional] |
|**active** | **Boolean** | ~ |  [optional] |
|**apiPasswordLastFour** | **String** | ~ |  [optional] |
|**brand** | [**BrandEnum**](#BrandEnum) | ~ |  [optional] |
|**cccAgent** | **Boolean** | ~ |  [optional] |
|**created** | **OffsetDateTime** | ~ |  [optional] |
|**dateOfBirth** | **OffsetDateTime** | ~ |  [optional] |
|**disabled** | **Boolean** | ~ |  [optional] |
|**firstName** | **String** | ~ |  [optional] |
|**fullName** | **String** | ~ |  [optional] |
|**id** | **Long** | ~ |  [optional] |
|**industryName** | **String** | ~ |  [optional] |
|**lastName** | **String** | ~ |  [optional] |
|**musicOnHold** | [**MusicOnHoldEnum**](#MusicOnHoldEnum) | ~ |  [optional] |
|**notificationSoundEnabled** | **Boolean** | ~ |  [optional] |
|**optIn** | **Boolean** | ~ |  [optional] |
|**optInNumber** | **String** | ~ |  [optional] |
|**permissions** | **Set&lt;String&gt;** | ~ |  [optional] |
|**phoneNumber** | **String** | ~ |  [optional] |
|**phoneNumberExtension** | **String** | ~ |  [optional] |
|**phoneNumberExtensionDelaySec** | **Integer** | ~ |  [optional] |
|**phoneNumberForDisplay** | **String** | ~ |  [optional] |
|**phoneNumberVerified** | **Boolean** | ~ |  [optional] |
|**profileEmail** | **String** | ~ |  [optional] |
|**signupComplete** | **Boolean** | ~ |  [optional] |
|**soaUser** | [**User**](User.md) |  |  [optional] |
|**teamSeat** | **Boolean** | ~ |  [optional] |
|**userState** | [**UserStateEnum**](#UserStateEnum) | ~ |  [optional] |
|**userStatePending** | **Boolean** | ~ |  [optional] |
|**visible** | **Boolean** | ~ |  [optional] |



## Enum: BrandEnum

| Name | Value |
|---- | -----|
| EZTEXTING | &quot;EZTEXTING&quot; |
| CLUBTEXTING | &quot;CLUBTEXTING&quot; |
| GROUPTEXTING | &quot;GROUPTEXTING&quot; |
| TELLMYCELL | &quot;TELLMYCELL&quot; |
| EZ | &quot;EZ&quot; |
| CALLFIRE | &quot;CALLFIRE&quot; |
| TESLA | &quot;TESLA&quot; |



## Enum: MusicOnHoldEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| SILENCE | &quot;SILENCE&quot; |
| ALTERNATIVE | &quot;ALTERNATIVE&quot; |
| BLUES | &quot;BLUES&quot; |
| CELTIC | &quot;CELTIC&quot; |
| CLASSICAL | &quot;CLASSICAL&quot; |
| COUNTRY | &quot;COUNTRY&quot; |
| INSTRUMENTAL | &quot;INSTRUMENTAL&quot; |
| JAZZ | &quot;JAZZ&quot; |
| NEOPUNK | &quot;NEOPUNK&quot; |
| NEW_AGE | &quot;NEW_AGE&quot; |
| POP | &quot;POP&quot; |
| ROCK | &quot;ROCK&quot; |
| SWING | &quot;SWING&quot; |
| TECHNO | &quot;TECHNO&quot; |



## Enum: UserStateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| NEW_AUTH_INVITE | &quot;NEW_AUTH_INVITE&quot; |
| NEW_USER_INVITE | &quot;NEW_USER_INVITE&quot; |
| EXISTING_USER_INVITE | &quot;EXISTING_USER_INVITE&quot; |



