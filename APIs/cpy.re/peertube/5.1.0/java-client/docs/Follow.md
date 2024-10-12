

# Follow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**follower** | [**Actor**](Actor.md) |  |  [optional] |
|**following** | [**Actor**](Actor.md) |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**score** | **BigDecimal** | score reflecting the reachability of the actor, with steps of &#x60;10&#x60; and a base score of &#x60;1000&#x60;. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| ACCEPTED | &quot;accepted&quot; |



