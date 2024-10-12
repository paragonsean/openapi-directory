# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesCustomerClient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedLabels** | **[String]** | Output only. The resource names of the labels owned by the requesting customer that are applied to the client customer. Label resource names have the form: &#x60;customers/{customer_id}/labels/{label_id}&#x60; | [optional] [readonly] 
**clientCustomer** | **String** | Output only. The resource name of the client-customer which is linked to the given customer. Read only. | [optional] [readonly] 
**currencyCode** | **String** | Output only. Currency code (for example, &#39;USD&#39;, &#39;EUR&#39;) for the client. Read only. | [optional] [readonly] 
**descriptiveName** | **String** | Output only. Descriptive name for the client. Read only. | [optional] [readonly] 
**hidden** | **Boolean** | Output only. Specifies whether this is a hidden account. Read only. | [optional] [readonly] 
**id** | **String** | Output only. The ID of the client customer. Read only. | [optional] [readonly] 
**level** | **String** | Output only. Distance between given customer and client. For self link, the level value will be 0. Read only. | [optional] [readonly] 
**manager** | **Boolean** | Output only. Identifies if the client is a manager. Read only. | [optional] [readonly] 
**resourceName** | **String** | Output only. The resource name of the customer client. CustomerClient resource names have the form: &#x60;customers/{customer_id}/customerClients/{client_customer_id}&#x60; | [optional] [readonly] 
**status** | **String** | Output only. The status of the client customer. Read only. | [optional] [readonly] 
**testAccount** | **Boolean** | Output only. Identifies if the client is a test account. Read only. | [optional] [readonly] 
**timeZone** | **String** | Output only. Common Locale Data Repository (CLDR) string representation of the time zone of the client, for example, America/Los_Angeles. Read only. | [optional] [readonly] 



## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `CANCELED` (value: `"CANCELED"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `CLOSED` (value: `"CLOSED"`)




