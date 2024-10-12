# FirebaseHostingApi.CloudRunRewrite

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **String** | Optional. User-provided region where the Cloud Run service is hosted. Defaults to &#x60;us-central1&#x60; if not supplied. | [optional] 
**serviceId** | **String** | Required. User-defined ID of the Cloud Run service. | [optional] 
**tag** | **String** | Optional. User-provided TrafficConfig tag to send traffic to. When omitted, traffic is sent to the service-wide URI | [optional] 


