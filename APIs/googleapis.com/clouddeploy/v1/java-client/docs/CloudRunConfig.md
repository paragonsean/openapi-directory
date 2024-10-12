

# CloudRunConfig

CloudRunConfig contains the Cloud Run runtime configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automaticTrafficControl** | **Boolean** | Whether Cloud Deploy should update the traffic stanza in a Cloud Run Service on the user&#39;s behalf to facilitate traffic splitting. This is required to be true for CanaryDeployments, but optional for CustomCanaryDeployments. |  [optional] |
|**canaryRevisionTags** | **List&lt;String&gt;** | Optional. A list of tags that are added to the canary revision while the canary phase is in progress. |  [optional] |
|**priorRevisionTags** | **List&lt;String&gt;** | Optional. A list of tags that are added to the prior revision while the canary phase is in progress. |  [optional] |
|**stableRevisionTags** | **List&lt;String&gt;** | Optional. A list of tags that are added to the final stable revision when the stable phase is applied. |  [optional] |



