# AzureMlWebServicesManagementClient.WebServiceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**{String: AssetItem}**](AssetItem.md) | Contains user defined properties describing web service assets. Properties are expressed as Key/Value pairs. | [optional] 
**commitmentPlan** | [**CommitmentPlan**](CommitmentPlan.md) |  | [optional] 
**createdOn** | **Date** | Read Only: The date and time when the web service was created. | [optional] [readonly] 
**description** | **String** | The description of the web service. | [optional] 
**diagnostics** | [**DiagnosticsConfiguration**](DiagnosticsConfiguration.md) |  | [optional] 
**exampleRequest** | [**ExampleRequest**](ExampleRequest.md) |  | [optional] 
**exposeSampleData** | **Boolean** | When set to true, sample data is included in the web service&#39;s swagger definition. The default value is true. | [optional] 
**input** | [**ServiceInputOutputSpecification**](ServiceInputOutputSpecification.md) |  | [optional] 
**keys** | [**WebServiceKeys**](WebServiceKeys.md) |  | [optional] 
**machineLearningWorkspace** | [**MachineLearningWorkspace**](MachineLearningWorkspace.md) |  | [optional] 
**modifiedOn** | **Date** | Read Only: The date and time when the web service was last modified. | [optional] [readonly] 
**output** | [**ServiceInputOutputSpecification**](ServiceInputOutputSpecification.md) |  | [optional] 
**packageType** | **String** | Specifies the package type. Valid values are Graph (Specifies a web service published through the Machine Learning Studio) and Code (Specifies a web service published using code such as Python). Note: Code is not supported at this time. | 
**parameters** | [**{String: WebServiceParameter}**](WebServiceParameter.md) | The set of global parameters values defined for the web service, given as a global parameter name to default value map. If no default value is specified, the parameter is considered to be required. | [optional] 
**payloadsInBlobStorage** | **Boolean** | When set to true, indicates that the payload size is larger than 3 MB. Otherwise false. If the payload size exceed 3 MB, the payload is stored in a blob and the PayloadsLocation parameter contains the URI of the blob. Otherwise, this will be set to false and Assets, Input, Output, Package, Parameters, ExampleRequest are inline. The Payload sizes is determined by adding the size of the Assets, Input, Output, Package, Parameters, and the ExampleRequest. | [optional] 
**payloadsLocation** | [**BlobLocation**](BlobLocation.md) |  | [optional] 
**provisioningState** | **String** | Read Only: The provision state of the web service. Valid values are Unknown, Provisioning, Succeeded, and Failed. | [optional] [readonly] 
**readOnly** | **Boolean** | When set to true, indicates that the web service is read-only and can no longer be updated or patched, only removed. Default, is false. Note: Once set to true, you cannot change its value. | [optional] 
**realtimeConfiguration** | [**RealtimeConfiguration**](RealtimeConfiguration.md) |  | [optional] 
**storageAccount** | [**StorageAccount**](StorageAccount.md) |  | [optional] 
**swaggerLocation** | **String** | Read Only: Contains the URI of the swagger spec associated with this web service. | [optional] [readonly] 
**title** | **String** | The title of the web service. | [optional] 



## Enum: PackageTypeEnum


* `Graph` (value: `"Graph"`)





## Enum: ProvisioningStateEnum


* `Unknown` (value: `"Unknown"`)

* `Provisioning` (value: `"Provisioning"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)




