

# HostSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | A user-specified string that returns this host in searches. |  [optional] |
|**hdfsBaseConfig** | [**HdfsBaseConfig**](HdfsBaseConfig.md) |  |  [optional] |
|**hostname** | **String** | Deprecated. Please use &#39;name&#39; instead. |  |
|**id** | **String** | Unique identifier for host. |  |
|**mssqlCbtEffectiveStatus** | **MssqlCbtEffectiveStatusType** |  |  [optional] |
|**mssqlCbtEnabled** | **MssqlCbtStatusType** |  |  [optional] |
|**name** | **String** | IP address or hostname of the host. |  [optional] |
|**nasBaseConfig** | [**NasBaseConfig**](NasBaseConfig.md) |  |  [optional] |
|**operatingSystem** | **String** | Operating system of the host. One of Windows, Linux, AIX, HPUX, and SunOS. |  [optional] |
|**operatingSystemType** | **String** | The operating system of the host. Possible choices are Windows, Linux, AIX, HPUX, SunOS. |  [optional] |
|**organizationId** | **String** | The ID of the organization to which the host is assigned (set by envoy). |  [optional] |
|**organizationName** | **String** | The name of the organization to which the host is assigned (set by envoy). |  [optional] |
|**primaryClusterId** | **String** | ID of the Rubrik cluster to which the host belongs. |  [optional] |
|**status** | **String** | Specifies the connect status for the host. Status is Refreshing while discovery is running or Connected once discovery was successful and the host is available. |  [optional] |



