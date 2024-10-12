# AmazonMacie2.UpdateFindingsFilterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The action to perform on findings that match the filter criteria. To suppress (automatically archive) findings that match the criteria, set this value to ARCHIVE. Valid values are: | [optional] 
**clientToken** | **String** | A unique, case-sensitive token that you provide to ensure the idempotency of the request. | [optional] 
**description** | **String** | &lt;p&gt;A custom description of the filter. The description can contain as many as 512 characters.&lt;/p&gt; &lt;p&gt;We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users of your account might be able to see this description, depending on the actions that they&#39;re allowed to perform in Amazon Macie.&lt;/p&gt; | [optional] 
**findingCriteria** | [**CreateFindingsFilterRequestFindingCriteria**](CreateFindingsFilterRequestFindingCriteria.md) |  | [optional] 
**name** | **String** | &lt;p&gt;A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters.&lt;/p&gt; &lt;p&gt;We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users of your account might be able to see this name, depending on the actions that they&#39;re allowed to perform in Amazon Macie.&lt;/p&gt; | [optional] 
**position** | **Number** | The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings. | [optional] 



## Enum: ActionEnum


* `ARCHIVE` (value: `"ARCHIVE"`)

* `NOOP` (value: `"NOOP"`)




