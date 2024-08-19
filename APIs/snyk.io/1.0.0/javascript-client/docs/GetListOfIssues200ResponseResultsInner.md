# SnykApi.GetListOfIssues200ResponseResultsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixedDate** | **String** | The date that the issue was fixed | [optional] 
**introducedDate** | **String** | The date that the issue was introduced into the project | 
**isFixed** | **Boolean** | Whether the issue has been fixed | 
**issue** | [**GetListOfIssues200ResponseResultsInnerIssue**](GetListOfIssues200ResponseResultsInnerIssue.md) |  | 
**patchedDate** | **String** | The date that the issue was patched | [optional] 
**projects** | **[Object]** | When &#x60;groupBy&#x60; is used, multiple projects may be returned per issue | 
**project** | [**GetListOfIssues200ResponseResultsInnerOneOf1Project**](GetListOfIssues200ResponseResultsInnerOneOf1Project.md) |  | 


