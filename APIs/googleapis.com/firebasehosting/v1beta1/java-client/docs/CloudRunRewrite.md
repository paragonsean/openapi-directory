

# CloudRunRewrite

A configured rewrite that directs requests to a Cloud Run service. If the Cloud Run service does not exist when setting or updating your Firebase Hosting configuration, then the request fails. Any errors from the Cloud Run service are passed to the end user (for example, if you delete a service, any requests directed to that service receive a `404` error).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**region** | **String** | Optional. User-provided region where the Cloud Run service is hosted. Defaults to &#x60;us-central1&#x60; if not supplied. |  [optional] |
|**serviceId** | **String** | Required. User-defined ID of the Cloud Run service. |  [optional] |
|**tag** | **String** | Optional. User-provided TrafficConfig tag to send traffic to. When omitted, traffic is sent to the service-wide URI |  [optional] |



