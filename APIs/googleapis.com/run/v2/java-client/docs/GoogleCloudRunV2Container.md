

# GoogleCloudRunV2Container

A single application container. This specifies both the container to run, the command to run in the container and the arguments to supply to it. Note that additional arguments can be supplied by the system to the container at runtime.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **List&lt;String&gt;** | Arguments to the entrypoint. The docker image&#39;s CMD is used if this is not provided. |  [optional] |
|**command** | **List&lt;String&gt;** | Entrypoint array. Not executed within a shell. The docker image&#39;s ENTRYPOINT is used if this is not provided. |  [optional] |
|**dependsOn** | **List&lt;String&gt;** | Names of the containers that must start before this container. |  [optional] |
|**env** | [**List&lt;GoogleCloudRunV2EnvVar&gt;**](GoogleCloudRunV2EnvVar.md) | List of environment variables to set in the container. |  [optional] |
|**image** | **String** | Required. Name of the container image in Dockerhub, Google Artifact Registry, or Google Container Registry. If the host is not provided, Dockerhub is assumed. |  [optional] |
|**livenessProbe** | [**GoogleCloudRunV2Probe**](GoogleCloudRunV2Probe.md) |  |  [optional] |
|**name** | **String** | Name of the container specified as a DNS_LABEL (RFC 1123). |  [optional] |
|**ports** | [**List&lt;GoogleCloudRunV2ContainerPort&gt;**](GoogleCloudRunV2ContainerPort.md) | List of ports to expose from the container. Only a single port can be specified. The specified ports must be listening on all interfaces (0.0.0.0) within the container to be accessible. If omitted, a port number will be chosen and passed to the container through the PORT environment variable for the container to listen on. |  [optional] |
|**resources** | [**GoogleCloudRunV2ResourceRequirements**](GoogleCloudRunV2ResourceRequirements.md) |  |  [optional] |
|**startupProbe** | [**GoogleCloudRunV2Probe**](GoogleCloudRunV2Probe.md) |  |  [optional] |
|**volumeMounts** | [**List&lt;GoogleCloudRunV2VolumeMount&gt;**](GoogleCloudRunV2VolumeMount.md) | Volume to mount into the container&#39;s filesystem. |  [optional] |
|**workingDir** | **String** | Container&#39;s working directory. If not specified, the container runtime&#39;s default will be used, which might be configured in the container image. |  [optional] |



