# LgtmApiSpecification.QueryjobStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed** | **Number** | The number of projects for which the query failed. | [optional] 
**pending** | **Number** | The number of projects scheduled for execution but pending. For very large jobs, not all projects are scheduled at the same time. Therefore, this number might increase as more projects are scheduled. This means that &#x60;successful + failed + pending&#x60; might be smaller than the total number of project that will be analyzed.  | [optional] 
**successWithResult** | **Number** | The number of projects for which the query returned results. | [optional] 
**successWithoutResult** | **Number** | The number of projects for which the query was successful but returned no results. | [optional] 
**successful** | **Number** | The number of projects for which the query completed succesfully. These are broken down further between the ones that have results (&#x60;success-with-result&#x60;) and the ones that do not (&#x60;success-without-result&#x60;): &#x60;successful &#x3D; success-with-result + success-without-result&#x60;.  | [optional] 


