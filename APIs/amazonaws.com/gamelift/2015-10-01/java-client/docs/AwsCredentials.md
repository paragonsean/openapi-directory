

# AwsCredentials

Temporary access credentials used for uploading game build files to Amazon GameLift. They are valid for a limited time. If they expire before you upload your game build, get a new set by calling <a href=\"https://docs.aws.amazon.com/gamelift/latest/apireference/API_RequestUploadCredentials.html\">RequestUploadCredentials</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessKeyId** | [**String**](String.md) |  |  [optional] |
|**secretAccessKey** | [**String**](String.md) |  |  [optional] |
|**sessionToken** | [**String**](String.md) |  |  [optional] |



