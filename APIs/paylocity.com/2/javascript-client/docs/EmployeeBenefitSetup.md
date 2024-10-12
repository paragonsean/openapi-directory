# PaylocityApi.EmployeeBenefitSetup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefitClass** | **String** | Benefit Class code. Values are configured in Web Pay Company &gt; Setup &gt; Benefits &gt; Classes.&lt;br  /&gt;Max length: 30 | [optional] 
**benefitClassEffectiveDate** | **String** | Date when Benefit Class takes effect. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. | [optional] 
**benefitSalary** | **Number** | Salary used to configure benefits.&lt;br  /&gt;Decimal(12,2) | [optional] 
**benefitSalaryEffectiveDate** | **String** | Date when Benefit Salary takes effect. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. | [optional] 
**doNotApplyAdministrativePeriod** | **Boolean** | Applicable only for HR Enhanced clients and Benefit Classes with ACA Employment Type of Full Time. | [optional] 
**isMeasureAcaEligibility** | **Boolean** | Only valid for HR Enhanced clients and Benefit Classes that are ACA Employment Type of Full Time. | [optional] 


