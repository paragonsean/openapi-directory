

# AlgorithmSpecification

<p>Specifies the training algorithm to use in a <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html\">CreateTrainingJob</a> request.</p> <p>For more information about algorithms provided by SageMaker, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html\">Algorithms</a>. For information about using your own algorithms, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html\">Using Your Own Algorithms with Amazon SageMaker</a>. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**trainingImage** | [**String**](String.md) |  |  [optional] |
|**algorithmName** | [**String**](String.md) |  |  [optional] |
|**trainingInputMode** | **TrainingInputMode** |  |  |
|**metricDefinitions** | [**List**](List.md) |  |  [optional] |
|**enableSageMakerMetricsTimeSeries** | [**Boolean**](Boolean.md) |  |  [optional] |
|**containerEntrypoint** | [**List**](List.md) |  |  [optional] |
|**containerArguments** | [**List**](List.md) |  |  [optional] |
|**trainingImageConfig** | [**AlgorithmSpecificationTrainingImageConfig**](AlgorithmSpecificationTrainingImageConfig.md) |  |  [optional] |



