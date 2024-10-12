

# ReleaseChannel

ReleaseChannel indicates which release channel a cluster is subscribed to. Release channels are arranged in order of risk. When a cluster is subscribed to a release channel, Google maintains both the master version and the node version. Node auto-upgrade defaults to true and cannot be disabled.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) | channel specifies which release channel the cluster is subscribed to. |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| RAPID | &quot;RAPID&quot; |
| REGULAR | &quot;REGULAR&quot; |
| STABLE | &quot;STABLE&quot; |



