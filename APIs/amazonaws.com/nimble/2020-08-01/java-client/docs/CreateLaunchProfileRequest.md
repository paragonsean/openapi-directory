

# CreateLaunchProfileRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A human-readable description of the launch profile. |  [optional] |
|**ec2SubnetIds** | **List&lt;String&gt;** | Specifies the IDs of the EC2 subnets where streaming sessions will be accessible from. These subnets must support the specified instance types.  |  |
|**launchProfileProtocolVersions** | **List&lt;String&gt;** | The version number of the protocol that is used by the launch profile. The only valid version is \&quot;2021-03-31\&quot;. |  |
|**name** | **String** | The name for the launch profile. |  |
|**streamConfiguration** | [**CreateLaunchProfileRequestStreamConfiguration**](CreateLaunchProfileRequestStreamConfiguration.md) |  |  |
|**studioComponentIds** | **List&lt;String&gt;** | Unique identifiers for a collection of studio components that can be used with this launch profile. |  |
|**tags** | **Map&lt;String, String&gt;** | A collection of labels, in the form of key-value pairs, that apply to this resource. |  [optional] |



