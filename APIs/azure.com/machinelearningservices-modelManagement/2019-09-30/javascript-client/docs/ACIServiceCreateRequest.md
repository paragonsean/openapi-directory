# AzureMachineLearningModelManagementService.ACIServiceCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appInsightsEnabled** | **Boolean** | Whether or not Application Insights is enabled. | [optional] [default to false]
**authEnabled** | **Boolean** | Whether or not authentication is enabled on the service. | [optional] [default to false]
**cname** | **String** | The CName for the service. | [optional] 
**containerResourceRequirements** | [**ContainerResourceRequirements**](ContainerResourceRequirements.md) |  | [optional] 
**dataCollection** | [**ModelDataCollection**](ModelDataCollection.md) |  | [optional] 
**dnsNameLabel** | **String** | The Dns label for the service. | [optional] 
**sslCertificate** | **String** | The SSL certificate to use if SSL is enabled. | [optional] 
**sslEnabled** | **Boolean** | Whether or not SSL is enabled. | [optional] [default to false]
**sslKey** | **String** | The SSL key for the certificate. | [optional] 


