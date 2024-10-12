

# ReturnTransferResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The unique identifier of the return. |  [optional] |
|**reference** | **String** | Your internal reference for the return. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The resulting status of the return.  Possible values: **Authorised**, **Declined**. |  [optional] |
|**transferId** | **String** | The unique identifier of the original transfer. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AUTHORISED | &quot;Authorised&quot; |
| DECLINED | &quot;Declined&quot; |



