

# CertificateExtensionConstraints

Describes a set of X.509 extensions that may be part of some certificate issuance controls.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalExtensions** | [**List&lt;ObjectId&gt;**](ObjectId.md) | Optional. A set of ObjectIds identifying custom X.509 extensions. Will be combined with known_extensions to determine the full set of X.509 extensions. |  [optional] |
|**knownExtensions** | [**List&lt;KnownExtensionsEnum&gt;**](#List&lt;KnownExtensionsEnum&gt;) | Optional. A set of named X.509 extensions. Will be combined with additional_extensions to determine the full set of X.509 extensions. |  [optional] |



## Enum: List&lt;KnownExtensionsEnum&gt;

| Name | Value |
|---- | -----|
| KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED | &quot;KNOWN_CERTIFICATE_EXTENSION_UNSPECIFIED&quot; |
| BASE_KEY_USAGE | &quot;BASE_KEY_USAGE&quot; |
| EXTENDED_KEY_USAGE | &quot;EXTENDED_KEY_USAGE&quot; |
| CA_OPTIONS | &quot;CA_OPTIONS&quot; |
| POLICY_IDS | &quot;POLICY_IDS&quot; |
| AIA_OCSP_SERVERS | &quot;AIA_OCSP_SERVERS&quot; |
| NAME_CONSTRAINTS | &quot;NAME_CONSTRAINTS&quot; |



