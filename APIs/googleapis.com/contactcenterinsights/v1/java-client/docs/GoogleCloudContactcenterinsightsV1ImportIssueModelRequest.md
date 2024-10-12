

# GoogleCloudContactcenterinsightsV1ImportIssueModelRequest

Request to import an issue model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createNewModel** | **Boolean** | Optional. If set to true, will create a new issue model from the imported file with randomly generated IDs for the issue model and corresponding issues. Otherwise, replaces an existing model with the same ID as the file. |  [optional] |
|**gcsSource** | [**GoogleCloudContactcenterinsightsV1ImportIssueModelRequestGcsSource**](GoogleCloudContactcenterinsightsV1ImportIssueModelRequestGcsSource.md) |  |  [optional] |
|**parent** | **String** | Required. The parent resource of the issue model. |  [optional] |



