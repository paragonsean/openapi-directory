# ContentApiForShopping.HolidaysHoliday

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countryCode** | **String** | The CLDR territory code of the country in which the holiday is available. E.g. \&quot;US\&quot;, \&quot;DE\&quot;, \&quot;GB\&quot;. A holiday cutoff can only be configured in a shipping settings service with matching delivery country. Always present. | [optional] 
**date** | **String** | Date of the holiday, in ISO 8601 format. E.g. \&quot;2016-12-25\&quot; for Christmas 2016. Always present. | [optional] 
**deliveryGuaranteeDate** | **String** | Date on which the order has to arrive at the customer&#39;s, in ISO 8601 format. E.g. \&quot;2016-12-24\&quot; for 24th December 2016. Always present. | [optional] 
**deliveryGuaranteeHour** | **String** | Hour of the day in the delivery location&#39;s timezone on the guaranteed delivery date by which the order has to arrive at the customer&#39;s. Possible values are: 0 (midnight), 1, ..., 12 (noon), 13, ..., 23. Always present. | [optional] 
**id** | **String** | Unique identifier for the holiday to be used when configuring holiday cutoffs. Always present. | [optional] 
**type** | **String** | The holiday type. Always present. Acceptable values are: - \&quot;&#x60;Christmas&#x60;\&quot; - \&quot;&#x60;Easter&#x60;\&quot; - \&quot;&#x60;Father&#39;s Day&#x60;\&quot; - \&quot;&#x60;Halloween&#x60;\&quot; - \&quot;&#x60;Independence Day (USA)&#x60;\&quot; - \&quot;&#x60;Mother&#39;s Day&#x60;\&quot; - \&quot;&#x60;Thanksgiving&#x60;\&quot; - \&quot;&#x60;Valentine&#39;s Day&#x60;\&quot;  | [optional] 


