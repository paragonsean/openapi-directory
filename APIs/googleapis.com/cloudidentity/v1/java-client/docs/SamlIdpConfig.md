

# SamlIdpConfig

SAML IDP (identity provider) configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changePasswordUri** | **String** | The **Change Password URL** of the identity provider. Users will be sent to this URL when changing their passwords at &#x60;myaccount.google.com&#x60;. This takes precedence over the change password URL configured at customer-level. Must use &#x60;HTTPS&#x60;. |  [optional] |
|**entityId** | **String** | Required. The SAML **Entity ID** of the identity provider. |  [optional] |
|**logoutRedirectUri** | **String** | The **Logout Redirect URL** (sign-out page URL) of the identity provider. When a user clicks the sign-out link on a Google page, they will be redirected to this URL. This is a pure redirect with no attached SAML &#x60;LogoutRequest&#x60; i.e. SAML single logout is not supported. Must use &#x60;HTTPS&#x60;. |  [optional] |
|**singleSignOnServiceUri** | **String** | Required. The &#x60;SingleSignOnService&#x60; endpoint location (sign-in page URL) of the identity provider. This is the URL where the &#x60;AuthnRequest&#x60; will be sent. Must use &#x60;HTTPS&#x60;. Assumed to accept the &#x60;HTTP-Redirect&#x60; binding. |  [optional] |



