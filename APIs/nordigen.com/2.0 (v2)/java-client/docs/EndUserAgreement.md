

# EndUserAgreement

Represents an end-user agreement.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accepted** | **OffsetDateTime** | The date &amp; time at which the end user accepted the agreement. |  [optional] [readonly] |
|**accessScope** | **List&lt;List&lt;Object&gt;&gt;** | Array containing one or several values of [&#39;balances&#39;, &#39;details&#39;, &#39;transactions&#39;] |  [optional] |
|**accessValidForDays** | **Integer** | Number of days from acceptance that the access can be used. |  [optional] |
|**created** | **OffsetDateTime** | The date &amp; time at which the end user agreement was created. |  [optional] [readonly] |
|**id** | **UUID** | The ID of this End User Agreement, used to refer to this end user agreement in other API calls. |  [optional] [readonly] |
|**institutionId** | **String** | an Institution ID for this EUA |  |
|**maxHistoricalDays** | **Integer** | Maximum number of days of transaction data to retrieve. |  [optional] |



