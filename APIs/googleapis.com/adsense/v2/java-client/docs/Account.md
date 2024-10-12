

# Account

Representation of an account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Creation time of the account. |  [optional] [readonly] |
|**displayName** | **String** | Output only. Display name of this account. |  [optional] [readonly] |
|**name** | **String** | Output only. Resource name of the account. Format: accounts/pub-[0-9]+ |  [optional] [readonly] |
|**pendingTasks** | **List&lt;String&gt;** | Output only. Outstanding tasks that need to be completed as part of the sign-up process for a new account. e.g. \&quot;billing-profile-creation\&quot;, \&quot;phone-pin-verification\&quot;. |  [optional] [readonly] |
|**premium** | **Boolean** | Output only. Whether this account is premium. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the account. |  [optional] [readonly] |
|**timeZone** | [**TimeZone**](TimeZone.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| READY | &quot;READY&quot; |
| NEEDS_ATTENTION | &quot;NEEDS_ATTENTION&quot; |
| CLOSED | &quot;CLOSED&quot; |



