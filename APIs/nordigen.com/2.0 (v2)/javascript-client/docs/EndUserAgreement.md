# NordigenAccountInformationServicesApi.EndUserAgreement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **Date** | The date &amp; time at which the end user accepted the agreement. | [optional] [readonly] 
**accessScope** | **[[Object]]** | Array containing one or several values of [&#39;balances&#39;, &#39;details&#39;, &#39;transactions&#39;] | [optional] 
**accessValidForDays** | **Number** | Number of days from acceptance that the access can be used. | [optional] [default to 90]
**created** | **Date** | The date &amp; time at which the end user agreement was created. | [optional] [readonly] 
**id** | **String** | The ID of this End User Agreement, used to refer to this end user agreement in other API calls. | [optional] [readonly] 
**institutionId** | **String** | an Institution ID for this EUA | 
**maxHistoricalDays** | **Number** | Maximum number of days of transaction data to retrieve. | [optional] [default to 90]


