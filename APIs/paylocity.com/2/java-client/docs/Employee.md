

# Employee

The employee model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalDirectDeposit** | [**List&lt;DirectDepositAdditionalDirectDepositInner&gt;**](DirectDepositAdditionalDirectDepositInner.md) | Add up to 19 direct deposit accounts in addition to the main direct deposit account. IMPORTANT: A direct deposit update will remove ALL existing main and additional direct deposit information in WebPay and replace with information provided on the request. GET API will not return direct deposit data. |  [optional] |
|**additionalRate** | [**List&lt;EmployeeAdditionalRateInner&gt;**](EmployeeAdditionalRateInner.md) | Add Additional Rates. |  [optional] |
|**benefitSetup** | [**EmployeeBenefitSetup**](EmployeeBenefitSetup.md) |  |  [optional] |
|**birthDate** | **String** | Employee birthdate. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. |  [optional] |
|**coEmpCode** | **String** | Unique idenifier for SSO.&lt;br  /&gt;Max length: 20 |  [optional] |
|**companyFEIN** | **String** | Company FEIN as defined in Web Pay, applicable with GET requests only.&lt;br  /&gt; Max length: 20 |  [optional] |
|**companyName** | **String** | Company name as defined in Web Pay, applicable with GET requests only.&lt;br  /&gt; Max length: 50 |  [optional] |
|**currency** | **String** | Employee is paid in this currency. &lt;br  /&gt;Max length: 30 |  [optional] |
|**customBooleanFields** | [**List&lt;EmployeeCustomBooleanFieldsInner&gt;**](EmployeeCustomBooleanFieldsInner.md) | Up to 8 custom fields of boolean (checkbox) type value. |  [optional] |
|**customDateFields** | [**List&lt;EmployeeCustomDateFieldsInner&gt;**](EmployeeCustomDateFieldsInner.md) | Up to 8 custom fields of the date type value. |  [optional] |
|**customDropDownFields** | [**List&lt;EmployeeCustomDropDownFieldsInner&gt;**](EmployeeCustomDropDownFieldsInner.md) | Up to 8 custom fields of the dropdown type value. |  [optional] |
|**customNumberFields** | [**List&lt;EmployeeCustomNumberFieldsInner&gt;**](EmployeeCustomNumberFieldsInner.md) | Up to 8 custom fields of numeric type value. |  [optional] |
|**customTextFields** | [**List&lt;EmployeeCustomTextFieldsInner&gt;**](EmployeeCustomTextFieldsInner.md) | Up to 8 custom fields of text type value. |  [optional] |
|**departmentPosition** | [**EmployeeDepartmentPosition**](EmployeeDepartmentPosition.md) |  |  [optional] |
|**disabilityDescription** | **String** | Indicates if employee has disability status. |  [optional] |
|**emergencyContacts** | [**List&lt;EmployeeEmergencyContactsInner&gt;**](EmployeeEmergencyContactsInner.md) | Add or update Emergency Contacts. |  [optional] |
|**employeeId** | **String** | Leave blank to have Web Pay automatically assign the next available employee ID.&lt;br  /&gt;Max length: 9 |  [optional] |
|**ethnicity** | **String** | Employee ethnicity.&lt;br  /&gt; Max length: 10 |  [optional] |
|**federalTax** | [**EmployeeFederalTax**](EmployeeFederalTax.md) |  |  [optional] |
|**firstName** | **String** | Employee first name. &lt;br  /&gt;Max length: 40 |  [optional] |
|**gender** | **String** | Employee gender. Common values *M* (Male), *F* (Female). &lt;br  /&gt;Max length: 1 |  [optional] |
|**homeAddress** | [**EmployeeHomeAddress**](EmployeeHomeAddress.md) |  |  [optional] |
|**isHighlyCompensated** | **Boolean** | Indicates if employee meets the highly compensated employee criteria. |  [optional] |
|**isSmoker** | **Boolean** | Indicates if employee is a smoker. |  [optional] |
|**lastName** | **String** | Employee last name. &lt;br  /&gt;Max length: 40 |  [optional] |
|**localTax** | [**List&lt;EmployeeLocalTaxInner&gt;**](EmployeeLocalTaxInner.md) | Add, update, or delete local tax code, filing status, and exemptions including  PA-PSD taxes. |  [optional] |
|**mainDirectDeposit** | [**EmployeeMainDirectDeposit**](EmployeeMainDirectDeposit.md) |  |  [optional] |
|**maritalStatus** | **String** | Employee marital status. Common values *D (Divorced), M (Married), S (Single), W (Widowed)*. &lt;br  /&gt;Max length: 10 |  [optional] |
|**middleName** | **String** | Employee middle name.&lt;br  /&gt; Max length: 20 |  [optional] |
|**nonPrimaryStateTax** | [**EmployeeNonPrimaryStateTax**](EmployeeNonPrimaryStateTax.md) |  |  [optional] |
|**ownerPercent** | **BigDecimal** | Percentage of employee&#39;s ownership in the company, entered as a whole number. &lt;br  /&gt; Decimal (12,2) |  [optional] |
|**preferredName** | **String** | Employee preferred display name.&lt;br  /&gt; Max length: 20 |  [optional] |
|**primaryPayRate** | [**EmployeePrimaryPayRate**](EmployeePrimaryPayRate.md) |  |  [optional] |
|**primaryStateTax** | [**EmployeePrimaryStateTax**](EmployeePrimaryStateTax.md) |  |  [optional] |
|**priorLastName** | **String** | Prior last name if applicable.&lt;br  /&gt;Max length: 40 |  [optional] |
|**salutation** | **String** | Employee preferred salutation. &lt;br  /&gt;Max length: 10 |  [optional] |
|**ssn** | **String** | Employee social security number. Leave it blank if valid social security number not available. &lt;br  /&gt;Max length: 11 |  [optional] |
|**status** | [**EmployeeStatus**](EmployeeStatus.md) |  |  [optional] |
|**suffix** | **String** | Employee name suffix. Common values are *Jr, Sr, II*.&lt;br  /&gt;Max length: 30 |  [optional] |
|**taxSetup** | [**EmployeeTaxSetup**](EmployeeTaxSetup.md) |  |  [optional] |
|**veteranDescription** | **String** | Indicates if employee is a veteran. |  [optional] |
|**webTime** | [**EmployeeWebTime**](EmployeeWebTime.md) |  |  [optional] |
|**workAddress** | [**EmployeeWorkAddress**](EmployeeWorkAddress.md) |  |  [optional] |
|**workEligibility** | [**EmployeeWorkEligibility**](EmployeeWorkEligibility.md) |  |  [optional] |



