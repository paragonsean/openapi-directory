# AwsGroundStation.ListEphemeridesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The end time to list in UTC. The operation will return an ephemeris if its expiration time is within the time range defined by the &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. | 
**satelliteId** | **String** | The AWS Ground Station satellite ID to list ephemeris for. | 
**startTime** | **Date** | The start time to list in UTC. The operation will return an ephemeris if its expiration time is within the time range defined by the &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. | 
**statusList** | [**[EphemerisStatus]**](EphemerisStatus.md) | The list of ephemeris status to return. | [optional] 


