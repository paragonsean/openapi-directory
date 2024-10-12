

# ResourceHealthSummary

Base class to define the health summary of the resources contained under an Arm resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categorizedResourceCounts** | **Map&lt;String, Integer&gt;** | The categorized resource counts. |  [optional] |
|**issues** | [**List&lt;HealthErrorSummary&gt;**](HealthErrorSummary.md) | The list of summary of health errors across the resources under the container. |  [optional] |
|**resourceCount** | **Integer** | The count of total resources under the container. |  [optional] |



