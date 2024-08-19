

# GoogleCloudAiplatformV1beta1PythonPackageSpec

The spec of a Python packaged code.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **List&lt;String&gt;** | Command line arguments to be passed to the Python task. |  [optional] |
|**env** | [**List&lt;GoogleCloudAiplatformV1beta1EnvVar&gt;**](GoogleCloudAiplatformV1beta1EnvVar.md) | Environment variables to be passed to the python module. Maximum limit is 100. |  [optional] |
|**executorImageUri** | **String** | Required. The URI of a container image in Artifact Registry that will run the provided Python package. Vertex AI provides a wide range of executor images with pre-installed packages to meet users&#39; various use cases. See the list of [pre-built containers for training](https://cloud.google.com/vertex-ai/docs/training/pre-built-containers). You must use an image from this list. |  [optional] |
|**packageUris** | **List&lt;String&gt;** | Required. The Google Cloud Storage location of the Python package files which are the training program and its dependent packages. The maximum number of package URIs is 100. |  [optional] |
|**pythonModule** | **String** | Required. The Python module name to run after installing the packages. |  [optional] |



