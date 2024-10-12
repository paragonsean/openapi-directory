# ChromePolicyApi.GoogleChromePolicyVersionsV1ResolveRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageSize** | **Number** | The maximum number of policies to return, defaults to 100 and has a maximum of 1000. | [optional] 
**pageToken** | **String** | The page token used to retrieve a specific page of the request. | [optional] 
**policySchemaFilter** | **String** | Required. The schema filter to apply to the resolve request. Specify a schema name to view a particular schema, for example: chrome.users.ShowLogoutButton Wildcards are supported, but only in the leaf portion of the schema name. Wildcards cannot be used in namespace directly. Please read https://developers.google.com/chrome/policy/guides/policy-schemas for details on schema namespaces. For example: Valid: \&quot;chrome.users.*\&quot;, \&quot;chrome.users.apps.*\&quot;, \&quot;chrome.printers.*\&quot; Invalid: \&quot;*\&quot;, \&quot;*.users\&quot;, \&quot;chrome.*\&quot;, \&quot;chrome.*.apps.*\&quot; | [optional] 
**policyTargetKey** | [**GoogleChromePolicyVersionsV1PolicyTargetKey**](GoogleChromePolicyVersionsV1PolicyTargetKey.md) |  | [optional] 


