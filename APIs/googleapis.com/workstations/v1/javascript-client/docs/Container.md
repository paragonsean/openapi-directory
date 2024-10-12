# CloudWorkstationsApi.Container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **[String]** | Optional. Arguments passed to the entrypoint. | [optional] 
**command** | **[String]** | Optional. If set, overrides the default ENTRYPOINT specified by the image. | [optional] 
**env** | **{String: String}** | Optional. Environment variables passed to the container&#39;s entrypoint. | [optional] 
**image** | **String** | Optional. A Docker container image that defines a custom environment. Cloud Workstations provides a number of [preconfigured images](https://cloud.google.com/workstations/docs/preconfigured-base-images), but you can create your own [custom container images](https://cloud.google.com/workstations/docs/custom-container-images). If using a private image, the &#x60;host.gceInstance.serviceAccount&#x60; field must be specified in the workstation configuration. If using a custom container image, the service account must have [Artifact Registry Reader](https://cloud.google.com/artifact-registry/docs/access-control#roles) permission to pull the specified image. Otherwise, the image must be publicly accessible. | [optional] 
**runAsUser** | **Number** | Optional. If set, overrides the USER specified in the image with the given uid. | [optional] 
**workingDir** | **String** | Optional. If set, overrides the default DIR specified by the image. | [optional] 


