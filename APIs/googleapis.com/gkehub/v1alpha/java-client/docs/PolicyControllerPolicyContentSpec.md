

# PolicyControllerPolicyContentSpec

PolicyContentSpec defines the user's desired content configuration on the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bundles** | [**Map&lt;String, PolicyControllerBundleInstallSpec&gt;**](PolicyControllerBundleInstallSpec.md) | map of bundle name to BundleInstallSpec. The bundle name maps to the &#x60;bundleName&#x60; key in the &#x60;policycontroller.gke.io/constraintData&#x60; annotation on a constraint. |  [optional] |
|**templateLibrary** | [**PolicyControllerTemplateLibraryConfig**](PolicyControllerTemplateLibraryConfig.md) |  |  [optional] |



