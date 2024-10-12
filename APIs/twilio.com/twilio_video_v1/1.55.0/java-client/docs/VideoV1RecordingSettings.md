

# VideoV1RecordingSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the RecordingSettings resource. |  [optional] |
|**awsCredentialsSid** | **String** | The SID of the stored Credential resource. |  [optional] |
|**awsS3Url** | **URI** | The URL of the AWS S3 bucket where the recordings are stored. We only support DNS-compliant URLs like &#x60;https://documentation-example-twilio-bucket/recordings&#x60;, where &#x60;recordings&#x60; is the path in which you want the recordings to be stored. This URL accepts only URI-valid characters, as described in the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-2). |  [optional] |
|**awsStorageEnabled** | **Boolean** | Whether all recordings are written to the &#x60;aws_s3_url&#x60;. When &#x60;false&#x60;, all recordings are stored in our cloud. |  [optional] |
|**encryptionEnabled** | **Boolean** | Whether all recordings are stored in an encrypted form. The default is &#x60;false&#x60;. |  [optional] |
|**encryptionKeySid** | **String** | The SID of the Public Key resource used for encryption. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource and show the user in the console |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |



