# ListenApiPodcastSearchDirectoryAndInsightsApi.EpisodeSearchResultPodcast

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genreIds** | **[Number]** |  | [optional] 
**id** | **String** | Podcast id, which can be used to further fetch detailed podcast metadata via &#x60;GET /podcasts/{id}&#x60;. | [optional] 
**image** | **String** | Image url for this podcast&#39;s artwork. If you are using PRO/ENTERPRISE plan, then it&#39;s a high resolution image (1400x1400). If you are using FREE plan, then it&#39;s the same as **thumbnail**, low resolution image (300x300).  | [optional] 
**listenScore** | **Number** | The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100. If the score is not available, it&#39;ll be null. Learn more at listennotes.com/listen-score  | [optional] 
**listenScoreGlobalRank** | **String** | The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world. For example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score. If the ranking is not available, it&#39;ll be null. Learn more at listennotes.com/listen-score  | [optional] 
**listennotesUrl** | **String** | The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com). | [optional] 
**publisherHighlighted** | **String** | Highlighted segment of this podcast&#39;s publisher name. | [optional] 
**publisherOriginal** | **String** | Plain text of this podcast&#39;s publisher name. | [optional] 
**thumbnail** | **String** | Thumbnail image url for this podcast&#39;s artwork (300x300). | [optional] 
**titleHighlighted** | **String** | Highlighted segment of podcast name. | [optional] 
**titleOriginal** | **String** | Plain text of podcast name. | [optional] 


