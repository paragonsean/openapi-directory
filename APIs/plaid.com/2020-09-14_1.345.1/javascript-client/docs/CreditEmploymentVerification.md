# ThePlaidApi.CreditEmploymentVerification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | ID of the payroll provider account. | 
**employeeType** | **String** | The type of employment for the individual. &#x60;\&quot;FULL_TIME\&quot;&#x60;: A full-time employee. &#x60;\&quot;PART_TIME\&quot;&#x60;: A part-time employee. &#x60;\&quot;CONTRACTOR\&quot;&#x60;: An employee typically hired externally through a contracting group. &#x60;\&quot;TEMPORARY\&quot;&#x60;: A temporary employee. &#x60;\&quot;OTHER\&quot;&#x60;: The employee type is not one of the above defined types. | 
**employer** | [**CreditEmployerVerification**](CreditEmployerVerification.md) |  | 
**endDate** | **Date** | End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD). | 
**lastPaystubDate** | **Date** | The date of the employee&#39;s most recent paystub in ISO 8601 format (YYYY-MM-DD). | 
**platformIds** | [**CreditPlatformIds**](CreditPlatformIds.md) |  | 
**startDate** | **Date** | Start of employment in ISO 8601 format (YYYY-MM-DD). | 
**status** | **String** | Current employment status. | 
**title** | **String** | Current title of employee. | 


