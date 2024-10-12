

# SubmissionAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionCategory** | [**ActionCategoryEnum**](#ActionCategoryEnum) |  |  |
|**actionType** | [**ActionTypeEnum**](#ActionTypeEnum) |  |  |
|**id** | **String** |  |  |
|**integrationId** | **String** |  |  |
|**resultData** | **Object** |  |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |



## Enum: ActionCategoryEnum

| Name | Value |
|---- | -----|
| NOTIFICATION | &quot;notification&quot; |
| FILE_UPLOAD | &quot;file_upload&quot; |



## Enum: ActionTypeEnum

| Name | Value |
|---- | -----|
| WEBHOOK | &quot;webhook&quot; |
| SLACK_WEBHOOK | &quot;slack_webhook&quot; |
| EMAIL | &quot;email&quot; |
| AWS_S3_UPLOAD | &quot;aws_s3_upload&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| PROCESSED | &quot;processed&quot; |
| FAILED | &quot;failed&quot; |
| ERROR | &quot;error&quot; |



