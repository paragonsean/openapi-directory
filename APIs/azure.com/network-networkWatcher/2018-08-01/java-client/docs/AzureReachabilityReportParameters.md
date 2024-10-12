

# AzureReachabilityReportParameters

Geographic and time constraints for Azure reachability report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureLocations** | **List&lt;String&gt;** | Optional Azure regions to scope the query to. |  [optional] |
|**endTime** | **OffsetDateTime** | The end time for the Azure reachability report. |  |
|**providerLocation** | [**AzureReachabilityReportLocation**](AzureReachabilityReportLocation.md) |  |  |
|**providers** | **List&lt;String&gt;** | List of Internet service providers. |  [optional] |
|**startTime** | **OffsetDateTime** | The start time for the Azure reachability report. |  |



