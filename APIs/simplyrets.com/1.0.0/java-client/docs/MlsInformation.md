

# MlsInformation

RETS MLS Vendor Data

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**area** | **String** | MLS Area major. The major marketing area name, as defined by the MLS or other non-governmental organization. |  [optional] |
|**areaMinor** | **String** | MLS Area minor. The minor/sub marketing area name, as defined by the MLS or other non-governmental organization. |  [optional] |
|**daysOnMarket** | **Long** | Amount of days the property has been Active |  [optional] |
|**originatingSystemName** | **String** | Alias for the listing office or brokerage  This field corresponds to the data-dictionary &#x60;OriginatingSystemName&#x60; field  The name of the originating record provider.  Most commonly the name of the MLS. The place where the listing is originally input by the member.  The legal name of the company.  To be used for display.  If you&#39;re RETS provider aggregates feeds from multiple MLS&#39;s, this will be the name of the corresponding MLS.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Normalized MLS Status Code. Compliant with data dictionary v1.3 ListingStatus Listing statuses depend on your MLS&#39;s availability. Below is a brief description of each status with possible synonyms which may map to your MLS-specific statuses  - Active: Active Listing which is still on the market - ActiveUnderContract: An offer has been accepted but the listing is still on market. Synonyms: Accepting Backup Offers, Backup Offer, Active With Accepted. Synonyms: Offer, Backup, Contingent - Pending: An offer has been accepted and the listing is no longer on market. Synonyms: Offer Accepted, Under Contract - Hold: The listing has been withdrawn from the market, but a contract   still exists between the seller and the listing member. Synonyms: Hold, Hold Do Not Show, Temp Off Market - Withdrawn: The listing has been withdrawn from the market, but a contract   still exists between the seller and the listing member. Synonyms: Hold, Hold Do Not Show, Temp Off Market - Closed: The purchase agreement has been fulfilled or the lease   agreement has been executed. Synonyms: Sold, Leased, Rented, Closed Sale - Expired: The listing contract has expired - Delete: The listing contract was never valid or other reason for the contract to be nullified. Synonyms: Kill, Zap - Incomplete: The listing has not yet be completely entered and is not yet   published in the MLS. Synonyms: Draft, Partially Complted - ComingSoon  |  [optional] |
|**statusText** | **String** | Raw MLS status text. This &#x60;field&#x60; comes directly from your RETS data field and is not normalized.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| ACTIVE_UNDER_CONTRACT_BACKUP_OFFER_ | &quot;ActiveUnderContract (Backup-Offer)&quot; |
| PENDING | &quot;Pending&quot; |
| HOLD | &quot;Hold&quot; |
| WITHDRAWN | &quot;Withdrawn&quot; |
| CLOSED | &quot;Closed&quot; |
| EXPIRED | &quot;Expired&quot; |
| DELETE | &quot;Delete&quot; |
| INCOMPLETE | &quot;Incomplete&quot; |
| COMING_SOON | &quot;ComingSoon&quot; |



