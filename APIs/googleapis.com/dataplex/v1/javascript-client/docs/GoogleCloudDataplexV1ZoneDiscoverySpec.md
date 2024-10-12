# CloudDataplexApi.GoogleCloudDataplexV1ZoneDiscoverySpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csvOptions** | [**GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptions**](GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptions.md) |  | [optional] 
**enabled** | **Boolean** | Required. Whether discovery is enabled. | [optional] 
**excludePatterns** | **[String]** | Optional. The list of patterns to apply for selecting data to exclude during discovery. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names. | [optional] 
**includePatterns** | **[String]** | Optional. The list of patterns to apply for selecting data to include during discovery if only a subset of the data should considered. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names. | [optional] 
**jsonOptions** | [**GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptions**](GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptions.md) |  | [optional] 
**schedule** | **String** | Optional. Cron schedule (https://en.wikipedia.org/wiki/Cron) for running discovery periodically. Successive discovery runs must be scheduled at least 60 minutes apart. The default value is to run discovery every 60 minutes. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: \&quot;CRON_TZ&#x3D;${IANA_TIME_ZONE}\&quot; or TZ&#x3D;${IANA_TIME_ZONE}\&quot;. The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, CRON_TZ&#x3D;America/New_York 1 * * * *, or TZ&#x3D;America/New_York 1 * * * *. | [optional] 


