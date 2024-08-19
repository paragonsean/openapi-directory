

# CloseAccountResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The new status of the account. &gt;Permitted values: &#x60;Active&#x60;, &#x60;Inactive&#x60;, &#x60;Suspended&#x60;, &#x60;Closed&#x60;. |  [optional] |
|**submittedAsync** | **Boolean** | Indicates whether the request is processed asynchronously. Depending on the request&#39;s platform settings, the following scenarios may be applied: * **true**: The request is queued and will be executed when the providing service is available in the order in which the requests are received. * **false**: The processing of the request is immediately attempted; it may result in an error if the providing service is unavailable. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| CLOSED | &quot;Closed&quot; |
| INACTIVE | &quot;Inactive&quot; |
| SUSPENDED | &quot;Suspended&quot; |



