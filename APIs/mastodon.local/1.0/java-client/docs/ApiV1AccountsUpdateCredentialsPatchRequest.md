

# ApiV1AccountsUpdateCredentialsPatchRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avatar** | **String** | Avatar image encoded using multipart/form-data |  [optional] |
|**bot** | **Boolean** | Whether the account has a bot flag. |  [optional] |
|**discoverable** | **String** | Whether the account should be shown in the profile directory. |  [optional] |
|**displayName** | **String** | The display name to use for the profile. |  [optional] |
|**fieldsAttributes** | **Object** | Profile metadata &#x60;name&#x60; and &#x60;value&#x60;. (By default, max 4 fields and 255 characters per property/value) |  [optional] |
|**header** | **String** | Header image encoded using multipart/form-data |  [optional] |
|**locked** | **Boolean** | Whether manual approval of follow requests is required. |  [optional] |
|**note** | **String** | The account bio. |  [optional] |
|**source** | [**ApiV1AccountsUpdateCredentialsPatchRequestSource**](ApiV1AccountsUpdateCredentialsPatchRequestSource.md) |  |  [optional] |



