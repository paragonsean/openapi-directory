

# PhaseConfig

PhaseConfig represents the configuration for a phase in the custom canary deployment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**percentage** | **Integer** | Required. Percentage deployment for the phase. |  [optional] |
|**phaseId** | **String** | Required. The ID to assign to the &#x60;Rollout&#x60; phase. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: &#x60;^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$&#x60;. |  [optional] |
|**postdeploy** | [**Postdeploy**](Postdeploy.md) |  |  [optional] |
|**predeploy** | [**Predeploy**](Predeploy.md) |  |  [optional] |
|**profiles** | **List&lt;String&gt;** | Skaffold profiles to use when rendering the manifest for this phase. These are in addition to the profiles list specified in the &#x60;DeliveryPipeline&#x60; stage. |  [optional] |
|**verify** | **Boolean** | Whether to run verify tests after the deployment. |  [optional] |



