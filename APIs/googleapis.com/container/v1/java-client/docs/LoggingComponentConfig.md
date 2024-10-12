

# LoggingComponentConfig

LoggingComponentConfig is cluster logging component configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableComponents** | [**List&lt;EnableComponentsEnum&gt;**](#List&lt;EnableComponentsEnum&gt;) | Select components to collect logs. An empty set would disable all logging. |  [optional] |



## Enum: List&lt;EnableComponentsEnum&gt;

| Name | Value |
|---- | -----|
| COMPONENT_UNSPECIFIED | &quot;COMPONENT_UNSPECIFIED&quot; |
| SYSTEM_COMPONENTS | &quot;SYSTEM_COMPONENTS&quot; |
| WORKLOADS | &quot;WORKLOADS&quot; |
| APISERVER | &quot;APISERVER&quot; |
| SCHEDULER | &quot;SCHEDULER&quot; |
| CONTROLLER_MANAGER | &quot;CONTROLLER_MANAGER&quot; |



