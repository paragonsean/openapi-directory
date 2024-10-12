

# Detail

A detail for a distro and package affected by this vulnerability and its associated fix (if one is available).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affectedCpeUri** | **String** | Required. The [CPE URI](https://cpe.mitre.org/specification/) this vulnerability affects. |  [optional] |
|**affectedPackage** | **String** | Required. The package this vulnerability affects. |  [optional] |
|**affectedVersionEnd** | [**Version**](Version.md) |  |  [optional] |
|**affectedVersionStart** | [**Version**](Version.md) |  |  [optional] |
|**description** | **String** | A vendor-specific description of this vulnerability. |  [optional] |
|**fixedCpeUri** | **String** | The distro recommended [CPE URI](https://cpe.mitre.org/specification/) to update to that contains a fix for this vulnerability. It is possible for this to be different from the affected_cpe_uri. |  [optional] |
|**fixedPackage** | **String** | The distro recommended package to update to that contains a fix for this vulnerability. It is possible for this to be different from the affected_package. |  [optional] |
|**fixedVersion** | [**Version**](Version.md) |  |  [optional] |
|**isObsolete** | **Boolean** | Whether this detail is obsolete. Occurrences are expected not to point to obsolete details. |  [optional] |
|**packageType** | **String** | The type of package; whether native or non native (e.g., ruby gems, node.js packages, etc.). |  [optional] |
|**severityName** | **String** | The distro assigned severity of this vulnerability. |  [optional] |
|**source** | **String** | The source from which the information in this Detail was obtained. |  [optional] |
|**sourceUpdateTime** | **String** | The time this information was last changed at the source. This is an upstream timestamp from the underlying information source - e.g. Ubuntu security tracker. |  [optional] |
|**vendor** | **String** | The name of the vendor of the product. |  [optional] |



