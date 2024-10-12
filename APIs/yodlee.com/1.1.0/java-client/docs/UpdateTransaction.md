

# UpdateTransaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryId** | **Long** |  |  |
|**categorySource** | [**CategorySourceEnum**](#CategorySourceEnum) |  |  |
|**container** | [**ContainerEnum**](#ContainerEnum) |  |  |
|**description** | [**Description**](Description.md) |  |  [optional] |
|**memo** | **String** |  |  [optional] |



## Enum: CategorySourceEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;SYSTEM&quot; |
| USER | &quot;USER&quot; |



## Enum: ContainerEnum

| Name | Value |
|---- | -----|
| BANK | &quot;bank&quot; |
| CREDIT_CARD | &quot;creditCard&quot; |
| INVESTMENT | &quot;investment&quot; |
| INSURANCE | &quot;insurance&quot; |
| LOAN | &quot;loan&quot; |
| REWARD | &quot;reward&quot; |
| REAL_ESTATE | &quot;realEstate&quot; |
| OTHER_ASSETS | &quot;otherAssets&quot; |
| OTHER_LIABILITIES | &quot;otherLiabilities&quot; |



