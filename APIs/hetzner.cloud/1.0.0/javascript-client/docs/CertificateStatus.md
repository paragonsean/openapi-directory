# HetznerCloudApi.CertificateStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**CertificateStatusError**](CertificateStatusError.md) |  | [optional] 
**issuance** | **String** | Status of the issuance process of the Certificate | [optional] 
**renewal** | **String** | Status of the renewal process of the Certificate. | [optional] 



## Enum: IssuanceEnum


* `pending` (value: `"pending"`)

* `completed` (value: `"completed"`)

* `failed` (value: `"failed"`)





## Enum: RenewalEnum


* `scheduled` (value: `"scheduled"`)

* `pending` (value: `"pending"`)

* `failed` (value: `"failed"`)

* `unavailable` (value: `"unavailable"`)




