

# ACIServiceResponse

The response for an ACI service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appInsightsEnabled** | **Boolean** | Whether or not Application Insights is enabled. |  [optional] |
|**authEnabled** | **Boolean** | Whether or not authentication is enabled on the service. |  [optional] |
|**cname** | **String** | The CName for the service. |  [optional] |
|**containerResourceRequirements** | [**ContainerResourceRequirements**](ContainerResourceRequirements.md) |  |  [optional] |
|**dataCollection** | [**ModelDataCollection**](ModelDataCollection.md) |  |  [optional] |
|**environment** | [**ModelEnvironmentDefinition**](ModelEnvironmentDefinition.md) |  |  [optional] |
|**imageDetails** | [**DockerImageResponse**](DockerImageResponse.md) |  |  [optional] |
|**imageId** | **String** | The Id of the Image. |  [optional] |
|**location** | **String** | The location of the service. |  [optional] |
|**modelConfigMap** | **Map&lt;String, Object&gt;** | Details on the models and configurations. |  [optional] |
|**models** | [**List&lt;Model&gt;**](Model.md) | The list of models. |  [optional] |
|**publicFqdn** | **String** | The public Fqdn for the service. |  [optional] |
|**publicIp** | **String** | The public IP address for the service. |  [optional] |
|**scoringUri** | **String** | The Uri for sending scoring requests. |  [optional] |
|**sslCertificate** | **String** | The SSL certificate to use if SSL is enabled. |  [optional] |
|**sslEnabled** | **Boolean** | Whether or not SSL is enabled. |  [optional] |
|**sslKey** | **String** | The SSL key for the certificate. |  [optional] |
|**swaggerUri** | **String** | The Uri for sending swagger requests. |  [optional] |



