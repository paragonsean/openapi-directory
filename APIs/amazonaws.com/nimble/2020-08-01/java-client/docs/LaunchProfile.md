

# LaunchProfile

<p>A launch profile controls your artist workforce’s access to studio components, like compute farms, shared file systems, managed file systems, and license server configurations, as well as instance types and Amazon Machine Images (AMIs). </p> <p>Studio administrators create launch profiles in the Nimble Studio console. Artists can use their launch profiles to launch an instance from the Nimble Studio portal. Each user’s launch profile defines how they can launch a streaming session. By default, studio admins can use all launch profiles.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**createdBy** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**ec2SubnetIds** | [**List**](List.md) |  |  [optional] |
|**launchProfileId** | [**String**](String.md) |  |  [optional] |
|**launchProfileProtocolVersions** | [**List**](List.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**state** | [**LaunchProfileState**](LaunchProfileState.md) |  |  [optional] |
|**statusCode** | [**LaunchProfileStatusCode**](LaunchProfileStatusCode.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**streamConfiguration** | [**LaunchProfileStreamConfiguration**](LaunchProfileStreamConfiguration.md) |  |  [optional] |
|**studioComponentIds** | [**List**](List.md) |  |  [optional] |
|**tags** | [**Map**](Map.md) |  |  [optional] |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**updatedBy** | [**String**](String.md) |  |  [optional] |
|**validationResults** | [**List**](List.md) |  |  [optional] |



