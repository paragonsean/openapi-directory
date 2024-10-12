# ContentApiForShopping.OrderCustomerMarketingRightsInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**explicitMarketingPreference** | **String** | Last known customer selection regarding marketing preferences. In certain cases this selection might not be known, so this field would be empty. If a customer selected &#x60;granted&#x60; in their most recent order, they can be subscribed to marketing emails. Customers who have chosen &#x60;denied&#x60; must not be subscribed, or must be unsubscribed if already opted-in. Acceptable values are: - \&quot;&#x60;denied&#x60;\&quot; - \&quot;&#x60;granted&#x60;\&quot;  | [optional] 
**lastUpdatedTimestamp** | **String** | Timestamp when last time marketing preference was updated. Could be empty, if user wasn&#39;t offered a selection yet. | [optional] 
**marketingEmailAddress** | **String** | Email address that can be used for marketing purposes. The field may be empty even if &#x60;explicitMarketingPreference&#x60; is &#39;granted&#39;. This happens when retrieving an old order from the customer who deleted their account. | [optional] 


