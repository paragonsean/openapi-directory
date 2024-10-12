# CallFireApiDocumentation.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | ~ | [optional] 
**address** | **String** | ~ | [optional] 
**age** | [**Duration**](Duration.md) |  | [optional] 
**agencyManagedAccounts** | **Boolean** | ~ | [optional] 
**allowedToCreateCampaign** | **Boolean** | ~ | [optional] 
**apiCallLimit** | **Number** | ~ | [optional] 
**archived** | **Boolean** | ~ | [optional] 
**autoAddDoNotContact** | **Boolean** | ~ | [optional] 
**brand** | **String** | ~ | [optional] 
**canceled** | **Boolean** | ~ | [optional] 
**canceledOrArchived** | **Boolean** | ~ | [optional] 
**city** | **String** | ~ | [optional] 
**companyName** | **String** | ~ | [optional] 
**country** | **String** | ~ | [optional] 
**countryOrDefault** | **String** | ~ | [optional] 
**created** | **Date** | ~ | [optional] 
**dateTimeZone** | [**DateTimeZone**](DateTimeZone.md) |  | [optional] 
**defaultNotificationTtlMillis** | **Number** | ~ | [optional] 
**defaultNumberId** | **Number** | ~ | [optional] 
**ein** | **String** | ~ | [optional] 
**entityType** | **String** | ~ | [optional] 
**ez** | **Boolean** | ~ | [optional] 
**failedVerificationAttempts** | **Number** | ~ | [optional] 
**fromNumberPool** | **String** | ~ | [optional] 
**id** | **Number** | An id of an account | [optional] 
**industry** | **String** | ~ | [optional] 
**industryName** | **String** | ~ | [optional] 
**key** | **String** | ~ | [optional] 
**localTimeZoneRestriction** | [**LocalTimeZoneRestriction**](LocalTimeZoneRestriction.md) |  | [optional] 
**locale** | [**Locale**](Locale.md) |  | [optional] 
**maxAgents** | **Number** | ~ | [optional] 
**messageClass** | **String** | ~ | [optional] 
**messageFlows** | **[String]** | ~ | [optional] 
**name** | **String** | Name associated with an account | [optional] 
**outboundThreshold** | **Number** | ~ | [optional] 
**receiverPeriodCall** | **Number** | ~ | [optional] 
**receiverPeriodEnabled** | **Boolean** | ~ | [optional] 
**receiverPeriodGlobal** | **Number** | ~ | [optional] 
**receiverPeriodText** | **Number** | ~ | [optional] 
**receiverPeriodTimeUnit** | **String** | ~ | [optional] 
**retainOnlyMetadata** | **Boolean** | ~ | [optional] 
**retainOnlyMetadataLastDetailRecordId** | **Number** | ~ | [optional] 
**retainOnlyMetadataLastModified** | **Date** | ~ | [optional] 
**scrub** | **Boolean** | ~ | [optional] 
**sharedShortCodeAllowed** | **Boolean** | ~ | [optional] 
**sharedShortCodeId** | **Number** | ~ | [optional] 
**soaAccount** | [**Account**](Account.md) |  | [optional] 
**startCapable** | **Boolean** | ~ | [optional] 
**state** | **String** | ~ | [optional] 
**status** | **String** | ~ | [optional] 
**textOutboundThreshold** | **Number** | ~ | [optional] 
**timeZone** | [**TimeZone**](TimeZone.md) |  | [optional] 
**timeZoneId** | [**ZoneId**](ZoneId.md) |  | [optional] 
**trustLevel** | **String** | ~ | [optional] 
**tsrAgreement** | **Date** | ~ | [optional] 
**tsrInitials** | **String** | ~ | [optional] 
**uiContext** | **String** | ~ | [optional] 
**universal** | **Boolean** | ~ | [optional] 
**website** | **String** | ~ | [optional] 
**zipcode** | **String** | ~ | [optional] 



## Enum: BrandEnum


* `EZTEXTING` (value: `"EZTEXTING"`)

* `CLUBTEXTING` (value: `"CLUBTEXTING"`)

* `GROUPTEXTING` (value: `"GROUPTEXTING"`)

* `TELLMYCELL` (value: `"TELLMYCELL"`)

* `EZ` (value: `"EZ"`)

* `CALLFIRE` (value: `"CALLFIRE"`)

* `TESLA` (value: `"TESLA"`)





## Enum: CountryEnum


* `US` (value: `"US"`)

* `CA` (value: `"CA"`)





## Enum: CountryOrDefaultEnum


* `US` (value: `"US"`)

* `CA` (value: `"CA"`)





## Enum: EntityTypeEnum


* `SP` (value: `"SP"`)

* `COMPANY` (value: `"COMPANY"`)





## Enum: IndustryEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `ADVERTISING` (value: `"ADVERTISING"`)

* `AUTOMOTIVE` (value: `"AUTOMOTIVE"`)

* `COLLECTIONS` (value: `"COLLECTIONS"`)

* `CONSULTING` (value: `"CONSULTING"`)

* `DECLINE` (value: `"DECLINE"`)

* `EDUCATION` (value: `"EDUCATION"`)

* `EMERGENCY` (value: `"EMERGENCY"`)

* `ENTERTAINMENT` (value: `"ENTERTAINMENT"`)

* `FINANCE` (value: `"FINANCE"`)

* `HOSPITALITY` (value: `"HOSPITALITY"`)

* `HEALTHFITNESS` (value: `"HEALTHFITNESS"`)

* `HEALTHCARE` (value: `"HEALTHCARE"`)

* `INSURANCE` (value: `"INSURANCE"`)

* `LEAD` (value: `"LEAD"`)

* `OTHER` (value: `"OTHER"`)

* `POLITICAL` (value: `"POLITICAL"`)

* `REAL_ESTATE` (value: `"REAL_ESTATE"`)

* `RETAIL` (value: `"RETAIL"`)

* `SEARCH_MARKETING` (value: `"SEARCH_MARKETING"`)

* `TELECOM` (value: `"TELECOM"`)





## Enum: ReceiverPeriodTimeUnitEnum


* `NANOSECONDS` (value: `"NANOSECONDS"`)

* `MICROSECONDS` (value: `"MICROSECONDS"`)

* `MILLISECONDS` (value: `"MILLISECONDS"`)

* `SECONDS` (value: `"SECONDS"`)

* `MINUTES` (value: `"MINUTES"`)

* `HOURS` (value: `"HOURS"`)

* `DAYS` (value: `"DAYS"`)





## Enum: StatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `PENDING_CANCELLED` (value: `"PENDING_CANCELLED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `ARCHIVING` (value: `"ARCHIVING"`)

* `ARCHIVED` (value: `"ARCHIVED"`)





## Enum: TrustLevelEnum


* `LOCKED` (value: `"LOCKED"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `PROBATION` (value: `"PROBATION"`)

* `NORMAL` (value: `"NORMAL"`)

* `TRUSTED` (value: `"TRUSTED"`)




