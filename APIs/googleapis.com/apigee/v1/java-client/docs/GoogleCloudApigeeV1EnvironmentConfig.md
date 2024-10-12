

# GoogleCloudApigeeV1EnvironmentConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addonsConfig** | [**GoogleCloudApigeeV1RuntimeAddonsConfig**](GoogleCloudApigeeV1RuntimeAddonsConfig.md) |  |  [optional] |
|**arcConfigLocation** | **String** | The location for the config blob of API Runtime Control, aka Envoy Adapter, for op-based authentication as a URI, e.g. a Cloud Storage URI. This is only used by Envoy-based gateways. |  [optional] |
|**createTime** | **String** | Time that the environment configuration was created. |  [optional] |
|**dataCollectors** | [**List&lt;GoogleCloudApigeeV1DataCollectorConfig&gt;**](GoogleCloudApigeeV1DataCollectorConfig.md) | List of data collectors used by the deployments in the environment. |  [optional] |
|**debugMask** | [**GoogleCloudApigeeV1DebugMask**](GoogleCloudApigeeV1DebugMask.md) |  |  [optional] |
|**deploymentGroups** | [**List&lt;GoogleCloudApigeeV1DeploymentGroupConfig&gt;**](GoogleCloudApigeeV1DeploymentGroupConfig.md) | List of deployment groups in the environment. |  [optional] |
|**deployments** | [**List&lt;GoogleCloudApigeeV1DeploymentConfig&gt;**](GoogleCloudApigeeV1DeploymentConfig.md) | List of deployments in the environment. |  [optional] |
|**envScopedRevisionId** | **String** | Revision ID for environment-scoped resources (e.g. target servers, keystores) in this config. This ID will increment any time a resource not scoped to a deployment group changes. |  [optional] |
|**featureFlags** | **Map&lt;String, String&gt;** | Feature flags inherited from the organization and environment. |  [optional] |
|**flowhooks** | [**List&lt;GoogleCloudApigeeV1FlowHookConfig&gt;**](GoogleCloudApigeeV1FlowHookConfig.md) | List of flow hooks in the environment. |  [optional] |
|**forwardProxyUri** | **String** | The forward proxy&#39;s url to be used by the runtime. When set, runtime will send requests to the target via the given forward proxy. This is only used by programmable gateways. |  [optional] |
|**gatewayConfigLocation** | **String** | The location for the gateway config blob as a URI, e.g. a Cloud Storage URI. This is only used by Envoy-based gateways. |  [optional] |
|**keystores** | [**List&lt;GoogleCloudApigeeV1KeystoreConfig&gt;**](GoogleCloudApigeeV1KeystoreConfig.md) | List of keystores in the environment. |  [optional] |
|**name** | **String** | Name of the environment configuration in the following format: &#x60;organizations/{org}/environments/{env}/configs/{config}&#x60; |  [optional] |
|**provider** | **String** | Used by the Control plane to add context information to help detect the source of the document during diagnostics and debugging. |  [optional] |
|**pubsubTopic** | **String** | Name of the PubSub topic for the environment. |  [optional] |
|**resourceReferences** | [**List&lt;GoogleCloudApigeeV1ReferenceConfig&gt;**](GoogleCloudApigeeV1ReferenceConfig.md) | List of resource references in the environment. |  [optional] |
|**resources** | [**List&lt;GoogleCloudApigeeV1ResourceConfig&gt;**](GoogleCloudApigeeV1ResourceConfig.md) | List of resource versions in the environment. |  [optional] |
|**revisionId** | **String** | Revision ID of the environment configuration. The higher the value, the more recently the configuration was deployed. |  [optional] |
|**sequenceNumber** | **String** | DEPRECATED: Use revision_id. |  [optional] |
|**targets** | [**List&lt;GoogleCloudApigeeV1TargetServerConfig&gt;**](GoogleCloudApigeeV1TargetServerConfig.md) | List of target servers in the environment. Disabled target servers are not displayed. |  [optional] |
|**traceConfig** | [**GoogleCloudApigeeV1RuntimeTraceConfig**](GoogleCloudApigeeV1RuntimeTraceConfig.md) |  |  [optional] |
|**uid** | **String** | Unique ID for the environment configuration. The ID will only change if the environment is deleted and recreated. |  [optional] |



