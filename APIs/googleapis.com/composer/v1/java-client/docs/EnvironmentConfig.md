

# EnvironmentConfig

Configuration information for an environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**airflowByoidUri** | **String** | Output only. The &#39;bring your own identity&#39; variant of the URI of the Apache Airflow Web UI hosted within this environment, to be accessed with external identities using workforce identity federation (see [Access environments with workforce identity federation](/composer/docs/composer-2/access-environments-with-workforce-identity-federation)). |  [optional] [readonly] |
|**airflowUri** | **String** | Output only. The URI of the Apache Airflow Web UI hosted within this environment (see [Airflow web interface](/composer/docs/how-to/accessing/airflow-web-interface)). |  [optional] |
|**dagGcsPrefix** | **String** | Output only. The Cloud Storage prefix of the DAGs for this environment. Although Cloud Storage objects reside in a flat namespace, a hierarchical file tree can be simulated using \&quot;/\&quot;-delimited object name prefixes. DAG objects for this environment reside in a simulated directory with the given prefix. |  [optional] |
|**dataRetentionConfig** | [**DataRetentionConfig**](DataRetentionConfig.md) |  |  [optional] |
|**databaseConfig** | [**DatabaseConfig**](DatabaseConfig.md) |  |  [optional] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**environmentSize** | [**EnvironmentSizeEnum**](#EnvironmentSizeEnum) | Optional. The size of the Cloud Composer environment. This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. |  [optional] |
|**gkeCluster** | **String** | Output only. The Kubernetes Engine cluster used to run this environment. |  [optional] |
|**maintenanceWindow** | [**MaintenanceWindow**](MaintenanceWindow.md) |  |  [optional] |
|**masterAuthorizedNetworksConfig** | [**MasterAuthorizedNetworksConfig**](MasterAuthorizedNetworksConfig.md) |  |  [optional] |
|**nodeConfig** | [**NodeConfig**](NodeConfig.md) |  |  [optional] |
|**nodeCount** | **Integer** | The number of nodes in the Kubernetes Engine cluster that will be used to run this environment. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. |  [optional] |
|**privateEnvironmentConfig** | [**PrivateEnvironmentConfig**](PrivateEnvironmentConfig.md) |  |  [optional] |
|**recoveryConfig** | [**RecoveryConfig**](RecoveryConfig.md) |  |  [optional] |
|**resilienceMode** | [**ResilienceModeEnum**](#ResilienceModeEnum) | Optional. Resilience mode of the Cloud Composer Environment. This field is supported for Cloud Composer environments in versions composer-2.2.0-airflow-*.*.* and newer. |  [optional] |
|**softwareConfig** | [**SoftwareConfig**](SoftwareConfig.md) |  |  [optional] |
|**webServerConfig** | [**WebServerConfig**](WebServerConfig.md) |  |  [optional] |
|**webServerNetworkAccessControl** | [**WebServerNetworkAccessControl**](WebServerNetworkAccessControl.md) |  |  [optional] |
|**workloadsConfig** | [**WorkloadsConfig**](WorkloadsConfig.md) |  |  [optional] |



## Enum: EnvironmentSizeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENVIRONMENT_SIZE_UNSPECIFIED&quot; |
| SMALL | &quot;ENVIRONMENT_SIZE_SMALL&quot; |
| MEDIUM | &quot;ENVIRONMENT_SIZE_MEDIUM&quot; |
| LARGE | &quot;ENVIRONMENT_SIZE_LARGE&quot; |



## Enum: ResilienceModeEnum

| Name | Value |
|---- | -----|
| RESILIENCE_MODE_UNSPECIFIED | &quot;RESILIENCE_MODE_UNSPECIFIED&quot; |
| HIGH_RESILIENCE | &quot;HIGH_RESILIENCE&quot; |



