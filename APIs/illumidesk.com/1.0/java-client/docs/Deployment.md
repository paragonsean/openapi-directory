

# Deployment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**config** | [**DeploymentConfig**](DeploymentConfig.md) |  |  [optional] |
|**createdAt** | **String** | Date and time when server was created. |  [optional] |
|**createdBy** | **String** | User that created server. |  [optional] |
|**framework** | [**FrameworkEnum**](#FrameworkEnum) | Framework that the deployment will have access to. |  [optional] |
|**id** | **String** | Deploymeny unique identifier |  [optional] |
|**name** | **String** | Deployment name. |  [optional] |
|**project** | **String** | Project name. |  [optional] |
|**runtime** | [**RuntimeEnum**](#RuntimeEnum) | Language runtime the deployment will use. |  [optional] |



## Enum: FrameworkEnum

| Name | Value |
|---- | -----|
| TENSORFLOW | &quot;tensorflow&quot; |



## Enum: RuntimeEnum

| Name | Value |
|---- | -----|
| PYTHON2_7 | &quot;python2.7&quot; |



