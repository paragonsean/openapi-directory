

# ReconciliationReport

Reconciliation report (Hotel Ads only). Covers the Reconciliation Reports functionality in pre-v3.0 API versions. Lets you see the status, validate, and upload your Commissions reconciliation reports. This only applies if you are in the Google Hotel Ads Commissions Program (GHACP). For more information about working with reconciliation reports in Hotel Center, refer to [Reconciliation reports](//support.google.com/hotelprices/answer/7019060#sending).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contents** | **String** | Required. The contents of the commission report. Report contents must conform to the requirements specified in [Reconciliation reports] (//support.google.com/hotelprices/answer/7019060#creating). |  [optional] |
|**fileName** | **String** | Required. Desired filename of the reconciliation report. |  [optional] |
|**name** | **String** | Resource name in the format &#x60;accounts/{account_id}/reconciliationReports/{datetime}~{filename}&#x60;. The value for &#x60;{datetime}&#x60; must be from 0001-01-01T00:00:00 to 9999-12-31T23:59:59 inclusive. |  [optional] |



