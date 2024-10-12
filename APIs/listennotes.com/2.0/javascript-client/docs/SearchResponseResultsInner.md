# ListenApiPodcastSearchDirectoryAndInsightsApi.SearchResponseResultsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio** | **String** | Audio url of this episode, which can be played directly. | [optional] 
**audioLengthSec** | **Number** | Average audio length of all episodes of this podcast. In seconds. | [optional] 
**descriptionHighlighted** | **String** | Highlighted segment of this curated list&#39;s description | [optional] 
**descriptionOriginal** | **String** | Plain text of this curated list&#39;s description | [optional] 
**explicitContent** | **Boolean** | Whether this podcast contains explicit language. | [optional] 
**id** | **String** | Curated list id, which can be used to further fetch detailed curated list metadata via &#x60;GET /curated_podcasts/{id}&#x60;. | [optional] 
**image** | **String** | Image url for this podcast&#39;s artwork. If you are using PRO/ENTERPRISE plan, then it&#39;s a high resolution image (1400x1400). If you are using FREE plan, then it&#39;s the same as **thumbnail**, low resolution image (300x300).  | [optional] 
**itunesId** | **Number** | iTunes id for this podcast. | [optional] 
**link** | **String** | Web link of this episode. | [optional] 
**listennotesUrl** | **String** | The url of this curated list on [ListenNotes.com](https://www.ListenNotes.com). | [optional] 
**podcast** | [**EpisodeSearchResultPodcast**](EpisodeSearchResultPodcast.md) |  | [optional] 
**pubDateMs** | **Number** | Published date of this curated list. In milliseconds. | [optional] 
**rss** | **String** | RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan. | [optional] 
**thumbnail** | **String** | Thumbnail image url for this podcast&#39;s artwork (300x300). | [optional] 
**titleHighlighted** | **String** | Highlighted segment of this curated list&#39;s title | [optional] 
**titleOriginal** | **String** | Plain text of this curated list&#39;s title | [optional] 
**transcriptsHighlighted** | **[String]** | Up to 2 highlighted segments of the audio transcript of this episode. | [optional] 
**earliestPubDateMs** | **Number** | The published date of the oldest episode of this podcast. In milliseconds | [optional] 
**email** | **String** | The email of this podcast&#39;s producer. This field is available only in the PRO/ENTERPRISE plan. | [optional] 
**genreIds** | **[Number]** |  | [optional] 
**latestEpisodeId** | **String** | The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via &#x60;GET /episodes/{id}&#x60;. | [optional] 
**latestPubDateMs** | **Number** | The published date of the latest episode of this podcast. In milliseconds | [optional] 
**listenScore** | **Number** | The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100. If the score is not available, it&#39;ll be null. Learn more at listennotes.com/listen-score  | [optional] 
**listenScoreGlobalRank** | **String** | The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world. For example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score. If the ranking is not available, it&#39;ll be null. Learn more at listennotes.com/listen-score  | [optional] 
**publisherHighlighted** | **String** | Highlighted segment of this podcast&#39;s publisher name. | [optional] 
**publisherOriginal** | **String** | Plain text of this podcast&#39;s publisher name. | [optional] 
**totalEpisodes** | **Number** | Total number of episodes in this podcast. | [optional] 
**updateFrequencyHours** | **Number** | How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it&#39;s every 166 hours (or weekly). | [optional] 
**website** | **String** | Website url of this podcast. | [optional] 
**podcasts** | [**[PodcastMinimum]**](PodcastMinimum.md) | Up to 5 podcasts in this curated list. | [optional] 
**sourceDomain** | **String** | The domain name of the source of this curated list. | [optional] 
**sourceUrl** | **String** | Url of the source of this curated list. | [optional] 
**total** | **Number** | The total number of podcasts in this curated list. | [optional] 


