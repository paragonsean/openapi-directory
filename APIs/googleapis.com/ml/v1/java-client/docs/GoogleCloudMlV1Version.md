

# GoogleCloudMlV1Version

Represents a version of the model. Each version is a trained model deployed in the cloud, ready to handle prediction requests. A model can have multiple versions. You can get information about all of the versions of a given model by calling projects.models.versions.list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceleratorConfig** | [**GoogleCloudMlV1AcceleratorConfig**](GoogleCloudMlV1AcceleratorConfig.md) |  |  [optional] |
|**autoScaling** | [**GoogleCloudMlV1AutoScaling**](GoogleCloudMlV1AutoScaling.md) |  |  [optional] |
|**container** | [**GoogleCloudMlV1ContainerSpec**](GoogleCloudMlV1ContainerSpec.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time the version was created. |  [optional] |
|**deploymentUri** | **String** | The Cloud Storage URI of a directory containing trained model artifacts to be used to create the model version. See the [guide to deploying models](/ai-platform/prediction/docs/deploying-models) for more information. The total number of files under this directory must not exceed 1000. During projects.models.versions.create, AI Platform Prediction copies all files from the specified directory to a location managed by the service. From then on, AI Platform Prediction uses these copies of the model artifacts to serve predictions, not the original files in Cloud Storage, so this location is useful only as a historical record. If you specify container, then this field is optional. Otherwise, it is required. Learn [how to use this field with a custom container](/ai-platform/prediction/docs/custom-container-requirements#artifacts). |  [optional] |
|**description** | **String** | Optional. The description specified for the version when it was created. |  [optional] |
|**errorMessage** | **String** | Output only. The details of a failure or a cancellation. |  [optional] |
|**etag** | **byte[]** | &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of a model from overwriting each other. It is strongly suggested that systems make use of the &#x60;etag&#x60; in the read-modify-write cycle to perform model updates in order to avoid race conditions: An &#x60;etag&#x60; is returned in the response to &#x60;GetVersion&#x60;, and systems are expected to put that etag in the request to &#x60;UpdateVersion&#x60; to ensure that their change will be applied to the model as intended. |  [optional] |
|**explanationConfig** | [**GoogleCloudMlV1ExplanationConfig**](GoogleCloudMlV1ExplanationConfig.md) |  |  [optional] |
|**framework** | [**FrameworkEnum**](#FrameworkEnum) | Optional. The machine learning framework AI Platform uses to train this version of the model. Valid values are &#x60;TENSORFLOW&#x60;, &#x60;SCIKIT_LEARN&#x60;, &#x60;XGBOOST&#x60;. If you do not specify a framework, AI Platform will analyze files in the deployment_uri to determine a framework. If you choose &#x60;SCIKIT_LEARN&#x60; or &#x60;XGBOOST&#x60;, you must also set the runtime version of the model to 1.4 or greater. Do **not** specify a framework if you&#39;re deploying a [custom prediction routine](/ai-platform/prediction/docs/custom-prediction-routines) or if you&#39;re using a [custom container](/ai-platform/prediction/docs/use-custom-container). |  [optional] |
|**isDefault** | **Boolean** | Output only. If true, this version will be used to handle prediction requests that do not specify a version. You can change the default version by calling projects.methods.versions.setDefault. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. One or more labels that you can add, to organize your model versions. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels. Note that this field is not updatable for mls1* models. |  [optional] |
|**lastMigrationModelId** | **String** | Output only. The [AI Platform (Unified) &#x60;Model&#x60;](https://cloud.google.com/ai-platform-unified/docs/reference/rest/v1beta1/projects.locations.models) ID for the last [model migration](https://cloud.google.com/ai-platform-unified/docs/start/migrating-to-ai-platform-unified). |  [optional] [readonly] |
|**lastMigrationTime** | **String** | Output only. The last time this version was successfully [migrated to AI Platform (Unified)](https://cloud.google.com/ai-platform-unified/docs/start/migrating-to-ai-platform-unified). |  [optional] [readonly] |
|**lastUseTime** | **String** | Output only. The time the version was last used for prediction. |  [optional] |
|**machineType** | **String** | Optional. The type of machine on which to serve the model. Currently only applies to online prediction service. To learn about valid values for this field, read [Choosing a machine type for online prediction](/ai-platform/prediction/docs/machine-types-online-prediction). If this field is not specified and you are using a [regional endpoint](/ai-platform/prediction/docs/regional-endpoints), then the machine type defaults to &#x60;n1-standard-2&#x60;. If this field is not specified and you are using the global endpoint (&#x60;ml.googleapis.com&#x60;), then the machine type defaults to &#x60;mls1-c1-m2&#x60;. |  [optional] |
|**manualScaling** | [**GoogleCloudMlV1ManualScaling**](GoogleCloudMlV1ManualScaling.md) |  |  [optional] |
|**name** | **String** | Required. The name specified for the version when it was created. The version name must be unique within the model it is created in. |  [optional] |
|**packageUris** | **List&lt;String&gt;** | Optional. Cloud Storage paths (&#x60;gs://…&#x60;) of packages for [custom prediction routines](/ml-engine/docs/tensorflow/custom-prediction-routines) or [scikit-learn pipelines with custom code](/ml-engine/docs/scikit/exporting-for-prediction#custom-pipeline-code). For a custom prediction routine, one of these packages must contain your Predictor class (see [&#x60;predictionClass&#x60;](#Version.FIELDS.prediction_class)). Additionally, include any dependencies used by your Predictor or scikit-learn pipeline uses that are not already included in your selected [runtime version](/ml-engine/docs/tensorflow/runtime-version-list). If you specify this field, you must also set [&#x60;runtimeVersion&#x60;](#Version.FIELDS.runtime_version) to 1.4 or greater. |  [optional] |
|**predictionClass** | **String** | Optional. The fully qualified name (module_name.class_name) of a class that implements the Predictor interface described in this reference field. The module containing this class should be included in a package provided to the [&#x60;packageUris&#x60; field](#Version.FIELDS.package_uris). Specify this field if and only if you are deploying a [custom prediction routine (beta)](/ml-engine/docs/tensorflow/custom-prediction-routines). If you specify this field, you must set [&#x60;runtimeVersion&#x60;](#Version.FIELDS.runtime_version) to 1.4 or greater and you must set &#x60;machineType&#x60; to a [legacy (MLS1) machine type](/ml-engine/docs/machine-types-online-prediction). The following code sample provides the Predictor interface: class Predictor(object): \&quot;\&quot;\&quot;Interface for constructing custom predictors.\&quot;\&quot;\&quot; def predict(self, instances, **kwargs): \&quot;\&quot;\&quot;Performs custom prediction. Instances are the decoded values from the request. They have already been deserialized from JSON. Args: instances: A list of prediction input instances. **kwargs: A dictionary of keyword args provided as additional fields on the predict request body. Returns: A list of outputs containing the prediction results. This list must be JSON serializable. \&quot;\&quot;\&quot; raise NotImplementedError() @classmethod def from_path(cls, model_dir): \&quot;\&quot;\&quot;Creates an instance of Predictor using the given path. Loading of the predictor should be done in this method. Args: model_dir: The local directory that contains the exported model file along with any additional files uploaded when creating the version resource. Returns: An instance implementing this Predictor class. \&quot;\&quot;\&quot; raise NotImplementedError() Learn more about [the Predictor interface and custom prediction routines](/ml-engine/docs/tensorflow/custom-prediction-routines). |  [optional] |
|**pythonVersion** | **String** | Required. The version of Python used in prediction. The following Python versions are available: * Python &#39;3.7&#39; is available when &#x60;runtime_version&#x60; is set to &#39;1.15&#39; or later. * Python &#39;3.5&#39; is available when &#x60;runtime_version&#x60; is set to a version from &#39;1.4&#39; to &#39;1.14&#39;. * Python &#39;2.7&#39; is available when &#x60;runtime_version&#x60; is set to &#39;1.15&#39; or earlier. Read more about the Python versions available for [each runtime version](/ml-engine/docs/runtime-version-list). |  [optional] |
|**requestLoggingConfig** | [**GoogleCloudMlV1RequestLoggingConfig**](GoogleCloudMlV1RequestLoggingConfig.md) |  |  [optional] |
|**routes** | [**GoogleCloudMlV1RouteMap**](GoogleCloudMlV1RouteMap.md) |  |  [optional] |
|**runtimeVersion** | **String** | Required. The AI Platform runtime version to use for this deployment. For more information, see the [runtime version list](/ml-engine/docs/runtime-version-list) and [how to manage runtime versions](/ml-engine/docs/versioning). |  [optional] |
|**serviceAccount** | **String** | Optional. Specifies the service account for resource access control. If you specify this field, then you must also specify either the &#x60;containerSpec&#x60; or the &#x60;predictionClass&#x60; field. Learn more about [using a custom service account](/ai-platform/prediction/docs/custom-service-account). |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of a version. |  [optional] |



## Enum: FrameworkEnum

| Name | Value |
|---- | -----|
| FRAMEWORK_UNSPECIFIED | &quot;FRAMEWORK_UNSPECIFIED&quot; |
| TENSORFLOW | &quot;TENSORFLOW&quot; |
| SCIKIT_LEARN | &quot;SCIKIT_LEARN&quot; |
| XGBOOST | &quot;XGBOOST&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| READY | &quot;READY&quot; |
| CREATING | &quot;CREATING&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |



