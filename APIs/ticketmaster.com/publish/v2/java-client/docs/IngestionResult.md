

# IngestionResult

This class defines the IngestionResult on the Publish API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Id of the entity ingested in the discovery api |  [optional] |
|**ignoredProperties** | **Map&lt;String, Object&gt;** | List properties that are ignored in the validation |  [optional] |
|**invalidProperties** | **Map&lt;String, Object&gt;** | List of invalid properties |  [optional] |
|**invalidValues** | **Map&lt;String, Object&gt;** | List of invalid values |  [optional] |
|**missingProperties** | **Map&lt;String, Object&gt;** | List of properties that should be present in your entity to ease its dicovery |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the result |  |
|**unknownProperties** | **Map&lt;String, Object&gt;** | List of unknown properties that will be dropped |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ERROR | &quot;Error&quot; |
| SUCCESS_WARNING | &quot;SuccessWarning&quot; |
| SUCCESS | &quot;Success&quot; |



