# ListenApiPodcastSearchDirectoryAndInsightsApi.EpisodeSearchResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio** | **String** | Audio url of this episode, which can be played directly. | [optional] 
**audioLengthSec** | **Number** | Audio length of this episode. In seconds. | [optional] 
**descriptionHighlighted** | **String** | Highlighted segment of this episode&#39;s description | [optional] 
**descriptionOriginal** | **String** | Plain text of this episode&#39;s description | [optional] 
**explicitContent** | **Boolean** | Whether this podcast contains explicit language. | [optional] 
**id** | **String** | Episode id, which can be used to further fetch detailed episode metadata via &#x60;GET /episodes/{id}&#x60;. | [optional] 
**image** | **String** | Image url for this episode. If an episode doesn&#39;t have its own image, then this field would be the url of the podcast artwork image. If you are using PRO/ENTERPRISE plan, then it&#39;s a high resolution image (1400x1400). If you are using FREE plan, then it&#39;s the same as **thumbnail**, low resolution image (300x300).  | [optional] 
**itunesId** | **Number** | iTunes id for this podcast. | [optional] 
**link** | **String** | Web link of this episode. | [optional] 
**listennotesUrl** | **String** | The url of this episode on [ListenNotes.com](https://www.ListenNotes.com). | [optional] 
**podcast** | [**EpisodeSearchResultPodcast**](EpisodeSearchResultPodcast.md) |  | [optional] 
**pubDateMs** | **Number** | Published date for this episode. In millisecond. | [optional] 
**rss** | **String** | RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan. | [optional] 
**thumbnail** | **String** | Thumbnail image (300x300) url for this episode. If an episode doesn&#39;t have its own image, then this field would be the url of the podcast artwork thumbnail image.  | [optional] 
**titleHighlighted** | **String** | Highlighted segment of this episode&#39;s title | [optional] 
**titleOriginal** | **String** | Plain text of this episode&#39; title | [optional] 
**transcriptsHighlighted** | **[String]** | Up to 2 highlighted segments of the audio transcript of this episode. | [optional] 


