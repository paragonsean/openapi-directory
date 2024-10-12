

# ServiceFromTemplateDescription

Defines description for creating a Service Fabric service from a template defined in the application manifest. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationName** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  |
|**initializationData** | **List&lt;Integer&gt;** | Array of bytes to be sent as an integer array. Each element of array is a number between 0 and 255. |  [optional] |
|**serviceDnsName** | **String** | The DNS name of the service. It requires the DNS system service to be enabled in Service Fabric cluster. |  [optional] |
|**serviceName** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. |  |
|**servicePackageActivationMode** | **ServicePackageActivationMode** |  |  [optional] |
|**serviceTypeName** | **String** | Name of the service type as specified in the service manifest. |  |



