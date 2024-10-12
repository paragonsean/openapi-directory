

# PaginatedArtifactList

A paginated list of Artifacts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continuationToken** | **String** | The token used in retrieving the next page.  If null, there are no additional pages. |  [optional] |
|**nextLink** | **String** | The link to the next page constructed using the continuationToken.  If null, there are no additional pages. |  [optional] |
|**value** | [**List&lt;Artifact&gt;**](Artifact.md) | An array of objects of type Artifact. |  [optional] |



