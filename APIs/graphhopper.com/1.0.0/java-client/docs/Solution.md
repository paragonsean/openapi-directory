

# Solution

Only available if status field indicates `finished`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completionTime** | **Long** | Overall completion time in seconds, i.e. the sum of each routes/drivers operation time. |  [optional] |
|**costs** | **Integer** |  |  [optional] |
|**distance** | **Integer** | Overall distance travelled in meter, i.e. the sum of each route&#39;s transport distance |  [optional] |
|**maxOperationTime** | **Long** | Operation time of longest route in seconds. |  [optional] |
|**noUnassigned** | **Integer** | Number of jobs that could not be assigned to final solution. |  [optional] |
|**noVehicles** | **Integer** | Number of employed vehicles. |  [optional] |
|**preparationTime** | **Long** | Overall preparation time in seconds. |  [optional] |
|**routes** | [**List&lt;Route&gt;**](Route.md) | An array of routes |  [optional] |
|**serviceDuration** | **Long** | Overall service time in seconds. |  [optional] |
|**time** | **Long** | Use &#x60;transport_time&#x60; instead. |  [optional] |
|**transportTime** | **Long** | Overall time travelled in seconds, i.e. the sum of each route&#39;s transport time. |  [optional] |
|**unassigned** | [**SolutionUnassigned**](SolutionUnassigned.md) |  |  [optional] |
|**waitingTime** | **Long** | Overall waiting time in seconds. |  [optional] |



