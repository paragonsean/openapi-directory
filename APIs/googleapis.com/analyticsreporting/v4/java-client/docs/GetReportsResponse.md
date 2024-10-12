

# GetReportsResponse

The main response class which holds the reports from the Reporting API `batchGet` call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**queryCost** | **Integer** | The amount of resource quota tokens deducted to execute the query. Includes all responses. |  [optional] |
|**reports** | [**List&lt;Report&gt;**](Report.md) | Responses corresponding to each of the request. |  [optional] |
|**resourceQuotasRemaining** | [**ResourceQuotasRemaining**](ResourceQuotasRemaining.md) |  |  [optional] |



