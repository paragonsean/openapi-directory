

# CategoryDTO

group of things (ie. customers or projects) similar in some way (ie. VIP customers)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | should this value be available on the XTRF selection lists |  [optional] |
|**_default** | **Boolean** | should this value be set by default in XTRF selection lists |  [optional] |
|**id** | **Long** | internal identifier |  [optional] |
|**name** | **String** | localised name (formatted in the current user&#39;s locale) |  [optional] |
|**preferred** | **Boolean** | should this value be available on the top of XTRF selection lists, in the Preferred section |  [optional] |
|**supportedClasses** | [**Set&lt;SupportedClassesEnum&gt;**](#Set&lt;SupportedClassesEnum&gt;) | set of types for which this category can be selected |  [optional] |



## Enum: Set&lt;SupportedClassesEnum&gt;

| Name | Value |
|---- | -----|
| PROJECT | &quot;PROJECT&quot; |
| QUOTE | &quot;QUOTE&quot; |
| QUOTE_TASK | &quot;QUOTE_TASK&quot; |
| TASK | &quot;TASK&quot; |
| PROVIDER | &quot;PROVIDER&quot; |
| CUSTOMER | &quot;CUSTOMER&quot; |
| CUSTOMER_PERSON | &quot;CUSTOMER_PERSON&quot; |
| PROVIDER_PERSON | &quot;PROVIDER_PERSON&quot; |
| FINANCIAL_REPORT | &quot;FINANCIAL_REPORT&quot; |
| REMINDER | &quot;REMINDER&quot; |
| PROVIDER_INVOICE | &quot;PROVIDER_INVOICE&quot; |
| CUSTOMER_INVOICE | &quot;CUSTOMER_INVOICE&quot; |
| PROJECT_GROUP | &quot;PROJECT_GROUP&quot; |



