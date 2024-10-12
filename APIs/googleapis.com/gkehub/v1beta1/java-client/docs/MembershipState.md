

# MembershipState

State of the Membership resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Output only. The current state of the Membership resource. |  [optional] [readonly] |
|**description** | **String** | This field is never set by the Hub Service. |  [optional] |
|**updateTime** | **String** | This field is never set by the Hub Service. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| SERVICE_UPDATING | &quot;SERVICE_UPDATING&quot; |



