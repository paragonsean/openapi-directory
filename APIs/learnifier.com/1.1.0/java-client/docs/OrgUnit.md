

# OrgUnit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalId** | **String** | The external id (foreign key). Must not exceed 255 characters. |  [optional] |
|**id** | **Long** | Unique identifier representing a specific organization unit. Id numbers are never reused. |  |
|**name** | **String** | The name of the client. |  [optional] |
|**parentId** | **Long** | Unique identifier of the parent or *null* if there is no parent. |  [optional] |
|**type** | **String** | The organization unit type. The only type is *client* at the moment. |  |



