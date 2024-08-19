# PaylocityApi.EmployeeAdditionalRateInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changeReason** | **String** | Not required. If populated, must match one of the system coded values available in the Additional Rates Change Reason drop down.&lt;br /&gt; | [optional] 
**costCenter1** | **String** | Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 1 drop down. This cell must be in a text format.&lt;br /&gt; | [optional] 
**costCenter2** | **String** | Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 2 drop down. This cell must be in a text format.&lt;br /&gt; | [optional] 
**costCenter3** | **String** | Not required. Valid values must match one of the system coded cost centers available in the Additional Rates Cost Center level 3 drop down. This cell must be in a text format.&lt;br /&gt; | [optional] 
**effectiveDate** | **String** | Required. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.&lt;br /&gt; | [optional] 
**endCheckDate** | **String** | Not required. Must match one of the system coded check dates available in the Additional Rates End Check Date drop down. Common formats include *MM-DD-CCYY*, *CCYY-MM-DD*.&lt;br /&gt; | [optional] 
**job** | **String** | Not required. If populated, must match one of the system coded values available in the Additional Rates Job drop down.&lt;br /&gt; | [optional] 
**rate** | **Number** | Required. Enter dollar amount that corresponds to the Per selection.&lt;br /&gt; | [optional] 
**rateCode** | **String** | Required. If populated, must match one of the system coded values available in the Additional Rates Rate Code drop down.&lt;br /&gt; | [optional] 
**rateNotes** | **String** | Not required.&lt;br  /&gt;Max length: 4000&lt;br /&gt; | [optional] 
**ratePer** | **String** | Required. Valid values are HOUR or WEEK.&lt;br /&gt; | [optional] 
**shift** | **String** | Not required. If populated, must match one of the system coded values available in the Additional Rates Shift drop down.&lt;br /&gt; | [optional] 


