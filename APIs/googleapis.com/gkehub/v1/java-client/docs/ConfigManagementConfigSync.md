

# ConfigManagementConfigSync

Configuration for Config Sync

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowVerticalScale** | **Boolean** | Set to true to allow the vertical scaling. Defaults to false which disallows vertical scaling. This field is deprecated. |  [optional] |
|**enabled** | **Boolean** | Enables the installation of ConfigSync. If set to true, ConfigSync resources will be created and the other ConfigSync fields will be applied if exist. If set to false, all other ConfigSync fields will be ignored, ConfigSync resources will be deleted. If omitted, ConfigSync resources will be managed depends on the presence of the git or oci field. |  [optional] |
|**git** | [**ConfigManagementGitConfig**](ConfigManagementGitConfig.md) |  |  [optional] |
|**metricsGcpServiceAccountEmail** | **String** | The Email of the Google Cloud Service Account (GSA) used for exporting Config Sync metrics to Cloud Monitoring and Cloud Monarch when Workload Identity is enabled. The GSA should have the Monitoring Metric Writer (roles/monitoring.metricWriter) IAM role. The Kubernetes ServiceAccount &#x60;default&#x60; in the namespace &#x60;config-management-monitoring&#x60; should be bound to the GSA. |  [optional] |
|**oci** | [**ConfigManagementOciConfig**](ConfigManagementOciConfig.md) |  |  [optional] |
|**preventDrift** | **Boolean** | Set to true to enable the Config Sync admission webhook to prevent drifts. If set to &#x60;false&#x60;, disables the Config Sync admission webhook and does not prevent drifts. |  [optional] |
|**sourceFormat** | **String** | Specifies whether the Config Sync Repo is in \&quot;hierarchical\&quot; or \&quot;unstructured\&quot; mode. |  [optional] |



