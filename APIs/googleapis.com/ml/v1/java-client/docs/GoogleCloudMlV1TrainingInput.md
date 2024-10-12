

# GoogleCloudMlV1TrainingInput

Represents input parameters for a training job. When using the gcloud command to submit your training job, you can specify the input parameters as command-line arguments and/or in a YAML configuration file referenced from the --config command-line argument. For details, see the guide to [submitting a training job](/ai-platform/training/docs/training-jobs).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **List&lt;String&gt;** | Optional. Command-line arguments passed to the training application when it starts. If your job uses a custom container, then the arguments are passed to the container&#39;s &#x60;ENTRYPOINT&#x60; command. |  [optional] |
|**enableWebAccess** | **Boolean** | Optional. Whether you want AI Platform Training to enable [interactive shell access](https://cloud.google.com/ai-platform/training/docs/monitor-debug-interactive-shell) to training containers. If set to &#x60;true&#x60;, you can access interactive shells at the URIs given by TrainingOutput.web_access_uris or HyperparameterOutput.web_access_uris (within TrainingOutput.trials). |  [optional] |
|**encryptionConfig** | [**GoogleCloudMlV1EncryptionConfig**](GoogleCloudMlV1EncryptionConfig.md) |  |  [optional] |
|**evaluatorConfig** | [**GoogleCloudMlV1ReplicaConfig**](GoogleCloudMlV1ReplicaConfig.md) |  |  [optional] |
|**evaluatorCount** | **String** | Optional. The number of evaluator replicas to use for the training job. Each replica in the cluster will be of the type specified in &#x60;evaluator_type&#x60;. This value can only be used when &#x60;scale_tier&#x60; is set to &#x60;CUSTOM&#x60;. If you set this value, you must also set &#x60;evaluator_type&#x60;. The default value is zero. |  [optional] |
|**evaluatorType** | **String** | Optional. Specifies the type of virtual machine to use for your training job&#39;s evaluator nodes. The supported values are the same as those described in the entry for &#x60;masterType&#x60;. This value must be consistent with the category of machine type that &#x60;masterType&#x60; uses. In other words, both must be Compute Engine machine types or both must be legacy machine types. This value must be present when &#x60;scaleTier&#x60; is set to &#x60;CUSTOM&#x60; and &#x60;evaluatorCount&#x60; is greater than zero. |  [optional] |
|**hyperparameters** | [**GoogleCloudMlV1HyperparameterSpec**](GoogleCloudMlV1HyperparameterSpec.md) |  |  [optional] |
|**jobDir** | **String** | Optional. A Google Cloud Storage path in which to store training outputs and other data needed for training. This path is passed to your TensorFlow program as the &#39;--job-dir&#39; command-line argument. The benefit of specifying this field is that Cloud ML validates the path for use in training. |  [optional] |
|**masterConfig** | [**GoogleCloudMlV1ReplicaConfig**](GoogleCloudMlV1ReplicaConfig.md) |  |  [optional] |
|**masterType** | **String** | Optional. Specifies the type of virtual machine to use for your training job&#39;s master worker. You must specify this field when &#x60;scaleTier&#x60; is set to &#x60;CUSTOM&#x60;. You can use certain Compute Engine machine types directly in this field. See the [list of compatible Compute Engine machine types](/ai-platform/training/docs/machine-types#compute-engine-machine-types). Alternatively, you can use the certain legacy machine types in this field. See the [list of legacy machine types](/ai-platform/training/docs/machine-types#legacy-machine-types). Finally, if you want to use a TPU for training, specify &#x60;cloud_tpu&#x60; in this field. Learn more about the [special configuration options for training with TPUs](/ai-platform/training/docs/using-tpus#configuring_a_custom_tpu_machine). |  [optional] |
|**network** | **String** | Optional. The full name of the [Compute Engine network](/vpc/docs/vpc) to which the Job is peered. For example, &#x60;projects/12345/global/networks/myVPC&#x60;. The format of this field is &#x60;projects/{project}/global/networks/{network}&#x60;, where {project} is a project number (like &#x60;12345&#x60;) and {network} is network name. Private services access must already be configured for the network. If left unspecified, the Job is not peered with any network. [Learn about using VPC Network Peering.](/ai-platform/training/docs/vpc-peering). |  [optional] |
|**packageUris** | **List&lt;String&gt;** | Required. The Google Cloud Storage location of the packages with the training program and any additional dependencies. The maximum number of package URIs is 100. |  [optional] |
|**parameterServerConfig** | [**GoogleCloudMlV1ReplicaConfig**](GoogleCloudMlV1ReplicaConfig.md) |  |  [optional] |
|**parameterServerCount** | **String** | Optional. The number of parameter server replicas to use for the training job. Each replica in the cluster will be of the type specified in &#x60;parameter_server_type&#x60;. This value can only be used when &#x60;scale_tier&#x60; is set to &#x60;CUSTOM&#x60;. If you set this value, you must also set &#x60;parameter_server_type&#x60;. The default value is zero. |  [optional] |
|**parameterServerType** | **String** | Optional. Specifies the type of virtual machine to use for your training job&#39;s parameter server. The supported values are the same as those described in the entry for &#x60;master_type&#x60;. This value must be consistent with the category of machine type that &#x60;masterType&#x60; uses. In other words, both must be Compute Engine machine types or both must be legacy machine types. This value must be present when &#x60;scaleTier&#x60; is set to &#x60;CUSTOM&#x60; and &#x60;parameter_server_count&#x60; is greater than zero. |  [optional] |
|**pythonModule** | **String** | Required. The Python module name to run after installing the packages. |  [optional] |
|**pythonVersion** | **String** | Optional. The version of Python used in training. You must either specify this field or specify &#x60;masterConfig.imageUri&#x60;. The following Python versions are available: * Python &#39;3.7&#39; is available when &#x60;runtime_version&#x60; is set to &#39;1.15&#39; or later. * Python &#39;3.5&#39; is available when &#x60;runtime_version&#x60; is set to a version from &#39;1.4&#39; to &#39;1.14&#39;. * Python &#39;2.7&#39; is available when &#x60;runtime_version&#x60; is set to &#39;1.15&#39; or earlier. Read more about the Python versions available for [each runtime version](/ml-engine/docs/runtime-version-list). |  [optional] |
|**region** | **String** | Required. The region to run the training job in. See the [available regions](/ai-platform/training/docs/regions) for AI Platform Training. |  [optional] |
|**runtimeVersion** | **String** | Optional. The AI Platform runtime version to use for training. You must either specify this field or specify &#x60;masterConfig.imageUri&#x60;. For more information, see the [runtime version list](/ai-platform/training/docs/runtime-version-list) and learn [how to manage runtime versions](/ai-platform/training/docs/versioning). |  [optional] |
|**scaleTier** | [**ScaleTierEnum**](#ScaleTierEnum) | Required. Specifies the machine types, the number of replicas for workers and parameter servers. |  [optional] |
|**scheduling** | [**GoogleCloudMlV1Scheduling**](GoogleCloudMlV1Scheduling.md) |  |  [optional] |
|**serviceAccount** | **String** | Optional. The email address of a service account to use when running the training appplication. You must have the &#x60;iam.serviceAccounts.actAs&#x60; permission for the specified service account. In addition, the AI Platform Training Google-managed service account must have the &#x60;roles/iam.serviceAccountAdmin&#x60; role for the specified service account. [Learn more about configuring a service account.](/ai-platform/training/docs/custom-service-account) If not specified, the AI Platform Training Google-managed service account is used by default. |  [optional] |
|**useChiefInTfConfig** | **Boolean** | Optional. Use &#x60;chief&#x60; instead of &#x60;master&#x60; in the &#x60;TF_CONFIG&#x60; environment variable when training with a custom container. Defaults to &#x60;false&#x60;. [Learn more about this field.](/ai-platform/training/docs/distributed-training-details#chief-versus-master) This field has no effect for training jobs that don&#39;t use a custom container. |  [optional] |
|**workerConfig** | [**GoogleCloudMlV1ReplicaConfig**](GoogleCloudMlV1ReplicaConfig.md) |  |  [optional] |
|**workerCount** | **String** | Optional. The number of worker replicas to use for the training job. Each replica in the cluster will be of the type specified in &#x60;worker_type&#x60;. This value can only be used when &#x60;scale_tier&#x60; is set to &#x60;CUSTOM&#x60;. If you set this value, you must also set &#x60;worker_type&#x60;. The default value is zero. |  [optional] |
|**workerType** | **String** | Optional. Specifies the type of virtual machine to use for your training job&#39;s worker nodes. The supported values are the same as those described in the entry for &#x60;masterType&#x60;. This value must be consistent with the category of machine type that &#x60;masterType&#x60; uses. In other words, both must be Compute Engine machine types or both must be legacy machine types. If you use &#x60;cloud_tpu&#x60; for this value, see special instructions for [configuring a custom TPU machine](/ml-engine/docs/tensorflow/using-tpus#configuring_a_custom_tpu_machine). This value must be present when &#x60;scaleTier&#x60; is set to &#x60;CUSTOM&#x60; and &#x60;workerCount&#x60; is greater than zero. |  [optional] |



## Enum: ScaleTierEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;BASIC&quot; |
| STANDARD_1 | &quot;STANDARD_1&quot; |
| PREMIUM_1 | &quot;PREMIUM_1&quot; |
| BASIC_GPU | &quot;BASIC_GPU&quot; |
| BASIC_TPU | &quot;BASIC_TPU&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



