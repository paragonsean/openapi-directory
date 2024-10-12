

# Document

Increase generates certain documents / forms automatically for your application; they can be listed here. Currently the only supported document type is IRS Form 1099-INT.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | The type of document. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time at which the Document was created. |  |
|**entityId** | **String** | The identifier of the Entity the document was generated for. |  |
|**fileId** | **String** | The identifier of the File containing the Document&#39;s contents. |  |
|**id** | **String** | The Document identifier. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;document&#x60;. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| ACCOUNT_OPENING_DISCLOSURES | &quot;account_opening_disclosures&quot; |
| ANTI_MONEY_LAUNDERING_POLICY | &quot;anti_money_laundering_policy&quot; |
| ANTI_MONEY_LAUNDERING_PROCEDURES | &quot;anti_money_laundering_procedures&quot; |
| AUDIT_REPORT | &quot;audit_report&quot; |
| BACKGROUND_CHECKS | &quot;background_checks&quot; |
| BUSINESS_CONTINUITY_PLAN | &quot;business_continuity_plan&quot; |
| COLLECTIONS_POLICY | &quot;collections_policy&quot; |
| COMPLAINTS_POLICY | &quot;complaints_policy&quot; |
| COMPLAINT_REPORT | &quot;complaint_report&quot; |
| COMPLIANCE_REPORT | &quot;compliance_report&quot; |
| COMPLIANCE_STAFFING_PLAN | &quot;compliance_staffing_plan&quot; |
| COMPLIANCE_MANAGEMENT_SYSTEM_POLICY | &quot;compliance_management_system_policy&quot; |
| CONSUMER_PRIVACY_NOTICE | &quot;consumer_privacy_notice&quot; |
| CONSUMER_PROTECTION_POLICY | &quot;consumer_protection_policy&quot; |
| CORPORATE_FORMATION_DOCUMENT | &quot;corporate_formation_document&quot; |
| CREDIT_MONITORING_REPORT | &quot;credit_monitoring_report&quot; |
| CUSTOMER_INFORMATION_PROGRAM_POLICY | &quot;customer_information_program_policy&quot; |
| ELECTRONIC_FUNDS_TRANFER_ACT_POLICY | &quot;electronic_funds_tranfer_act_policy&quot; |
| EMPLOYEE_OVERVIEW | &quot;employee_overview&quot; |
| END_USER_TERMS_OF_SERVICE | &quot;end_user_terms_of_service&quot; |
| E_SIGN_POLICY | &quot;e_sign_policy&quot; |
| FINANCIAL_STATEMENT | &quot;financial_statement&quot; |
| FORM_1099_INT | &quot;form_1099_int&quot; |
| FRAUD_PREVENTION_POLICY | &quot;fraud_prevention_policy&quot; |
| FUNDS_AVAILABILITY_POLICY | &quot;funds_availability_policy&quot; |
| FUNDS_AVAILABILITY_DISCLOSURE | &quot;funds_availability_disclosure&quot; |
| FUNDS_FLOW_DIAGRAM | &quot;funds_flow_diagram&quot; |
| GRAMM_LEACH_BLILEY_ACT_POLICY | &quot;gramm_leach_bliley_act_policy&quot; |
| INFORMATION_SECURITY_POLICY | &quot;information_security_policy&quot; |
| INSURANCE_POLICY | &quot;insurance_policy&quot; |
| INVESTOR_PRESENTATION | &quot;investor_presentation&quot; |
| LOAN_APPLICATION_PROCESSING_POLICY | &quot;loan_application_processing_policy&quot; |
| MANAGEMENT_BIOGRAPHY | &quot;management_biography&quot; |
| MARKETING_AND_ADVERTISING_POLICY | &quot;marketing_and_advertising_policy&quot; |
| NETWORK_SECURITY_DIAGRAM | &quot;network_security_diagram&quot; |
| ONBOARDING_QUESTIONNAIRE | &quot;onboarding_questionnaire&quot; |
| PENETRATION_TEST_REPORT | &quot;penetration_test_report&quot; |
| PROGRAM_RISK_ASSESSMENT | &quot;program_risk_assessment&quot; |
| SECURITY_AUDIT_REPORT | &quot;security_audit_report&quot; |
| SERVICING_POLICY | &quot;servicing_policy&quot; |
| TRANSACTION_MONITORING_REPORT | &quot;transaction_monitoring_report&quot; |
| TRUTH_IN_SAVINGS_ACT_POLICY | &quot;truth_in_savings_act_policy&quot; |
| UNDERWRITING_POLICY | &quot;underwriting_policy&quot; |
| VENDOR_LIST | &quot;vendor_list&quot; |
| VENDOR_MANAGEMENT_POLICY | &quot;vendor_management_policy&quot; |
| VENDOR_RISK_MANAGEMENT_REPORT | &quot;vendor_risk_management_report&quot; |
| VOLUME_FORECAST | &quot;volume_forecast&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DOCUMENT | &quot;document&quot; |



