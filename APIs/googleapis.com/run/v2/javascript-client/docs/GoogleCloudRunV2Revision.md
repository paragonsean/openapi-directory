# CloudRunAdminApi.GoogleCloudRunV2Revision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. | [optional] [readonly] 
**conditions** | [**[GoogleCloudRunV2Condition]**](GoogleCloudRunV2Condition.md) | Output only. The Condition of this Revision, containing its readiness status, and detailed error information in case it did not reach a serving state. | [optional] [readonly] 
**containers** | [**[GoogleCloudRunV2Container]**](GoogleCloudRunV2Container.md) | Holds the single container that defines the unit of execution for this Revision. | [optional] 
**createTime** | **String** | Output only. The creation time. | [optional] [readonly] 
**deleteTime** | **String** | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. | [optional] [readonly] 
**encryptionKey** | **String** | A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek | [optional] 
**encryptionKeyRevocationAction** | **String** | The action to take if the encryption key is revoked. | [optional] 
**encryptionKeyShutdownDuration** | **String** | If encryption_key_revocation_action is SHUTDOWN, the duration before shutting down all instances. The minimum increment is 1 hour. | [optional] 
**etag** | **String** | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. | [optional] [readonly] 
**executionEnvironment** | **String** | The execution environment being used to host this Revision. | [optional] 
**expireTime** | **String** | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. | [optional] [readonly] 
**generation** | **String** | Output only. A number that monotonically increases every time the user modifies the desired state. | [optional] [readonly] 
**labels** | **{String: String}** | Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google&#39;s billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels. | [optional] [readonly] 
**launchStage** | **String** | The least stable launch stage needed to create this resource, as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports &#x60;ALPHA&#x60;, &#x60;BETA&#x60;, and &#x60;GA&#x60;. Note that this value might not be what was used as input. For example, if ALPHA was provided as input in the parent resource, but only BETA and GA-level features are were, this field will be BETA. | [optional] 
**logUri** | **String** | Output only. The Google Console URI to obtain logs for the Revision. | [optional] [readonly] 
**maxInstanceRequestConcurrency** | **Number** | Sets the maximum number of requests that each serving instance can receive. | [optional] 
**name** | **String** | Output only. The unique name of this Revision. | [optional] [readonly] 
**observedGeneration** | **String** | Output only. The generation of this Revision currently serving traffic. See comments in &#x60;reconciling&#x60; for additional information on reconciliation process in Cloud Run. | [optional] [readonly] 
**reconciling** | **Boolean** | Output only. Indicates whether the resource&#39;s reconciliation is still in progress. See comments in &#x60;Service.reconciling&#x60; for additional information on reconciliation process in Cloud Run. | [optional] [readonly] 
**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**scaling** | [**GoogleCloudRunV2RevisionScaling**](GoogleCloudRunV2RevisionScaling.md) |  | [optional] 
**scalingStatus** | [**GoogleCloudRunV2RevisionScalingStatus**](GoogleCloudRunV2RevisionScalingStatus.md) |  | [optional] 
**service** | **String** | Output only. The name of the parent service. | [optional] [readonly] 
**serviceAccount** | **String** | Email address of the IAM service account associated with the revision of the service. The service account represents the identity of the running revision, and determines what permissions the revision has. | [optional] 
**sessionAffinity** | **Boolean** | Enable session affinity. | [optional] 
**timeout** | **String** | Max allowed time for an instance to respond to a request. | [optional] 
**uid** | **String** | Output only. Server assigned unique identifier for the Revision. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. | [optional] [readonly] 
**updateTime** | **String** | Output only. The last-modified time. | [optional] [readonly] 
**volumes** | [**[GoogleCloudRunV2Volume]**](GoogleCloudRunV2Volume.md) | A list of Volumes to make available to containers. | [optional] 
**vpcAccess** | [**GoogleCloudRunV2VpcAccess**](GoogleCloudRunV2VpcAccess.md) |  | [optional] 



## Enum: EncryptionKeyRevocationActionEnum


* `ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED` (value: `"ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED"`)

* `PREVENT_NEW` (value: `"PREVENT_NEW"`)

* `SHUTDOWN` (value: `"SHUTDOWN"`)





## Enum: ExecutionEnvironmentEnum


* `UNSPECIFIED` (value: `"EXECUTION_ENVIRONMENT_UNSPECIFIED"`)

* `GEN1` (value: `"EXECUTION_ENVIRONMENT_GEN1"`)

* `GEN2` (value: `"EXECUTION_ENVIRONMENT_GEN2"`)





## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `UNIMPLEMENTED` (value: `"UNIMPLEMENTED"`)

* `PRELAUNCH` (value: `"PRELAUNCH"`)

* `EARLY_ACCESS` (value: `"EARLY_ACCESS"`)

* `ALPHA` (value: `"ALPHA"`)

* `BETA` (value: `"BETA"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)




