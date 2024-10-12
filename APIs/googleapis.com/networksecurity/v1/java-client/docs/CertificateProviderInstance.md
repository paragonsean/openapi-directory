

# CertificateProviderInstance

Specification of a TLS certificate provider instance. Workloads may have one or more CertificateProvider instances (plugins) and one of them is enabled and configured by specifying this message. Workloads use the values from this message to locate and load the CertificateProvider instance configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pluginInstance** | **String** | Required. Plugin instance name, used to locate and load CertificateProvider instance configuration. Set to \&quot;google_cloud_private_spiffe\&quot; to use Certificate Authority Service certificate provider instance. |  [optional] |



