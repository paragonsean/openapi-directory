# MastodonApiSpecificationHttpsGithubComMastodonMastodon.Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**Account**](Account.md) |  | [optional] 
**application** | [**Application**](Application.md) |  | [optional] 
**bookmarked** | **Boolean** | Have you bookmarked this status? | [optional] 
**card** | [**Card**](Card.md) |  | [optional] 
**content** | **String** | HTML-encoded status content. | [optional] 
**createdAt** | **Date** | The date when this status was created. | [optional] 
**emojis** | [**[Emoji]**](Emoji.md) | Custom emoji to be used when rendering status content. | [optional] 
**favourited** | **Boolean** | Have you favourited this status? | [optional] 
**favouritesCount** | **Number** | How many favourites this status has received. | [optional] 
**id** | **String** | ID of the status in the database. Cast from an integer but not guaranteed to be a number. | [optional] 
**inReplyToAccountId** | **String** | ID of the account being replied to. | [optional] 
**inReplyToId** | **String** | ID of the status being replied. Cast from an integer but not guaranteed to be a number. | [optional] 
**language** | **String** | Primary language of this status. ISO 639 Part 1 two-letter language code. | [optional] 
**mediaAttachments** | [**[Attachment]**](Attachment.md) | Media that is attached to this status. | [optional] 
**mentions** | [**[Mention]**](Mention.md) | Mentions of users within the status content. | [optional] 
**muted** | **Boolean** | Have you muted notifications for this status&#39;s conversation? | [optional] 
**pinned** | **Boolean** | Have you pinned this status? Only appears if the status is pinnable. | [optional] 
**poll** | [**Poll**](Poll.md) |  | [optional] 
**reblog** | [**Status**](Status.md) |  | [optional] 
**reblogged** | **Boolean** | Have you boosted this status? | [optional] 
**reblogsCount** | **Number** | How many boosts this status has received. | [optional] 
**repliesCount** | **Number** | How many replies this status has received. | [optional] 
**sensitive** | **Boolean** | Is this status marked as sensitive content? | [optional] 
**spoilerText** | **String** | Subject or summary line, below which status content is collapsed until expanded. | [optional] 
**tags** | [**[Tag]**](Tag.md) | Hashtags used within the status content. | [optional] 
**text** | **String** | Plain-text source of a status. Returned instead of &#x60;content&#x60; when status is deleted, so the user may redraft from the source text without the client having to reverse-engineer the original text from the HTML content. | [optional] 
**uri** | **String** | URI of the status used for federation. | [optional] 
**url** | **String** | A link to the status&#39;s HTML representation. | [optional] 
**visibility** | **String** | Visibility of this status. | [optional] 



## Enum: VisibilityEnum


* `public` (value: `"public"`)

* `unlisted` (value: `"unlisted"`)

* `private` (value: `"private"`)

* `direct` (value: `"direct"`)




