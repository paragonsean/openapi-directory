

# SharingSettings

Specifies options for sharing SageMaker Studio notebooks. These settings are specified as part of <code>DefaultUserSettings</code> when the <code>CreateDomain</code> API is called, and as part of <code>UserSettings</code> when the <code>CreateUserProfile</code> API is called. When <code>SharingSettings</code> is not specified, notebook sharing isn't allowed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**notebookOutputOption** | [**NotebookOutputOption**](NotebookOutputOption.md) |  |  [optional] |
|**s3OutputPath** | [**String**](String.md) |  |  [optional] |
|**s3KmsKeyId** | [**String**](String.md) |  |  [optional] |



