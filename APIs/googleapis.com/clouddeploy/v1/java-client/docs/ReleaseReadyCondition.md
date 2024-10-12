

# ReleaseReadyCondition

ReleaseReadyCondition contains information around the status of the Release. If a release is not ready, you cannot create a rollout with the release.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | **Boolean** | True if the Release is in a valid state. Otherwise at least one condition in &#x60;ReleaseCondition&#x60; is in an invalid state. Iterate over those conditions and see which condition(s) has status &#x3D; false to find out what is wrong with the Release. |  [optional] |



