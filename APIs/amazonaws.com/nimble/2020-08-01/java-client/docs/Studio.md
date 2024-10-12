

# Studio

<p>Represents a studio resource.</p> <p>A studio is the core resource used with Nimble Studio. You must create a studio first, before any other resource type can be created. All other resources you create and manage in Nimble Studio are contained within a studio.</p> <p>When creating a studio, you must provides two IAM roles for use with the Nimble Studio portal. These roles are assumed by your users when they log in to the Nimble Studio portal via IAM Identity Center and your identity source.</p> <p>The user role must have the <code>AmazonNimbleStudio-StudioUser</code> managed policy attached for the portal to function properly.</p> <p>The admin role must have the <code>AmazonNimbleStudio-StudioAdmin</code> managed policy attached for the portal to function properly.</p> <p>Your studio roles must trust the <code>identity.nimble.amazonaws.com</code> service principal to function properly.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminRoleArn** | [**String**](String.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**displayName** | [**String**](String.md) |  |  [optional] |
|**homeRegion** | [**String**](String.md) |  |  [optional] |
|**ssoClientId** | [**String**](String.md) |  |  [optional] |
|**state** | [**StudioState**](StudioState.md) |  |  [optional] |
|**statusCode** | [**StudioStatusCode**](StudioStatusCode.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**studioEncryptionConfiguration** | [**StudioStudioEncryptionConfiguration**](StudioStudioEncryptionConfiguration.md) |  |  [optional] |
|**studioId** | [**String**](String.md) |  |  [optional] |
|**studioName** | [**String**](String.md) |  |  [optional] |
|**studioUrl** | [**String**](String.md) |  |  [optional] |
|**tags** | [**Map**](Map.md) |  |  [optional] |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**userRoleArn** | [**String**](String.md) |  |  [optional] |



