# LookerGoogleCloudCoreApi.ServiceAttachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionStatus** | **String** | Output only. Connection status. | [optional] [readonly] 
**localFqdn** | **String** | Required. Fully qualified domain name that will be used in the private DNS record created for the service attachment. | [optional] 
**targetServiceAttachmentUri** | **String** | Required. URI of the service attachment to connect to. Format: projects/{project}/regions/{region}/serviceAttachments/{service_attachment} | [optional] 



## Enum: ConnectionStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `ACCEPTED` (value: `"ACCEPTED"`)

* `PENDING` (value: `"PENDING"`)

* `REJECTED` (value: `"REJECTED"`)

* `NEEDS_ATTENTION` (value: `"NEEDS_ATTENTION"`)

* `CLOSED` (value: `"CLOSED"`)




