

# ServiceConfig

Describes the Service being deployed. Currently Supported : Cloud Run (fully managed).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allTrafficOnLatestRevision** | **Boolean** | Whether 100% of traffic is routed to the latest revision. On CreateFunction and UpdateFunction, when set to true, the revision being deployed will serve 100% of traffic, ignoring any traffic split settings, if any. On GetFunction, true will be returned if the latest revision is serving 100% of traffic. |  [optional] |
|**availableCpu** | **String** | The number of CPUs used in a single container instance. Default value is calculated from available memory. Supports the same values as Cloud Run, see https://cloud.google.com/run/docs/reference/rest/v1/Container#resourcerequirements Example: \&quot;1\&quot; indicates 1 vCPU |  [optional] |
|**availableMemory** | **String** | The amount of memory available for a function. Defaults to 256M. Supported units are k, M, G, Mi, Gi. If no unit is supplied the value is interpreted as bytes. See https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go a full description. |  [optional] |
|**environmentVariables** | **Map&lt;String, String&gt;** | Environment variables that shall be available during function execution. |  [optional] |
|**ingressSettings** | [**IngressSettingsEnum**](#IngressSettingsEnum) | The ingress settings for the function, controlling what traffic can reach it. |  [optional] |
|**maxInstanceCount** | **Integer** | The limit on the maximum number of function instances that may coexist at a given time. In some cases, such as rapid traffic surges, Cloud Functions may, for a short period of time, create more instances than the specified max instances limit. If your function cannot tolerate this temporary behavior, you may want to factor in a safety margin and set a lower max instances value than your function can tolerate. See the [Max Instances](https://cloud.google.com/functions/docs/max-instances) Guide for more details. |  [optional] |
|**maxInstanceRequestConcurrency** | **Integer** | Sets the maximum number of concurrent requests that each instance can receive. Defaults to 1. |  [optional] |
|**minInstanceCount** | **Integer** | The limit on the minimum number of function instances that may coexist at a given time. Function instances are kept in idle state for a short period after they finished executing the request to reduce cold start time for subsequent requests. Setting a minimum instance count will ensure that the given number of instances are kept running in idle state always. This can help with cold start times when jump in incoming request count occurs after the idle instance would have been stopped in the default case. |  [optional] |
|**revision** | **String** | Output only. The name of service revision. |  [optional] [readonly] |
|**secretEnvironmentVariables** | [**List&lt;SecretEnvVar&gt;**](SecretEnvVar.md) | Secret environment variables configuration. |  [optional] |
|**secretVolumes** | [**List&lt;SecretVolume&gt;**](SecretVolume.md) | Secret volumes configuration. |  [optional] |
|**securityLevel** | [**SecurityLevelEnum**](#SecurityLevelEnum) | Security level configure whether the function only accepts https. This configuration is only applicable to 1st Gen functions with Http trigger. By default https is optional for 1st Gen functions; 2nd Gen functions are https ONLY. |  [optional] |
|**service** | **String** | Output only. Name of the service associated with a Function. The format of this field is &#x60;projects/{project}/locations/{region}/services/{service}&#x60; |  [optional] [readonly] |
|**serviceAccountEmail** | **String** | The email of the service&#39;s service account. If empty, defaults to &#x60;{project_number}-compute@developer.gserviceaccount.com&#x60;. |  [optional] |
|**timeoutSeconds** | **Integer** | The function execution timeout. Execution is considered failed and can be terminated if the function is not completed at the end of the timeout period. Defaults to 60 seconds. |  [optional] |
|**uri** | **String** | Output only. URI of the Service deployed. |  [optional] [readonly] |
|**vpcConnector** | **String** | The Serverless VPC Access connector that this cloud function can connect to. The format of this field is &#x60;projects/_*_/locations/_*_/connectors/_*&#x60;. |  [optional] |
|**vpcConnectorEgressSettings** | [**VpcConnectorEgressSettingsEnum**](#VpcConnectorEgressSettingsEnum) | The egress settings for the connector, controlling what traffic is diverted through it. |  [optional] |



## Enum: IngressSettingsEnum

| Name | Value |
|---- | -----|
| INGRESS_SETTINGS_UNSPECIFIED | &quot;INGRESS_SETTINGS_UNSPECIFIED&quot; |
| ALLOW_ALL | &quot;ALLOW_ALL&quot; |
| ALLOW_INTERNAL_ONLY | &quot;ALLOW_INTERNAL_ONLY&quot; |
| ALLOW_INTERNAL_AND_GCLB | &quot;ALLOW_INTERNAL_AND_GCLB&quot; |



## Enum: SecurityLevelEnum

| Name | Value |
|---- | -----|
| SECURITY_LEVEL_UNSPECIFIED | &quot;SECURITY_LEVEL_UNSPECIFIED&quot; |
| SECURE_ALWAYS | &quot;SECURE_ALWAYS&quot; |
| SECURE_OPTIONAL | &quot;SECURE_OPTIONAL&quot; |



## Enum: VpcConnectorEgressSettingsEnum

| Name | Value |
|---- | -----|
| VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED | &quot;VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED&quot; |
| PRIVATE_RANGES_ONLY | &quot;PRIVATE_RANGES_ONLY&quot; |
| ALL_TRAFFIC | &quot;ALL_TRAFFIC&quot; |



