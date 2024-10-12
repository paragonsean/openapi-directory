

# CommitteeTotalsHouseSenate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allOtherLoans** | **BigDecimal** |  |  [optional] |
|**candidateContribution** | **BigDecimal** |  |  [optional] |
|**cashOnHandBeginningPeriod** | **BigDecimal** |  |  [optional] |
|**committeeDesignation** | **String** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  |  [optional] |
|**committeeDesignationFull** | **String** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  |  [optional] |
|**committeeId** | **String** |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |  [optional] |
|**committeeName** | **String** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. |  [optional] |
|**committeeState** | **String** |  State of the committee&#39;s address as filed on the Form 1  |  [optional] |
|**committeeType** | **String** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  |  [optional] |
|**committeeTypeFull** | **String** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  |  [optional] |
|**contributionRefunds** | **BigDecimal** |  |  [optional] |
|**contributions** | **BigDecimal** | Contribution |  [optional] |
|**contributionsIeAndPartyExpendituresMadePercent** | **BigDecimal** |  |  [optional] |
|**coverageEndDate** | **OffsetDateTime** |  |  [optional] |
|**coverageStartDate** | **OffsetDateTime** |  |  [optional] |
|**cycle** | **Integer** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  |  |
|**disbursements** | **BigDecimal** | Disbursements |  [optional] |
|**filingFrequency** | **String** | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  |  [optional] |
|**filingFrequencyFull** | **String** | The one-letter      code of the filing frequency:          - A Administratively terminated          - D Debt          - M Monthly filer          - Q Quarterly filer          - T Terminated          - W Waived  |  [optional] |
|**firstF1Date** | **LocalDate** | The day the FEC received the committee&#39;s first Form 1 |  [optional] |
|**firstFileDate** | **LocalDate** | The day the FEC received the committee&#39;s first filing. This is usually a Form 1 committee registration. |  [optional] |
|**individualContributions** | **BigDecimal** |  |  [optional] |
|**individualContributionsPercent** | **BigDecimal** |  |  [optional] |
|**individualItemizedContributions** | **BigDecimal** | Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. |  [optional] |
|**individualUnitemizedContributions** | **BigDecimal** | Unitemized contributions are made individuals whose aggregate contributions total $200 or less per individual per year. Be aware, some filers choose to itemize donations $200 or less and in that case those donations will appear in the itemized total. |  [optional] |
|**lastBeginningImageNumber** | **String** |  |  [optional] |
|**lastCashOnHandEndPeriod** | **BigDecimal** |  |  [optional] |
|**lastDebtsOwedByCommittee** | **BigDecimal** |  |  [optional] |
|**lastDebtsOwedToCommittee** | **BigDecimal** |  |  [optional] |
|**lastReportTypeFull** | **String** |  |  [optional] |
|**lastReportYear** | **Integer** |  |  [optional] |
|**loanRepayments** | **BigDecimal** |  |  [optional] |
|**loanRepaymentsCandidateLoans** | **BigDecimal** |  |  [optional] |
|**loanRepaymentsOtherLoans** | **BigDecimal** |  |  [optional] |
|**loans** | **BigDecimal** |  |  [optional] |
|**loansMadeByCandidate** | **BigDecimal** |  |  [optional] |
|**netContributions** | **BigDecimal** |  |  [optional] |
|**netOperatingExpenditures** | **BigDecimal** |  |  [optional] |
|**offsetsToOperatingExpenditures** | **BigDecimal** |  |  [optional] |
|**operatingExpenditures** | **BigDecimal** |  |  [optional] |
|**operatingExpendituresPercent** | **BigDecimal** |  |  [optional] |
|**organizationType** | **String** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  |  [optional] |
|**organizationTypeFull** | **String** | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  |  [optional] |
|**otherDisbursements** | **BigDecimal** |  |  [optional] |
|**otherPoliticalCommitteeContributions** | **BigDecimal** |  |  [optional] |
|**otherReceipts** | **BigDecimal** |  |  [optional] |
|**partyAndOtherCommitteeContributionsPercent** | **BigDecimal** |  |  [optional] |
|**partyFull** | **String** | Party affiliated with a candidate or committee |  [optional] |
|**pdfUrl** | **String** |  |  [optional] |
|**politicalPartyCommitteeContributions** | **BigDecimal** |  |  [optional] |
|**receipts** | **BigDecimal** |  |  [optional] |
|**refundedIndividualContributions** | **BigDecimal** |  |  [optional] |
|**refundedOtherPoliticalCommitteeContributions** | **BigDecimal** |  |  [optional] |
|**refundedPoliticalPartyCommitteeContributions** | **BigDecimal** |  |  [optional] |
|**reportForm** | **String** |  |  [optional] |
|**transactionCoverageDate** | **LocalDate** |  |  [optional] |
|**transfersFromOtherAuthorizedCommittee** | **BigDecimal** |  |  [optional] |
|**transfersToOtherAuthorizedCommittee** | **BigDecimal** |  |  [optional] |
|**treasurerName** | **String** | Name of the Committee&#39;s treasurer. If multiple treasurers for the committee, the most recent treasurer will be shown. |  [optional] |



