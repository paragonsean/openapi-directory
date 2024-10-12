# SecurityCenter.JitNetworkAccessRequestPort

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedSourceAddressPrefix** | **String** | Mutually exclusive with the \&quot;allowedSourceAddressPrefixes\&quot; parameter. Should be an IP address or CIDR, for example \&quot;192.168.0.3\&quot; or \&quot;192.168.0.0/16\&quot;. | [optional] 
**allowedSourceAddressPrefixes** | **[String]** | Mutually exclusive with the \&quot;allowedSourceAddressPrefix\&quot; parameter. | [optional] 
**endTimeUtc** | **Date** | The date &amp; time at which the request ends in UTC | 
**number** | **Number** |  | 
**status** | **String** | The status of the port | 
**statusReason** | **String** | A description of why the &#x60;status&#x60; has its value | 



## Enum: StatusEnum


* `Revoked` (value: `"Revoked"`)

* `Initiated` (value: `"Initiated"`)





## Enum: StatusReasonEnum


* `Expired` (value: `"Expired"`)

* `UserRequested` (value: `"UserRequested"`)

* `NewerRequestInitiated` (value: `"NewerRequestInitiated"`)




