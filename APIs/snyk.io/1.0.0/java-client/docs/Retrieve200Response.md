

# Retrieve200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoDepUpgradeEnabled** | **Boolean** | Defines if the functionality is enabled |  [optional] |
|**autoDepUpgradeIgnoredDependencies** | **List&lt;Object&gt;** | A list of strings defining what dependencies should be ignored |  [optional] |
|**autoDepUpgradeLimit** | **BigDecimal** | A limit on how many automatic dependency upgrade PRs can be opened simultaneously |  [optional] |
|**autoDepUpgradeMinAge** | **BigDecimal** | The age (in days) that an automatic dependency check is valid for |  [optional] |
|**autoRemediationPrs** | [**Retrieve200ResponseAutoRemediationPrs**](Retrieve200ResponseAutoRemediationPrs.md) |  |  [optional] |
|**dockerfileSCMEnabled** | **Boolean** | If true, will automatically detect and scan Dockerfiles in your Git repositories, surface base image vulnerabilities and recommend possible fixes |  [optional] |
|**manualRemediationPrs** | [**Retrieve200ResponseManualRemediationPrs**](Retrieve200ResponseManualRemediationPrs.md) |  |  [optional] |
|**pullRequestAssignment** | [**Retrieve200ResponsePullRequestAssignment**](Retrieve200ResponsePullRequestAssignment.md) |  |  [optional] |
|**pullRequestFailOnAnyVulns** | **Boolean** | If an opened PR should fail to be validated if any vulnerable dependencies have been detected |  [optional] |
|**pullRequestFailOnlyForHighSeverity** | **Boolean** | If an opened PR only should fail its validation if any dependencies are marked as being of high severity |  [optional] |
|**pullRequestTestEnabled** | **Boolean** | If opened PRs should be tested |  [optional] |



