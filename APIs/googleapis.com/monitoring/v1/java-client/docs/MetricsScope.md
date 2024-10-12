

# MetricsScope

Represents a Metrics Scope (https://cloud.google.com/monitoring/settings#concept-scope) in Cloud Monitoring, which specifies one or more Google projects and zero or more AWS accounts to monitor together.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when this Metrics Scope was created. |  [optional] [readonly] |
|**monitoredProjects** | [**List&lt;MonitoredProject&gt;**](MonitoredProject.md) | Output only. The list of projects monitored by this Metrics Scope. |  [optional] [readonly] |
|**name** | **String** | Immutable. The resource name of the Monitoring Metrics Scope. On input, the resource name can be specified with the scoping project ID or number. On output, the resource name is specified with the scoping project number. Example: locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER} |  [optional] |
|**updateTime** | **String** | Output only. The time when this Metrics Scope record was last updated. |  [optional] [readonly] |



