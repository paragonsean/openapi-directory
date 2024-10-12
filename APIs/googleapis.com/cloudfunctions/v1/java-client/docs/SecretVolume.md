

# SecretVolume

Configuration for a secret volume. It has the information necessary to fetch the secret value from secret manager and make it available as files mounted at the requested paths within the application container. Secret value is not a part of the configuration. Every filesystem read operation performs a lookup in secret manager to retrieve the secret value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mountPath** | **String** | The path within the container to mount the secret volume. For example, setting the mount_path as &#x60;/etc/secrets&#x60; would mount the secret value files under the &#x60;/etc/secrets&#x60; directory. This directory will also be completely shadowed and unavailable to mount any other secrets. Recommended mount paths: /etc/secrets Restricted mount paths: /cloudsql, /dev/log, /pod, /proc, /var/log |  [optional] |
|**projectId** | **String** | Project identifier (preferrably project number but can also be the project ID) of the project that contains the secret. If not set, it will be populated with the function&#39;s project assuming that the secret exists in the same project as of the function. |  [optional] |
|**secret** | **String** | Name of the secret in secret manager (not the full resource name). |  [optional] |
|**versions** | [**List&lt;SecretVersion&gt;**](SecretVersion.md) | List of secret versions to mount for this secret. If empty, the &#x60;latest&#x60; version of the secret will be made available in a file named after the secret under the mount point. |  [optional] |



