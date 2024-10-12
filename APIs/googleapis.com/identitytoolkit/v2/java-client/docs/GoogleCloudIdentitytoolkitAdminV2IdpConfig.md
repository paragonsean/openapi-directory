

# GoogleCloudIdentitytoolkitAdminV2IdpConfig

The SAML IdP (Identity Provider) configuration when the project acts as the relying party.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**idpCertificates** | [**List&lt;GoogleCloudIdentitytoolkitAdminV2IdpCertificate&gt;**](GoogleCloudIdentitytoolkitAdminV2IdpCertificate.md) | IDP&#39;s public keys for verifying signature in the assertions. |  [optional] |
|**idpEntityId** | **String** | Unique identifier for all SAML entities. |  [optional] |
|**signRequest** | **Boolean** | Indicates if outbounding SAMLRequest should be signed. |  [optional] |
|**ssoUrl** | **String** | URL to send Authentication request to. |  [optional] |



