

# CandidateCommitteeTotalsHouseSenate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allOtherLoans** | **BigDecimal** |  |  [optional] |
|**candidateContribution** | **BigDecimal** |  |  [optional] |
|**candidateElectionYear** | **Integer** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  |  |
|**candidateId** | **String** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  |  |
|**contributionRefunds** | **BigDecimal** |  |  [optional] |
|**contributions** | **BigDecimal** | Contribution |  [optional] |
|**coverageEndDate** | **OffsetDateTime** |  |  [optional] |
|**coverageStartDate** | **OffsetDateTime** |  |  [optional] |
|**cycle** | **Integer** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  |  |
|**disbursements** | **BigDecimal** | Disbursements |  [optional] |
|**electionFull** | **Boolean** |  |  |
|**exemptLegalAccountingDisbursement** | **BigDecimal** |  |  [optional] |
|**federalFunds** | **BigDecimal** |  |  [optional] |
|**fundraisingDisbursements** | **BigDecimal** |  |  [optional] |
|**individualContributions** | **BigDecimal** |  |  [optional] |
|**individualItemizedContributions** | **BigDecimal** | Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. |  [optional] |
|**individualUnitemizedContributions** | **BigDecimal** | Unitemized contributions are made individuals whose aggregate contributions total $200 or less per individual per year. Be aware, some filers choose to itemize donations $200 or less and in that case those donations will appear in the itemized total. |  [optional] |
|**lastBeginningImageNumber** | **String** |  |  [optional] |
|**lastCashOnHandEndPeriod** | **BigDecimal** |  |  [optional] |
|**lastDebtsOwedByCommittee** | **BigDecimal** |  |  [optional] |
|**lastDebtsOwedToCommittee** | **BigDecimal** |  |  [optional] |
|**lastNetContributions** | **BigDecimal** |  |  [optional] |
|**lastNetOperatingExpenditures** | **BigDecimal** |  |  [optional] |
|**lastReportTypeFull** | **String** |  |  [optional] |
|**lastReportYear** | **Integer** |  |  [optional] |
|**loanRepayments** | **BigDecimal** |  |  [optional] |
|**loanRepaymentsCandidateLoans** | **BigDecimal** |  |  [optional] |
|**loanRepaymentsOtherLoans** | **BigDecimal** |  |  [optional] |
|**loans** | **BigDecimal** |  |  [optional] |
|**loansMadeByCandidate** | **BigDecimal** |  |  [optional] |
|**netContributions** | **BigDecimal** |  |  [optional] |
|**netOperatingExpenditures** | **BigDecimal** |  |  [optional] |
|**offsetsToFundraisingExpenditures** | **BigDecimal** |  |  [optional] |
|**offsetsToLegalAccounting** | **BigDecimal** |  |  [optional] |
|**offsetsToOperatingExpenditures** | **BigDecimal** |  |  [optional] |
|**operatingExpenditures** | **BigDecimal** |  |  [optional] |
|**otherDisbursements** | **BigDecimal** |  |  [optional] |
|**otherPoliticalCommitteeContributions** | **BigDecimal** |  |  [optional] |
|**otherReceipts** | **BigDecimal** |  |  [optional] |
|**politicalPartyCommitteeContributions** | **BigDecimal** |  |  [optional] |
|**receipts** | **BigDecimal** |  |  [optional] |
|**refundedIndividualContributions** | **BigDecimal** |  |  [optional] |
|**refundedOtherPoliticalCommitteeContributions** | **BigDecimal** |  |  [optional] |
|**refundedPoliticalPartyCommitteeContributions** | **BigDecimal** |  |  [optional] |
|**totalOffsetsToOperatingExpenditures** | **BigDecimal** |  |  [optional] |
|**transactionCoverageDate** | **OffsetDateTime** |  |  [optional] |
|**transfersFromOtherAuthorizedCommittee** | **BigDecimal** |  |  [optional] |
|**transfersToOtherAuthorizedCommittee** | **BigDecimal** |  |  [optional] |



