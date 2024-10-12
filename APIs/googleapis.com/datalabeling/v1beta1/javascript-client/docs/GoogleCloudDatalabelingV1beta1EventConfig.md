# DataLabelingApi.GoogleCloudDatalabelingV1beta1EventConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationSpecSets** | **[String]** | Required. The list of annotation spec set resource name. Similar to video classification, we support selecting event from multiple AnnotationSpecSet at the same time. | [optional] 
**clipLength** | **Number** | Videos will be cut to smaller clips to make it easier for labelers to work on. Users can configure is field in seconds, if not set, default value is 60s. | [optional] 
**overlapLength** | **Number** | The overlap length between different video clips. Users can configure is field in seconds, if not set, default value is 1s. | [optional] 


