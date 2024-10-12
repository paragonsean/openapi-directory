# AlerterSystemApi.PingGet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertLogs** | **[String]** | The alert logs that are related to this resource instance. | [optional] 
**createdAt** | **Date** | When the resource instance was created. This date-time is in the UTC timezone. | [optional] [readonly] 
**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. | [optional] 
**expectNextPingAt** | **Date** | When to expect the next ping for a Last Ping monitor type. This date-time is always interpreted to be in the timezone of the monitor. Any UTC offset is ignored. Supply either \&quot;expectNextPingAt\&quot;, or \&quot;expectNextPingAtEpoch\&quot;, or a X_NEXT_PING request header, not more than one of those options. Must be blank for other monitor types. | [optional] 
**expectNextPingAtEpoch** | **Number** | When to expect the next ping for a Last Ping monitor type, expressed in epoch timestamp format. Supply either \&quot;expectNextPingAt\&quot;, or \&quot;expectNextPingAtEpoch\&quot;, or a X_NEXT_PING request header, not more than one of those options. Must be blank for other monitor types. | [optional] 
**id** | **String** | The unique identifier of the resource instance. | [optional] [readonly] 
**ipAddress** | **String** | The IP address where this resource originated. | [optional] 
**monitor** | **String** | The monitor that is related to this resource instance. | 
**monitorStatusLog** | **String** | The monitor status that resulted from the ping. | [optional] 
**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. | [optional] 
**pingCustomCode** | **String** | The client-supplied custom code that is appended to the ping. Only the first 10 characters are used and saved. | [optional] 
**pingCustomPayload** | **String** | The client-supplied custom payload that is saved with the ping. Only the first 100 characters are saved. This value overrides the value of an monitor&#39;s alert payload, if the ping results in an alert. | [optional] 
**pingMethodCode** | **String** | The method of the ping. | [optional] 
**resourceOwner** | **String** | The name of the person who owns this resource. | [optional] 


