# KubernetesEngineApi.MonitoringComponentConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableComponents** | **[String]** | Select components to collect metrics. An empty set would disable all monitoring. | [optional] 



## Enum: [EnableComponentsEnum]


* `COMPONENT_UNSPECIFIED` (value: `"COMPONENT_UNSPECIFIED"`)

* `SYSTEM_COMPONENTS` (value: `"SYSTEM_COMPONENTS"`)

* `WORKLOADS` (value: `"WORKLOADS"`)

* `APISERVER` (value: `"APISERVER"`)

* `SCHEDULER` (value: `"SCHEDULER"`)

* `CONTROLLER_MANAGER` (value: `"CONTROLLER_MANAGER"`)

* `STORAGE` (value: `"STORAGE"`)

* `HPA` (value: `"HPA"`)

* `POD` (value: `"POD"`)

* `DAEMONSET` (value: `"DAEMONSET"`)

* `DEPLOYMENT` (value: `"DEPLOYMENT"`)

* `STATEFULSET` (value: `"STATEFULSET"`)




