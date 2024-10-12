# GkeHubApi.Authority

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identityProvider** | **String** | Output only. An identity provider that reflects the &#x60;issuer&#x60; in the workload identity pool. | [optional] [readonly] 
**issuer** | **String** | Optional. A JSON Web Token (JWT) issuer URI. &#x60;issuer&#x60; must start with &#x60;https://&#x60; and be a valid URL with length &lt;2000 characters. If set, then Google will allow valid OIDC tokens from this issuer to authenticate within the workload_identity_pool. OIDC discovery will be performed on this URI to validate tokens from the issuer. Clearing &#x60;issuer&#x60; disables Workload Identity. &#x60;issuer&#x60; cannot be directly modified; it must be cleared (and Workload Identity disabled) before using a new issuer (and re-enabling Workload Identity). | [optional] 
**oidcJwks** | **Blob** | Optional. OIDC verification keys for this Membership in JWKS format (RFC 7517). When this field is set, OIDC discovery will NOT be performed on &#x60;issuer&#x60;, and instead OIDC tokens will be validated using this field. | [optional] 
**workloadIdentityPool** | **String** | Output only. The name of the workload identity pool in which &#x60;issuer&#x60; will be recognized. There is a single Workload Identity Pool per Hub that is shared between all Memberships that belong to that Hub. For a Hub hosted in {PROJECT_ID}, the workload pool format is &#x60;{PROJECT_ID}.hub.id.goog&#x60;, although this is subject to change in newer versions of this API. | [optional] [readonly] 


