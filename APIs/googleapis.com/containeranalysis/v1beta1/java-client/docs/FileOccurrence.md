

# FileOccurrence

FileOccurrence represents an SPDX File Information section: https://spdx.github.io/spdx-spec/4-file-information/

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributions** | **List&lt;String&gt;** | This field provides a place for the SPDX data creator to record, at the file level, acknowledgements that may be needed to be communicated in some contexts |  [optional] |
|**comment** | **String** | This field provides a place for the SPDX file creator to record any general comments about the file |  [optional] |
|**contributors** | **List&lt;String&gt;** | This field provides a place for the SPDX file creator to record file contributors |  [optional] |
|**copyright** | **String** | Identify the copyright holder of the file, as well as any dates present |  [optional] |
|**filesLicenseInfo** | **List&lt;String&gt;** | This field contains the license information actually found in the file, if any |  [optional] |
|**id** | **String** | Uniquely identify any element in an SPDX document which may be referenced by other elements |  [optional] |
|**licenseConcluded** | [**License**](License.md) |  |  [optional] |
|**notice** | **String** | This field provides a place for the SPDX file creator to record license notices or other such related notices found in the file |  [optional] |



