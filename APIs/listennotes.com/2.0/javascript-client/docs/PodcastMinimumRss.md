# ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastMinimumRss

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Podcast id, which can be used to further fetch detailed podcast metadata via &#x60;GET /podcasts/{id}&#x60;. | [optional] 
**image** | **String** | Image url for this podcast&#39;s artwork. If you are using PRO/ENTERPRISE plan, then it&#39;s a high resolution image (1400x1400). If you are using FREE plan, then it&#39;s the same as **thumbnail**, low resolution image (300x300).  | [optional] 
**listennotesUrl** | **String** | The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com). | [optional] 
**publisher** | **String** | Podcast publisher name. | [optional] 
**rss** | **String** | RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan. | [optional] 
**thumbnail** | **String** | Thumbnail image url for this podcast&#39;s artwork (300x300). | [optional] 
**title** | **String** | Podcast name. | [optional] 


