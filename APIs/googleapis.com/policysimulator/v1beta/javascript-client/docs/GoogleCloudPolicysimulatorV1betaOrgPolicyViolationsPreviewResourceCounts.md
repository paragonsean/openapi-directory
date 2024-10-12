# PolicySimulatorApi.GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreviewResourceCounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliant** | **Number** | Output only. Number of scanned resources with zero violations. | [optional] [readonly] 
**errors** | **Number** | Output only. Number of resources that returned an error when scanned. | [optional] [readonly] 
**noncompliant** | **Number** | Output only. Number of scanned resources with at least one violation. | [optional] [readonly] 
**scanned** | **Number** | Output only. Number of resources checked for compliance. Must equal: unenforced + noncompliant + compliant + error | [optional] [readonly] 
**unenforced** | **Number** | Output only. Number of resources where the constraint was not enforced, i.e. the Policy set &#x60;enforced: false&#x60; for that resource. | [optional] [readonly] 


