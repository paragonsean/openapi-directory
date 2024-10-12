

# ListRoutinesResponse

Describes the format of a single result page when listing routines.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token to request the next page of results. |  [optional] |
|**routines** | [**List&lt;Routine&gt;**](Routine.md) | Routines in the requested dataset. Unless read_mask is set in the request, only the following fields are populated: etag, project_id, dataset_id, routine_id, routine_type, creation_time, last_modified_time, language, and remote_function_options. |  [optional] |



