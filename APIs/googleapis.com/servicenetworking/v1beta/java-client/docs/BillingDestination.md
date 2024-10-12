

# BillingDestination

Configuration of a specific billing destination (Currently only support bill against consumer project).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metrics** | **List&lt;String&gt;** | Names of the metrics to report to this billing destination. Each name must be defined in Service.metrics section. |  [optional] |
|**monitoredResource** | **String** | The monitored resource type. The type must be defined in Service.monitored_resources section. |  [optional] |



