

# DataSubjectRightDeleteStatusRequest200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | explanation message of the status |  |
|**sasUrl** | **String** | Azure Storage shared access signature (SAS) URL for exported user data. |  [optional] |
|**sasUrlExpired** | **Boolean** | Whether Azure Storage shared access signature (SAS) URL has expired or not. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of data subject right request |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| CREATED | &quot;Created&quot; |
| QUEUED | &quot;Queued&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |



