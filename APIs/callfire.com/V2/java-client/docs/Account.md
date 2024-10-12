

# Account

Object represents user account in Callfire system

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | ~ |  [optional] |
|**address** | **String** | ~ |  [optional] |
|**age** | [**Duration**](Duration.md) |  |  [optional] |
|**agencyManagedAccounts** | **Boolean** | ~ |  [optional] |
|**allowedToCreateCampaign** | **Boolean** | ~ |  [optional] |
|**apiCallLimit** | **Integer** | ~ |  [optional] |
|**archived** | **Boolean** | ~ |  [optional] |
|**autoAddDoNotContact** | **Boolean** | ~ |  [optional] |
|**brand** | [**BrandEnum**](#BrandEnum) | ~ |  [optional] |
|**canceled** | **Boolean** | ~ |  [optional] |
|**canceledOrArchived** | **Boolean** | ~ |  [optional] |
|**city** | **String** | ~ |  [optional] |
|**companyName** | **String** | ~ |  [optional] |
|**country** | [**CountryEnum**](#CountryEnum) | ~ |  [optional] |
|**countryOrDefault** | [**CountryOrDefaultEnum**](#CountryOrDefaultEnum) | ~ |  [optional] |
|**created** | **OffsetDateTime** | ~ |  [optional] |
|**dateTimeZone** | [**DateTimeZone**](DateTimeZone.md) |  |  [optional] |
|**defaultNotificationTtlMillis** | **Long** | ~ |  [optional] |
|**defaultNumberId** | **Long** | ~ |  [optional] |
|**ein** | **String** | ~ |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | ~ |  [optional] |
|**ez** | **Boolean** | ~ |  [optional] |
|**failedVerificationAttempts** | **Integer** | ~ |  [optional] |
|**fromNumberPool** | **String** | ~ |  [optional] |
|**id** | **Long** | An id of an account |  [optional] |
|**industry** | [**IndustryEnum**](#IndustryEnum) | ~ |  [optional] |
|**industryName** | **String** | ~ |  [optional] |
|**key** | **String** | ~ |  [optional] |
|**localTimeZoneRestriction** | [**LocalTimeZoneRestriction**](LocalTimeZoneRestriction.md) |  |  [optional] |
|**locale** | [**Locale**](Locale.md) |  |  [optional] |
|**maxAgents** | **Integer** | ~ |  [optional] |
|**messageClass** | **String** | ~ |  [optional] |
|**messageFlows** | **Set&lt;String&gt;** | ~ |  [optional] |
|**name** | **String** | Name associated with an account |  [optional] |
|**outboundThreshold** | **Integer** | ~ |  [optional] |
|**receiverPeriodCall** | **Integer** | ~ |  [optional] |
|**receiverPeriodEnabled** | **Boolean** | ~ |  [optional] |
|**receiverPeriodGlobal** | **Integer** | ~ |  [optional] |
|**receiverPeriodText** | **Integer** | ~ |  [optional] |
|**receiverPeriodTimeUnit** | [**ReceiverPeriodTimeUnitEnum**](#ReceiverPeriodTimeUnitEnum) | ~ |  [optional] |
|**retainOnlyMetadata** | **Boolean** | ~ |  [optional] |
|**retainOnlyMetadataLastDetailRecordId** | **Long** | ~ |  [optional] |
|**retainOnlyMetadataLastModified** | **OffsetDateTime** | ~ |  [optional] |
|**scrub** | **Boolean** | ~ |  [optional] |
|**sharedShortCodeAllowed** | **Boolean** | ~ |  [optional] |
|**sharedShortCodeId** | **Long** | ~ |  [optional] |
|**soaAccount** | [**Account**](Account.md) |  |  [optional] |
|**startCapable** | **Boolean** | ~ |  [optional] |
|**state** | **String** | ~ |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | ~ |  [optional] |
|**textOutboundThreshold** | **Integer** | ~ |  [optional] |
|**timeZone** | [**TimeZone**](TimeZone.md) |  |  [optional] |
|**timeZoneId** | [**ZoneId**](ZoneId.md) |  |  [optional] |
|**trustLevel** | [**TrustLevelEnum**](#TrustLevelEnum) | ~ |  [optional] |
|**tsrAgreement** | **OffsetDateTime** | ~ |  [optional] |
|**tsrInitials** | **String** | ~ |  [optional] |
|**uiContext** | **String** | ~ |  [optional] |
|**universal** | **Boolean** | ~ |  [optional] |
|**website** | **String** | ~ |  [optional] |
|**zipcode** | **String** | ~ |  [optional] |



## Enum: BrandEnum

| Name | Value |
|---- | -----|
| EZTEXTING | &quot;EZTEXTING&quot; |
| CLUBTEXTING | &quot;CLUBTEXTING&quot; |
| GROUPTEXTING | &quot;GROUPTEXTING&quot; |
| TELLMYCELL | &quot;TELLMYCELL&quot; |
| EZ | &quot;EZ&quot; |
| CALLFIRE | &quot;CALLFIRE&quot; |
| TESLA | &quot;TESLA&quot; |



## Enum: CountryEnum

| Name | Value |
|---- | -----|
| US | &quot;US&quot; |
| CA | &quot;CA&quot; |



## Enum: CountryOrDefaultEnum

| Name | Value |
|---- | -----|
| US | &quot;US&quot; |
| CA | &quot;CA&quot; |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| SP | &quot;SP&quot; |
| COMPANY | &quot;COMPANY&quot; |



## Enum: IndustryEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| ADVERTISING | &quot;ADVERTISING&quot; |
| AUTOMOTIVE | &quot;AUTOMOTIVE&quot; |
| COLLECTIONS | &quot;COLLECTIONS&quot; |
| CONSULTING | &quot;CONSULTING&quot; |
| DECLINE | &quot;DECLINE&quot; |
| EDUCATION | &quot;EDUCATION&quot; |
| EMERGENCY | &quot;EMERGENCY&quot; |
| ENTERTAINMENT | &quot;ENTERTAINMENT&quot; |
| FINANCE | &quot;FINANCE&quot; |
| HOSPITALITY | &quot;HOSPITALITY&quot; |
| HEALTHFITNESS | &quot;HEALTHFITNESS&quot; |
| HEALTHCARE | &quot;HEALTHCARE&quot; |
| INSURANCE | &quot;INSURANCE&quot; |
| LEAD | &quot;LEAD&quot; |
| OTHER | &quot;OTHER&quot; |
| POLITICAL | &quot;POLITICAL&quot; |
| REAL_ESTATE | &quot;REAL_ESTATE&quot; |
| RETAIL | &quot;RETAIL&quot; |
| SEARCH_MARKETING | &quot;SEARCH_MARKETING&quot; |
| TELECOM | &quot;TELECOM&quot; |



## Enum: ReceiverPeriodTimeUnitEnum

| Name | Value |
|---- | -----|
| NANOSECONDS | &quot;NANOSECONDS&quot; |
| MICROSECONDS | &quot;MICROSECONDS&quot; |
| MILLISECONDS | &quot;MILLISECONDS&quot; |
| SECONDS | &quot;SECONDS&quot; |
| MINUTES | &quot;MINUTES&quot; |
| HOURS | &quot;HOURS&quot; |
| DAYS | &quot;DAYS&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| PENDING_CANCELLED | &quot;PENDING_CANCELLED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| ARCHIVING | &quot;ARCHIVING&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |



## Enum: TrustLevelEnum

| Name | Value |
|---- | -----|
| LOCKED | &quot;LOCKED&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| PROBATION | &quot;PROBATION&quot; |
| NORMAL | &quot;NORMAL&quot; |
| TRUSTED | &quot;TRUSTED&quot; |



