

# GetPostAndRelatedData200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | [**User**](User.md) |  |  [optional] |
|**authorOfferCount** | **Integer** | Count of offer posts made by the post author in the last 90 days. |  [optional] |
|**authorPosts** | [**List&lt;Post&gt;**](Post.md) | Other active posts from the post author in the last 90 days. A maximum of 30 posts will be returned.  |  [optional] |
|**authorWantedCount** | **Integer** | Count of wanted posts made by the post author in the last 90 days. |  [optional] |
|**bookmarked** | **Boolean** | Whether or not the current user has bookmarked this post.  Will be null for api key requests and for the current users&#39; posts. |  [optional] |
|**feedback** | [**List&lt;Feedback&gt;**](Feedback.md) | Feedback the current user has left on the post author. |  [optional] |
|**groups** | [**List&lt;Group&gt;**](Group.md) | The groups the post is published on. |  [optional] |
|**post** | [**Post**](Post.md) |  |  [optional] |
|**replied** | **Boolean** | Whether or not the current user has replied to this post.  Will be null for api key requests and for the current users&#39; posts. |  [optional] |
|**userCanReply** | **Boolean** | Whether or not the current user (if any) can reply to this post. Unverified users cannot reply to posts until they verify their account.  |  [optional] |
|**viewed** | **Boolean** | Whether or not the current user has previously viewed this post.  Will be null for api key requests and for the current users&#39; posts. |  [optional] |



