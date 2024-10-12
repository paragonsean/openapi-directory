

# LaunchProfileInitialization

<p>A launch profile initialization contains information required for a workstation or server to connect to a launch profile.</p> <p>This includes scripts, endpoints, security groups, subnets, and other configuration.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeDirectory** | [**LaunchProfileInitializationActiveDirectory**](LaunchProfileInitializationActiveDirectory.md) |  |  [optional] |
|**ec2SecurityGroupIds** | [**List**](List.md) |  |  [optional] |
|**launchProfileId** | [**String**](String.md) |  |  [optional] |
|**launchProfileProtocolVersion** | [**String**](String.md) |  |  [optional] |
|**launchPurpose** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**platform** | [**LaunchProfilePlatform**](LaunchProfilePlatform.md) |  |  [optional] |
|**systemInitializationScripts** | [**List**](List.md) |  |  [optional] |
|**userInitializationScripts** | [**List**](List.md) |  |  [optional] |



