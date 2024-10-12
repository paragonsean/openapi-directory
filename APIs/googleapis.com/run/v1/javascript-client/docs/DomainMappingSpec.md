# CloudRunAdminApi.DomainMappingSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificateMode** | **String** | The mode of the certificate. | [optional] 
**forceOverride** | **Boolean** | If set, the mapping will override any mapping set before this spec was set. It is recommended that the user leaves this empty to receive an error warning about a potential conflict and only set it once the respective UI has given such a warning. | [optional] 
**routeName** | **String** | The name of the Knative Route that this DomainMapping applies to. The route must exist. | [optional] 



## Enum: CertificateModeEnum


* `CERTIFICATE_MODE_UNSPECIFIED` (value: `"CERTIFICATE_MODE_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `AUTOMATIC` (value: `"AUTOMATIC"`)




