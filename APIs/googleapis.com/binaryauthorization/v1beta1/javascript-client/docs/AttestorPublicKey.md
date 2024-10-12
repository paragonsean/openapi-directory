# BinaryAuthorizationApi.AttestorPublicKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asciiArmoredPgpPublicKey** | **String** | ASCII-armored representation of a PGP public key, as the entire output by the command &#x60;gpg --export --armor foo@example.com&#x60; (either LF or CRLF line endings). When using this field, &#x60;id&#x60; should be left blank. The BinAuthz API handlers will calculate the ID and fill it in automatically. BinAuthz computes this ID as the OpenPGP RFC4880 V4 fingerprint, represented as upper-case hex. If &#x60;id&#x60; is provided by the caller, it will be overwritten by the API-calculated ID. | [optional] 
**comment** | **String** | Optional. A descriptive comment. This field may be updated. | [optional] 
**id** | **String** | The ID of this public key. Signatures verified by BinAuthz must include the ID of the public key that can be used to verify them, and that ID must match the contents of this field exactly. Additional restrictions on this field can be imposed based on which public key type is encapsulated. See the documentation on &#x60;public_key&#x60; cases below for details. | [optional] 
**pkixPublicKey** | [**PkixPublicKey**](PkixPublicKey.md) |  | [optional] 


