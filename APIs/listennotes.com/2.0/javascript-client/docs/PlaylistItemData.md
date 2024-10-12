# ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistItemData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio** | **String** | Audio url, which can be played directly. | [optional] 
**audioLengthSec** | **Number** | Audio length in seconds. | [optional] 
**description** | **String** | Html of this episode&#39;s full description | [optional] 
**explicitContent** | **Boolean** | Whether this podcast contains explicit language. | [optional] 
**id** | **String** | Episode id or podcast id. | [optional] 
**image** | **String** | High resolution image url of this custom audio. | [optional] 
**link** | **String** | Web link of this episode. | [optional] 
**listennotesEditUrl** | **String** | Edit url of this episode where you can update the audio url if you find the audio is broken. | [optional] 
**listennotesUrl** | **String** | The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com). | [optional] 
**maybeAudioInvalid** | **Boolean** | Whether or not this episode&#39;s audio is invalid. Podcasters may delete the original audio. | [optional] 
**podcast** | [**PodcastMinimum**](PodcastMinimum.md) |  | [optional] 
**pubDateMs** | **Number** | Published date (in milliseconds) of this custom audio. For now, it&#39;s the same as **added_at_ms** of this playlist item.  | [optional] 
**thumbnail** | **String** | Low resolution image url of this custom audio. | [optional] 
**title** | **String** | Episode title or podcast title. | [optional] 
**country** | **String** | The country where this podcast is produced. | [optional] 
**earliestPubDateMs** | **Number** | The published date of the oldest episode of this podcast. In milliseconds | [optional] 
**email** | **String** | The email of this podcast&#39;s producer. This field is available only in the PRO/ENTERPRISE plan. | [optional] 
**extra** | [**PodcastExtraField**](PodcastExtraField.md) |  | [optional] 
**genreIds** | **[Number]** |  | [optional] 
**isClaimed** | **Boolean** | Whether this podcast is claimed by its producer on [ListenNotes.com](https://www.ListenNotes.com). | [optional] 
**itunesId** | **Number** | iTunes id for this podcast. | [optional] 
**language** | **String** | The language of this podcast. You can get all supported languages from &#x60;GET /languages&#x60;. | [optional] 
**latestEpisodeId** | **String** | The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via &#x60;GET /episodes/{id}&#x60;. | [optional] 
**latestPubDateMs** | **Number** | The published date of the latest episode of this podcast. In milliseconds | [optional] 
**listenScore** | **Number** | The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100. If the score is not available, it&#39;ll be null. Learn more at listennotes.com/listen-score  | [optional] 
**listenScoreGlobalRank** | **String** | The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world. For example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score. If the ranking is not available, it&#39;ll be null. Learn more at listennotes.com/listen-score  | [optional] 
**lookingFor** | [**PodcastLookingForField**](PodcastLookingForField.md) |  | [optional] 
**publisher** | **String** | Podcast publisher name. | [optional] 
**rss** | **String** | RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan. | [optional] 
**totalEpisodes** | **Number** | Total number of episodes in this podcast. | [optional] 
**type** | [**PodcastTypeField**](PodcastTypeField.md) |  | [optional] 
**updateFrequencyHours** | **Number** | How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it&#39;s every 166 hours (or weekly). | [optional] 
**website** | **String** | Website url of this podcast. | [optional] 
**error** | **String** | Why this episode or podcast is deleted? | [optional] 
**status** | **String** | The status of this episode or podcast. For now, the only possible value is **deleted**. | [optional] 


