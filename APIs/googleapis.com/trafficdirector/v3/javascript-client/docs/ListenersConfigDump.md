# TrafficDirectorApi.ListenersConfigDump

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamicListeners** | [**[DynamicListener]**](DynamicListener.md) | State for any warming, active, or draining listeners. | [optional] 
**staticListeners** | [**[StaticListener]**](StaticListener.md) | The statically loaded listener configs. | [optional] 
**versionInfo** | **String** | This is the :ref:&#x60;version_info &#x60; in the last processed LDS discovery response. If there are only static bootstrap listeners, this field will be \&quot;\&quot;. | [optional] 


