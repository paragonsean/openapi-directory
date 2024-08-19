

# CreateWarehouseRequestBody

A create warehouse request body

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | Timestamp that indicates when the warehouse was created |  [optional] [readonly] |
|**isDefault** | **Boolean** | Designates which single warehouse is the default on the account |  [optional] |
|**name** | **String** | Name of the warehouse |  |
|**originAddress** | [**Address**](Address.md) | The origin address of the warehouse |  |
|**returnAddress** | [**Address**](Address.md) | The return address associated with the warehouse |  [optional] |
|**warehouseId** | **String** | A string that uniquely identifies the warehouse |  [optional] [readonly] |



