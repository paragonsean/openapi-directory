# ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingAvailabilityTourgrades200ResponseAllOfDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ageBands** | **[Object]** | **array** of age band objects describing the age bands and respective passenger counts allowed to book *this* tour grade; &#x60;null&#x60; if &#x60;ageBandsRequired&#x60; is filled and &#x60;available&#x60; is &#x60;false&#x60; | [optional] 
**ageBandsRequired** | **[[BookingAvailabilityTourgrades200ResponseAllOfDataInnerAgeBandsRequiredInnerInner]]** | **array of arrays** of age band objects describing the traveler mixes eligible to book *this* tour grade; &#x60;null&#x60; if &#x60;ageBands&#x60; is filled and &#x60;available&#x60; is &#x60;true&#x60; - **note**: multiple objects; structure will depend on available tour grades – see response sample for an example, but the exact result you receive will differ  | [optional] 
**available** | **Boolean** | **indicator** - &#x60;true&#x60; if this tour grade is available to be booked according to the traveler mix specified | [optional] 
**bookingDate** | **String** | **date** on which *this* tour grade operates | [optional] 
**currencyCode** | **String** | **currency code for the specified currency** (will be &#x60;&#39;ERROR&#39;&#x60; if &#x60;available&#x60; is &#x60;false&#x60;) | [optional] 
**defaultLanguageCode** | **String** | **language code for standard langauge** for *this* product | [optional] 
**gradeCode** | **String** | **alphanumeric identifier** of *this* tour grade | [optional] 
**gradeDepartureTime** | **String** | **time** of *this* product | [optional] 
**gradeDescription** | **String** | **natural-language description** of the tour grade | [optional] 
**gradeTitle** | **String** | **natural-language title** of the tour grade | [optional] 
**langServices** | **Object** | **object** detailing language services available for *this* product** (will be &#x60;null&#x60; if &#x60;available&#x60; is &#x60;false&#x60;) | [optional] 
**merchantNetPrice** | **Number** | **numeric merchant net rate** for *this* tour grade **Note**: will be &#x60;0&#x60; if &#x60;available&#x60; is &#x60;false&#x60; - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  | [optional] 
**merchantNetPriceFormatted** | **String** | **currency-formatted merchant net rate** for *this* tour grade **Note**: will be empty if &#x60;available&#x60; is &#x60;false&#x60; - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  | [optional] 
**retailPrice** | **Number** | **numeric suggested retail price** for *this* tour grade **Note**: will be &#x60;0&#x60; if &#x60;available&#x60; is &#x60;false&#x60; - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  | [optional] 
**retailPriceFormatted** | **String** | **currency-formatted suggested retail price** for *this* tour grade **Note**: (will be &#39;&#39; if &#x60;available&#x60; is &#x60;false&#x60;) - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  | [optional] 
**sortOrder** | **Number** | **sort order** for *this* tour grade availability object | [optional] 
**unavailableReason** | **String** | **enum specifier of reason for product unavailability** (will be &#x60;null&#x60; if &#x60;available&#x60; is &#x60;true&#x60;) | [optional] 


