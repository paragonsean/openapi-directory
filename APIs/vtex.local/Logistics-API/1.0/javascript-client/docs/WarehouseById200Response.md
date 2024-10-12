# LogisticsApi.WarehouseById200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**isActive** | **Boolean** | Shows if the warehouse is active (&#x60;true&#x60;) or inactive (&#x60;false&#x60;). | [optional] 
**name** | **String** |  | [optional] 
**pickupPointIds** | **[Object]** | This field returns a list of the [pickup points&#39; IDs](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R) associated with the given warehouse. | [optional] 
**priority** | **Number** | If the warehouse was configured as a priority. When no priority was set, the value returns&#x60;0&#x60;. | [optional] 
**warehouseDocks** | [**[WarehouseDock12]**](WarehouseDock12.md) |  | [optional] 


