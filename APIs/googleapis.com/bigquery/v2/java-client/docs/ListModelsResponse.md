

# ListModelsResponse

Response format for a single page when listing BigQuery ML models.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**models** | [**List&lt;Model&gt;**](Model.md) | Models in the requested dataset. Only the following fields are populated: model_reference, model_type, creation_time, last_modified_time and labels. |  [optional] |
|**nextPageToken** | **String** | A token to request the next page of results. |  [optional] |



