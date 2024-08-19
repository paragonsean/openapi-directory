

# InstanceGroup

Defines an instance group for heterogeneous cluster training. When requesting a training job using the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html\">CreateTrainingJob</a> API, you can configure multiple instance groups .

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceType** | [**TrainingInstanceType**](TrainingInstanceType.md) |  |  |
|**instanceCount** | [**Integer**](Integer.md) |  |  |
|**instanceGroupName** | [**String**](String.md) |  |  |



