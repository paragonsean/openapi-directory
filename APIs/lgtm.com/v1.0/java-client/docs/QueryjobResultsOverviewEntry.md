

# QueryjobResultsOverviewEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | **String** | Error message. Only applies if &#x60;status&#x60; is &#x60;error&#x60;. |  [optional] |
|**external** | **Integer** | Number of results that refer to elements outside the source tree (e.g., libraries). Only applies if &#x60;status&#x60; is &#x60;success&#x60;. |  [optional] |
|**internal** | **Integer** | Number of results that refer to elements within the source tree. Only applies if &#x60;status&#x60; is &#x60;success&#x60;. |  [optional] |
|**project** | [**Project**](Project.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Describes whether the query was sucessfully executed against the project. |  [optional] |
|**total** | **Integer** | Number of results returned by the query. This is broken down further into &#x60;internal&#x60; and &#x60;external&#x60; results. Only applies if &#x60;status&#x60; is &#x60;success&#x60;.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| ERROR | &quot;error&quot; |



