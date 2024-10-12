

# MonitoringComponentConfig

MonitoringComponentConfig is cluster monitoring component configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableComponents** | [**List&lt;EnableComponentsEnum&gt;**](#List&lt;EnableComponentsEnum&gt;) | Select components to collect metrics. An empty set would disable all monitoring. |  [optional] |



## Enum: List&lt;EnableComponentsEnum&gt;

| Name | Value |
|---- | -----|
| COMPONENT_UNSPECIFIED | &quot;COMPONENT_UNSPECIFIED&quot; |
| SYSTEM_COMPONENTS | &quot;SYSTEM_COMPONENTS&quot; |
| APISERVER | &quot;APISERVER&quot; |
| SCHEDULER | &quot;SCHEDULER&quot; |
| CONTROLLER_MANAGER | &quot;CONTROLLER_MANAGER&quot; |
| STORAGE | &quot;STORAGE&quot; |
| HPA | &quot;HPA&quot; |
| POD | &quot;POD&quot; |
| DAEMONSET | &quot;DAEMONSET&quot; |
| DEPLOYMENT | &quot;DEPLOYMENT&quot; |
| STATEFULSET | &quot;STATEFULSET&quot; |



