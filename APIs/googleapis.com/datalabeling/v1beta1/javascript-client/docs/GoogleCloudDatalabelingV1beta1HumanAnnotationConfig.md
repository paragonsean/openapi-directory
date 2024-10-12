# DataLabelingApi.GoogleCloudDatalabelingV1beta1HumanAnnotationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotatedDatasetDescription** | **String** | Optional. A human-readable description for AnnotatedDataset. The description can be up to 10000 characters long. | [optional] 
**annotatedDatasetDisplayName** | **String** | Required. A human-readable name for AnnotatedDataset defined by users. Maximum of 64 characters . | [optional] 
**contributorEmails** | **[String]** | Optional. If you want your own labeling contributors to manage and work on this labeling request, you can set these contributors here. We will give them access to the question types in crowdcompute. Note that these emails must be registered in crowdcompute worker UI: https://crowd-compute.appspot.com/ | [optional] 
**instruction** | **String** | Required. Instruction resource name. | [optional] 
**labelGroup** | **String** | Optional. A human-readable label used to logically group labeling tasks. This string must match the regular expression &#x60;[a-zA-Z\\\\d_-]{0,128}&#x60;. | [optional] 
**languageCode** | **String** | Optional. The Language of this question, as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). Default value is en-US. Only need to set this when task is language related. For example, French text classification. | [optional] 
**questionDuration** | **String** | Optional. Maximum duration for contributors to answer a question. Maximum is 3600 seconds. Default is 3600 seconds. | [optional] 
**replicaCount** | **Number** | Optional. Replication of questions. Each question will be sent to up to this number of contributors to label. Aggregated answers will be returned. Default is set to 1. For image related labeling, valid values are 1, 3, 5. | [optional] 
**userEmailAddress** | **String** | Email of the user who started the labeling task and should be notified by email. If empty no notification will be sent. | [optional] 


