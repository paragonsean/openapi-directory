# HetznerCloudApi.ServersGet200ResponseServersInnerIso

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **String** | Type of cpu architecture this iso is compatible with. Null indicates no restriction on the architecture (wildcard). | 
**deprecated** | **String** | ISO 8601 timestamp of deprecation, null if ISO is still available. After the deprecation time it will no longer be possible to attach the ISO to Servers. | 
**description** | **String** | Description of the ISO | 
**id** | **Number** | ID of the Resource | 
**name** | **String** | Unique identifier of the ISO. Only set for public ISOs | 
**type** | **String** | Type of the ISO | 



## Enum: ArchitectureEnum


* `x86` (value: `"x86"`)

* `arm` (value: `"arm"`)





## Enum: TypeEnum


* `public` (value: `"public"`)

* `private` (value: `"private"`)




