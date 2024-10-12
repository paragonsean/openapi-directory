

# FormEntryAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | Timestamp of the submission |  [optional] |
|**fields** | [**List&lt;FormEntryField&gt;**](FormEntryField.md) |  |  [optional] |
|**modified** | **OffsetDateTime** | Timestamp of the field modified date |  [optional] |
|**paths** | **List&lt;String&gt;** | Full paths to files associated with the form submission |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Form entry status |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| COMPLETED | &quot;completed&quot; |



