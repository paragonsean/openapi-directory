

# ApiV2010Account


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authToken** | **String** | The authorization token for this account. This token should be kept a secret, so no sharing. |  [optional] |
|**dateCreated** | **String** | The date that this account was created, in GMT in RFC 2822 format |  [optional] |
|**dateUpdated** | **String** | The date that this account was last updated, in GMT in RFC 2822 format. |  [optional] |
|**friendlyName** | **String** | A human readable description of this account, up to 64 characters long. By default the FriendlyName is your email address. |  [optional] |
|**ownerAccountSid** | **String** | The unique 34 character id that represents the parent of this account. The OwnerAccountSid of a parent account is it&#39;s own sid. |  [optional] |
|**sid** | **String** | A 34 character string that uniquely identifies this resource. |  [optional] |
|**status** | **AccountEnumStatus** |  |  [optional] |
|**subresourceUris** | **Object** | A Map of various subresources available for the given Account Instance |  [optional] |
|**type** | **AccountEnumType** |  |  [optional] |
|**uri** | **String** | The URI for this resource, relative to &#x60;https://api.twilio.com&#x60; |  [optional] |



