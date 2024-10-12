

# AllWarehouses200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Code that identifies a warehouse. |  |
|**isActive** | **Boolean** | Shows if the warehouse is active (&#x60;true&#x60;) or inactive (&#x60;false&#x60;). |  |
|**name** | **String** | Name of the warehouse. |  |
|**pickupPointIds** | **List&lt;Object&gt;** | This field returns a list of the [pickup points&#39; IDs](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R) associated with the given warehouse. |  |
|**priority** | **Integer** | If the warehouse was configured as a priority. When no priority was set, the value returns&#x60;0&#x60;. |  |
|**warehouseDocks** | [**List&lt;WarehouseDock11&gt;**](WarehouseDock11.md) | Information related to the docks available for the warehouses. |  |



