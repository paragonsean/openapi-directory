# CertificateAuthorityApi.CertificateExtensionConstraints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalExtensions** | [**[ObjectId]**](ObjectId.md) | Optional. A set of ObjectIds identifying custom X.509 extensions. Will be combined with known_extensions to determine the full set of X.509 extensions. | [optional] 
**knownExtensions** | **[String]** | Optional. A set of named X.509 extensions. Will be combined with additional_extensions to determine the full set of X.509 extensions. | [optional] 



## Enum: [KnownExtensionsEnum]


* `KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED` (value: `"KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED"`)

* `BASE_KEY_USAGE` (value: `"BASE_KEY_USAGE"`)

* `EXTENDED_KEY_USAGE` (value: `"EXTENDED_KEY_USAGE"`)

* `CA_OPTIONS` (value: `"CA_OPTIONS"`)

* `POLICY_IDS` (value: `"POLICY_IDS"`)

* `AIA_OCSP_SERVERS` (value: `"AIA_OCSP_SERVERS"`)

* `NAME_CONSTRAINTS` (value: `"NAME_CONSTRAINTS"`)




