# AmazonMacie2.CreateClassificationJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowListIds** | **[String]** | An array of unique identifiers, one for each allow list for the job to use when it analyzes data. | [optional] 
**clientToken** | **String** | A unique, case-sensitive token that you provide to ensure the idempotency of the request. | 
**customDataIdentifierIds** | **[String]** | An array of unique identifiers, one for each custom data identifier for the job to use when it analyzes data. To use only managed data identifiers, don&#39;t specify a value for this property and specify a value other than NONE for the managedDataIdentifierSelector property. | [optional] 
**description** | **String** | A custom description of the job. The description can contain as many as 200 characters. | [optional] 
**initialRun** | **Boolean** | &lt;p&gt;For a recurring job, specifies whether to analyze all existing, eligible objects immediately after the job is created (true). To analyze only those objects that are created or changed after you create the job and before the job&#39;s first scheduled run, set this value to false.&lt;/p&gt; &lt;p&gt;If you configure the job to run only once, don&#39;t specify a value for this property.&lt;/p&gt; | [optional] 
**jobType** | **String** | The schedule for running a classification job. Valid values are: | 
**managedDataIdentifierIds** | **[String]** | &lt;p&gt;An array of unique identifiers, one for each managed data identifier for the job to include (use) or exclude (not use) when it analyzes data. Inclusion or exclusion depends on the managed data identifier selection type that you specify for the job (managedDataIdentifierSelector).&lt;/p&gt; &lt;p&gt;To retrieve a list of valid values for this property, use the ListManagedDataIdentifiers operation.&lt;/p&gt; | [optional] 
**managedDataIdentifierSelector** | **String** | The selection type that determines which managed data identifiers a classification job uses to analyze data. Valid values are: | [optional] 
**name** | **String** | A custom name for the job. The name can contain as many as 500 characters. | 
**s3JobDefinition** | [**CreateClassificationJobRequestS3JobDefinition**](CreateClassificationJobRequestS3JobDefinition.md) |  | 
**samplingPercentage** | **Number** | The sampling depth, as a percentage, for the job to apply when processing objects. This value determines the percentage of eligible objects that the job analyzes. If this value is less than 100, Amazon Macie selects the objects to analyze at random, up to the specified percentage, and analyzes all the data in those objects. | [optional] 
**scheduleFrequency** | [**CreateClassificationJobRequestScheduleFrequency**](CreateClassificationJobRequestScheduleFrequency.md) |  | [optional] 
**tags** | **{String: String}** | A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource. | [optional] 



## Enum: JobTypeEnum


* `ONE_TIME` (value: `"ONE_TIME"`)

* `SCHEDULED` (value: `"SCHEDULED"`)





## Enum: ManagedDataIdentifierSelectorEnum


* `ALL` (value: `"ALL"`)

* `EXCLUDE` (value: `"EXCLUDE"`)

* `INCLUDE` (value: `"INCLUDE"`)

* `NONE` (value: `"NONE"`)

* `RECOMMENDED` (value: `"RECOMMENDED"`)




