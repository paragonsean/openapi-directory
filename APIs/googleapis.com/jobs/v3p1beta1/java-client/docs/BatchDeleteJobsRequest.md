

# BatchDeleteJobsRequest

Input only. Batch delete jobs request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filter** | **String** | Required. The filter string specifies the jobs to be deleted. Supported operator: &#x3D;, AND The fields eligible for filtering are: * &#x60;companyName&#x60; (Required) * &#x60;requisitionId&#x60; (Required) Sample Query: companyName &#x3D; \&quot;projects/api-test-project/companies/123\&quot; AND requisitionId &#x3D; \&quot;req-1\&quot; |  [optional] |



