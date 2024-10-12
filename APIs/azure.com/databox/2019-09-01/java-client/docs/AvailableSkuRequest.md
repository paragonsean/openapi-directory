

# AvailableSkuRequest

The filters for showing the available skus.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | ISO country code. Country for hardware shipment. For codes check: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements |  |
|**location** | **String** | Location for data transfer. For locations check: https://management.azure.com/subscriptions/SUBSCRIPTIONID/locations?api-version&#x3D;2018-01-01 |  |
|**skuNames** | [**List&lt;SkuNamesEnum&gt;**](#List&lt;SkuNamesEnum&gt;) | Sku Names to filter for available skus |  [optional] |
|**transferType** | [**TransferTypeEnum**](#TransferTypeEnum) | Type of the transfer. |  |



## Enum: List&lt;SkuNamesEnum&gt;

| Name | Value |
|---- | -----|
| DATA_BOX | &quot;DataBox&quot; |
| DATA_BOX_DISK | &quot;DataBoxDisk&quot; |
| DATA_BOX_HEAVY | &quot;DataBoxHeavy&quot; |



## Enum: TransferTypeEnum

| Name | Value |
|---- | -----|
| IMPORT_TO_AZURE | &quot;ImportToAzure&quot; |



