

# BackendPoolsSettings

Settings that apply to all backend pools.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enforceCertificateNameCheck** | [**EnforceCertificateNameCheckEnum**](#EnforceCertificateNameCheckEnum) | Whether to enforce certificate name check on HTTPS requests to all backend pools. No effect on non-HTTPS requests. |  [optional] |
|**sendRecvTimeoutSeconds** | **Integer** | Send and receive timeout on forwarding request to the backend. When timeout is reached, the request fails and returns. |  [optional] |



## Enum: EnforceCertificateNameCheckEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



