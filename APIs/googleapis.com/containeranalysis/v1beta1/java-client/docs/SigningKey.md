

# SigningKey

This defines the format used to record keys used in the software supply chain. An in-toto link is attested using one or more keys defined in the in-toto layout. An example of this is: { \"key_id\": \"776a00e29f3559e0141b3b096f696abc6cfb0c657ab40f441132b345b0...\", \"key_type\": \"rsa\", \"public_key_value\": \"-----BEGIN PUBLIC KEY-----\\nMIIBojANBgkqhkiG9w0B...\", \"key_scheme\": \"rsassa-pss-sha256\" } The format for in-toto's key definition can be found in section 4.2 of the in-toto specification.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyId** | **String** | key_id is an identifier for the signing key. |  [optional] |
|**keyScheme** | **String** | This field contains the corresponding signature scheme. Eg: \&quot;rsassa-pss-sha256\&quot;. |  [optional] |
|**keyType** | **String** | This field identifies the specific signing method. Eg: \&quot;rsa\&quot;, \&quot;ed25519\&quot;, and \&quot;ecdsa\&quot;. |  [optional] |
|**publicKeyValue** | **String** | This field contains the actual public key. |  [optional] |



