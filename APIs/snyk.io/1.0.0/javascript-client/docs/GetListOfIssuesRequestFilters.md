# SnykApi.GetListOfIssuesRequestFilters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exploitMaturity** | **[Object]** | The exploit maturity levels of issues to filter the results by | [optional] 
**fixable** | **Boolean** | If set to &#x60;true&#x60;, only include issues which are fixable, if set to &#x60;false&#x60;, only include issues which are not fixable. An issue is fixable if it is either upgradable, patchable or pinnable. Also see isUpgradable, isPatchable and isPinnable filters. | [optional] 
**identifier** | **String** | Search term to filter issue name by, or an exact CVE or CWE | [optional] 
**ignored** | **Boolean** | If set to &#x60;true&#x60;, only include issues which are ignored, if set to &#x60;false&#x60;, only include issues which are not ignored | [optional] 
**isFixed** | **Boolean** | If set to &#x60;true&#x60;, only include issues which are fixed, if set to &#x60;false&#x60;, only include issues which are not fixed | [optional] 
**isPatchable** | **Boolean** | If set to &#x60;true&#x60;, only include issues which are patchable, if set to &#x60;false&#x60;, only include issues which are not patchable | [optional] 
**isPinnable** | **Boolean** | If set to &#x60;true&#x60;, only include issues which are pinnable, if set to &#x60;false&#x60;, only include issues which are not pinnable | [optional] 
**isUpgradable** | **Boolean** | If set to &#x60;true&#x60;, only include issues which are upgradable, if set to &#x60;false&#x60;, only include issues which are not upgradable | [optional] 
**issues** | **Object** | The list of issue IDs to filter issues by | [optional] 
**languages** | **[Object]** | The type of languages to filter the results by | [optional] 
**orgs** | **Object** | The list of org IDs to filter the results by | 
**patched** | **Boolean** | If set to &#x60;true&#x60;, only include issues which are patched, if set to &#x60;false&#x60;, only include issues which are not patched | [optional] 
**priorityScore** | [**GetIssueCountsRequestFiltersPriorityScore**](GetIssueCountsRequestFiltersPriorityScore.md) |  | [optional] 
**projects** | **Object** | The list of project IDs to filter issues by, max projects allowed is 1000 | [optional] 
**severity** | **[Object]** | The severity levels of issues to filter the results by | [optional] 
**types** | **[Object]** | The type of issues to filter the results by | [optional] 


