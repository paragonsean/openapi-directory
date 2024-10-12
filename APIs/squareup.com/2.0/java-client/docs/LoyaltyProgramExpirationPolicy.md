

# LoyaltyProgramExpirationPolicy

Describes when the loyalty program expires.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expirationDuration** | **String** | The number of months before points expire, in &#x60;P[n]M&#x60; RFC 3339 duration format. For example, a value of &#x60;P12M&#x60; represents a duration of 12 months.  Points are valid through the last day of the month in which they are scheduled to expire. For example, with a  &#x60;P12M&#x60; duration, points earned on July 6, 2020 expire on August 1, 2021. |  |



