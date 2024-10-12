

# ResourceStatistics

Provides statistical data for sensitive data discovery metrics that apply to an S3 bucket that Amazon Macie monitors and analyzes for your account. The statistics capture the results of automated sensitive data discovery activities that Macie has performed for the bucket. The data is available only if automated sensitive data discovery is currently enabled for your account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**totalBytesClassified** | [**Integer**](Integer.md) |  |  [optional] |
|**totalDetections** | [**Integer**](Integer.md) |  |  [optional] |
|**totalDetectionsSuppressed** | [**Integer**](Integer.md) |  |  [optional] |
|**totalItemsClassified** | [**Integer**](Integer.md) |  |  [optional] |
|**totalItemsSensitive** | [**Integer**](Integer.md) |  |  [optional] |
|**totalItemsSkipped** | [**Integer**](Integer.md) |  |  [optional] |
|**totalItemsSkippedInvalidEncryption** | [**Integer**](Integer.md) |  |  [optional] |
|**totalItemsSkippedInvalidKms** | [**Integer**](Integer.md) |  |  [optional] |
|**totalItemsSkippedPermissionDenied** | [**Integer**](Integer.md) |  |  [optional] |



