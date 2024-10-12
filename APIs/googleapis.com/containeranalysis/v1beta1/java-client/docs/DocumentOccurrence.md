

# DocumentOccurrence

DocumentOccurrence represents an SPDX Document Creation Information section: https://spdx.github.io/spdx-spec/2-document-creation-information/

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Identify when the SPDX file was originally created. The date is to be specified according to combined date and time in UTC format as specified in ISO 8601 standard |  [optional] |
|**creatorComment** | **String** | A field for creators of the SPDX file to provide general comments about the creation of the SPDX file or any other relevant comment not included in the other fields |  [optional] |
|**creators** | **List&lt;String&gt;** | Identify who (or what, in the case of a tool) created the SPDX file. If the SPDX file was created by an individual, indicate the person&#39;s name |  [optional] |
|**documentComment** | **String** | A field for creators of the SPDX file content to provide comments to the consumers of the SPDX document |  [optional] |
|**externalDocumentRefs** | **List&lt;String&gt;** | Identify any external SPDX documents referenced within this SPDX document |  [optional] |
|**id** | **String** | Identify the current SPDX document which may be referenced in relationships by other files, packages internally and documents externally |  [optional] |
|**licenseListVersion** | **String** | A field for creators of the SPDX file to provide the version of the SPDX License List used when the SPDX file was created |  [optional] |
|**namespace** | **String** | Provide an SPDX document specific namespace as a unique absolute Uniform Resource Identifier (URI) as specified in RFC-3986, with the exception of the ‘#’ delimiter |  [optional] |
|**title** | **String** | Identify name of this document as designated by creator |  [optional] |



