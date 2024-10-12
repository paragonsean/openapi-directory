# AmazonSecurityLake.ListLogSourcesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **[String]** | The list of Amazon Web Services accounts for which log sources are displayed. | [optional] 
**maxResults** | **Number** | The maximum number of accounts for which the log sources are displayed. | [optional] 
**nextToken** | **String** | If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page. | [optional] 
**regions** | **[String]** | The list of regions for which log sources are displayed. | [optional] 
**sources** | [**[LogSourceResource]**](LogSourceResource.md) | The list of sources for which log sources are displayed. | [optional] 


