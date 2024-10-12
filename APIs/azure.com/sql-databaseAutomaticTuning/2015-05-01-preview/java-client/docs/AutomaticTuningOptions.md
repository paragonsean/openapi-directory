

# AutomaticTuningOptions

Automatic tuning properties for individual advisors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actualState** | [**ActualStateEnum**](#ActualStateEnum) | Automatic tuning option actual state. |  [optional] [readonly] |
|**desiredState** | [**DesiredStateEnum**](#DesiredStateEnum) | Automatic tuning option desired state. |  [optional] |
|**reasonCode** | **Integer** | Reason code if desired and actual state are different. |  [optional] [readonly] |
|**reasonDesc** | [**ReasonDescEnum**](#ReasonDescEnum) | Reason description if desired and actual state are different. |  [optional] [readonly] |



## Enum: ActualStateEnum

| Name | Value |
|---- | -----|
| OFF | &quot;Off&quot; |
| ON | &quot;On&quot; |



## Enum: DesiredStateEnum

| Name | Value |
|---- | -----|
| OFF | &quot;Off&quot; |
| ON | &quot;On&quot; |
| DEFAULT | &quot;Default&quot; |



## Enum: ReasonDescEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |
| AUTO_CONFIGURED | &quot;AutoConfigured&quot; |
| INHERITED_FROM_SERVER | &quot;InheritedFromServer&quot; |
| QUERY_STORE_OFF | &quot;QueryStoreOff&quot; |
| QUERY_STORE_READ_ONLY | &quot;QueryStoreReadOnly&quot; |
| NOT_SUPPORTED | &quot;NotSupported&quot; |



