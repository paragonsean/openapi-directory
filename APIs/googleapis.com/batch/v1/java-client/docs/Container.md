

# Container

Container runnable.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockExternalNetwork** | **Boolean** | If set to true, external network access to and from container will be blocked, containers that are with block_external_network as true can still communicate with each other, network cannot be specified in the &#x60;container.options&#x60; field. |  [optional] |
|**commands** | **List&lt;String&gt;** | Overrides the &#x60;CMD&#x60; specified in the container. If there is an ENTRYPOINT (either in the container image or with the entrypoint field below) then commands are appended as arguments to the ENTRYPOINT. |  [optional] |
|**enableImageStreaming** | **Boolean** | Optional. If set to true, this container runnable uses Image streaming. Use Image streaming to allow the runnable to initialize without waiting for the entire container image to download, which can significantly reduce startup time for large container images. When &#x60;enableImageStreaming&#x60; is set to true, the container runtime is [containerd](https://containerd.io/) instead of Docker. Additionally, this container runnable only supports the following &#x60;container&#x60; subfields: &#x60;imageUri&#x60;, &#x60;commands[]&#x60;, &#x60;entrypoint&#x60;, and &#x60;volumes[]&#x60;; any other &#x60;container&#x60; subfields are ignored. For more information about the requirements and limitations for using Image streaming with Batch, see the [&#x60;image-streaming&#x60; sample on GitHub](https://github.com/GoogleCloudPlatform/batch-samples/tree/main/api-samples/image-streaming). |  [optional] |
|**entrypoint** | **String** | Overrides the &#x60;ENTRYPOINT&#x60; specified in the container. |  [optional] |
|**imageUri** | **String** | The URI to pull the container image from. |  [optional] |
|**options** | **String** | Arbitrary additional options to include in the \&quot;docker run\&quot; command when running this container, e.g. \&quot;--network host\&quot;. |  [optional] |
|**password** | **String** | Required if the container image is from a private Docker registry. The password to login to the Docker registry that contains the image. For security, it is strongly recommended to specify an encrypted password by using a Secret Manager secret: &#x60;projects/_*_/secrets/_*_/versions/_*&#x60;. Warning: If you specify the password using plain text, you risk the password being exposed to any users who can view the job or its logs. To avoid this risk, specify a secret that contains the password instead. Learn more about [Secret Manager](https://cloud.google.com/secret-manager/docs/) and [using Secret Manager with Batch](https://cloud.google.com/batch/docs/create-run-job-secret-manager). |  [optional] |
|**username** | **String** | Required if the container image is from a private Docker registry. The username to login to the Docker registry that contains the image. You can either specify the username directly by using plain text or specify an encrypted username by using a Secret Manager secret: &#x60;projects/_*_/secrets/_*_/versions/_*&#x60;. However, using a secret is recommended for enhanced security. Caution: If you specify the username using plain text, you risk the username being exposed to any users who can view the job or its logs. To avoid this risk, specify a secret that contains the username instead. Learn more about [Secret Manager](https://cloud.google.com/secret-manager/docs/) and [using Secret Manager with Batch](https://cloud.google.com/batch/docs/create-run-job-secret-manager). |  [optional] |
|**volumes** | **List&lt;String&gt;** | Volumes to mount (bind mount) from the host machine files or directories into the container, formatted to match docker run&#39;s --volume option, e.g. /foo:/bar, or /foo:/bar:ro If the &#x60;TaskSpec.Volumes&#x60; field is specified but this field is not, Batch will mount each volume from the host machine to the container with the same mount path by default. In this case, the default mount option for containers will be read-only (ro) for existing persistent disks and read-write (rw) for other volume types, regardless of the original mount options specified in &#x60;TaskSpec.Volumes&#x60;. If you need different mount settings, you can explicitly configure them in this field. |  [optional] |



