

# ListEphemeridesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The end time to list in UTC. The operation will return an ephemeris if its expiration time is within the time range defined by the &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. |  |
|**satelliteId** | **String** | The AWS Ground Station satellite ID to list ephemeris for. |  |
|**startTime** | **OffsetDateTime** | The start time to list in UTC. The operation will return an ephemeris if its expiration time is within the time range defined by the &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. |  |
|**statusList** | **List&lt;EphemerisStatus&gt;** | The list of ephemeris status to return. |  [optional] |



