

# UserPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atId** | **String** | The URL of the user&#39;s JSON representation. |  [optional] |
|**address** | [**UserPostRequestAddress**](UserPostRequestAddress.md) |  |  [optional] |
|**birthdate** | **String** | The user&#39;s birthday, represented as an ISO 8601:2004 [ISO8601‑2004] YYYY-MM-DD format. |  [optional] |
|**email** | **String** | The user&#39;s preferred email address. |  [optional] |
|**emailVerified** | **Boolean** | True if the user&#39;s e-mail address has been verified; otherwise false. |  [optional] |
|**familyName** | **String** | The user&#39;s surname(s) or last name(s). |  [optional] |
|**gender** | **String** | The enduser&#39;s gender. Possible values are: female, male, and unknown. |  [optional] |
|**givenName** | **String** | The user&#39;s given name(s) or first name(s). |  [optional] |
|**locale** | **String** | The user&#39;s locale, represented as a BCP47 [RFC5646] language tag. It is an ISO 639-1 Alpha-2 language code in lowercase and an ISO 3166-1 Alpha-2 country code in uppercase letters, separated by a dash. |  [optional] |
|**me** | **String** | The simplified URL of the user&#39;s profile page. |  [optional] |
|**middleName** | **String** | The user&#39;s middle name(s). |  [optional] |
|**name** | **String** | The user&#39;s full name in displayable form, including all name parts, possibly including titles and suffixes, ordered according to the enduser&#39;s locale and preferences. |  [optional] |
|**nickname** | **String** | A casual name of the User that may or may not be the same as the given_name. |  [optional] |
|**password** | **String** | The user&#39;s generated password. |  [optional] |
|**phoneNumber** | **String** | The user&#39;s preferred telephone number. |  [optional] |
|**phoneNumberVerified** | **Boolean** | True if the enduser&#39;s phone number has been verified; otherwise false. |  [optional] |
|**picture** | **String** | The URL of the user&#39;s profile picture. |  [optional] |
|**preferredUsername** | **String** | A shorthand name by which the user wishes to be referred to at the Relying Party. |  [optional] |
|**profile** | **String** | The URL of the user&#39;s profile page. |  [optional] |
|**sub** | **String** | Subject - User identifier at the issuer. |  |
|**uid** | **String** | The user&#39;s simplified, shortened identifier at the Issuer. |  [optional] |
|**updatedAt** | **BigDecimal** | The time when the User&#39;s information was last updated. Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time. |  [optional] |
|**webmail** | **String** | The URL of user&#39;s mailbox in a webmail application. |  [optional] |
|**website** | **String** | The URL of the user&#39;s webpage or blog. |  [optional] |
|**zoneinfo** | **String** | A string from the zoneinfo time zone database representing the user&#39;s time zone. For example, Europe/Paris or America/Los_Angeles. |  [optional] |



