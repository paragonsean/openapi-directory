

# StatusTypeV2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionRequiredBy** | [**StatusTypeV2ActionRequiredBy**](StatusTypeV2ActionRequiredBy.md) |  |  [optional] |
|**code** | **String** | Code, see [status codes](#section/Getting-Started/Status-Codes) |  |
|**detail** | **String** |  |  [optional] |
|**detailCode** | **String** |  |  |
|**id** | **Integer** | Depricated, use code instead |  [optional] |
|**isClosed** | **Boolean** | Depricated, does this status event close the order |  [optional] |
|**name** | **String** | Depricated, use stage/state instead |  [optional] |
|**reason** | **String** | Depricated |  [optional] |
|**stage** | [**StatusTypeV2Stage**](StatusTypeV2Stage.md) |  |  |
|**state** | [**StatusTypeV2Stage**](StatusTypeV2Stage.md) |  |  |



