# AmazonMacie2.GetFindingStatisticsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**findingCriteria** | [**CreateFindingsFilterRequestFindingCriteria**](CreateFindingsFilterRequestFindingCriteria.md) |  | [optional] 
**groupBy** | **String** | &lt;p&gt;The finding property to use to group the query results. Valid values are:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;classificationDetails.jobId - The unique identifier for the classification job that produced the finding.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;resourcesAffected.s3Bucket.name - The name of the S3 bucket that the finding applies to.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;severity.description - The severity level of the finding, such as High or Medium.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;type - The type of finding, such as Policy:IAMUser/S3BucketPublic and SensitiveData:S3Object/Personal.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | 
**size** | **Number** | The maximum number of items to include in each page of the response. | [optional] 
**sortCriteria** | [**GetFindingStatisticsRequestSortCriteria**](GetFindingStatisticsRequestSortCriteria.md) |  | [optional] 



## Enum: GroupByEnum


* `resourcesAffected.s3Bucket.name` (value: `"resourcesAffected.s3Bucket.name"`)

* `type` (value: `"type"`)

* `classificationDetails.jobId` (value: `"classificationDetails.jobId"`)

* `severity.description` (value: `"severity.description"`)




