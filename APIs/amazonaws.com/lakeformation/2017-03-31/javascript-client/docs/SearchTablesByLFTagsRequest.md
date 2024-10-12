# AwsLakeFormation.SearchTablesByLFTagsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextToken** | **String** | A continuation token, if this is not the first call to retrieve this list. | [optional] 
**maxResults** | **Number** | The maximum number of results to return. | [optional] 
**catalogId** | **String** | The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.  | [optional] 
**expression** | [**[LFTag]**](LFTag.md) | A list of conditions (&lt;code&gt;LFTag&lt;/code&gt; structures) to search for in table resources. | 


