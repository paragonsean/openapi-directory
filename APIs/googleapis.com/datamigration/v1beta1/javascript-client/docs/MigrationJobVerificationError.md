# DatabaseMigrationApi.MigrationJobVerificationError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorCode** | **String** | Output only. An instance of ErrorCode specifying the error that occurred. | [optional] [readonly] 
**errorDetailMessage** | **String** | Output only. A specific detailed error message, if supplied by the engine. | [optional] [readonly] 
**errorMessage** | **String** | Output only. A formatted message with further details about the error and a CTA. | [optional] [readonly] 



## Enum: ErrorCodeEnum


* `ERROR_CODE_UNSPECIFIED` (value: `"ERROR_CODE_UNSPECIFIED"`)

* `CONNECTION_FAILURE` (value: `"CONNECTION_FAILURE"`)

* `AUTHENTICATION_FAILURE` (value: `"AUTHENTICATION_FAILURE"`)

* `INVALID_CONNECTION_PROFILE_CONFIG` (value: `"INVALID_CONNECTION_PROFILE_CONFIG"`)

* `VERSION_INCOMPATIBILITY` (value: `"VERSION_INCOMPATIBILITY"`)

* `CONNECTION_PROFILE_TYPES_INCOMPATIBILITY` (value: `"CONNECTION_PROFILE_TYPES_INCOMPATIBILITY"`)

* `UNSUPPORTED_GTID_MODE` (value: `"UNSUPPORTED_GTID_MODE"`)

* `UNSUPPORTED_DEFINER` (value: `"UNSUPPORTED_DEFINER"`)

* `CANT_RESTART_RUNNING_MIGRATION` (value: `"CANT_RESTART_RUNNING_MIGRATION"`)

* `TABLES_WITH_LIMITED_SUPPORT` (value: `"TABLES_WITH_LIMITED_SUPPORT"`)

* `UNSUPPORTED_DATABASE_LOCALE` (value: `"UNSUPPORTED_DATABASE_LOCALE"`)

* `UNSUPPORTED_DATABASE_FDW_CONFIG` (value: `"UNSUPPORTED_DATABASE_FDW_CONFIG"`)

* `ERROR_RDBMS` (value: `"ERROR_RDBMS"`)

* `SOURCE_SIZE_EXCEEDS_THRESHOLD` (value: `"SOURCE_SIZE_EXCEEDS_THRESHOLD"`)

* `EXISTING_CONFLICTING_DATABASES` (value: `"EXISTING_CONFLICTING_DATABASES"`)

* `PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE` (value: `"PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE"`)

* `EXISTING_DATA` (value: `"EXISTING_DATA"`)

* `SOURCE_MAX_SUBSCRIPTIONS` (value: `"SOURCE_MAX_SUBSCRIPTIONS"`)




