# ShipEngineApi.CreateWarehouseRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Timestamp that indicates when the warehouse was created | [optional] [readonly] 
**isDefault** | **Boolean** | Designates which single warehouse is the default on the account | [optional] [default to false]
**name** | **String** | Name of the warehouse | 
**originAddress** | [**Address**](Address.md) | The origin address of the warehouse | 
**returnAddress** | [**Address**](Address.md) | The return address associated with the warehouse | [optional] 
**warehouseId** | **String** | A string that uniquely identifies the warehouse | [optional] [readonly] 


