

# GoogleCloudRetailV2alphaProject

Metadata that describes a Cloud Retail Project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enrolledSolutions** | [**List&lt;EnrolledSolutionsEnum&gt;**](#List&lt;EnrolledSolutionsEnum&gt;) | Output only. Retail API solutions that the project has enrolled. |  [optional] [readonly] |
|**name** | **String** | Output only. Full resource name of the retail project, such as &#x60;projects/{project_id_or_number}/retailProject&#x60;. |  [optional] [readonly] |



## Enum: List&lt;EnrolledSolutionsEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SOLUTION_TYPE_UNSPECIFIED&quot; |
| RECOMMENDATION | &quot;SOLUTION_TYPE_RECOMMENDATION&quot; |
| SEARCH | &quot;SOLUTION_TYPE_SEARCH&quot; |



