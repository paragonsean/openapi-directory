

# DiscoverableProgramMerchantSignupInfo

Information about the merchant hosted signup flow for a program.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**signupSharedDatas** | [**List&lt;SignupSharedDatasEnum&gt;**](#List&lt;SignupSharedDatasEnum&gt;) |  User data that is sent in a POST request to the signup website URL. This information is encoded and then shared so that the merchant&#39;s website can prefill fields used to enroll the user for the discoverable program. |  [optional] |
|**signupWebsite** | [**Uri**](Uri.md) |  |  [optional] |



## Enum: List&lt;SignupSharedDatasEnum&gt;

| Name | Value |
|---- | -----|
| SHARED_DATA_TYPE_UNSPECIFIED | &quot;SHARED_DATA_TYPE_UNSPECIFIED&quot; |
| FIRST_NAME | &quot;FIRST_NAME&quot; |
| LAST_NAME | &quot;LAST_NAME&quot; |
| STREET_ADDRESS | &quot;STREET_ADDRESS&quot; |
| ADDRESS_LINE_1 | &quot;ADDRESS_LINE_1&quot; |
| ADDRESS_LINE_2 | &quot;ADDRESS_LINE_2&quot; |
| ADDRESS_LINE_3 | &quot;ADDRESS_LINE_3&quot; |
| CITY | &quot;CITY&quot; |
| STATE | &quot;STATE&quot; |
| ZIPCODE | &quot;ZIPCODE&quot; |
| COUNTRY | &quot;COUNTRY&quot; |
| EMAIL | &quot;EMAIL&quot; |
| PHONE | &quot;PHONE&quot; |



