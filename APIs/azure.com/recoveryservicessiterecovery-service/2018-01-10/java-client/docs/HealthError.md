

# HealthError

Health Error

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTimeUtc** | **OffsetDateTime** | Error creation time (UTC) |  [optional] |
|**entityId** | **String** | ID of the entity. |  [optional] |
|**errorCategory** | **String** | Category of error. |  [optional] |
|**errorCode** | **String** | Error code. |  [optional] |
|**errorLevel** | **String** | Level of error. |  [optional] |
|**errorMessage** | **String** | Error message. |  [optional] |
|**errorSource** | **String** | Source of error. |  [optional] |
|**errorType** | **String** | Type of error. |  [optional] |
|**innerHealthErrors** | [**List&lt;InnerHealthError&gt;**](InnerHealthError.md) | The inner health errors. HealthError having a list of HealthError as child errors is problematic. InnerHealthError is used because this will prevent an infinite loop of structures when Hydra tries to auto-generate the contract. We are exposing the related health errors as inner health errors and all API consumers can utilize this in the same fashion as Exception -&amp;gt; InnerException. |  [optional] |
|**possibleCauses** | **String** | Possible causes of error. |  [optional] |
|**recommendedAction** | **String** | Recommended action to resolve error. |  [optional] |
|**recoveryProviderErrorMessage** | **String** | DRA error message. |  [optional] |
|**summaryMessage** | **String** | Summary message of the entity. |  [optional] |



