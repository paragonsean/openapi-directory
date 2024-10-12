

# ServersGet200ResponseServersInnerImage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundTo** | **Integer** | ID of Server the Image is bound to. Only set for Images of type &#x60;backup&#x60;. |  |
|**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) |  |
|**createdFrom** | [**ImagesGet200ResponseImagesInnerCreatedFrom**](ImagesGet200ResponseImagesInnerCreatedFrom.md) |  |  |
|**deleted** | **String** | Point in time where the Image was deleted (in ISO-8601 format) |  |
|**deprecated** | **String** | Point in time when the Image is considered to be deprecated (in ISO-8601 format) |  |
|**description** | **String** | Description of the Image |  |
|**diskSize** | **BigDecimal** | Size of the disk contained in the Image in GB |  |
|**id** | **Integer** | ID of the Resource |  |
|**imageSize** | **BigDecimal** | Size of the Image file in our storage in GB. For snapshot Images this is the value relevant for calculating costs for the Image. |  |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels (key-value pairs) |  |
|**name** | **String** | Unique identifier of the Image. This value is only set for system Images. |  |
|**osFlavor** | [**OsFlavorEnum**](#OsFlavorEnum) | Flavor of operating system contained in the Image |  |
|**osVersion** | **String** | Operating system version |  |
|**protection** | [**FloatingIpsGet200ResponseFloatingIpsInnerProtection**](FloatingIpsGet200ResponseFloatingIpsInnerProtection.md) |  |  |
|**rapidDeploy** | **Boolean** | Indicates that rapid deploy of the Image is available |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Whether the Image can be used or if it&#39;s still being created or unavailable |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the Image |  |



## Enum: OsFlavorEnum

| Name | Value |
|---- | -----|
| UBUNTU | &quot;ubuntu&quot; |
| CENTOS | &quot;centos&quot; |
| DEBIAN | &quot;debian&quot; |
| FEDORA | &quot;fedora&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| CREATING | &quot;creating&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;system&quot; |
| APP | &quot;app&quot; |
| SNAPSHOT | &quot;snapshot&quot; |
| BACKUP | &quot;backup&quot; |
| TEMPORARY | &quot;temporary&quot; |



