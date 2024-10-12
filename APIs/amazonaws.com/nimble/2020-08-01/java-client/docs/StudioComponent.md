

# StudioComponent

<p>A studio component represents a network resource to be used by a studio's users and workflows. A typical studio contains studio components for each of the following: render farm, Active Directory, licensing, and file system.</p> <p>Access to a studio component is managed by specifying security groups for the resource, as well as its endpoint.</p> <p>A studio component also has a set of initialization scripts that are returned by <code>GetLaunchProfileInitialization</code>. These initialization scripts run on streaming sessions when they start. They provide users with flexibility in controlling how the studio resources are configured on a streaming session.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  [optional] |
|**_configuration** | [**CreateStudioComponentRequestConfiguration**](CreateStudioComponentRequestConfiguration.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**createdBy** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**ec2SecurityGroupIds** | [**List**](List.md) |  |  [optional] |
|**initializationScripts** | [**List**](List.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**runtimeRoleArn** | [**String**](String.md) |  |  [optional] |
|**scriptParameters** | [**List**](List.md) |  |  [optional] |
|**secureInitializationRoleArn** | [**String**](String.md) |  |  [optional] |
|**state** | [**StudioComponentState**](StudioComponentState.md) |  |  [optional] |
|**statusCode** | [**StudioComponentStatusCode**](StudioComponentStatusCode.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**studioComponentId** | [**String**](String.md) |  |  [optional] |
|**subtype** | [**StudioComponentSubtype**](StudioComponentSubtype.md) |  |  [optional] |
|**tags** | [**Map**](Map.md) |  |  [optional] |
|**type** | [**StudioComponentType**](StudioComponentType.md) |  |  [optional] |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**updatedBy** | [**String**](String.md) |  |  [optional] |



