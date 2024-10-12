

# Container

A single application container. This specifies both the container to run, the command to run in the container and the arguments to supply to it. Note that additional arguments may be supplied by the system to the container at runtime.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **List&lt;String&gt;** | Arguments to the entrypoint. The docker image&#39;s CMD is used if this is not provided. Variable references are not supported in Cloud Run. |  [optional] |
|**command** | **List&lt;String&gt;** | Entrypoint array. Not executed within a shell. The docker image&#39;s ENTRYPOINT is used if this is not provided. Variable references are not supported in Cloud Run. |  [optional] |
|**env** | [**List&lt;EnvVar&gt;**](EnvVar.md) | List of environment variables to set in the container. EnvVar with duplicate names are generally allowed; if referencing a secret, the name must be unique for the container. For non-secret EnvVar names, the Container will only get the last-declared one. |  [optional] |
|**envFrom** | [**List&lt;EnvFromSource&gt;**](EnvFromSource.md) | Not supported by Cloud Run. |  [optional] |
|**image** | **String** | Required. Name of the container image in Dockerhub, Google Artifact Registry, or Google Container Registry. If the host is not provided, Dockerhub is assumed. |  [optional] |
|**imagePullPolicy** | **String** | Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. |  [optional] |
|**livenessProbe** | [**Probe**](Probe.md) |  |  [optional] |
|**name** | **String** | Name of the container specified as a DNS_LABEL (RFC 1123). |  [optional] |
|**ports** | [**List&lt;ContainerPort&gt;**](ContainerPort.md) | List of ports to expose from the container. Only a single port can be specified. The specified ports must be listening on all interfaces (0.0.0.0) within the container to be accessible. If omitted, a port number will be chosen and passed to the container through the PORT environment variable for the container to listen on. |  [optional] |
|**readinessProbe** | [**Probe**](Probe.md) |  |  [optional] |
|**resources** | [**ResourceRequirements**](ResourceRequirements.md) |  |  [optional] |
|**securityContext** | [**SecurityContext**](SecurityContext.md) |  |  [optional] |
|**startupProbe** | [**Probe**](Probe.md) |  |  [optional] |
|**terminationMessagePath** | **String** | Path at which the file to which the container&#39;s termination message will be written is mounted into the container&#39;s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. |  [optional] |
|**terminationMessagePolicy** | **String** | Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated. |  [optional] |
|**volumeMounts** | [**List&lt;VolumeMount&gt;**](VolumeMount.md) | Volume to mount into the container&#39;s filesystem. Only supports SecretVolumeSources. Pod volumes to mount into the container&#39;s filesystem. |  [optional] |
|**workingDir** | **String** | Container&#39;s working directory. If not specified, the container runtime&#39;s default will be used, which might be configured in the container image. |  [optional] |



