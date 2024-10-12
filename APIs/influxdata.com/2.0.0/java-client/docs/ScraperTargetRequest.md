

# ScraperTargetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowInsecure** | **Boolean** | Skip TLS verification on endpoint. |  [optional] |
|**bucketID** | **String** | The ID of the bucket to write to. |  [optional] |
|**name** | **String** | The name of the scraper target. |  [optional] |
|**orgID** | **String** | The organization ID. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the metrics to be parsed. |  [optional] |
|**url** | **String** | The URL of the metrics endpoint. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PROMETHEUS | &quot;prometheus&quot; |



