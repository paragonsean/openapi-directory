

# ServiceAttachment

Service attachment configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionStatus** | [**ConnectionStatusEnum**](#ConnectionStatusEnum) | Output only. Connection status. |  [optional] [readonly] |
|**localFqdn** | **String** | Required. Fully qualified domain name that will be used in the private DNS record created for the service attachment. |  [optional] |
|**targetServiceAttachmentUri** | **String** | Required. URI of the service attachment to connect to. Format: projects/{project}/regions/{region}/serviceAttachments/{service_attachment} |  [optional] |



## Enum: ConnectionStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| PENDING | &quot;PENDING&quot; |
| REJECTED | &quot;REJECTED&quot; |
| NEEDS_ATTENTION | &quot;NEEDS_ATTENTION&quot; |
| CLOSED | &quot;CLOSED&quot; |



