

# DataSubjectRightOperation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | Application identifier if applicable |  [optional] |
|**context** | **String** | JSON object decribing what to delete (TODO - make separate definition?) |  |
|**operationId** | **UUID** | Unique operation identifier |  |
|**participant** | **String** | Participant to execute the response |  |
|**participantData** | **String** | String field to be used by participant for any intermediate statuses or data they need to save |  [optional] |
|**requestId** | **UUID** | Unique request identifier |  |
|**requestType** | [**RequestTypeEnum**](#RequestTypeEnum) | Request type |  |
|**status** | [**StatusEnum**](#StatusEnum) | Operation status |  |



## Enum: RequestTypeEnum

| Name | Value |
|---- | -----|
| UNSUPPORTED | &quot;Unsupported&quot; |
| DELETE | &quot;Delete&quot; |
| PURGE | &quot;Purge&quot; |
| UNDO_DELETE | &quot;UndoDelete&quot; |
| SCHEDULED | &quot;Scheduled&quot; |
| APP_DELETE | &quot;AppDelete&quot; |
| APP_PURGE | &quot;AppPurge&quot; |
| APP_UNDO_DELETE | &quot;AppUndoDelete&quot; |
| EXPORT | &quot;Export&quot; |
| CUSTOMER_ACCOUNT_DELETE | &quot;CustomerAccountDelete&quot; |
| CUSTOMER_ACCOUNT_EXPORT | &quot;CustomerAccountExport&quot; |
| CUSTOMER_USER_DELETE | &quot;CustomerUserDelete&quot; |
| CUSTOMER_USER_EXPORT | &quot;CustomerUserExport&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| CREATED | &quot;Created&quot; |
| QUEUED | &quot;Queued&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |



