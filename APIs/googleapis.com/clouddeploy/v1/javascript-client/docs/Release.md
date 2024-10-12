# CloudDeployApi.Release

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandoned** | **Boolean** | Output only. Indicates whether this is an abandoned release. | [optional] [readonly] 
**annotations** | **{String: String}** | User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. | [optional] 
**buildArtifacts** | [**[BuildArtifact]**](BuildArtifact.md) | List of artifacts to pass through to Skaffold command. | [optional] 
**condition** | [**ReleaseCondition**](ReleaseCondition.md) |  | [optional] 
**createTime** | **String** | Output only. Time at which the &#x60;Release&#x60; was created. | [optional] [readonly] 
**customTargetTypeSnapshots** | [**[CustomTargetType]**](CustomTargetType.md) | Output only. Snapshot of the custom target types referenced by the targets taken at release creation time. | [optional] [readonly] 
**deliveryPipelineSnapshot** | [**DeliveryPipeline**](DeliveryPipeline.md) |  | [optional] 
**deployParameters** | **{String: String}** | Optional. The deploy parameters to use for all targets in this release. | [optional] 
**description** | **String** | Description of the &#x60;Release&#x60;. Max length is 255 characters. | [optional] 
**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] 
**labels** | **{String: String}** | Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;&#x3D; 128 bytes. | [optional] 
**name** | **String** | Optional. Name of the &#x60;Release&#x60;. Format is &#x60;projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/a-z{0,62}&#x60;. | [optional] 
**renderEndTime** | **String** | Output only. Time at which the render completed. | [optional] [readonly] 
**renderStartTime** | **String** | Output only. Time at which the render began. | [optional] [readonly] 
**renderState** | **String** | Output only. Current state of the render operation. | [optional] [readonly] 
**skaffoldConfigPath** | **String** | Filepath of the Skaffold config inside of the config URI. | [optional] 
**skaffoldConfigUri** | **String** | Cloud Storage URI of tar.gz archive containing Skaffold configuration. | [optional] 
**skaffoldVersion** | **String** | The Skaffold version to use when operating on this release, such as \&quot;1.20.0\&quot;. Not all versions are valid; Cloud Deploy supports a specific set of versions. If unset, the most recent supported Skaffold version will be used. | [optional] 
**targetArtifacts** | [**{String: TargetArtifact}**](TargetArtifact.md) | Output only. Map from target ID to the target artifacts created during the render operation. | [optional] [readonly] 
**targetRenders** | [**{String: TargetRender}**](TargetRender.md) | Output only. Map from target ID to details of the render operation for that target. | [optional] [readonly] 
**targetSnapshots** | [**[Target]**](Target.md) | Output only. Snapshot of the targets taken at release creation time. | [optional] [readonly] 
**uid** | **String** | Output only. Unique identifier of the &#x60;Release&#x60;. | [optional] [readonly] 



## Enum: RenderStateEnum


* `RENDER_STATE_UNSPECIFIED` (value: `"RENDER_STATE_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)




