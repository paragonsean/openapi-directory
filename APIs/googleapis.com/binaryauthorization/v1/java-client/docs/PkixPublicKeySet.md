

# PkixPublicKeySet

A bundle of PKIX public keys, used to authenticate attestation signatures. Generally, a signature is considered to be authenticated by a `PkixPublicKeySet` if any of the public keys verify it (i.e. it is an \"OR\" of the keys).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pkixPublicKeys** | [**List&lt;PkixPublicKey&gt;**](PkixPublicKey.md) | Required. &#x60;pkix_public_keys&#x60; must have at least one entry. |  [optional] |



