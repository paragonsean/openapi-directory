

# ListProjectsResult

 Result structure used for requests to list projects in AWS Mobile Hub. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projects** | [**List&lt;ProjectSummary&gt;**](ProjectSummary.md) |  List of projects.  |  [optional] |
|**nextToken** | **String** |  Pagination token. Set to null to start listing records from start. If non-null pagination token is returned in a result, then pass its value in here in another request to list more entries.  |  [optional] |



