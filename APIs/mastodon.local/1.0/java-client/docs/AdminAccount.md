

# AdminAccount

Admin-level information about a given account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**Account**](Account.md) |  |  [optional] |
|**approved** | **Boolean** | Whether the account is currently approved. |  [optional] |
|**confirmed** | **Boolean** | Whether the account has confirmed their email address. |  [optional] |
|**createdAt** | **OffsetDateTime** | When the account was first discovered. |  [optional] |
|**createdByApplicationId** | **String** | The ID of the application that created this account. Cast from an integer, but not guaranteed to be a number. |  [optional] |
|**disabled** | **Boolean** | Whether the account is currently disabled. |  [optional] |
|**email** | **String** | The email address associated with the account. |  [optional] |
|**id** | **String** | The ID of the account in the database. Cast from an integer, but not guaranteed to be a number. |  [optional] |
|**inviteRequest** | **String** | Invite request text ??? |  [optional] |
|**invitedByAccountId** | **String** | The ID of the account that invited this user. Cast from an integer, but not guaranteed to be a number. |  [optional] |
|**ip** | **String** | The IP address last used to login to this account. |  [optional] |
|**locale** | **String** | The locale of the account. ISO 639 Part 1 two-letter language code. |  [optional] |
|**role** | **String** | The current role of the account. Enumerable oneOf. |  [optional] |
|**silenced** | **Boolean** | Whether the account is currently silenced. |  [optional] |
|**suspended** | **Boolean** | Whether the account is currently suspended. |  [optional] |
|**username** | **String** | The username of the account. |  [optional] |



