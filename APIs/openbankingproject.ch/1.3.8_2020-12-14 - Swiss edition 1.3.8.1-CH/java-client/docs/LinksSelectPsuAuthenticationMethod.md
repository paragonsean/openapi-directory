

# LinksSelectPsuAuthenticationMethod

A list of hyperlinks to be recognised by the TPP. The actual hyperlinks used in the response depend on the dynamical decisions of the ASPSP when processing the request.  **Remark:** All links can be relative or full links, to be decided by the ASPSP.  **Remark:** This method can be applied before or after PSU identification. This leads to many possible hyperlink responses. Type of links admitted in this response, (further links might be added for ASPSP defined extensions):  - 'scaRedirect':   In case of an SCA Redirect Approach, the ASPSP is transmitting the link to which to   redirect the PSU browser. - 'scaOAuth':   In case of a SCA OAuth2 Approach, the ASPSP is transmitting the URI where the   configuration of the Authorisation Server can be retrieved.   The configuration follows the OAuth 2.0 Authorisation Server Metadata specification. * 'confirmation':    Might be added by the ASPSP if either the \"scaRedirect\" or \"scaOAuth\" hyperlink is returned    in the same response message.    This hyperlink defines the URL to the resource which needs to be updated with      * a confirmation code as retrieved after the plain redirect authentication process with the ASPSP authentication server or     * an access token as retrieved by submitting an authorization code after the integrated OAuth based authentication process with the ASPSP authentication server. - 'updatePsuIdentification':    The link to the authorisation or cancellation authorisation sub-resource,    where PSU identification data needs to be uploaded. - 'updatePsuAuthentication':   The link to the authorisation or cancellation authorisation sub-resource,   where PSU authentication data needs to be uploaded.   - 'updateEncryptedPsuAuthentication':   The link to the authorisation or cancellation authorisation sub-resource,   where PSU authentication encrypted data needs to be uploaded. - 'updateAdditionalPsuAuthentication':     The link to the payment initiation or account information resource,     which needs to be updated by an additional PSU password. - 'updateAdditionalEncryptedPsuAuthentication':     The link to the payment initiation or account information resource,     which needs to be updated by an additional encrypted PSU password. - 'authoriseTransaction':   The link to the authorisation or cancellation authorisation sub-resource,   where the authorisation data has to be uploaded, e.g. the TOP received by SMS. - 'scaStatus':   The link to retrieve the scaStatus of the corresponding authorisation sub-resource. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authoriseTransaction** | [**HrefType**](HrefType.md) |  |  [optional] |
|**confirmation** | [**HrefType**](HrefType.md) |  |  [optional] |
|**scaOAuth** | [**HrefType**](HrefType.md) |  |  [optional] |
|**scaRedirect** | [**HrefType**](HrefType.md) |  |  [optional] |
|**scaStatus** | [**HrefType**](HrefType.md) |  |  [optional] |
|**updateAdditionalEncryptedPsuAuthentication** | [**HrefType**](HrefType.md) |  |  [optional] |
|**updateAdditionalPsuAuthentication** | [**HrefType**](HrefType.md) |  |  [optional] |
|**updatePsuAuthentication** | [**HrefType**](HrefType.md) |  |  [optional] |
|**updatePsuIdentification** | [**HrefType**](HrefType.md) |  |  [optional] |



