

# ContaineranalysisGoogleDevtoolsCloudbuildV1Volume

Volume describes a Docker container volume which is mounted into build steps in order to persist files across build step execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the volume to mount. Volume names must be unique per build step and must be valid names for Docker volumes. Each named volume must be used by at least two build steps. |  [optional] |
|**path** | **String** | Path at which to mount the volume. Paths must be absolute and cannot conflict with other volume paths on the same build step or with certain reserved volume paths. |  [optional] |



