

# ConnectionStatus

ConnectionStatus indicates the state of the connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State. |  [optional] |
|**status** | **String** | Status provides detailed information for the state. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| ERROR | &quot;ERROR&quot; |
| AUTHORIZATION_REQUIRED | &quot;AUTHORIZATION_REQUIRED&quot; |



