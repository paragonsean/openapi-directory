

# Identity

Represents an email address, a profile on networks like github and twitter, or a record in another system.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | The email of the person in the source system |  [optional] |
|**name** | **String** | The name of the person in the source system |  [optional] |
|**source** | **String** | The type of source: known values include github, twitter, discourse, email, linkedin, devto. Custom values can also be used |  |
|**sourceHost** | **String** | Specifies the location of the source, such as the host of a Discourse instance |  [optional] |
|**uid** | **String** | The uid of the person in the source system |  [optional] |
|**url** | **String** | For custom identities, an optional link to the profile on the source system |  [optional] |
|**username** | **String** | The username of the person in the source system |  [optional] |



