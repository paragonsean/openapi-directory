# OnDemandScanningApi.PackageIssue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affectedCpeUri** | **String** | Required. The [CPE URI](https://cpe.mitre.org/specification/) this vulnerability was found in. | [optional] 
**affectedPackage** | **String** | Required. The package this vulnerability was found in. | [optional] 
**affectedVersion** | [**Version**](Version.md) |  | [optional] 
**effectiveSeverity** | **String** | Output only. The distro or language system assigned severity for this vulnerability when that is available and note provider assigned severity when it is not available. | [optional] [readonly] 
**fileLocation** | [**[GrafeasV1FileLocation]**](GrafeasV1FileLocation.md) | The location at which this package was found. | [optional] 
**fixAvailable** | **Boolean** | Output only. Whether a fix is available for this package. | [optional] 
**fixedCpeUri** | **String** | The [CPE URI](https://cpe.mitre.org/specification/) this vulnerability was fixed in. It is possible for this to be different from the affected_cpe_uri. | [optional] 
**fixedPackage** | **String** | The package this vulnerability was fixed in. It is possible for this to be different from the affected_package. | [optional] 
**fixedVersion** | [**Version**](Version.md) |  | [optional] 
**packageType** | **String** | The type of package (e.g. OS, MAVEN, GO). | [optional] 



## Enum: EffectiveSeverityEnum


* `SEVERITY_UNSPECIFIED` (value: `"SEVERITY_UNSPECIFIED"`)

* `MINIMAL` (value: `"MINIMAL"`)

* `LOW` (value: `"LOW"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `HIGH` (value: `"HIGH"`)

* `CRITICAL` (value: `"CRITICAL"`)




