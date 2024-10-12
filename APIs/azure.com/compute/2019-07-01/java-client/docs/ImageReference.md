

# ImageReference

Specifies information about the image to use. You can specify information about platform images, marketplace images, or virtual machine images. This element is required when you want to use a platform image, marketplace image, or virtual machine image, but is not used in other creation operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exactVersion** | **String** | Specifies in decimal numbers, the version of platform image or marketplace image used to create the virtual machine. This readonly field differs from &#39;version&#39;, only if the value specified in &#39;version&#39; field is &#39;latest&#39;. |  [optional] [readonly] |
|**offer** | **String** | Specifies the offer of the platform image or marketplace image used to create the virtual machine. |  [optional] |
|**publisher** | **String** | The image publisher. |  [optional] |
|**sku** | **String** | The image SKU. |  [optional] |
|**version** | **String** | Specifies the version of the platform image or marketplace image used to create the virtual machine. The allowed formats are Major.Minor.Build or &#39;latest&#39;. Major, Minor, and Build are decimal numbers. Specify &#39;latest&#39; to use the latest version of an image available at deploy time. Even if you use &#39;latest&#39;, the VM image will not automatically update after deploy time even if a new version becomes available. |  [optional] |
|**id** | **String** | Resource Id |  [optional] |



