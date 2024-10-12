# HetznerCloudApi.ServersGet200ResponseServersInnerImage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundTo** | **Number** | ID of Server the Image is bound to. Only set for Images of type &#x60;backup&#x60;. | 
**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) | 
**createdFrom** | [**ImagesGet200ResponseImagesInnerCreatedFrom**](ImagesGet200ResponseImagesInnerCreatedFrom.md) |  | 
**deleted** | **String** | Point in time where the Image was deleted (in ISO-8601 format) | 
**deprecated** | **String** | Point in time when the Image is considered to be deprecated (in ISO-8601 format) | 
**description** | **String** | Description of the Image | 
**diskSize** | **Number** | Size of the disk contained in the Image in GB | 
**id** | **Number** | ID of the Resource | 
**imageSize** | **Number** | Size of the Image file in our storage in GB. For snapshot Images this is the value relevant for calculating costs for the Image. | 
**labels** | **{String: String}** | User-defined labels (key-value pairs) | 
**name** | **String** | Unique identifier of the Image. This value is only set for system Images. | 
**osFlavor** | **String** | Flavor of operating system contained in the Image | 
**osVersion** | **String** | Operating system version | 
**protection** | [**FloatingIpsGet200ResponseFloatingIpsInnerProtection**](FloatingIpsGet200ResponseFloatingIpsInnerProtection.md) |  | 
**rapidDeploy** | **Boolean** | Indicates that rapid deploy of the Image is available | [optional] 
**status** | **String** | Whether the Image can be used or if it&#39;s still being created or unavailable | 
**type** | **String** | Type of the Image | 



## Enum: OsFlavorEnum


* `ubuntu` (value: `"ubuntu"`)

* `centos` (value: `"centos"`)

* `debian` (value: `"debian"`)

* `fedora` (value: `"fedora"`)

* `unknown` (value: `"unknown"`)





## Enum: StatusEnum


* `available` (value: `"available"`)

* `creating` (value: `"creating"`)

* `unavailable` (value: `"unavailable"`)





## Enum: TypeEnum


* `system` (value: `"system"`)

* `app` (value: `"app"`)

* `snapshot` (value: `"snapshot"`)

* `backup` (value: `"backup"`)

* `temporary` (value: `"temporary"`)




