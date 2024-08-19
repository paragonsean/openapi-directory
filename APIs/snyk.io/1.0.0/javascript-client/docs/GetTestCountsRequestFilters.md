# SnykApi.GetTestCountsRequestFilters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isPrivate** | **Boolean** | If set to &#x60;true&#x60;, only include tests which were conducted against private projects, if set to &#x60;false&#x60; only include tests which were conducted against public projects | [optional] 
**issuesPrevented** | **Boolean** | If set to &#x60;true&#x60;, only include tests which prevented issues from being introduced, if set to &#x60;false&#x60; only include tests which did not prevent issues from being introduced | [optional] 
**orgs** | **Object** | The list of org IDs to filter the results by | 
**projects** | **Object** | The list of project IDs to filter issues by, max projects allowed is 1000 | [optional] 


