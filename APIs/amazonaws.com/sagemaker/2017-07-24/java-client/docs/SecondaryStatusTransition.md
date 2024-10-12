

# SecondaryStatusTransition

<p>An array element of <code>SecondaryStatusTransitions</code> for <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html\">DescribeTrainingJob</a>. It provides additional details about a status that the training job has transitioned through. A training job can be in one of several states, for example, starting, downloading, training, or uploading. Within each state, there are a number of intermediate states. For example, within the starting state, SageMaker could be starting the training job or launching the ML instances. These transitional states are referred to as the job's secondary status. </p> <p/>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**SecondaryStatus**](SecondaryStatus.md) |  |  |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |



