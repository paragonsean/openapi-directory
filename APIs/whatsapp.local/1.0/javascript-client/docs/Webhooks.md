# WhatsAppBusinessApi.Webhooks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxConcurrentRequests** | **Number** | Configures the maximum number of inflight callback requests that are sent out. Can be set to 6 (default), 12, 18, or 24. | [optional] [default to MaxConcurrentRequestsEnum.6]
**url** | **String** | Inbound and outbound notifications are routed to this URL. A HTTPS-based endpoint is required; HTTP will not work. | [optional] 



## Enum: MaxConcurrentRequestsEnum


* `6` (value: `6`)

* `12` (value: `12`)

* `18` (value: `18`)

* `24` (value: `24`)




