# CloudFunctionsApi.BuildConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automaticUpdatePolicy** | **Object** | Security patches are applied automatically to the runtime without requiring the function to be redeployed. | [optional] 
**build** | **String** | Output only. The Cloud Build name of the latest successful deployment of the function. | [optional] [readonly] 
**dockerRegistry** | **String** | Docker Registry to use for this deployment. This configuration is only applicable to 1st Gen functions, 2nd Gen functions can only use Artifact Registry. If &#x60;docker_repository&#x60; field is specified, this field will be automatically set as &#x60;ARTIFACT_REGISTRY&#x60;. If unspecified, it currently defaults to &#x60;CONTAINER_REGISTRY&#x60;. This field may be overridden by the backend for eligible deployments. | [optional] 
**dockerRepository** | **String** | Repository in Artifact Registry to which the function docker image will be pushed after it is built by Cloud Build. If specified by user, it is created and managed by user with a customer managed encryption key. Otherwise, GCF will create and use a repository named &#39;gcf-artifacts&#39; for every deployed region. It must match the pattern &#x60;projects/{project}/locations/{location}/repositories/{repository}&#x60;. Cross-project repositories are not supported. Cross-location repositories are not supported. Repository format must be &#39;DOCKER&#39;. | [optional] 
**entryPoint** | **String** | The name of the function (as defined in source code) that will be executed. Defaults to the resource name suffix, if not specified. For backward compatibility, if function with given name is not found, then the system will try to use function named \&quot;function\&quot;. For Node.js this is name of a function exported by the module specified in &#x60;source_location&#x60;. | [optional] 
**environmentVariables** | **{String: String}** | User-provided build-time environment variables for the function | [optional] 
**onDeployUpdatePolicy** | [**OnDeployUpdatePolicy**](OnDeployUpdatePolicy.md) |  | [optional] 
**runtime** | **String** | The runtime in which to run the function. Required when deploying a new function, optional when updating an existing function. For a complete list of possible choices, see the [&#x60;gcloud&#x60; command reference](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime). | [optional] 
**serviceAccount** | **String** | [Preview] Service account to be used for building the container | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 
**sourceProvenance** | [**SourceProvenance**](SourceProvenance.md) |  | [optional] 
**sourceToken** | **String** | An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments. | [optional] 
**workerPool** | **String** | Name of the Cloud Build Custom Worker Pool that should be used to build the function. The format of this field is &#x60;projects/{project}/locations/{region}/workerPools/{workerPool}&#x60; where {project} and {region} are the project id and region respectively where the worker pool is defined and {workerPool} is the short name of the worker pool. If the project id is not the same as the function, then the Cloud Functions Service Agent (service-@gcf-admin-robot.iam.gserviceaccount.com) must be granted the role Cloud Build Custom Workers Builder (roles/cloudbuild.customworkers.builder) in the project. | [optional] 



## Enum: DockerRegistryEnum


* `DOCKER_REGISTRY_UNSPECIFIED` (value: `"DOCKER_REGISTRY_UNSPECIFIED"`)

* `CONTAINER_REGISTRY` (value: `"CONTAINER_REGISTRY"`)

* `ARTIFACT_REGISTRY` (value: `"ARTIFACT_REGISTRY"`)




