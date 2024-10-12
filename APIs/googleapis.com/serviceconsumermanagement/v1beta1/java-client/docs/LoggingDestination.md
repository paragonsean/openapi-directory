

# LoggingDestination

Configuration of a specific logging destination (the producer project or the consumer project).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**logs** | **List&lt;String&gt;** | Names of the logs to be sent to this destination. Each name must be defined in the Service.logs section. If the log name is not a domain scoped name, it will be automatically prefixed with the service name followed by \&quot;/\&quot;. |  [optional] |
|**monitoredResource** | **String** | The monitored resource type. The type must be defined in the Service.monitored_resources section. |  [optional] |



