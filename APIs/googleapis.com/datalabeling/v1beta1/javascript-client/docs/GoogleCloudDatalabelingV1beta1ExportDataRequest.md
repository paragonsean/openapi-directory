# DataLabelingApi.GoogleCloudDatalabelingV1beta1ExportDataRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotatedDataset** | **String** | Required. Annotated dataset resource name. DataItem in Dataset and their annotations in specified annotated dataset will be exported. It&#39;s in format of projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/ {annotated_dataset_id} | [optional] 
**filter** | **String** | Optional. Filter is not supported at this moment. | [optional] 
**outputConfig** | [**GoogleCloudDatalabelingV1beta1OutputConfig**](GoogleCloudDatalabelingV1beta1OutputConfig.md) |  | [optional] 
**userEmailAddress** | **String** | Email of the user who started the export task and should be notified by email. If empty no notification will be sent. | [optional] 


