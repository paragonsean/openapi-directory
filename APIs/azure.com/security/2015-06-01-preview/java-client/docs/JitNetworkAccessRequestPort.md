

# JitNetworkAccessRequestPort


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedSourceAddressPrefix** | **String** | Mutually exclusive with the \&quot;allowedSourceAddressPrefixes\&quot; parameter. Should be an IP address or CIDR, for example \&quot;192.168.0.3\&quot; or \&quot;192.168.0.0/16\&quot;. |  [optional] |
|**allowedSourceAddressPrefixes** | **List&lt;String&gt;** | Mutually exclusive with the \&quot;allowedSourceAddressPrefix\&quot; parameter. |  [optional] |
|**endTimeUtc** | **OffsetDateTime** | The date &amp; time at which the request ends in UTC |  |
|**number** | **Integer** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the port |  |
|**statusReason** | [**StatusReasonEnum**](#StatusReasonEnum) | A description of why the &#x60;status&#x60; has its value |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| REVOKED | &quot;Revoked&quot; |
| INITIATED | &quot;Initiated&quot; |



## Enum: StatusReasonEnum

| Name | Value |
|---- | -----|
| EXPIRED | &quot;Expired&quot; |
| USER_REQUESTED | &quot;UserRequested&quot; |
| NEWER_REQUEST_INITIATED | &quot;NewerRequestInitiated&quot; |



