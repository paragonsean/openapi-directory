

# ListContactsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | End time of a contact in UTC. |  |
|**groundStation** | **String** | Name of a ground station. |  [optional] |
|**maxResults** | **Integer** | Maximum number of contacts returned. |  [optional] |
|**missionProfileArn** | **String** | ARN of a mission profile. |  [optional] |
|**nextToken** | **String** | Next token returned in the request of a previous &lt;code&gt;ListContacts&lt;/code&gt; call. Used to get the next page of results. |  [optional] |
|**satelliteArn** | **String** | ARN of a satellite. |  [optional] |
|**startTime** | **OffsetDateTime** | Start time of a contact in UTC. |  |
|**statusList** | **List&lt;ContactStatus&gt;** | Status of a contact reservation. |  |



