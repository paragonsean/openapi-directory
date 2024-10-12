

# LinksPaymentInitiationCancel

A list of hyperlinks to be recognised by the TPP. The actual hyperlinks used in the response depend on the dynamical decisions of the ASPSP when processing the request.  Remark: All links can be relative or full links, to be decided by the ASPSP.  Type of links admitted in this response, (further links might be added for ASPSP defined extensions):    * 'startAuthorisation':     In case, where just the authorisation process of the cancellation needs to be started,     but no additional data needs to be updated for time being (no authentication method to be selected,     no PSU identification nor PSU authentication data to be uploaded).   * 'startAuthorisationWithPsuIdentification':      In case where a PSU identification needs to be updated when starting the cancellation authorisation:     The link to the cancellation-authorisations end-point, where the cancellation sub-resource has to be      generated while uploading the PSU identification data.   * 'startAuthorisationWithPsuAuthentication':     In case of a yet to be created authorisation sub-resource: The link to the cancalation authorisation end-point,     where the authorisation sub-resource has to be generated while uploading the PSU authentication data.   * 'startAuthorisationWithEncryptedPsuAuthentication':     Same as startAuthorisactionWithPsuAuthentication where the authentication data need to be encrypted on     application layer in uploading.   * 'startAuthorisationWithAuthenticationMethodSelection':     The link to the authorisation end-point, where the cancellation-authorisation sub-resource has to be     generated while selecting the authentication method. This link is contained under exactly the same     conditions as the data element 'scaMethods' 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**startAuthorisation** | [**HrefType**](HrefType.md) |  |  [optional] |
|**startAuthorisationWithAuthenticationMethodSelection** | [**HrefType**](HrefType.md) |  |  [optional] |
|**startAuthorisationWithEncryptedPsuAuthentication** | [**HrefType**](HrefType.md) |  |  [optional] |
|**startAuthorisationWithPsuAuthentication** | [**HrefType**](HrefType.md) |  |  [optional] |
|**startAuthorisationWithPsuIdentification** | [**HrefType**](HrefType.md) |  |  [optional] |



