

# CreateStreamingSessionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ec2InstanceType** | [**Ec2InstanceTypeEnum**](#Ec2InstanceTypeEnum) | The EC2 Instance type used for the streaming session. |  [optional] |
|**launchProfileId** | **String** | The ID of the launch profile used to control access from the streaming session. |  |
|**ownedBy** | **String** | The user ID of the user that owns the streaming session. The user that owns the session will be logging into the session and interacting with the virtual workstation. |  [optional] |
|**streamingImageId** | **String** | The ID of the streaming image. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A collection of labels, in the form of key-value pairs, that apply to this resource. |  [optional] |



## Enum: Ec2InstanceTypeEnum

| Name | Value |
|---- | -----|
| G4DN_XLARGE | &quot;g4dn.xlarge&quot; |
| G4DN_2XLARGE | &quot;g4dn.2xlarge&quot; |
| G4DN_4XLARGE | &quot;g4dn.4xlarge&quot; |
| G4DN_8XLARGE | &quot;g4dn.8xlarge&quot; |
| G4DN_12XLARGE | &quot;g4dn.12xlarge&quot; |
| G4DN_16XLARGE | &quot;g4dn.16xlarge&quot; |
| G3_4XLARGE | &quot;g3.4xlarge&quot; |
| G3S_XLARGE | &quot;g3s.xlarge&quot; |
| G5_XLARGE | &quot;g5.xlarge&quot; |
| G5_2XLARGE | &quot;g5.2xlarge&quot; |
| G5_4XLARGE | &quot;g5.4xlarge&quot; |
| G5_8XLARGE | &quot;g5.8xlarge&quot; |
| G5_16XLARGE | &quot;g5.16xlarge&quot; |



