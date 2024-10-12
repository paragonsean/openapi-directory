# ContentApiForShopping.ReturnPolicyPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastReturnDate** | **String** | Required. Last day for returning the items. In ISO 8601 format. When specifying the return window like this, set the policy type to \&quot;lastReturnDate\&quot;. Use this for seasonal overrides only. | [optional] 
**numberOfDays** | **String** | The number of days items can be returned after delivery, where one day is defined to be 24 hours after the delivery timestamp. When specifying the return window like this, set the policy type to \&quot;numberOfDaysAfterDelivery\&quot;. Acceptable values are 30, 45, 60, 90, 100, 180, 270 and 365 for the default policy. Additional policies further allow 14, 15, 21 and 28 days, but note that for most items a minimum of 30 days is required for returns. Exceptions may be made for electronics. A policy of less than 30 days can only be applied to those items. | [optional] 
**type** | **String** | Policy type. Use \&quot;lastReturnDate\&quot; for seasonal overrides only. Note that for most items a minimum of 30 days is required for returns. Exceptions may be made for electronics or non-returnable items such as food, perishables, and living things. A policy of less than 30 days can only be applied to those items. Acceptable values are: - \&quot;&#x60;lastReturnDate&#x60;\&quot; - \&quot;&#x60;lifetimeReturns&#x60;\&quot; - \&quot;&#x60;noReturns&#x60;\&quot; - \&quot;&#x60;numberOfDaysAfterDelivery&#x60;\&quot;  | [optional] 


