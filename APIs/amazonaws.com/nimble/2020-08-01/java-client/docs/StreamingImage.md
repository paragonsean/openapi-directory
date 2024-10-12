

# StreamingImage

<p>Represents a streaming image resource.</p> <p>Streaming images are used by studio users to select which operating system and software they want to use in a Nimble Studio streaming session.</p> <p>Amazon provides a number of streaming images that include popular 3rd-party software.</p> <p>You can create your own streaming images using an Amazon EC2 machine image that you create for this purpose. You can also include software that your users require.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**ec2ImageId** | [**String**](String.md) |  |  [optional] |
|**encryptionConfiguration** | [**StreamingImageEncryptionConfiguration**](StreamingImageEncryptionConfiguration.md) |  |  [optional] |
|**eulaIds** | [**List**](List.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**owner** | [**String**](String.md) |  |  [optional] |
|**platform** | [**String**](String.md) |  |  [optional] |
|**state** | [**StreamingImageState**](StreamingImageState.md) |  |  [optional] |
|**statusCode** | [**StreamingImageStatusCode**](StreamingImageStatusCode.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**streamingImageId** | [**String**](String.md) |  |  [optional] |
|**tags** | [**Map**](Map.md) |  |  [optional] |



