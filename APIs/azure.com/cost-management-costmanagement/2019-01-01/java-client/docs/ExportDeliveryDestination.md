

# ExportDeliveryDestination

The destination information for the delivery of the export. To allow access to a storage account, you must register the account's subscription with the Microsoft.CostManagementExports resource provider. This is required once per subscription. When creating an export in the Azure portal, it is done automatically. However, API users need to register the subscription. For more information see https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-supported-services .

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**container** | **String** | The name of the container where exports will be uploaded. |  |
|**resourceId** | **String** | The resource id of the storage account where exports will be delivered. |  |
|**rootFolderPath** | **String** | The name of the directory where exports will be uploaded. |  [optional] |



