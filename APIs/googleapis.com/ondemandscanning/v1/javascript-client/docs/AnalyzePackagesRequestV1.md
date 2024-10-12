# OnDemandScanningApi.AnalyzePackagesRequestV1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includeOsvData** | **Boolean** | [DEPRECATED] Whether to include OSV data in the scan. For backwards compatibility reasons, this field can be neither removed nor renamed. | [optional] 
**packages** | [**[PackageData]**](PackageData.md) | The packages to analyze. | [optional] 
**resourceUri** | **String** | Required. The resource URI of the container image being scanned. | [optional] 


