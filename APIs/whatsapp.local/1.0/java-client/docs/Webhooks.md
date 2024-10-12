

# Webhooks


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxConcurrentRequests** | [**MaxConcurrentRequestsEnum**](#MaxConcurrentRequestsEnum) | Configures the maximum number of inflight callback requests that are sent out. Can be set to 6 (default), 12, 18, or 24. |  [optional] |
|**url** | **String** | Inbound and outbound notifications are routed to this URL. A HTTPS-based endpoint is required; HTTP will not work. |  [optional] |



## Enum: MaxConcurrentRequestsEnum

| Name | Value |
|---- | -----|
| NUMBER_6 | 6 |
| NUMBER_12 | 12 |
| NUMBER_18 | 18 |
| NUMBER_24 | 24 |



