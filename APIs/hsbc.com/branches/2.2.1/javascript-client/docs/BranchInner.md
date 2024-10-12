# BranchLocatorApi.BranchInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | **[String]** | Accessibility is the ability and ease a customer can access a service, good, associate, or facility. Features which make the Bank accessible to disabled people | [optional] 
**availability** | **Object** | Days and times defining when the branch is available for use by a customer | [optional] 
**contactInfo** | [**[ContactInfoInner]**](ContactInfoInner.md) | Communication device number or electronic address used for communication. | [optional] 
**customerSegment** | **[String]** | The marketing segment which the branch is able to address in terms of customer type. Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another | 
**identification** | **String** | Unique and unambiguous identification of a branch of a financial institution. | 
**name** | **String** | Name by which a branch is known and which is usually used to identify that branch. | [optional] 
**note** | **String** | Summary description of services, facility and availability. | [optional] 
**otherAccessibility** | [**[OtherAccessibilityInner]**](OtherAccessibilityInner.md) | Enter any new code , name and description for any other Accessibility | [optional] 
**otherCustomerSegment** | [**[OtherCustomerSegmentInner]**](OtherCustomerSegmentInner.md) | Enter a new code , name and description for any other Customer Segment | [optional] 
**otherServiceAndFacility** | [**[OtherServiceAndFacilityInner]**](OtherServiceAndFacilityInner.md) | Enter any new code , name and description for any Other Facility | [optional] 
**photo** | **String** | Image related to the branch | [optional] 
**postalAddress** | **Object** | Information that locates and identifies a specific address, as defined by postal services. | 
**sequenceNumber** | **String** | Sequence Number that is used in conjunction with Identification to uniquely identify a branch. Physical branches should have 0 assigned, mobile and sub branches should have 1,2,3....etc. assigned. | 
**serviceAndFacility** | **[String]** | Service/Facilities offered at a branch. | [optional] 
**sortCode** | **[String]** | United Kingdom (UK) Sort Code - identifies British financial institutions on the British national clearing systems. The sort code, which is a six-digit number, is usually formatted as three pairs of numbers, for example 12-34-56. It identifies both the bank and the branch(s) where the account is held. | [optional] 
**type** | **String** | Codeset to indicate if a branch is physically in 1 location or is mobile | 



## Enum: [AccessibilityEnum]


* `AutomaticDoors` (value: `"AutomaticDoors"`)

* `AudioCashMachine` (value: `"AudioCashMachine"`)

* `ExternalRamp` (value: `"ExternalRamp"`)

* `HelpingHandUnit` (value: `"HelpingHandUnit"`)

* `InductionLoop` (value: `"InductionLoop"`)

* `InternalRamp` (value: `"InternalRamp"`)

* `LevelAccess` (value: `"LevelAccess"`)

* `LowerLevelCounter` (value: `"LowerLevelCounter"`)

* `Other` (value: `"Other"`)

* `WheelchairAccess` (value: `"WheelchairAccess"`)





## Enum: [CustomerSegmentEnum]


* `Business` (value: `"Business"`)

* `Corporate` (value: `"Corporate"`)

* `Other` (value: `"Other"`)

* `Personal` (value: `"Personal"`)

* `Private` (value: `"Private"`)

* `Premier` (value: `"Premier"`)

* `Select` (value: `"Select"`)

* `SME` (value: `"SME"`)

* `Wealth` (value: `"Wealth"`)





## Enum: [ServiceAndFacilityEnum]


* `AssistedServiceCounter` (value: `"AssistedServiceCounter"`)

* `ExternalATM` (value: `"ExternalATM"`)

* `AccountVerificationService` (value: `"AccountVerificationService"`)

* `BusinessCounter` (value: `"BusinessCounter"`)

* `BureauDeChange` (value: `"BureauDeChange"`)

* `BusinessDepositTerminal` (value: `"BusinessDepositTerminal"`)

* `BusinessITSupport` (value: `"BusinessITSupport"`)

* `CardIssuanceFacility` (value: `"CardIssuanceFacility"`)

* `CollectionLockers` (value: `"CollectionLockers"`)

* `CounterServices` (value: `"CounterServices"`)

* `ExternalQuickServicePoint` (value: `"ExternalQuickServicePoint"`)

* `InternalQuickServicePoint` (value: `"InternalQuickServicePoint"`)

* `InternalATM` (value: `"InternalATM"`)

* `LodgementDevice` (value: `"LodgementDevice"`)

* `MortgageAdvisor` (value: `"MortgageAdvisor"`)

* `MeetingRooms` (value: `"MeetingRooms"`)

* `NightSafe` (value: `"NightSafe"`)

* `OnlineBankingPoint` (value: `"OnlineBankingPoint"`)

* `OnDemandCurrency` (value: `"OnDemandCurrency"`)

* `Other` (value: `"Other"`)

* `Parking` (value: `"Parking"`)

* `PremierCounter` (value: `"PremierCounter"`)

* `QuickDeposit` (value: `"QuickDeposit"`)

* `SaturdayCounterService` (value: `"SaturdayCounterService"`)

* `StatementPrinter` (value: `"StatementPrinter"`)

* `SelfServiceAccountOpening` (value: `"SelfServiceAccountOpening"`)

* `VideoBanking` (value: `"VideoBanking"`)

* `WiFi` (value: `"WiFi"`)





## Enum: TypeEnum


* `Mobile` (value: `"Mobile"`)

* `Physical` (value: `"Physical"`)




