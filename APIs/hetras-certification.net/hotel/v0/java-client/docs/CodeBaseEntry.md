

# CodeBaseEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**Map&lt;String, LinkObject&gt;**](LinkObject.md) | Collection of links to related resources |  [optional] |
|**code** | **String** | The code value. This value you will see in reservations as market code and in other              resources like the revenue buckets in transactions |  [optional] |
|**_default** | **Boolean** | This attribute tells you if this code is the default code for the specific type or not.              Not all the types of codes need to have a default code |  [optional] |
|**id** | **String** | The id of the code |  [optional] |
|**name** | **String** | The name of the code that usually is more human readable |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type or category of the code |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GUEST_REQUEST | &quot;GuestRequest&quot; |
| REQUEST_DIETARY | &quot;RequestDietary&quot; |
| VIP_STATUS | &quot;VIPStatus&quot; |
| REASON_FOR_RATE_CHANGE | &quot;ReasonForRateChange&quot; |
| REGRETS | &quot;Regrets&quot; |
| MARKET_SEGMENTS | &quot;MarketSegments&quot; |
| SOURCE_OF_BUSINESS | &quot;SourceOfBusiness&quot; |
| LOYALTY_PROGRAM | &quot;LoyaltyProgram&quot; |
| CANCELLATION_REASON | &quot;CancellationReason&quot; |
| ACCOUNT_TYPE | &quot;AccountType&quot; |
| ACCOUNT_RANK | &quot;AccountRank&quot; |
| VIP_LEVEL | &quot;VIPLevel&quot; |
| TITLE | &quot;Title&quot; |
| CONTACT_FUNCTION | &quot;ContactFunction&quot; |
| TERRITORY | &quot;Territory&quot; |
| CORRESPONDENCE_TYPE | &quot;CorrespondenceType&quot; |
| EXTERNAL_PROGRAM_TYPE | &quot;ExternalProgramType&quot; |
| REVENUE_BUCKET | &quot;RevenueBucket&quot; |
| ADDITIONAL_REVENUE_BUCKET | &quot;AdditionalRevenueBucket&quot; |
| ADDITIONAL_STATISTICS_BUCKETS | &quot;AdditionalStatisticsBuckets&quot; |
| MEAL_PERIOD | &quot;MealPeriod&quot; |
| BILLING_CYCLE | &quot;BillingCycle&quot; |
| REMINDER_CYCLE | &quot;ReminderCycle&quot; |
| MAJOR_MARKET_SEGMENTS | &quot;MajorMarketSegments&quot; |
| DOCUMENT_TYPE | &quot;DocumentType&quot; |
| ACTIVITY_TYPE | &quot;ActivityType&quot; |
| RESERVATION_LABELS | &quot;ReservationLabels&quot; |



