# ServiceUsageApi.EnableRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableType** | **String** | Client and resource project enable type. | [optional] 
**groups** | **[String]** | DEPRECATED: Please use field &#x60;values&#x60;. Service group should have prefix &#x60;groups/&#x60;. The names of the service groups that are enabled (Not Implemented). Example: &#x60;groups/googleServices&#x60;. | [optional] 
**services** | **[String]** | DEPRECATED: Please use field &#x60;values&#x60;. Service should have prefix &#x60;services/&#x60;. The names of the services that are enabled. Example: &#x60;storage.googleapis.com&#x60;. | [optional] 
**values** | **[String]** | The names of the services or service groups that are enabled. Example: &#x60;services/storage.googleapis.com&#x60;, &#x60;groups/googleServices&#x60;, &#x60;groups/allServices&#x60;. | [optional] 



## Enum: EnableTypeEnum


* `ENABLE_TYPE_UNSPECIFIED` (value: `"ENABLE_TYPE_UNSPECIFIED"`)

* `CLIENT` (value: `"CLIENT"`)

* `RESOURCE` (value: `"RESOURCE"`)

* `V1_COMPATIBLE` (value: `"V1_COMPATIBLE"`)




