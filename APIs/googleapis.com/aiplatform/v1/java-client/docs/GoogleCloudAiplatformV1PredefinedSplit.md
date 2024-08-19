

# GoogleCloudAiplatformV1PredefinedSplit

Assigns input data to training, validation, and test sets based on the value of a provided key. Supported only for tabular Datasets.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | Required. The key is a name of one of the Dataset&#39;s data columns. The value of the key (either the label&#39;s value or value in the column) must be one of {&#x60;training&#x60;, &#x60;validation&#x60;, &#x60;test&#x60;}, and it defines to which set the given piece of data is assigned. If for a piece of data the key is not present or has an invalid value, that piece is ignored by the pipeline. |  [optional] |



