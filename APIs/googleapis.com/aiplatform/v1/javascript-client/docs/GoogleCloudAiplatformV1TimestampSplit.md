# VertexAiApi.GoogleCloudAiplatformV1TimestampSplit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | Required. The key is a name of one of the Dataset&#39;s data columns. The values of the key (the values in the column) must be in RFC 3339 &#x60;date-time&#x60; format, where &#x60;time-offset&#x60; &#x3D; &#x60;\&quot;Z\&quot;&#x60; (e.g. 1985-04-12T23:20:50.52Z). If for a piece of data the key is not present or has an invalid value, that piece is ignored by the pipeline. | [optional] 
**testFraction** | **Number** | The fraction of the input data that is to be used to evaluate the Model. | [optional] 
**trainingFraction** | **Number** | The fraction of the input data that is to be used to train the Model. | [optional] 
**validationFraction** | **Number** | The fraction of the input data that is to be used to validate the Model. | [optional] 


