# ServiceFabricClientApis.ServiceFromTemplateDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationName** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. | 
**initializationData** | **[Number]** | Array of bytes to be sent as an integer array. Each element of array is a number between 0 and 255. | [optional] 
**serviceDnsName** | **String** | The DNS name of the service. It requires the DNS system service to be enabled in Service Fabric cluster. | [optional] 
**serviceName** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. | 
**servicePackageActivationMode** | [**ServicePackageActivationMode**](ServicePackageActivationMode.md) |  | [optional] 
**serviceTypeName** | **String** | Name of the service type as specified in the service manifest. | 


