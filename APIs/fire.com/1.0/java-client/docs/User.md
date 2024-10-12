

# User


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailAddress** | **String** | email address for user |  [optional] |
|**firstName** | **String** | User first name |  [optional] |
|**id** | **Long** | The User ID for this User |  [optional] |
|**lastName** | **String** | User second name |  [optional] |
|**lastlogin** | **String** | Timestamp on when user last logged in. |  [optional] |
|**mobileApplicationDetails** | [**MobileApplication**](MobileApplication.md) |  |  [optional] |
|**mobileNumber** | **String** | User mobile number |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | User role |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of user |  [optional] |
|**userCvl** | **String** | Users Cvl type ID (shows up when status is LIVE) |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ADMIN | &quot;ADMIN&quot; |
| FULL_USER | &quot;FULL_USER&quot; |
| READ_ONLY | &quot;READ_ONLY&quot; |
| CARD_ONLY | &quot;CARD_ONLY&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| LIVE | &quot;LIVE&quot; |
| CLOSED | &quot;CLOSED&quot; |
| FROZEN | &quot;FROZEN&quot; |
| INVITE_SENT | &quot;INVITE_SENT&quot; |
| SMS_CODE_SENT | &quot;SMS_CODE_SENT&quot; |



