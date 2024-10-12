# TransitFeedsApi.FeedVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**d** | [**FeedVersionD**](FeedVersionD.md) |  | [optional] 
**err** | [**[FeedVersionIssue]**](FeedVersionIssue.md) | If you have included an &#x60;err&#x60; value of &#x60;1&#x60; in your request, then any errors detected when importing this feed version are included. | [optional] 
**f** | [**Feed**](Feed.md) |  | 
**id** | **String** | The unique ID for this feed. This is constructed using the feed ID and an internal ID (generally the date it was imported, but not always, so do not rely on this). | 
**size** | **Number** | The filesize in bytes of the feed version when compressed. | 
**ts** | **Number** | The timestamp of when this feed version was registered in the TransitFeeds.com system (in number of seconds since the epoch (January 1 1970 00:00:00 GMT). | 
**url** | **String** | This is the URL to directly download the feed version via the TranstiFeeds.com web site (and not via the API). In other words, you can provide a download URL without exposing your API key to others.  | 
**warn** | [**[FeedVersionIssue]**](FeedVersionIssue.md) | If you have included a &#x60;warn&#x60; value of &#x60;1&#x60; in your request, then any warnings detected when importing this feed version are included. | [optional] 


