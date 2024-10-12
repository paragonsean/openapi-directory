# HetznerCloudApi.CreateImageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the Image, will be auto-generated if not set | [optional] 
**labels** | [**CreateLoadBalancerRequestLabels**](CreateLoadBalancerRequestLabels.md) |  | [optional] 
**type** | **String** | Type of Image to create (default: &#x60;snapshot&#x60;) | [optional] 



## Enum: TypeEnum


* `snapshot` (value: `"snapshot"`)

* `backup` (value: `"backup"`)




