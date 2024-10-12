# VertexAiApi.GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingDataset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigquerySource** | [**GoogleCloudAiplatformV1BigQuerySource**](GoogleCloudAiplatformV1BigQuerySource.md) |  | [optional] 
**dataFormat** | **String** | Data format of the dataset, only applicable if the input is from Google Cloud Storage. The possible formats are: \&quot;tf-record\&quot; The source file is a TFRecord file. \&quot;csv\&quot; The source file is a CSV file. \&quot;jsonl\&quot; The source file is a JSONL file. | [optional] 
**dataset** | **String** | The resource name of the Dataset used to train this Model. | [optional] 
**gcsSource** | [**GoogleCloudAiplatformV1GcsSource**](GoogleCloudAiplatformV1GcsSource.md) |  | [optional] 
**loggingSamplingStrategy** | [**GoogleCloudAiplatformV1SamplingStrategy**](GoogleCloudAiplatformV1SamplingStrategy.md) |  | [optional] 
**targetField** | **String** | The target field name the model is to predict. This field will be excluded when doing Predict and (or) Explain for the training data. | [optional] 


