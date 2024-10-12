

# CreateHeartbeat


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**application** | **String** | Optional string to identify which application logged this message. You can use this if you have multiple applications and services logging to the same log.  If not set, the application name \&quot;Heartbeats\&quot; will be set on all log messages generated from this heartbeat. |  [optional] |
|**reason** | **String** | If result is \&quot;Degraded\&quot; or \&quot;Unhealthy\&quot; you can use this property to specify why. |  [optional] |
|**result** | **String** | The result of this heartbeat. Can be \&quot;Healthy, \&quot;Degraded\&quot;, or \&quot;Unhealthy\&quot;. Defaults to \&quot;Healthy\&quot; |  [optional] |
|**took** | **Long** | Optional long for specifying how many milliseconds it took to execute the task resulting in this heartbeat. This can be used to get a better overview  of how long a scheduled task or service is running or to figure out if the grace period should be increased. |  [optional] |
|**version** | **String** | Optional string to identify which version of your application logged this message. If not specified, any errors, warnings, or information messages will get  the newest version number created through deployment tracking as with normal log messages. |  [optional] |



