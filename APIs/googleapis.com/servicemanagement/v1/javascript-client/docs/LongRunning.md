# ServiceManagementApi.LongRunning

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initialPollDelay** | **String** | Initial delay after which the first poll request will be made. Default value: 5 seconds. | [optional] 
**maxPollDelay** | **String** | Maximum time between two subsequent poll requests. Default value: 45 seconds. | [optional] 
**pollDelayMultiplier** | **Number** | Multiplier to gradually increase delay between subsequent polls until it reaches max_poll_delay. Default value: 1.5. | [optional] 
**totalPollTimeout** | **String** | Total polling timeout. Default value: 5 minutes. | [optional] 


