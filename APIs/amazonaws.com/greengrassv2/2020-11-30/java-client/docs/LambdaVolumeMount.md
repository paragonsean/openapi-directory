

# LambdaVolumeMount

Contains information about a volume that Linux processes in a container can access. When you define a volume, the IoT Greengrass Core software mounts the source files to the destination inside the container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourcePath** | [**String**](String.md) |  |  |
|**destinationPath** | [**String**](String.md) |  |  |
|**permission** | [**LambdaFilesystemPermission**](LambdaFilesystemPermission.md) |  |  [optional] |
|**addGroupOwner** | [**Boolean**](Boolean.md) |  |  [optional] |



