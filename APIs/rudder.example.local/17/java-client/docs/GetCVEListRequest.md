

# GetCVEListRequest

List of CVE ids you want

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cveIds** | **List&lt;String&gt;** |  |  [optional] |
|**maxScore** | **String** | Only send CVE with a score lower than the value |  [optional] |
|**minScore** | **String** | Only send CVE with a score higher than the value |  [optional] |
|**onlyScore** | **Boolean** | Only send score of the cve, and not the whole detailed list |  [optional] |
|**publishedDate** | **LocalDate** | Only send CVE with a publication date more recent than the value |  [optional] |



