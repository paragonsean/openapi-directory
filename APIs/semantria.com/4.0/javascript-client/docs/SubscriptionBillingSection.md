# Semantria.SubscriptionBillingSection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appSeatsAllocated** | **Number** | Number of allocated application cells permitted to work with the API | 
**appSeatsPermitted** | **Number** | Number of permitted application to work with the same API account | 
**dataCallsBalance** | **Number** | Represents actual value of remained data API calls | 
**dataCallsLimit** | **Number** | Represents the limit of data API calls per \&quot;data_calls_limit_interval\&quot; value | 
**dataCallsLimitInterval** | **Number** | Represents an interval for the \&quot;data_calls_limit\&quot; value of current subscription | 
**docsBalance** | **Number** | Current transaction balance. Applicable for pay-as-you-go subscriptions only | 
**docsLimit** | **Number** | Represents the transactions limit per \&quot;docs_limit_interval\&quot; value | 
**docsLimitInterval** | **Number** | Represents the timeframe for the \&quot;docs_limit\&quot; value of current subscription | 
**docsSuggested** | **Number** | Represents the amount of favorable documents suggested for throughput subscriptions | 
**docsSuggestedInterval** | **Number** | Represents the timeframe for the “docs_suggested” value of the current subscription | 
**expirationDate** | **String** | Expiration date of current subscription. Defined as a Unix time stamp | 
**limitType** | **String** | Subscription type can have either pay-as-you-go or throughput value | 
**pollingCallsBalance** | **Number** | Represents actual value of remained polling API calls | 
**pollingCallsLimit** | **Number** | Represents the limit of polling API calls per \&quot;polling_calls_limit_interval\&quot; value | 
**pollingCallsLimitInterval** | **Number** | Represents an interval for the \&quot;polling_calls_limit\&quot; value of current subscription | 
**priority** | **String** | Processing priority of current subscriber. Can have low, normal or high value | 
**settingsCallsBalance** | **Number** | Represents actual value of remained settings API calls | 
**settingsCallsLimit** | **Number** | Represents the limit of settings API calls per \&quot;settings_calls_limit_interval\&quot; value | 
**settingsCallsLimitInterval** | **Number** | Represents an interval for the \&quot;settings_calls_limit\&quot; value of current subscription | 


