

# Transition

Specifies when an object transitions to a specified storage class. For more information about Amazon S3 Lifecycle configuration rules, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html\"> Transitioning objects using Amazon S3 Lifecycle</a> in the <i>Amazon S3 User Guide</i>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**days** | [**Integer**](Integer.md) |  |  [optional] |
|**storageClass** | [**TransitionStorageClass**](TransitionStorageClass.md) |  |  [optional] |



