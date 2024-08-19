

# StagedEmployee

The staged employee model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalDirectDeposit** | [**List&lt;StagedEmployeeAdditionalDirectDepositInner&gt;**](StagedEmployeeAdditionalDirectDepositInner.md) | Add up to 19 direct deposit accounts in addition to the main direct deposit account. IMPORTANT: A direct deposit update will remove ALL existing main and additional direct deposit information in WebPay and replace with information provided on the request. GET API will not return direct deposit data. |  [optional] |
|**benefitSetup** | [**List&lt;StagedEmployeeBenefitSetupInner&gt;**](StagedEmployeeBenefitSetupInner.md) | Add setup values used for employee benefits integration, insurance plan settings, and ACA reporting. |  [optional] |
|**birthDate** | **String** | Employee birthdate. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. |  [optional] |
|**customBooleanFields** | [**List&lt;EmployeeCustomBooleanFieldsInner&gt;**](EmployeeCustomBooleanFieldsInner.md) | Up to 8 custom fields of boolean (checkbox) type value. |  [optional] |
|**customDateFields** | [**List&lt;EmployeeCustomDateFieldsInner&gt;**](EmployeeCustomDateFieldsInner.md) | Up to 8 custom fields of the date type value. |  [optional] |
|**customDropDownFields** | [**List&lt;EmployeeCustomDropDownFieldsInner&gt;**](EmployeeCustomDropDownFieldsInner.md) | Up to 8 custom fields of the dropdown type value. |  [optional] |
|**customNumberFields** | [**List&lt;EmployeeCustomNumberFieldsInner&gt;**](EmployeeCustomNumberFieldsInner.md) | Up to 8 custom fields of numeric type value. |  [optional] |
|**customTextFields** | [**List&lt;EmployeeCustomTextFieldsInner&gt;**](EmployeeCustomTextFieldsInner.md) | Up to 8 custom fields of text type value. |  [optional] |
|**departmentPosition** | [**List&lt;StagedEmployeeDepartmentPositionInner&gt;**](StagedEmployeeDepartmentPositionInner.md) | Add home department cost center, position, supervisor, reviewer, employment type, EEO class, pay settings, and union information. |  [optional] |
|**disabilityDescription** | **String** | Indicates if employee has disability status. |  [optional] |
|**employeeId** | **String** | Leave blank to have Web Pay automatically assign the next available employee ID.&lt;br  /&gt; Max length: 10 |  [optional] |
|**ethnicity** | **String** | Employee ethnicity.&lt;br  /&gt; Max length: 10 |  [optional] |
|**federalTax** | [**List&lt;StagedEmployeeFederalTaxInner&gt;**](StagedEmployeeFederalTaxInner.md) | Add federal tax amount type (taxCalculationCode), amount or percentage, filing status, and exemptions. |  [optional] |
|**firstName** | **String** | Employee first name. &lt;br  /&gt;Max length: 40 |  [optional] |
|**fitwExemptReason** | **String** | Reason code for FITW exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). &lt;br  /&gt; Max length: 30 |  [optional] |
|**futaExemptReason** | **String** | Reason code for FUTA exemption. Common values are *501* (5019c)(3) Organization), *IC* (Independent Contractor).&lt;br  /&gt; Max length: 30 |  [optional] |
|**gender** | **String** | Employee gender. Common values *M* (Male), *F* (Female). &lt;br  /&gt;Max length: 1 |  [optional] |
|**homeAddress** | [**List&lt;StagedEmployeeHomeAddressInner&gt;**](StagedEmployeeHomeAddressInner.md) | Add employee&#39;s home address, personal phone numbers, and personal email. |  [optional] |
|**isEmployee943** | **Boolean** | Indicates if employee in agriculture or farming. |  [optional] |
|**isSmoker** | **Boolean** | Indicates if employee is a smoker. |  [optional] |
|**lastName** | **String** | Employee last name. &lt;br  /&gt;Max length: 40 |  [optional] |
|**localTax** | [**List&lt;EmployeeLocalTaxInner&gt;**](EmployeeLocalTaxInner.md) | Add local tax code, filing status, and exemptions including PA-PSD taxes. |  [optional] |
|**mainDirectDeposit** | [**List&lt;StagedEmployeeMainDirectDepositInner&gt;**](StagedEmployeeMainDirectDepositInner.md) | Add the main direct deposit account. After deposits are made to any additional direct deposit accounts, the remaining net check is deposited in the main direct deposit account. IMPORTANT: A direct deposit update will remove ALL existing main and additional direct deposit information in WebPay and replace with what is provided on the request. GET API will not return direct deposit data. |  [optional] |
|**maritalStatus** | **String** | Employee marital status. Common values *D (Divorced), M (Married), S (Single), W (Widowed)*. &lt;br  /&gt;Max length: 10 |  [optional] |
|**medExemptReason** | **String** | Reason code for Medicare exemption. Common values are *501* (5019c)(3) Organization), *IC* (Independent Contractor).&lt;br  /&gt; Max length: 30 |  [optional] |
|**middleName** | **String** | Employee middle name.&lt;br  /&gt; Max length: 20 |  [optional] |
|**nonPrimaryStateTax** | [**List&lt;StagedEmployeeNonPrimaryStateTaxInner&gt;**](StagedEmployeeNonPrimaryStateTaxInner.md) | Add non-primary state tax code, amount type (taxCalculationCode), amount or percentage, filing status, exemptions, supplemental check (specialCheckCalc), and reciprocity code information. |  [optional] |
|**preferredName** | **String** | Employee preferred display name.&lt;br  /&gt; Max length: 20 |  [optional] |
|**primaryPayRate** | [**List&lt;StagedEmployeePrimaryPayRateInner&gt;**](StagedEmployeePrimaryPayRateInner.md) | Add hourly or salary pay rate, effective date, and pay frequency. |  [optional] |
|**primaryStateTax** | [**List&lt;StagedEmployeePrimaryStateTaxInner&gt;**](StagedEmployeePrimaryStateTaxInner.md) | Add primary state tax code, amount type (taxCalculationCode), amount or percentage, filing status, exemptions, and supplemental check (specialCheckCalc) information. Only one primary state is allowed. |  [optional] |
|**priorLastName** | **String** | Prior last name if applicable.&lt;br  /&gt;Max length: 40 |  [optional] |
|**salutation** | **String** | Employee preferred salutation. &lt;br  /&gt;Max length: 10 |  [optional] |
|**sitwExemptReason** | **String** | Reason code for SITW exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). &lt;br  /&gt; Max length: 30 |  [optional] |
|**ssExemptReason** | **String** | Reason code for Social Security exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). &lt;br  /&gt; Max length: 30 |  [optional] |
|**ssn** | **String** | Employee social security number. Leave it blank if valid social security number not available. &lt;br  /&gt;Max length: 11 |  [optional] |
|**status** | [**List&lt;StagedEmployeeStatusInner&gt;**](StagedEmployeeStatusInner.md) | Add employee status, change reason, effective date, and adjusted seniority date. Note that companies that are still in Implementation cannot hire future employees. |  [optional] |
|**suffix** | **String** | Employee name suffix. Common values are *Jr, Sr, II*.&lt;br  /&gt;Max length: 30 |  [optional] |
|**suiExemptReason** | **String** | Reason code for SUI exemption. Common values are *SE* (Statutory employee), *CR* (clergy/Religious). &lt;br  /&gt; Max length: 30 |  [optional] |
|**suiState** | **String** | Employee SUI (State Unemployment Insurance) state. &lt;br  /&gt;Max length: 2 |  [optional] |
|**taxDistributionCode1099R** | **String** | Employee 1099R distribution code. Common values are *7* (Normal Distribution), *F* (Charitable Gift Annuity). &lt;br  /&gt;Max length: 1 |  [optional] |
|**taxForm** | **String** | Employee tax form for reporting income. Valid values are *W2, 1099M, 1099R*. Default is W2. &lt;br  /&gt;Max length: 15 |  [optional] |
|**veteranDescription** | **String** | Indicates if employee is a veteran. |  [optional] |
|**webTime** | [**StagedEmployeeWebTime**](StagedEmployeeWebTime.md) |  |  [optional] |
|**workAddress** | [**List&lt;StagedEmployeeWorkAddressInner&gt;**](StagedEmployeeWorkAddressInner.md) | Add employee&#39;s work address, phone numbers, and email. Work Location drop down field is not included. |  [optional] |
|**workEligibility** | [**List&lt;StagedEmployeeWorkEligibilityInner&gt;**](StagedEmployeeWorkEligibilityInner.md) | Add I-9 work authorization information. |  [optional] |



