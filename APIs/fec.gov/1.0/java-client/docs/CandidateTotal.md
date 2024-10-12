

# CandidateTotal


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**candidateId** | **String** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  |  |
|**candidateInactive** | **Boolean** |  True indicates that a candidate is inactive.  |  [optional] |
|**cashOnHandEndPeriod** | **BigDecimal** | Ending cash balance on the most recent filing |  [optional] |
|**coverageEndDate** | **LocalDate** | Ending date of the reporting period |  [optional] |
|**coverageStartDate** | **LocalDate** | Beginning date of the reporting period |  [optional] |
|**cycle** | **Integer** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  |  |
|**debtsOwedByCommittee** | **BigDecimal** | Debts owed by the committee |  [optional] |
|**disbursements** | **BigDecimal** |  |  [optional] |
|**district** | **String** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. |  [optional] |
|**districtNumber** | **Integer** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. |  [optional] |
|**electionYear** | **Integer** | Year of election |  [optional] |
|**federalFundsFlag** | **Boolean** | A boolean the describes if a presidential candidate has accepted federal funds. The flag will be false for House and Senate candidates. |  [optional] |
|**hasRaisedFunds** | **Boolean** | A boolean that describes if a candidate&#39;s committee has ever received any receipts for their campaign for this particular office. (Candidates have separate candidate IDs for each office.) |  [optional] |
|**individualItemizedContributions** | **BigDecimal** | Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. |  [optional] |
|**isElection** | **Boolean** |  |  |
|**office** | **String** | Federal office candidate runs for: H, S or P |  [optional] |
|**otherPoliticalCommitteeContributions** | **BigDecimal** | Other committees contributions |  [optional] |
|**party** | **String** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. |  [optional] |
|**receipts** | **BigDecimal** |  |  [optional] |
|**state** | **String** | US state or territory where a candidate runs for office |  [optional] |
|**stateFull** | **String** | US state or territory where a candidate runs for office |  [optional] |
|**transfersFromOtherAuthorizedCommittee** | **BigDecimal** | Transfers from authorized committees |  [optional] |



