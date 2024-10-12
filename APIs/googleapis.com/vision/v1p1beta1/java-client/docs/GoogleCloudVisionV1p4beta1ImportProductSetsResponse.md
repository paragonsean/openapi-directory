

# GoogleCloudVisionV1p4beta1ImportProductSetsResponse

Response message for the `ImportProductSets` method. This message is returned by the google.longrunning.Operations.GetOperation method in the returned google.longrunning.Operation.response field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**referenceImages** | [**List&lt;GoogleCloudVisionV1p4beta1ReferenceImage&gt;**](GoogleCloudVisionV1p4beta1ReferenceImage.md) | The list of reference_images that are imported successfully. |  [optional] |
|**statuses** | [**List&lt;Status&gt;**](Status.md) | The rpc status for each ImportProductSet request, including both successes and errors. The number of statuses here matches the number of lines in the csv file, and statuses[i] stores the success or failure status of processing the i-th line of the csv, starting from line 0. |  [optional] |



