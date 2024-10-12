

# ScheduleAByStateRecipientTotals


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**committeeType** | **String** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  |  [optional] |
|**committeeTypeFull** | **String** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  |  [optional] |
|**count** | **Integer** | Number of records making up the total. |  [optional] |
|**cycle** | **Integer** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  |  [optional] |
|**state** | **String** | US state or territory |  [optional] |
|**stateFull** | **String** | US state or territory |  [optional] |
|**total** | **BigDecimal** | The calculated total. |  [optional] |



