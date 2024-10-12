# GraphHopperDirectionsApi.Solution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completionTime** | **Number** | Overall completion time in seconds, i.e. the sum of each routes/drivers operation time. | [optional] 
**costs** | **Number** |  | [optional] 
**distance** | **Number** | Overall distance travelled in meter, i.e. the sum of each route&#39;s transport distance | [optional] 
**maxOperationTime** | **Number** | Operation time of longest route in seconds. | [optional] 
**noUnassigned** | **Number** | Number of jobs that could not be assigned to final solution. | [optional] 
**noVehicles** | **Number** | Number of employed vehicles. | [optional] 
**preparationTime** | **Number** | Overall preparation time in seconds. | [optional] 
**routes** | [**[Route]**](Route.md) | An array of routes | [optional] 
**serviceDuration** | **Number** | Overall service time in seconds. | [optional] 
**time** | **Number** | Use &#x60;transport_time&#x60; instead. | [optional] 
**transportTime** | **Number** | Overall time travelled in seconds, i.e. the sum of each route&#39;s transport time. | [optional] 
**unassigned** | [**SolutionUnassigned**](SolutionUnassigned.md) |  | [optional] 
**waitingTime** | **Number** | Overall waiting time in seconds. | [optional] 


