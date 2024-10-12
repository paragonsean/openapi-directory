

# CreateLegalHoldRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | This is the string title of the legal hold. |  |
|**description** | **String** | This is the string description of the legal hold. |  |
|**idempotencyToken** | **String** | This is a user-chosen string used to distinguish between otherwise identical calls. Retrying a successful request with the same idempotency token results in a success message with no action taken. |  [optional] |
|**recoveryPointSelection** | [**CreateLegalHoldRequestRecoveryPointSelection**](CreateLegalHoldRequestRecoveryPointSelection.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - &#x3D; . _ : /.  |  [optional] |



