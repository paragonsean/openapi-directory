

# CodeScanningSarifsStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysesUrl** | **URI** | The REST API URL for getting the analyses associated with the upload. |  [optional] [readonly] |
|**errors** | **List&lt;String&gt;** | Any errors that ocurred during processing of the delivery. |  [optional] [readonly] |
|**processingStatus** | [**ProcessingStatusEnum**](#ProcessingStatusEnum) | &#x60;pending&#x60; files have not yet been processed, while &#x60;complete&#x60; means results from the SARIF have been stored. &#x60;failed&#x60; files have either not been processed at all, or could only be partially processed. |  [optional] |



## Enum: ProcessingStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| COMPLETE | &quot;complete&quot; |
| FAILED | &quot;failed&quot; |



