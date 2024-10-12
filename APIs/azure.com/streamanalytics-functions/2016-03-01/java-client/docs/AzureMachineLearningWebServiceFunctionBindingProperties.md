

# AzureMachineLearningWebServiceFunctionBindingProperties

The binding properties associated with an Azure Machine learning web service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiKey** | **String** | The API key used to authenticate with Request-Response endpoint. |  [optional] |
|**batchSize** | **Integer** | Number between 1 and 10000 describing maximum number of rows for every Azure ML RRS execute request. Default is 1000. |  [optional] |
|**endpoint** | **String** | The Request-Response execute endpoint of the Azure Machine Learning web service. Find out more here: https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-consume-web-services#request-response-service-rrs |  [optional] |
|**inputs** | [**AzureMachineLearningWebServiceInputs**](AzureMachineLearningWebServiceInputs.md) |  |  [optional] |
|**outputs** | [**List&lt;AzureMachineLearningWebServiceOutputColumn&gt;**](AzureMachineLearningWebServiceOutputColumn.md) | A list of outputs from the Azure Machine Learning web service endpoint execution. |  [optional] |



