

# LinksUpdatePsuIdentification

A list of hyperlinks to be recognised by the TPP. The actual hyperlinks used in the response depend on the dynamical decisions of the ASPSP when processing the request.  **Remark:** All links can be relative or full links, to be decided by the ASPSP.  Type of links admitted in this response, (further links might be added for ASPSP defined extensions):  - 'scaStatus': The link to retrieve the scaStatus of the corresponding authorisation sub-resource. - 'selectAuthenticationMethod': This is a link to a resource, where the TPP can select the applicable second factor authentication methods for the PSU, if there are several available authentication methods and if the PSU is already sufficiently authenticated.. If this link is contained, then there is also the data element \"scaMethods\" contained in the response body. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scaStatus** | [**HrefType**](HrefType.md) |  |  [optional] |
|**selectAuthenticationMethod** | [**HrefType**](HrefType.md) |  |  [optional] |



