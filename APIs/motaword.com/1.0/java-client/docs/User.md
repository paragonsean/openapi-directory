

# User


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billing** | [**BillingAddress**](BillingAddress.md) |  |  [optional] |
|**birthday** | **LocalDate** |  |  [optional] |
|**canWorkManualFiles** | **Boolean** | \\@deprecated. use &#x60;vendor&#x60; key |  [optional] |
|**city** | **String** | \\@deprecated. use mailing or billing key. |  [optional] |
|**client** | [**UserClient**](UserClient.md) |  |  [optional] |
|**corporateId** | **Long** |  |  [optional] |
|**country** | **String** | \\@deprecated. use mailing or billing key. |  [optional] |
|**createdAt** | **Long** | Unix epoch time |  [optional] |
|**doNotContact** | **Boolean** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**hasPwd** | **Boolean** |  |  [optional] |
|**id** | **Long** |  |  [optional] |
|**isClient** | **Boolean** |  |  [optional] |
|**isDeveloper** | **Boolean** |  |  [optional] |
|**isProofreader** | **Boolean** | \\@deprecated. use &#x60;vendor&#x60; key |  [optional] |
|**isProspect** | **Boolean** |  |  [optional] |
|**isSalesPerson** | **Boolean** |  |  [optional] |
|**isVendor** | **Boolean** |  |  [optional] |
|**languagePairs** | [**List&lt;LanguagePair&gt;**](LanguagePair.md) | \\@deprecated. use &#x60;vendor&#x60; key |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**lastSeenOnlineAt** | **Long** | Unix epoch time |  [optional] |
|**links** | [**UserLinks**](UserLinks.md) |  |  [optional] |
|**locale** | **String** | User Locale |  [optional] |
|**mailing** | [**Address**](Address.md) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**nativeLanguage** | **String** | \\@deprecated. Native language of user |  [optional] |
|**nps** | **Float** | \\@deprecated. use /stats endpoint for the current nps value. |  [optional] |
|**phoneNumber** | **String** |  |  [optional] |
|**profilePicturePath** | **String** |  |  [optional] |
|**socialMedia** | [**SocialMedia**](SocialMedia.md) |  |  [optional] |
|**state** | **String** | \\@deprecated. use mailing or billing key. |  [optional] |
|**status** | **String** |  |  [optional] |
|**street** | **String** | \\@deprecated. use mailing or billing key. |  [optional] |
|**timezone** | **String** |  |  [optional] |
|**tmsUserName** | **String** | \\@deprecated. use &#x60;vendor&#x60; key |  [optional] |
|**userGroups** | [**List&lt;UserGroup&gt;**](UserGroup.md) |  |  [optional] |
|**vendor** | [**UserVendor**](UserVendor.md) |  |  [optional] |
|**zipCode** | **String** | \\@deprecated. use mailing or billing key. new key name is \&quot;zip\&quot;. |  [optional] |



