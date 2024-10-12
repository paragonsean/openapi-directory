# AzureMachineLearningComputeManagementClient.SslConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | **String** | The SSL cert data in PEM format encoded as base64 string | [optional] 
**key** | **String** | The SSL key data in PEM format encoded as base64 string. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API. | [optional] 
**status** | **String** | SSL status. Allowed values are Enabled and Disabled. | [optional] [default to &#39;Enabled&#39;]



## Enum: StatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




