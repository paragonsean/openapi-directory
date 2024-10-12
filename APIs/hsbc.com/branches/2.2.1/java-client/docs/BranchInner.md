

# BranchInner

Information that locates and identifies a specific branch of a financial institution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessibility** | [**List&lt;AccessibilityEnum&gt;**](#List&lt;AccessibilityEnum&gt;) | Accessibility is the ability and ease a customer can access a service, good, associate, or facility. Features which make the Bank accessible to disabled people |  [optional] |
|**availability** | **Object** | Days and times defining when the branch is available for use by a customer |  [optional] |
|**contactInfo** | [**List&lt;ContactInfoInner&gt;**](ContactInfoInner.md) | Communication device number or electronic address used for communication. |  [optional] |
|**customerSegment** | [**List&lt;CustomerSegmentEnum&gt;**](#List&lt;CustomerSegmentEnum&gt;) | The marketing segment which the branch is able to address in terms of customer type. Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another |  |
|**identification** | **String** | Unique and unambiguous identification of a branch of a financial institution. |  |
|**name** | **String** | Name by which a branch is known and which is usually used to identify that branch. |  [optional] |
|**note** | **String** | Summary description of services, facility and availability. |  [optional] |
|**otherAccessibility** | [**List&lt;OtherAccessibilityInner&gt;**](OtherAccessibilityInner.md) | Enter any new code , name and description for any other Accessibility |  [optional] |
|**otherCustomerSegment** | [**List&lt;OtherCustomerSegmentInner&gt;**](OtherCustomerSegmentInner.md) | Enter a new code , name and description for any other Customer Segment |  [optional] |
|**otherServiceAndFacility** | [**List&lt;OtherServiceAndFacilityInner&gt;**](OtherServiceAndFacilityInner.md) | Enter any new code , name and description for any Other Facility |  [optional] |
|**photo** | **String** | Image related to the branch |  [optional] |
|**postalAddress** | **Object** | Information that locates and identifies a specific address, as defined by postal services. |  |
|**sequenceNumber** | **String** | Sequence Number that is used in conjunction with Identification to uniquely identify a branch. Physical branches should have 0 assigned, mobile and sub branches should have 1,2,3....etc. assigned. |  |
|**serviceAndFacility** | [**List&lt;ServiceAndFacilityEnum&gt;**](#List&lt;ServiceAndFacilityEnum&gt;) | Service/Facilities offered at a branch. |  [optional] |
|**sortCode** | **List&lt;String&gt;** | United Kingdom (UK) Sort Code - identifies British financial institutions on the British national clearing systems. The sort code, which is a six-digit number, is usually formatted as three pairs of numbers, for example 12-34-56. It identifies both the bank and the branch(s) where the account is held. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Codeset to indicate if a branch is physically in 1 location or is mobile |  |



## Enum: List&lt;AccessibilityEnum&gt;

| Name | Value |
|---- | -----|
| AUTOMATIC_DOORS | &quot;AutomaticDoors&quot; |
| AUDIO_CASH_MACHINE | &quot;AudioCashMachine&quot; |
| EXTERNAL_RAMP | &quot;ExternalRamp&quot; |
| HELPING_HAND_UNIT | &quot;HelpingHandUnit&quot; |
| INDUCTION_LOOP | &quot;InductionLoop&quot; |
| INTERNAL_RAMP | &quot;InternalRamp&quot; |
| LEVEL_ACCESS | &quot;LevelAccess&quot; |
| LOWER_LEVEL_COUNTER | &quot;LowerLevelCounter&quot; |
| OTHER | &quot;Other&quot; |
| WHEELCHAIR_ACCESS | &quot;WheelchairAccess&quot; |



## Enum: List&lt;CustomerSegmentEnum&gt;

| Name | Value |
|---- | -----|
| BUSINESS | &quot;Business&quot; |
| CORPORATE | &quot;Corporate&quot; |
| OTHER | &quot;Other&quot; |
| PERSONAL | &quot;Personal&quot; |
| PRIVATE | &quot;Private&quot; |
| PREMIER | &quot;Premier&quot; |
| SELECT | &quot;Select&quot; |
| SME | &quot;SME&quot; |
| WEALTH | &quot;Wealth&quot; |



## Enum: List&lt;ServiceAndFacilityEnum&gt;

| Name | Value |
|---- | -----|
| ASSISTED_SERVICE_COUNTER | &quot;AssistedServiceCounter&quot; |
| EXTERNAL_ATM | &quot;ExternalATM&quot; |
| ACCOUNT_VERIFICATION_SERVICE | &quot;AccountVerificationService&quot; |
| BUSINESS_COUNTER | &quot;BusinessCounter&quot; |
| BUREAU_DE_CHANGE | &quot;BureauDeChange&quot; |
| BUSINESS_DEPOSIT_TERMINAL | &quot;BusinessDepositTerminal&quot; |
| BUSINESS_IT_SUPPORT | &quot;BusinessITSupport&quot; |
| CARD_ISSUANCE_FACILITY | &quot;CardIssuanceFacility&quot; |
| COLLECTION_LOCKERS | &quot;CollectionLockers&quot; |
| COUNTER_SERVICES | &quot;CounterServices&quot; |
| EXTERNAL_QUICK_SERVICE_POINT | &quot;ExternalQuickServicePoint&quot; |
| INTERNAL_QUICK_SERVICE_POINT | &quot;InternalQuickServicePoint&quot; |
| INTERNAL_ATM | &quot;InternalATM&quot; |
| LODGEMENT_DEVICE | &quot;LodgementDevice&quot; |
| MORTGAGE_ADVISOR | &quot;MortgageAdvisor&quot; |
| MEETING_ROOMS | &quot;MeetingRooms&quot; |
| NIGHT_SAFE | &quot;NightSafe&quot; |
| ONLINE_BANKING_POINT | &quot;OnlineBankingPoint&quot; |
| ON_DEMAND_CURRENCY | &quot;OnDemandCurrency&quot; |
| OTHER | &quot;Other&quot; |
| PARKING | &quot;Parking&quot; |
| PREMIER_COUNTER | &quot;PremierCounter&quot; |
| QUICK_DEPOSIT | &quot;QuickDeposit&quot; |
| SATURDAY_COUNTER_SERVICE | &quot;SaturdayCounterService&quot; |
| STATEMENT_PRINTER | &quot;StatementPrinter&quot; |
| SELF_SERVICE_ACCOUNT_OPENING | &quot;SelfServiceAccountOpening&quot; |
| VIDEO_BANKING | &quot;VideoBanking&quot; |
| WI_FI | &quot;WiFi&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MOBILE | &quot;Mobile&quot; |
| PHYSICAL | &quot;Physical&quot; |



