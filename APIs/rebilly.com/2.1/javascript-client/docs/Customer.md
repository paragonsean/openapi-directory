# RebillyRestApi.Customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**[CustomerEmbeddedInner]**](CustomerEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[CustomerLinksInner]**](CustomerLinksInner.md) | The links related to resource. | [optional] [readonly] 
**averageValue** | [**CustomerAverageValue**](CustomerAverageValue.md) |  | [optional] 
**createdTime** | **Date** | The customer created time. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**defaultPaymentInstrument** | [**PaymentInstrument**](PaymentInstrument.md) |  | [optional] 
**email** | **String** | The customer&#39;s email. | [optional] [readonly] 
**firstName** | **String** | The customer&#39;s first name. | [optional] [readonly] 
**id** | **String** | The customer identifier string. | [optional] [readonly] 
**invoiceCount** | **Number** | An auto-incrementing number based on the sequence of invoices. If set to 0, then this record is a Lead, otherwise is a Customer. | [optional] [readonly] 
**lastName** | **String** | The customer&#39;s last name. | [optional] [readonly] 
**lastPaymentTime** | **Date** | The most recent time of an approved payment for the customer. | [optional] [readonly] 
**lifetimeRevenue** | [**CustomerLifetimeRevenue**](CustomerLifetimeRevenue.md) |  | [optional] 
**paymentCount** | **Number** | The number of approved payments for the customer. | [optional] [readonly] 
**paymentToken** | **String** | A write-only payment token; if supplied, it will be converted into a payment instrument and be set as the &#x60;defaultPaymentInstrument&#x60;. The value of this property will override the &#x60;defaultPaymentInstrument&#x60; in the case that both are supplied. The token may only be used once before it is expired.  | [optional] 
**primaryAddress** | [**ContactObject**](ContactObject.md) |  | [optional] 
**revision** | **Number** | The number of times the customer data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation.  | [optional] [readonly] 
**tags** | [**[Tag]**](Tag.md) | A list of customer&#39;s tags. | [optional] [readonly] 
**updatedTime** | **Date** | The customer updated time. | [optional] [readonly] 
**websiteId** | **String** | The website&#39;s ID. | [optional] 


