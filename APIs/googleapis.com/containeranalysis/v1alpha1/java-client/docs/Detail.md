

# Detail

Identifies all occurrences of this vulnerability in the package for a specific distro/location For example: glibc in cpe:/o:debian:debian_linux:8 for versions 2.1 - 2.2

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cpeUri** | **String** | The cpe_uri in [cpe format] (https://cpe.mitre.org/specification/) in which the vulnerability manifests. Examples include distro or storage location for vulnerable jar. This field can be used as a filter in list requests. |  [optional] |
|**description** | **String** | A vendor-specific description of this note. |  [optional] |
|**fixedLocation** | [**VulnerabilityLocation**](VulnerabilityLocation.md) |  |  [optional] |
|**isObsolete** | **Boolean** | Whether this Detail is obsolete. Occurrences are expected not to point to obsolete details. |  [optional] |
|**maxAffectedVersion** | [**Version**](Version.md) |  |  [optional] |
|**minAffectedVersion** | [**Version**](Version.md) |  |  [optional] |
|**_package** | **String** | The name of the package where the vulnerability was found. This field can be used as a filter in list requests. |  [optional] |
|**packageType** | **String** | The type of package; whether native or non native(ruby gems, node.js packages etc) |  [optional] |
|**severityName** | **String** | The severity (eg: distro assigned severity) for this vulnerability. |  [optional] |
|**source** | **String** | The source from which the information in this Detail was obtained. |  [optional] |
|**vendor** | **String** | The vendor of the product. e.g. \&quot;google\&quot; |  [optional] |



