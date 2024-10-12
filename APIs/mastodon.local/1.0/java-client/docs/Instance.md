

# Instance

Represents the software instance of Mastodon running on this domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approvalRequired** | **Boolean** | Whether registrations require moderator approval. |  |
|**contactAccount** | [**Account**](Account.md) |  |  [optional] |
|**description** | **String** | Admin-defined description of the Mastodon site. |  |
|**email** | **String** | An email that may be contacted for any inquiries. |  |
|**invitesEnabled** | **Boolean** | Whether invites are enabled. |  |
|**languages** | **List&lt;String&gt;** | Primary languages of the website and its staff. ISO 639 Part 1-5 language codes. |  |
|**registrations** | **Boolean** | Whether registrations are enabled. |  |
|**shortDescription** | **String** | A shorter description defined by the admin. |  |
|**stats** | **Object** | Statistics about how much information the instance contains. |  |
|**thumbnail** | **String** | Banner image for the website. |  [optional] |
|**title** | **String** | The title of the website. |  |
|**uri** | **String** | The domain name of the instance. |  |
|**urls** | **Object** | URLs of interest for clients apps. |  |
|**version** | **String** | The version of Mastodon installed on the instance. |  |



