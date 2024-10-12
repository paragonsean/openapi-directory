

# AutoscalingPolicy

Describes an autoscaling policy for Dataproc cluster autoscaler.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basicAlgorithm** | [**BasicAutoscalingAlgorithm**](BasicAutoscalingAlgorithm.md) |  |  [optional] |
|**id** | **String** | Required. The policy id.The id must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). Cannot begin or end with underscore or hyphen. Must consist of between 3 and 50 characters. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels to associate with this autoscaling policy. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with an autoscaling policy. |  [optional] |
|**name** | **String** | Output only. The \&quot;resource name\&quot; of the autoscaling policy, as described in https://cloud.google.com/apis/design/resource_names. For projects.regions.autoscalingPolicies, the resource name of the policy has the following format: projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id} For projects.locations.autoscalingPolicies, the resource name of the policy has the following format: projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id} |  [optional] [readonly] |
|**secondaryWorkerConfig** | [**InstanceGroupAutoscalingPolicyConfig**](InstanceGroupAutoscalingPolicyConfig.md) |  |  [optional] |
|**workerConfig** | [**InstanceGroupAutoscalingPolicyConfig**](InstanceGroupAutoscalingPolicyConfig.md) |  |  [optional] |



