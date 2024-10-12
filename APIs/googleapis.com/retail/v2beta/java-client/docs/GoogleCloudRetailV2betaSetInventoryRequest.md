

# GoogleCloudRetailV2betaSetInventoryRequest

Request message for ProductService.SetInventory method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowMissing** | **Boolean** | If set to true, and the Product with name Product.name is not found, the inventory update will still be processed and retained for at most 1 day until the Product is created. If set to false, a NOT_FOUND error is returned if the Product is not found. |  [optional] |
|**inventory** | [**GoogleCloudRetailV2betaProduct**](GoogleCloudRetailV2betaProduct.md) |  |  [optional] |
|**setMask** | **String** | Indicates which inventory fields in the provided Product to update. At least one field must be provided. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned and the entire update will be ignored. |  [optional] |
|**setTime** | **String** | The time when the request is issued, used to prevent out-of-order updates on inventory fields with the last update time recorded. If not provided, the internal system time will be used. |  [optional] |



