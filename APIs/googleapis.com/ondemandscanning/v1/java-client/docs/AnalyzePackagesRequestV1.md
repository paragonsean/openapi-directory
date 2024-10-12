

# AnalyzePackagesRequestV1

AnalyzePackagesRequest is the request to analyze a list of packages and create Vulnerability Occurrences for it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includeOsvData** | **Boolean** | [DEPRECATED] Whether to include OSV data in the scan. For backwards compatibility reasons, this field can be neither removed nor renamed. |  [optional] |
|**packages** | [**List&lt;PackageData&gt;**](PackageData.md) | The packages to analyze. |  [optional] |
|**resourceUri** | **String** | Required. The resource URI of the container image being scanned. |  [optional] |



