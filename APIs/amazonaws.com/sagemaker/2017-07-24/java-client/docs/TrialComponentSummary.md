

# TrialComponentSummary

A summary of the properties of a trial component. To get all the properties, call the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrialComponent.html\">DescribeTrialComponent</a> API and provide the <code>TrialComponentName</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**trialComponentName** | [**String**](String.md) |  |  [optional] |
|**trialComponentArn** | [**String**](String.md) |  |  [optional] |
|**displayName** | [**String**](String.md) |  |  [optional] |
|**trialComponentSource** | [**TrialComponentSource**](TrialComponentSource.md) |  |  [optional] |
|**status** | [**CreateTrialComponentRequestStatus**](CreateTrialComponentRequestStatus.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**createdBy** | [**DescribeTrialComponentResponseCreatedBy**](DescribeTrialComponentResponseCreatedBy.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedBy** | [**DescribeTrialComponentResponseLastModifiedBy**](DescribeTrialComponentResponseLastModifiedBy.md) |  |  [optional] |



