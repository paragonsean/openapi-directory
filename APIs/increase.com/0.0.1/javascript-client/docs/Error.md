# IncreaseApi.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **String** |  | 
**status** | **Number** |  | 
**title** | **String** |  | 
**type** | **String** |  | 
**errors** | **[Object]** | All errors related to parsing the request parameters. | 
**retryAfter** | **Number** |  | [optional] 



## Enum: StatusEnum


* `429` (value: `429`)





## Enum: TypeEnum


* `api_method_not_found_error` (value: `"api_method_not_found_error"`)

* `environment_mismatch_error` (value: `"environment_mismatch_error"`)

* `idempotency_conflict_error` (value: `"idempotency_conflict_error"`)

* `idempotency_unprocessable_error` (value: `"idempotency_unprocessable_error"`)

* `insufficient_permissions_error` (value: `"insufficient_permissions_error"`)

* `internal_server_error` (value: `"internal_server_error"`)

* `invalid_api_key_error` (value: `"invalid_api_key_error"`)

* `invalid_operation_error` (value: `"invalid_operation_error"`)

* `invalid_parameters_error` (value: `"invalid_parameters_error"`)

* `malformed_request_error` (value: `"malformed_request_error"`)

* `object_not_found_error` (value: `"object_not_found_error"`)

* `private_feature_error` (value: `"private_feature_error"`)

* `rate_limited_error` (value: `"rate_limited_error"`)




