# AmazonNimbleStudio.CreateStreamingSessionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ec2InstanceType** | **String** | The EC2 Instance type used for the streaming session. | [optional] 
**launchProfileId** | **String** | The ID of the launch profile used to control access from the streaming session. | 
**ownedBy** | **String** | The user ID of the user that owns the streaming session. The user that owns the session will be logging into the session and interacting with the virtual workstation. | [optional] 
**streamingImageId** | **String** | The ID of the streaming image. | [optional] 
**tags** | **{String: String}** | A collection of labels, in the form of key-value pairs, that apply to this resource. | [optional] 



## Enum: Ec2InstanceTypeEnum


* `g4dn.xlarge` (value: `"g4dn.xlarge"`)

* `g4dn.2xlarge` (value: `"g4dn.2xlarge"`)

* `g4dn.4xlarge` (value: `"g4dn.4xlarge"`)

* `g4dn.8xlarge` (value: `"g4dn.8xlarge"`)

* `g4dn.12xlarge` (value: `"g4dn.12xlarge"`)

* `g4dn.16xlarge` (value: `"g4dn.16xlarge"`)

* `g3.4xlarge` (value: `"g3.4xlarge"`)

* `g3s.xlarge` (value: `"g3s.xlarge"`)

* `g5.xlarge` (value: `"g5.xlarge"`)

* `g5.2xlarge` (value: `"g5.2xlarge"`)

* `g5.4xlarge` (value: `"g5.4xlarge"`)

* `g5.8xlarge` (value: `"g5.8xlarge"`)

* `g5.16xlarge` (value: `"g5.16xlarge"`)




