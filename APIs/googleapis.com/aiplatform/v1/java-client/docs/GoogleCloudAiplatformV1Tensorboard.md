

# GoogleCloudAiplatformV1Tensorboard

Tensorboard is a physical database that stores users' training metrics. A default Tensorboard is provided in each region of a Google Cloud project. If needed users can also create extra Tensorboards in their projects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobStoragePathPrefix** | **String** | Output only. Consumer project Cloud Storage path prefix used to store blob data, which can either be a bucket or directory. Does not end with a &#39;/&#39;. |  [optional] [readonly] |
|**createTime** | **String** | Output only. Timestamp when this Tensorboard was created. |  [optional] [readonly] |
|**description** | **String** | Description of this Tensorboard. |  [optional] |
|**displayName** | **String** | Required. User provided name of this Tensorboard. |  [optional] |
|**encryptionSpec** | [**GoogleCloudAiplatformV1EncryptionSpec**](GoogleCloudAiplatformV1EncryptionSpec.md) |  |  [optional] |
|**etag** | **String** | Used to perform a consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**isDefault** | **Boolean** | Used to indicate if the TensorBoard instance is the default one. Each project &amp; region can have at most one default TensorBoard instance. Creation of a default TensorBoard instance and updating an existing TensorBoard instance to be default will mark all other TensorBoard instances (if any) as non default. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels with user-defined metadata to organize your Tensorboards. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. |  [optional] |
|**name** | **String** | Output only. Name of the Tensorboard. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}&#x60; |  [optional] [readonly] |
|**runCount** | **Integer** | Output only. The number of Runs stored in this Tensorboard. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Timestamp when this Tensorboard was last updated. |  [optional] [readonly] |



