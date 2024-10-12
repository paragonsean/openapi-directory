

# ReportAnnotation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationType** | [**AnnotationTypeEnum**](#AnnotationTypeEnum) | The type of the report. |  [optional] |
|**createdOn** | **OffsetDateTime** | The timestamp when the report was created. |  [optional] |
|**details** | **String** | The details to show to users when clicking on the annotation. |  [optional] |
|**externalId** | **String** | ID of the annotation provided by the annotation creator. It can be used to identify the annotation as an alternative to it&#39;s generated uuid. It is not used by Bitbucket, but only by the annotation creator for updating or deleting this specific annotation. Needs to be unique. |  [optional] |
|**line** | **Integer** | The line number that the annotation should belong to. If no line number is provided, then it will default to 0 and in a pull request it will appear at the top of the file specified by the path field. |  [optional] |
|**link** | **URI** | A URL linking to the annotation in an external tool. |  [optional] |
|**path** | **String** | The path of the file on which this annotation should be placed. This is the path of the file relative to the git repository. If no path is provided, then it will appear in the overview modal on all pull requests where the tip of the branch is the given commit, regardless of which files were modified. |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | The state of the report. May be set to PENDING and later updated. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity of the annotation. |  [optional] |
|**summary** | **String** | The message to display to users. |  [optional] |
|**updatedOn** | **OffsetDateTime** | The timestamp when the report was updated. |  [optional] |
|**uuid** | **String** | The UUID that can be used to identify the annotation. |  [optional] |



## Enum: AnnotationTypeEnum

| Name | Value |
|---- | -----|
| VULNERABILITY | &quot;VULNERABILITY&quot; |
| CODE_SMELL | &quot;CODE_SMELL&quot; |
| BUG | &quot;BUG&quot; |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| PASSED | &quot;PASSED&quot; |
| FAILED | &quot;FAILED&quot; |
| SKIPPED | &quot;SKIPPED&quot; |
| IGNORED | &quot;IGNORED&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| CRITICAL | &quot;CRITICAL&quot; |
| HIGH | &quot;HIGH&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| LOW | &quot;LOW&quot; |



