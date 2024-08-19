

# GoogleCloudPolicysimulatorV1beta1ReplayConfig

The configuration used for a Replay.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**logSource** | [**LogSourceEnum**](#LogSourceEnum) | The logs to use as input for the Replay. |  [optional] |
|**policyOverlay** | [**Map&lt;String, GoogleIamV1Policy&gt;**](GoogleIamV1Policy.md) | A mapping of the resources that you want to simulate policies for and the policies that you want to simulate. Keys are the full resource names for the resources. For example, &#x60;//cloudresourcemanager.googleapis.com/projects/my-project&#x60;. For examples of full resource names for Google Cloud services, see https://cloud.google.com/iam/help/troubleshooter/full-resource-names. Values are Policy objects representing the policies that you want to simulate. Replays automatically take into account any IAM policies inherited through the resource hierarchy, and any policies set on descendant resources. You do not need to include these policies in the policy overlay. |  [optional] |



## Enum: LogSourceEnum

| Name | Value |
|---- | -----|
| LOG_SOURCE_UNSPECIFIED | &quot;LOG_SOURCE_UNSPECIFIED&quot; |
| RECENT_ACCESSES | &quot;RECENT_ACCESSES&quot; |



