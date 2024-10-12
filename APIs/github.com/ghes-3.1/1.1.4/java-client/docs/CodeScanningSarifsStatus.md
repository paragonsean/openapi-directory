

# CodeScanningSarifsStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysesUrl** | **URI** | The REST API URL for getting the analyses associated with the upload. |  [optional] [readonly] |
|**processingStatus** | [**ProcessingStatusEnum**](#ProcessingStatusEnum) | &#x60;pending&#x60; files have not yet been processed, while &#x60;complete&#x60; means all results in the SARIF have been stored. |  [optional] |



## Enum: ProcessingStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| COMPLETE | &quot;complete&quot; |



