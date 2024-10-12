

# ManagerExtendedInfo

The extended info of the manager.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | The etag of the resource. |  [optional] |
|**properties** | [**ManagerExtendedInfoProperties**](ManagerExtendedInfoProperties.md) |  |  [optional] |
|**id** | **String** | The path ID that uniquely identifies the object. |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) | The Kind of the object. Currently only Series8000 is supported |  [optional] |
|**name** | **String** | The name of the object. |  [optional] [readonly] |
|**type** | **String** | The hierarchical type of the object. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| SERIES8000 | &quot;Series8000&quot; |



