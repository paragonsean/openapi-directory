

# GoogleDevtoolsRemoteworkersV1test2AdminTemp

AdminTemp is a prelimiary set of administration tasks. It's called \"Temp\" because we do not yet know the best way to represent admin tasks; it's possible that this will be entirely replaced in later versions of this API. If this message proves to be sufficient, it will be renamed in the alpha or beta release of this API. This message (suitably marshalled into a protobuf.Any) can be used as the inline_assignment field in a lease; the lease assignment field should simply be `\"admin\"` in these cases. This message is heavily based on Swarming administration tasks from the LUCI project (http://github.com/luci/luci-py/appengine/swarming).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arg** | **String** | The argument to the admin action; see &#x60;Command&#x60; for semantics. |  [optional] |
|**command** | [**CommandEnum**](#CommandEnum) | The admin action; see &#x60;Command&#x60; for legal values. |  [optional] |



## Enum: CommandEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| BOT_UPDATE | &quot;BOT_UPDATE&quot; |
| BOT_RESTART | &quot;BOT_RESTART&quot; |
| BOT_TERMINATE | &quot;BOT_TERMINATE&quot; |
| HOST_RESTART | &quot;HOST_RESTART&quot; |



