

# Account


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** | Unique identifier of the account |  [optional] |
|**name** | **String** | Name of the account |  [optional] |
|**org** | **String** | Organization of the account |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the account |  [optional] |
|**ucis** | [**List&lt;AccountUcisInner&gt;**](AccountUcisInner.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETED | &quot;DELETED&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |



