

# ScheduleBByRecipientID


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**committeeId** | **String** |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |  |
|**committeeName** | **String** |  |  [optional] |
|**count** | **Integer** |  Number of records making up the total.  |  [optional] |
|**cycle** | **Integer** |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  |  |
|**memoCount** | **Integer** |  Number of records making up the total.  |  [optional] |
|**memoTotal** | **BigDecimal** |  Schedule B disbursements aggregated by memoed items only  |  [optional] |
|**recipientId** | **String** | The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC. |  |
|**recipientName** | **String** |  |  [optional] |
|**total** | **BigDecimal** |  Schedule B disbursements aggregated by non-memoed items only  |  [optional] |



