

# GooglePrivacyDlpV2DataProfileJobConfig

Configuration for setting up a job to scan resources for profile generation. Only one data profile configuration may exist per organization, folder, or project. The generated data profiles are retained according to the [data retention policy] (https://cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataProfileActions** | [**List&lt;GooglePrivacyDlpV2DataProfileAction&gt;**](GooglePrivacyDlpV2DataProfileAction.md) | Actions to execute at the completion of the job. |  [optional] |
|**inspectTemplates** | **List&lt;String&gt;** | Detection logic for profile generation. Not all template features are used by profiles. FindingLimits, include_quote and exclude_info_types have no impact on data profiling. Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including \&quot;global\&quot;). Each region is scanned using the applicable template. If no region-specific template is specified, but a \&quot;global\&quot; template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region&#39;s data will not be scanned. For more information, see https://cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency. |  [optional] |
|**location** | [**GooglePrivacyDlpV2DataProfileLocation**](GooglePrivacyDlpV2DataProfileLocation.md) |  |  [optional] |
|**projectId** | **String** | The project that will run the scan. The DLP service account that exists within this project must have access to all resources that are profiled, and the Cloud DLP API must be enabled. |  [optional] |



