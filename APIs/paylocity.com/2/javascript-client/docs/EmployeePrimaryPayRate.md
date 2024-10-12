# PaylocityApi.EmployeePrimaryPayRate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annualSalary** | **Number** | Employee annual salary.&lt;br /&gt;Decimal (12,6) | [optional] 
**baseRate** | **Number** | Employee base rate, used for Hourly employees. &lt;br  /&gt;Decimal (12,6) | [optional] 
**beginCheckDate** | **String** | The date of the first check on which the new pay rate will appear. This value is only applicable when updating an existing employee. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. | [optional] 
**changeReason** | **String** | Pay rate change reason.&lt;br  /&gt; Max length: 30 | [optional] 
**defaultHours** | **Number** | Employee default hours consistently worked. If autoPayType is set to D, employee will be paid hourly base rate for the defaultHours. &lt;br  /&gt;Decimal (12,2) | [optional] 
**effectiveDate** | **String** | The date the employee&#39;s pay rate takes effect. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. | [optional] 
**isAutoPay** | **Boolean** | If set to *True*, employee will be paid automatically using deafultHours. | [optional] 
**payFrequency** | **String** | Employee current pay frequency. Common values are *A (Annual), B (Bi-Weekly), D (Daily), M (Monthly), S (Semi-Monthly), Q (Quarterly), W (Weekly)*. &lt;br  /&gt;Max length: 5 | [optional] 
**payGrade** | **String** | Employee pay grade. Must match Company setup. &lt;br  /&gt; Max length: 10 | [optional] 
**payRateNote** | **String** | Pay rate notes regarding employee.&lt;br  /&gt; Max length: 250 | [optional] 
**payType** | **String** | Employee pay type (rate code). Valid values are *Hourly* or *Salary*. &lt;br  /&gt;Max length: 10 | [optional] 
**ratePer** | **String** | Employee base rate frequency used with payType Hourly. Common values are *Hour, Week*. Default is Hour. &lt;br  /&gt;Max length: 10 | [optional] 
**salary** | **Number** | Employee gross salary per pay period used with payType Salary.&lt;br  /&gt;Decimal (12,6) | [optional] 


