

# LinodeStats

CPU, IO, IPv4, and IPv6 statistics. Graph data, if available, is in \"[timestamp, reading]\" array format. Timestamp is a UNIX timestamp in EST. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cpu** | **List&lt;List&lt;BigDecimal&gt;&gt;** | Percentage of CPU used.  |  [optional] |
|**io** | [**LinodeStatsIo**](LinodeStatsIo.md) |  |  [optional] |
|**netv4** | [**LinodeStatsNetv4**](LinodeStatsNetv4.md) |  |  [optional] |
|**netv6** | [**LinodeStatsNetv6**](LinodeStatsNetv6.md) |  |  [optional] |
|**title** | **String** | The title for this data set. |  [optional] |



