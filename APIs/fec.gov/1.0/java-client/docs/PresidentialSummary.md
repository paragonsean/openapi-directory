

# PresidentialSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**candidateContributionsLessRepayments** | **BigDecimal** |  candidate contributions less repayments  |  [optional] |
|**candidateId** | **String** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.   -P00000001    All candidates   -P00000002    Democrasts   -P00000003    Republicans  |  [optional] |
|**candidateLastName** | **String** |  Candidate last name  |  [optional] |
|**candidateName** | **String** | Name of candidate running for office |  [optional] |
|**candidatePartyAffiliation** | **String** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. |  [optional] |
|**cashOnHandEnd** | **BigDecimal** | Ending cash balance on the most recent filing |  [optional] |
|**committeeDesignation** | **String** | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  |  [optional] |
|**committeeId** | **String** |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  |  [optional] |
|**committeeName** | **String** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. |  [optional] |
|**committeeType** | **String** | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  |  [optional] |
|**debtsOwedByCommittee** | **BigDecimal** | Debts owed by the committee |  [optional] |
|**disbursementsLessOffsets** | **BigDecimal** |  disbursements less offsets  |  [optional] |
|**electionYear** | **Integer** | Year of election |  [optional] |
|**exemptLegalAccountingDisbursement** | **BigDecimal** |  exempt legal accounting disbursement  |  [optional] |
|**federalFunds** | **BigDecimal** | Federal funds: Public funding of presidential elections means that qualified presidential candidates                 receive federal government funds to pay for the valid expenses of their political campaigns                 in both the primary and general elections. |  [optional] |
|**fundraisingDisbursements** | **BigDecimal** |  fundraising disbursements  |  [optional] |
|**individualContributionsLessRefunds** | **BigDecimal** |  individual contributions less refunds  |  [optional] |
|**netReceipts** | **BigDecimal** |  Contributions received  |  [optional] |
|**offsetsToOperatingExpenditures** | **BigDecimal** | Offsets to operating expenditures |  [optional] |
|**operatingExpenditures** | **BigDecimal** | Total operating expenditures |  [optional] |
|**otherDisbursements** | **BigDecimal** | Other disbursements |  [optional] |
|**pacContributionsLessRefunds** | **BigDecimal** |  pac contributions less refunds  |  [optional] |
|**partyContributionsLessRefunds** | **BigDecimal** |  party contributions less refunds  |  [optional] |
|**repaymentsLoansMadeByCandidate** | **BigDecimal** |  repayments loans made by candidate  |  [optional] |
|**repaymentsOtherLoans** | **BigDecimal** |  repayments other loans  |  [optional] |
|**roundedNetReceipts** | **BigDecimal** |  Net receipts, in millions  |  [optional] |
|**totalContributionRefunds** | **BigDecimal** |  total contribution refunds  |  [optional] |
|**totalLoanRepaymentsMade** | **BigDecimal** |  total loan repayments made  |  [optional] |
|**transfersFromAffiliatedCommittees** | **BigDecimal** |  transfers from affiliated committees  |  [optional] |
|**transfersToOtherAuthorizedCommittees** | **BigDecimal** |  transfers to other authorized committees  |  [optional] |



