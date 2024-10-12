# CloudIdentityApi.EntityKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The ID of the entity. For Google-managed entities, the &#x60;id&#x60; should be the email address of an existing group or user. Email addresses need to adhere to [name guidelines for users and groups](https://support.google.com/a/answer/9193374). For external-identity-mapped entities, the &#x60;id&#x60; must be a string conforming to the Identity Source&#39;s requirements. Must be unique within a &#x60;namespace&#x60;. | [optional] 
**namespace** | **String** | The namespace in which the entity exists. If not specified, the &#x60;EntityKey&#x60; represents a Google-managed entity such as a Google user or a Google Group. If specified, the &#x60;EntityKey&#x60; represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of &#x60;identitysources/{identity_source}&#x60;. | [optional] 


