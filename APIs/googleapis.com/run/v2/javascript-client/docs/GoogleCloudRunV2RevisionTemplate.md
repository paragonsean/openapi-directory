# CloudRunAdminApi.GoogleCloudRunV2RevisionTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. Cloud Run API v2 does not support annotations with &#x60;run.googleapis.com&#x60;, &#x60;cloud.googleapis.com&#x60;, &#x60;serving.knative.dev&#x60;, or &#x60;autoscaling.knative.dev&#x60; namespaces, and they will be rejected. All system annotations in v1 now have a corresponding field in v2 RevisionTemplate. This field follows Kubernetes annotations&#39; namespacing, limits, and rules. | [optional] 
**containers** | [**[GoogleCloudRunV2Container]**](GoogleCloudRunV2Container.md) | Holds the single container that defines the unit of execution for this Revision. | [optional] 
**encryptionKey** | **String** | A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek | [optional] 
**executionEnvironment** | **String** | The sandbox environment to host this Revision. | [optional] 
**healthCheckDisabled** | **Boolean** | Optional. Disables health checking containers during deployment. | [optional] 
**labels** | **{String: String}** | Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google&#39;s billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels. Cloud Run API v2 does not support labels with &#x60;run.googleapis.com&#x60;, &#x60;cloud.googleapis.com&#x60;, &#x60;serving.knative.dev&#x60;, or &#x60;autoscaling.knative.dev&#x60; namespaces, and they will be rejected. All system labels in v1 now have a corresponding field in v2 RevisionTemplate. | [optional] 
**maxInstanceRequestConcurrency** | **Number** | Sets the maximum number of requests that each serving instance can receive. | [optional] 
**revision** | **String** | The unique name for the revision. If this field is omitted, it will be automatically generated based on the Service name. | [optional] 
**scaling** | [**GoogleCloudRunV2RevisionScaling**](GoogleCloudRunV2RevisionScaling.md) |  | [optional] 
**serviceAccount** | **String** | Email address of the IAM service account associated with the revision of the service. The service account represents the identity of the running revision, and determines what permissions the revision has. If not provided, the revision will use the project&#39;s default service account. | [optional] 
**sessionAffinity** | **Boolean** | Optional. Enable session affinity. | [optional] 
**timeout** | **String** | Max allowed time for an instance to respond to a request. | [optional] 
**volumes** | [**[GoogleCloudRunV2Volume]**](GoogleCloudRunV2Volume.md) | A list of Volumes to make available to containers. | [optional] 
**vpcAccess** | [**GoogleCloudRunV2VpcAccess**](GoogleCloudRunV2VpcAccess.md) |  | [optional] 



## Enum: ExecutionEnvironmentEnum


* `UNSPECIFIED` (value: `"EXECUTION_ENVIRONMENT_UNSPECIFIED"`)

* `GEN1` (value: `"EXECUTION_ENVIRONMENT_GEN1"`)

* `GEN2` (value: `"EXECUTION_ENVIRONMENT_GEN2"`)




