

# StagedEmployeeWorkEligibilityInner

The Work Eligibility model

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alienOrAdmissionDocumentNumber** | **String** | Employee USCIS or Admission Number. &lt;br  /&gt; Must be 7-10 characters and may begin with an &#39;A&#39; |  [optional] |
|**attestedDate** | **String** | The date the I-9 Verification form was attested by Employer or Authorized representative. Common formats are *MM-DD-CCYY, CCYY-MM-DD*. |  [optional] |
|**countryOfIssuance** | **String** | If Foreign Passport number is provided, provide its country of issuance. Must match Paylocity setup.&lt;br  /&gt; Max length: 30 |  [optional] |
|**foreignPassportNumber** | **String** | Foreign Passport Number.&lt;br  /&gt; Max length: 50 |  [optional] |
|**i94AdmissionNumber** | **String** | Form I-94 admission number.&lt;br  /&gt; Must be 11 numeric characters |  [optional] |
|**i9DateVerified** | **String** | Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. |  [optional] |
|**i9Notes** | **String** | Notes regarding employee&#39;s i9.&lt;br  /&gt; Max length: 4000 |  [optional] |
|**isI9Verified** | **Boolean** | Indicates if employee I9 is verified. |  [optional] |
|**isSsnVerified** | **Boolean** | Indicates if employee SSN is verified. |  [optional] |
|**ssnDateVerified** | **String** | The date of employer verification of employee SSN. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. |  [optional] |
|**ssnNotes** | **String** | Notes regarding employee&#39;s SSN.&lt;br  /&gt; Max length: 4000 |  [optional] |
|**visaType** | **String** | Employee Visa type. Must match one of the system coded values.&lt;br  /&gt; Max length: 100 |  [optional] |
|**workAuthorization** | **String** | Employee work authorization. Must match one of the system coded values.&lt;br  /&gt; Max length: 100 |  [optional] |
|**workUntil** | **String** | End date of employee work eligibility.  Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*. |  [optional] |



