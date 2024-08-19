

# User


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **Integer** | Unique identifier of the user&#39;s account |  [optional] |
|**acountLabel** | **String** | The name of the user&#39;s account |  [optional] |
|**contactNumber** | **String** | Contact number of the user |  [optional] |
|**emailAddress** | **String** | Email address of the user |  [optional] |
|**firstName** | **String** | First name of the user |  [optional] |
|**id** | **Integer** | Unique identifier of the user |  [optional] |
|**lastName** | **String** | Last name of the user |  [optional] |
|**roles** | [**List&lt;UserRolesInner&gt;**](UserRolesInner.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the user |  [optional] |
|**ucis** | [**List&lt;UserUcisInner&gt;**](UserUcisInner.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETED | &quot;DELETED&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |



