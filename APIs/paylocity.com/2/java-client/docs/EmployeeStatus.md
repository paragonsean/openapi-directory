

# EmployeeStatus

Add or update employee status, change reason, effective date, and adjusted seniority date. Note that companies that are still in Implementation cannot hire future employees.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustedSeniorityDate** | **String** | Adjusted seniority date. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. |  [optional] |
|**changeReason** | **String** | Employee status change reason. Must match Company setup.&lt;br  /&gt; Max length: 15 |  [optional] |
|**effectiveDate** | **String** | Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. |  [optional] |
|**employeeStatus** | **String** | Employee current work status. Common values are *A* (Active), *L* (Leave of Absence), *T* (Terminated). &lt;br  /&gt;Max length: 20 |  [optional] |
|**hireDate** | **String** | Employee hired date. Updates to hire date are not allowed and will be ignored. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. |  [optional] |
|**isEligibleForRehire** | **Boolean** | Indicates if employee eligible for rehire. |  [optional] |
|**reHireDate** | **String** | Rehire date if employee is rehired.  Updates to re-hire date are not allowed and will be ignored. Common formats are *MM-DD-CCYY, CCYY-MM-DD*. |  [optional] |
|**statusType** | **String** | The Status Type associated with the Employee Status code. Each Employee Status  code for a company is assigned to one of the Status Type values of  A (Active), L (Leave of Absence), T (Terminated). |  [optional] |
|**terminationDate** | **String** | Employee termination date. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. |  [optional] |



