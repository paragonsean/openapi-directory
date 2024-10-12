# AdSenseManagementApi.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Creation time of the account. | [optional] [readonly] 
**displayName** | **String** | Output only. Display name of this account. | [optional] [readonly] 
**name** | **String** | Output only. Resource name of the account. Format: accounts/pub-[0-9]+ | [optional] [readonly] 
**pendingTasks** | **[String]** | Output only. Outstanding tasks that need to be completed as part of the sign-up process for a new account. e.g. \&quot;billing-profile-creation\&quot;, \&quot;phone-pin-verification\&quot;. | [optional] [readonly] 
**premium** | **Boolean** | Output only. Whether this account is premium. | [optional] [readonly] 
**state** | **String** | Output only. State of the account. | [optional] [readonly] 
**timeZone** | [**TimeZone**](TimeZone.md) |  | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `READY` (value: `"READY"`)

* `NEEDS_ATTENTION` (value: `"NEEDS_ATTENTION"`)

* `CLOSED` (value: `"CLOSED"`)




