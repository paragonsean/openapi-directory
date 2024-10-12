

# LinksUpdatePsuAuthentication

A list of hyperlinks to be recognised by the TPP. Might be contained, if several authentication methods are available for the PSU. Type of links admitted in this response:   * 'updateAdditionalPsuAuthentication':     The link to the payment initiation or account information resource,     which needs to be updated by an additional PSU password.     This link is only contained in rare cases,     where such additional passwords are needed for PSU authentications.   * 'updateAdditionalEncryptedPsuAuthentication':     The link to the payment initiation or account information resource,     which needs to be updated by an additional encrypted PSU password.     This link is only contained in rare cases, where such additional passwords are needed for PSU authentications.   * 'selectAuthenticationMethod':     This is a link to a resource, where the TPP can select the applicable second factor authentication     methods for the PSU, if there were several available authentication methods.     This link is only contained, if the PSU is already identified or authenticated with the first relevant     factor or alternatively an access token, if SCA is required and if the PSU has a choice between different     authentication methods.     If this link is contained, then there is also the data element 'scaMethods' contained in the response body.   * 'authoriseTransaction':      The link to the resource, where the \"Transaction authorisation request\" is sent to.      This is the link to the resource which will authorise the transaction by checking the SCA authentication      data within the Embedded SCA approach.   * 'scaStatus':     The link to retrieve the scaStatus of the corresponding authorisation sub-resource. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authoriseTransaction** | [**HrefType**](HrefType.md) |  |  [optional] |
|**scaStatus** | [**HrefType**](HrefType.md) |  |  [optional] |
|**selectAuthenticationMethod** | [**HrefType**](HrefType.md) |  |  [optional] |
|**updateAdditionalEncryptedPsuAuthentication** | [**HrefType**](HrefType.md) |  |  [optional] |
|**updateAdditionalPsuAuthentication** | [**HrefType**](HrefType.md) |  |  [optional] |



