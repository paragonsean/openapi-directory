

# GoogleCloudDataplexV1AssetDiscoverySpec

Settings to manage the metadata discovery and publishing for an asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**csvOptions** | [**GoogleCloudDataplexV1AssetDiscoverySpecCsvOptions**](GoogleCloudDataplexV1AssetDiscoverySpecCsvOptions.md) |  |  [optional] |
|**enabled** | **Boolean** | Optional. Whether discovery is enabled. |  [optional] |
|**excludePatterns** | **List&lt;String&gt;** | Optional. The list of patterns to apply for selecting data to exclude during discovery. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names. |  [optional] |
|**includePatterns** | **List&lt;String&gt;** | Optional. The list of patterns to apply for selecting data to include during discovery if only a subset of the data should considered. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names. |  [optional] |
|**jsonOptions** | [**GoogleCloudDataplexV1AssetDiscoverySpecJsonOptions**](GoogleCloudDataplexV1AssetDiscoverySpecJsonOptions.md) |  |  [optional] |
|**schedule** | **String** | Optional. Cron schedule (https://en.wikipedia.org/wiki/Cron) for running discovery periodically. Successive discovery runs must be scheduled at least 60 minutes apart. The default value is to run discovery every 60 minutes. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: \&quot;CRON_TZ&#x3D;${IANA_TIME_ZONE}\&quot; or TZ&#x3D;${IANA_TIME_ZONE}\&quot;. The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, CRON_TZ&#x3D;America/New_York 1 * * * *, or TZ&#x3D;America/New_York 1 * * * *. |  [optional] |



