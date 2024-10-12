# BinaryAuthorizationApi.Policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admissionWhitelistPatterns** | [**[AdmissionWhitelistPattern]**](AdmissionWhitelistPattern.md) | Optional. Admission policy allowlisting. A matching admission request will always be permitted. This feature is typically used to exclude Google or third-party infrastructure images from Binary Authorization policies. | [optional] 
**clusterAdmissionRules** | [**{String: AdmissionRule}**](AdmissionRule.md) | Optional. Per-cluster admission rules. Cluster spec format: &#x60;location.clusterId&#x60;. There can be at most one admission rule per cluster spec. A &#x60;location&#x60; is either a compute zone (e.g. us-central1-a) or a region (e.g. us-central1). For &#x60;clusterId&#x60; syntax restrictions see https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters. | [optional] 
**defaultAdmissionRule** | [**AdmissionRule**](AdmissionRule.md) |  | [optional] 
**description** | **String** | Optional. A descriptive comment. | [optional] 
**etag** | **String** | Optional. A checksum, returned by the server, that can be sent on update requests to ensure the policy has an up-to-date value before attempting to update it. See https://google.aip.dev/154. | [optional] 
**globalPolicyEvaluationMode** | **String** | Optional. Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not covered by the global policy will be subject to the project admission policy. This setting has no effect when specified inside a global admission policy. | [optional] 
**istioServiceIdentityAdmissionRules** | [**{String: AdmissionRule}**](AdmissionRule.md) | Optional. Per-istio-service-identity admission rules. Istio service identity spec format: &#x60;spiffe:///ns//sa/&#x60; or &#x60;/ns//sa/&#x60; e.g. &#x60;spiffe://example.com/ns/test-ns/sa/default&#x60; | [optional] 
**kubernetesNamespaceAdmissionRules** | [**{String: AdmissionRule}**](AdmissionRule.md) | Optional. Per-kubernetes-namespace admission rules. K8s namespace spec format: &#x60;[a-z.-]+&#x60;, e.g. &#x60;some-namespace&#x60; | [optional] 
**kubernetesServiceAccountAdmissionRules** | [**{String: AdmissionRule}**](AdmissionRule.md) | Optional. Per-kubernetes-service-account admission rules. Service account spec format: &#x60;namespace:serviceaccount&#x60;. e.g. &#x60;test-ns:default&#x60; | [optional] 
**name** | **String** | Output only. The resource name, in the format &#x60;projects/_*_/policy&#x60;. There is at most one policy per project. | [optional] [readonly] 
**updateTime** | **String** | Output only. Time when the policy was last updated. | [optional] [readonly] 



## Enum: GlobalPolicyEvaluationModeEnum


* `GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED` (value: `"GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED"`)

* `ENABLE` (value: `"ENABLE"`)

* `DISABLE` (value: `"DISABLE"`)




