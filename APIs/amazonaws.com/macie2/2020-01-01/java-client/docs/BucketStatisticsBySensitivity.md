

# BucketStatisticsBySensitivity

Provides aggregated statistical data for sensitive data discovery metrics that apply to S3 buckets, grouped by bucket sensitivity score (sensitivityScore). If automated sensitive data discovery is currently disabled for your account, the value for each metric is 0.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classificationError** | [**BucketStatisticsBySensitivityClassificationError**](BucketStatisticsBySensitivityClassificationError.md) |  |  [optional] |
|**notClassified** | [**BucketStatisticsBySensitivityNotClassified**](BucketStatisticsBySensitivityNotClassified.md) |  |  [optional] |
|**notSensitive** | [**BucketStatisticsBySensitivityNotSensitive**](BucketStatisticsBySensitivityNotSensitive.md) |  |  [optional] |
|**sensitive** | [**BucketStatisticsBySensitivitySensitive**](BucketStatisticsBySensitivitySensitive.md) |  |  [optional] |



