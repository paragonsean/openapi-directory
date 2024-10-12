

# Detail

Identifies all appearances of this vulnerability in the package for a specific distro/location. For example: glibc in cpe:/o:debian:debian_linux:8 for versions 2.1 - 2.2

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cpeUri** | **String** | Required. The CPE URI in [cpe format](https://cpe.mitre.org/specification/) in which the vulnerability manifests. Examples include distro or storage location for vulnerable jar. |  [optional] |
|**description** | **String** | A vendor-specific description of this note. |  [optional] |
|**fixedLocation** | [**VulnerabilityLocation**](VulnerabilityLocation.md) |  |  [optional] |
|**isObsolete** | **Boolean** | Whether this detail is obsolete. Occurrences are expected not to point to obsolete details. |  [optional] |
|**maxAffectedVersion** | [**Version**](Version.md) |  |  [optional] |
|**minAffectedVersion** | [**Version**](Version.md) |  |  [optional] |
|**_package** | **String** | Required. The name of the package where the vulnerability was found. |  [optional] |
|**packageType** | **String** | The type of package; whether native or non native(ruby gems, node.js packages etc). |  [optional] |
|**severityName** | **String** | The severity (eg: distro assigned severity) for this vulnerability. |  [optional] |
|**source** | **String** | The source from which the information in this Detail was obtained. |  [optional] |
|**sourceUpdateTime** | **String** | The time this information was last changed at the source. This is an upstream timestamp from the underlying information source - e.g. Ubuntu security tracker. |  [optional] |
|**vendor** | **String** | The name of the vendor of the product. |  [optional] |



