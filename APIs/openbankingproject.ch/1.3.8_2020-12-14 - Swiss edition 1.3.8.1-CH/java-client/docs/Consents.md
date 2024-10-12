

# Consents

Content of the body of a consent request. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**access** | [**AccountAccess**](AccountAccess.md) |  |  |
|**combinedServiceIndicator** | **Boolean** | If \&quot;true\&quot; indicates that a payment initiation service will be addressed in the same \&quot;session\&quot;.  |  |
|**frequencyPerDay** | **Integer** | This field indicates the requested maximum frequency for an access without PSU involvement per day. For a one-off access, this attribute is set to \&quot;1\&quot;.  The frequency needs to be greater equal to one.  If not otherwise agreed bilaterally between TPP and ASPSP, the frequency is less equal to 4.  |  |
|**recurringIndicator** | **Boolean** | \&quot;true\&quot;, if the consent is for recurring access to the account data.  \&quot;false\&quot;, if the consent is for one access to the account data.  |  |
|**validUntil** | **LocalDate** | This parameter is defining a valid until date (including the mentioned date) for the requested consent.  The content is the local ASPSP date in ISO-Date format, e.g. 2017-10-30.  Future dates might get adjusted by ASPSP.   If a maximal available date is requested, a date in far future is to be used: \&quot;9999-12-31\&quot;.   In both cases the consent object to be retrieved by the get consent request will contain the adjusted date.  |  |



