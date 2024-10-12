# BungieNetApi.SearchResultOfFireteamSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hasMore** | **Boolean** |  | [optional] 
**query** | [**QueriesPagedQuery**](QueriesPagedQuery.md) |  | [optional] 
**replacementContinuationToken** | **String** |  | [optional] 
**results** | [**[FireteamFireteamSummary]**](FireteamFireteamSummary.md) |  | [optional] 
**totalResults** | **Number** |  | [optional] 
**useTotalResults** | **Boolean** | If useTotalResults is true, then totalResults represents an accurate count.  If False, it does not, and may be estimated/only the size of the current page.  Either way, you should probably always only trust hasMore.  This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one. | [optional] 


