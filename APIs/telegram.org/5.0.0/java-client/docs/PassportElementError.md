

# PassportElementError

This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataHash** | **String** | Base64-encoded data hash |  |
|**fieldName** | **String** | Name of the data field which has the error |  |
|**message** | **String** | Error message |  |
|**source** | **String** | Error source, must be *unspecified* |  |
|**type** | **String** | Type of element of the user&#39;s Telegram Passport which has the issue |  |
|**fileHash** | **String** | Base64-encoded file hash |  |
|**fileHashes** | **List&lt;String&gt;** | List of base64-encoded file hashes |  |
|**elementHash** | **String** | Base64-encoded element hash |  |



