

# GetFindingStatisticsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**findingCriteria** | [**CreateFindingsFilterRequestFindingCriteria**](CreateFindingsFilterRequestFindingCriteria.md) |  |  [optional] |
|**groupBy** | [**GroupByEnum**](#GroupByEnum) | &lt;p&gt;The finding property to use to group the query results. Valid values are:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;classificationDetails.jobId - The unique identifier for the classification job that produced the finding.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;resourcesAffected.s3Bucket.name - The name of the S3 bucket that the finding applies to.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;severity.description - The severity level of the finding, such as High or Medium.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;type - The type of finding, such as Policy:IAMUser/S3BucketPublic and SensitiveData:S3Object/Personal.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; |  |
|**size** | **Integer** | The maximum number of items to include in each page of the response. |  [optional] |
|**sortCriteria** | [**GetFindingStatisticsRequestSortCriteria**](GetFindingStatisticsRequestSortCriteria.md) |  |  [optional] |



## Enum: GroupByEnum

| Name | Value |
|---- | -----|
| RESOURCES_AFFECTED_S3_BUCKET_NAME | &quot;resourcesAffected.s3Bucket.name&quot; |
| TYPE | &quot;type&quot; |
| CLASSIFICATION_DETAILS_JOB_ID | &quot;classificationDetails.jobId&quot; |
| SEVERITY_DESCRIPTION | &quot;severity.description&quot; |



