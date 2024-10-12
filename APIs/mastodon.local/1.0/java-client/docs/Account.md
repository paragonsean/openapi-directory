

# Account

Represents a user of Mastodon and their associated profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acct** | **String** | The Webfinger account URI. Equal to &#x60;username&#x60; for local users, or &#x60;username@domain&#x60; for |  [optional] |
|**avatar** | **String** | An image icon that is shown next to statuses and in the profile. The format is URL. |  [optional] |
|**avatarStatic** | **String** | A static version of the avatar. Equal to &#x60;avatar&#x60; if its value is a static image; different if &#x60;avatar&#x60; is an animated GIF. The format is URL. |  [optional] |
|**bot** | **Boolean** | A presentational flag. Indicates that the account may perform automated actions, may not be monitored, or identifies as a robot. |  [optional] |
|**createdAt** | **OffsetDateTime** | When the account was created. |  [optional] |
|**discoverable** | **Boolean** | Whether the account has opted into discovery features such as the profile directory. |  [optional] |
|**displayName** | **String** | The profile&#39;s display name. |  [optional] |
|**emojis** | [**List&lt;Emoji&gt;**](Emoji.md) | Custom emoji entities to be used when rendering the profile. If none, an empty array will be returned. |  [optional] |
|**fields** | [**List&lt;Field&gt;**](Field.md) | Additional metadata attached to a profile as name-value pairs. |  [optional] |
|**followersCount** | **Integer** | The reported followers of this profile. |  [optional] |
|**followingCount** | **Integer** | The reported follows of this profile. |  [optional] |
|**header** | **String** | An image banner that is shown above the profile and in profile cards. The format is URL. |  [optional] |
|**headerStatic** | **String** | A static version of the header. Equal to &#x60;header&#x60; if its value is a static image; different if &#x60;header&#x60; is an animated GIF. The format is URL. |  [optional] |
|**id** | **String** | The account id &#x60;header&#x60;. |  [optional] |
|**lastStatusAt** | **OffsetDateTime** | When the most recent status was posted. |  [optional] |
|**locked** | **Boolean** | Whether the account manually approves follow requests. |  [optional] |
|**moved** | [**Account**](Account.md) |  |  [optional] |
|**muteExpiresAt** | **OffsetDateTime** | When a timed mute will expire, if applicable. ISO 8601 Datetime. |  [optional] |
|**note** | **String** | The profile&#39;s bio / description. |  [optional] |
|**source** | [**Source**](Source.md) |  |  [optional] |
|**statusesCount** | **Integer** | How many statuses are attached to this account. |  [optional] |
|**suspended** | **Boolean** | An extra entity returned when an account is suspended. |  [optional] |
|**url** | **String** | The location of the user&#39;s profile page. (HTTPS URL) |  [optional] |
|**username** | **String** | The username of the account, not including domain. |  [optional] |



