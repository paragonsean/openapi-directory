

# GoogleCloudPolicysimulatorV1betaOrgPolicyViolationsPreviewResourceCounts

A summary of the state of all resources scanned for compliance with the changed OrgPolicy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compliant** | **Integer** | Output only. Number of scanned resources with zero violations. |  [optional] [readonly] |
|**errors** | **Integer** | Output only. Number of resources that returned an error when scanned. |  [optional] [readonly] |
|**noncompliant** | **Integer** | Output only. Number of scanned resources with at least one violation. |  [optional] [readonly] |
|**scanned** | **Integer** | Output only. Number of resources checked for compliance. Must equal: unenforced + noncompliant + compliant + error |  [optional] [readonly] |
|**unenforced** | **Integer** | Output only. Number of resources where the constraint was not enforced, i.e. the Policy set &#x60;enforced: false&#x60; for that resource. |  [optional] [readonly] |



