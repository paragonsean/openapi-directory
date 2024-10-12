

# Skcer400Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  [optional] |
|**errorDescription** | [**ErrorDescriptionEnum**](#ErrorDescriptionEnum) |  |  [optional] |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| MISSING_PARAMETER | &quot;missing_parameter&quot; |
| INVALID_PARAMETER | &quot;invalid_parameter&quot; |
| INVALID_FORMAT | &quot;invalid_format&quot; |
| INVALID_TXNID | &quot;invalid_txnid&quot; |
| INVALID_CONSENTID | &quot;invalid_consentid&quot; |



## Enum: ErrorDescriptionEnum

| Name | Value |
|---- | -----|
| PLEASE_PROVIDE_ALL_MANDATORY_PARAMETERS | &quot;Please provide all mandatory parameters&quot; |
| BAD_REQUEST | &quot;Bad request&quot; |
| THE_FORMAT_PARAMETER_IS_INVALID | &quot;The format parameter is invalid&quot; |
| THE_TXN_ID_PARAMETER_MUST_BE_IN_UUID_FORMAT | &quot;The txnId parameter must be in UUID format&quot; |
| THE_CONSENT_ID_PARAMETER_MUST_BE_IN_UUID_FORMAT | &quot;The consentId parameter must be in UUID format&quot; |



