

# ItemPurchase


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The identifier of the purchased item. |  |
|**ownership** | [**OwnershipEnum**](#OwnershipEnum) | The ownership of the purchased item. |  |
|**resolution** | [**ResolutionEnum**](#ResolutionEnum) | The resolution of the purchased item. |  |
|**title** | **String** | The title of the purchased item. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of item purchased. |  |



## Enum: OwnershipEnum

| Name | Value |
|---- | -----|
| SUBSCRIPTION | &quot;Subscription&quot; |
| FREE | &quot;Free&quot; |
| RENT | &quot;Rent&quot; |
| OWN | &quot;Own&quot; |
| NONE | &quot;None&quot; |



## Enum: ResolutionEnum

| Name | Value |
|---- | -----|
| SD | &quot;SD&quot; |
| HD_720 | &quot;HD-720&quot; |
| HD_1080 | &quot;HD-1080&quot; |
| HD_4_K | &quot;HD-4K&quot; |
| EXTERNAL | &quot;External&quot; |
| UNKNOWN | &quot;Unknown&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MOVIE | &quot;movie&quot; |
| SHOW | &quot;show&quot; |
| SEASON | &quot;season&quot; |
| EPISODE | &quot;episode&quot; |
| PROGRAM | &quot;program&quot; |
| LINK | &quot;link&quot; |
| TRAILER | &quot;trailer&quot; |
| CHANNEL | &quot;channel&quot; |
| CUSTOM_ASSET | &quot;customAsset&quot; |



