

# VcdClusterDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainType** | **ConfiguredSlaType** |  |  [optional] |
|**id** | **String** | ID assigned to a vCD Cluster object. |  |
|**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**name** | **String** | The name of the Rubrik object. |  |
|**primaryClusterId** | **String** | The ID of the cluster that manages the Rubrik object. |  |
|**slaLastUpdateTime** | **OffsetDateTime** | The UTC time when the SLA Domain was last updated. |  [optional] |
|**caCerts** | **String** | Concatenated X.509 certificates in Base64 encoded DER format. Each certificate must start with -----BEGIN CERTIFICATE----- and end with -----END CERTIFICATE-----. |  [optional] |
|**hostname** | **String** |  |  |
|**username** | **String** |  |  |
|**connectionStatus** | [**VcdConnectionStatus**](VcdConnectionStatus.md) |  |  [optional] |



