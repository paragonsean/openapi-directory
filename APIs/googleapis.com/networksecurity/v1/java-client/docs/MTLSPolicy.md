

# MTLSPolicy

Specification of the MTLSPolicy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientValidationCa** | [**List&lt;ValidationCA&gt;**](ValidationCA.md) | Required if the policy is to be used with Traffic Director. For external HTTPS load balancers it must be empty. Defines the mechanism to obtain the Certificate Authority certificate to validate the client certificate. |  [optional] |
|**clientValidationMode** | [**ClientValidationModeEnum**](#ClientValidationModeEnum) | When the client presents an invalid certificate or no certificate to the load balancer, the &#x60;client_validation_mode&#x60; specifies how the client connection is handled. Required if the policy is to be used with the external HTTPS load balancing. For Traffic Director it must be empty. |  [optional] |
|**clientValidationTrustConfig** | **String** | Reference to the TrustConfig from certificatemanager.googleapis.com namespace. If specified, the chain validation will be performed against certificates configured in the given TrustConfig. Allowed only if the policy is to be used with external HTTPS load balancers. |  [optional] |



## Enum: ClientValidationModeEnum

| Name | Value |
|---- | -----|
| CLIENT_VALIDATION_MODE_UNSPECIFIED | &quot;CLIENT_VALIDATION_MODE_UNSPECIFIED&quot; |
| ALLOW_INVALID_OR_MISSING_CLIENT_CERT | &quot;ALLOW_INVALID_OR_MISSING_CLIENT_CERT&quot; |
| REJECT_INVALID | &quot;REJECT_INVALID&quot; |



