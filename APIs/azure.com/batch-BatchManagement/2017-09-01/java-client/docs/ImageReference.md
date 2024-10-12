

# ImageReference


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | This property is mutually exclusive with other properties. The virtual machine image must be in the same region and subscription as the Azure Batch account. For information about the firewall settings for Batch node agent to communicate with Batch service see https://docs.microsoft.com/en-us/azure/batch/batch-api-basics#virtual-network-vnet-and-firewall-configuration . |  [optional] |
|**offer** | **String** | For example, UbuntuServer or WindowsServer. |  [optional] |
|**publisher** | **String** | For example, Canonical or MicrosoftWindowsServer. |  [optional] |
|**sku** | **String** | For example, 14.04.0-LTS or 2012-R2-Datacenter. |  [optional] |
|**version** | **String** | A value of &#39;latest&#39; can be specified to select the latest version of an image. If omitted, the default is &#39;latest&#39;. |  [optional] |



