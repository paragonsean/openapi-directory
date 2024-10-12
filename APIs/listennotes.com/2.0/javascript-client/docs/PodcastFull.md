# ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastFull

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioLengthSec** | **Number** | Average audio length of all episodes of this podcast. In seconds. | [optional] 
**country** | **String** | The country where this podcast is produced. | [optional] 
**description** | **String** | Html of this episode&#39;s full description | [optional] 
**earliestPubDateMs** | **Number** | The published date of the oldest episode of this podcast. In milliseconds | [optional] 
**email** | **String** | The email of this podcast&#39;s producer. This field is available only in the PRO/ENTERPRISE plan. | [optional] 
**episodes** | [**[EpisodeMinimum]**](EpisodeMinimum.md) |  | [optional] 
**explicitContent** | **Boolean** | Whether this podcast contains explicit language. | [optional] 
**extra** | [**PodcastExtraField**](PodcastExtraField.md) |  | [optional] 
**genreIds** | **[Number]** |  | [optional] 
**id** | **String** | Podcast id, which can be used to further fetch detailed podcast metadata via &#x60;GET /podcasts/{id}&#x60;. | [optional] 
**image** | **String** | Image url for this podcast&#39;s artwork. If you are using PRO/ENTERPRISE plan, then it&#39;s a high resolution image (1400x1400). If you are using FREE plan, then it&#39;s the same as **thumbnail**, low resolution image (300x300).  | [optional] 
**isClaimed** | **Boolean** | Whether this podcast is claimed by its producer on [ListenNotes.com](https://www.ListenNotes.com). | [optional] 
**itunesId** | **Number** | iTunes id for this podcast. | [optional] 
**language** | **String** | The language of this podcast. You can get all supported languages from &#x60;GET /languages&#x60;. | [optional] 
**latestEpisodeId** | **String** | The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via &#x60;GET /episodes/{id}&#x60;. | [optional] 
**latestPubDateMs** | **Number** | The published date of the latest episode of this podcast. In milliseconds | [optional] 
**listenScore** | **Number** | The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100. If the score is not available, it&#39;ll be null. Learn more at listennotes.com/listen-score  | [optional] 
**listenScoreGlobalRank** | **String** | The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world. For example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score. If the ranking is not available, it&#39;ll be null. Learn more at listennotes.com/listen-score  | [optional] 
**listennotesUrl** | **String** | The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com). | [optional] 
**lookingFor** | [**PodcastLookingForField**](PodcastLookingForField.md) |  | [optional] 
**nextEpisodePubDate** | **Number** | Passed to the **next_episode_pub_date** parameter of &#x60;GET /podcasts/{id}&#x60; to paginate through episodes of that podcast. | [optional] 
**publisher** | **String** | Podcast publisher name. | [optional] 
**rss** | **String** | RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan. | [optional] 
**thumbnail** | **String** | Thumbnail image url for this podcast&#39;s artwork (300x300). | [optional] 
**title** | **String** | Podcast name. | [optional] 
**totalEpisodes** | **Number** | Total number of episodes in this podcast. | [optional] 
**type** | [**PodcastTypeField**](PodcastTypeField.md) |  | [optional] 
**updateFrequencyHours** | **Number** | How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it&#39;s every 166 hours (or weekly). | [optional] 
**website** | **String** | Website url of this podcast. | [optional] 


