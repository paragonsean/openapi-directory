

# APIModelsCredentials


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bearerAction** | [**BearerActionEnum**](#BearerActionEnum) | The action to perform on the bearer token. Optional. Defaults to ‘None’. |  [optional] |
|**maCAction** | [**MaCActionEnum**](#MaCActionEnum) | The action to perform on the MAC token. Optional. Defaults to ‘None’. |  [optional] |
|**password** | **String** | A secret word or phrase that must be used to gain admission |  |
|**username** | **String** | A unique ID a user needs to login with |  |



## Enum: BearerActionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| RESET | &quot;Reset&quot; |
| DISABLE | &quot;Disable&quot; |



## Enum: MaCActionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| RESET | &quot;Reset&quot; |
| DISABLE | &quot;Disable&quot; |



