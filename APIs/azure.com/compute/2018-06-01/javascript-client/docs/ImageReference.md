# ComputeManagementClient.ImageReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer** | **String** | Specifies the offer of the platform image or marketplace image used to create the virtual machine. | [optional] 
**publisher** | **String** | The image publisher. | [optional] 
**sku** | **String** | The image SKU. | [optional] 
**version** | **String** | Specifies the version of the platform image or marketplace image used to create the virtual machine. The allowed formats are Major.Minor.Build or &#39;latest&#39;. Major, Minor, and Build are decimal numbers. Specify &#39;latest&#39; to use the latest version of an image available at deploy time. Even if you use &#39;latest&#39;, the VM image will not automatically update after deploy time even if a new version becomes available. | [optional] 
**id** | **String** | Resource Id | [optional] 


