# ListenApiPodcastSearchDirectoryAndInsightsApi.CuratedListSimple

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | This curated list&#39;s description. | [optional] 
**id** | **String** | Curated list id, which can be used to further fetch detailed curated list metadata via &#x60;GET /curated_podcasts/{id}&#x60;. | [optional] 
**listennotesUrl** | **String** | The url of this curated list on [ListenNotes.com](https://www.ListenNotes.com). | [optional] 
**podcasts** | [**[PodcastMinimum]**](PodcastMinimum.md) | Minimum meta data of up to 5 podcasts in this curated list. | [optional] 
**pubDateMs** | **Number** | Published date of this curated list. In milliseconds. | [optional] 
**sourceDomain** | **String** | The domain name of the source of this curated list. | [optional] 
**sourceUrl** | **String** | Url of the source of this curated list. | [optional] 
**title** | **String** | Curated list name. | [optional] 
**total** | **Number** | The total number of podcasts in this curated list. | [optional] 


