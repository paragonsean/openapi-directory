

# CommitteeReportsPacParty


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allLoansReceivedPeriod** | **BigDecimal** |  |  [optional] |
|**allLoansReceivedYtd** | **BigDecimal** |  |  [optional] |
|**allocatedFederalElectionLevinSharePeriod** | **BigDecimal** |  |  [optional] |
|**amendmentChain** | **List&lt;BigDecimal&gt;** |  The first value in the chain is the original filing.  The ordering in the chain reflects the order the amendments were filed up to the amendment being inspected.  |  [optional] |
|**amendmentIndicator** | **String** |  |  [optional] |
|**amendmentIndicatorFull** | **String** |  |  [optional] |
|**beginningImageNumber** | **String** |  |  [optional] |
|**calendarYtd** | **Integer** |  |  [optional] |
|**cashOnHandBeginningCalendarYtd** | **BigDecimal** |  |  [optional] |
|**cashOnHandBeginningPeriod** | **BigDecimal** | Balance for the committee at the start of the two-year period |  [optional] |
|**cashOnHandCloseYtd** | **BigDecimal** |  |  [optional] |
|**cashOnHandEndPeriod** | **BigDecimal** | Ending cash balance on the most recent filing |  [optional] |
|**committeeId** | **String** |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |  [optional] |
|**committeeName** | **String** | The name of the committee. If a committee changes its name,     the most recent name will be shown. Committee names are not unique. Use committee_id     for looking up records. |  [optional] |
|**committeeType** | **String** |  |  [optional] |
|**coordinatedExpendituresByPartyCommitteePeriod** | **BigDecimal** |  |  [optional] |
|**coordinatedExpendituresByPartyCommitteeYtd** | **BigDecimal** |  |  [optional] |
|**coverageEndDate** | **OffsetDateTime** | Ending date of the reporting period |  [optional] |
|**coverageStartDate** | **OffsetDateTime** | Beginning date of the reporting period |  [optional] |
|**csvUrl** | **String** |  |  [optional] |
|**cycle** | **Integer** |  Filter records to only those that are applicable to a given two-year period. This cycle follows the traditional House election cycle and subdivides the presidential and Senate elections into comparable two-year blocks. The cycle begins with an odd year and is named for its ending, even year.  |  [optional] |
|**debtsOwedByCommittee** | **BigDecimal** | Debts owed by the committee |  [optional] |
|**debtsOwedToCommittee** | **BigDecimal** | Debts owed to the committee |  [optional] |
|**documentDescription** | **String** |  |  [optional] |
|**endImageNumber** | **String** |  |  [optional] |
|**fecFileId** | **String** |  |  [optional] |
|**fecUrl** | **String** |  |  [optional] |
|**fedCandidateCommitteeContributionRefundsYtd** | **BigDecimal** |  |  [optional] |
|**fedCandidateCommitteeContributionsPeriod** | **BigDecimal** |  |  [optional] |
|**fedCandidateCommitteeContributionsYtd** | **BigDecimal** |  |  [optional] |
|**fedCandidateContributionRefundsPeriod** | **BigDecimal** |  |  [optional] |
|**fileNumber** | **Integer** |  |  [optional] |
|**htmlUrl** | **String** |  HTML link to the filing.  |  [optional] |
|**independentExpendituresPeriod** | **BigDecimal** |  |  [optional] |
|**independentExpendituresYtd** | **BigDecimal** |  |  [optional] |
|**individualItemizedContributionsPeriod** | **BigDecimal** | Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. total for the reporting period |  [optional] |
|**individualItemizedContributionsYtd** | **BigDecimal** | Individual itemized contributions are from individuals whose aggregate contributions total over $200 per individual per year. Be aware, some filers choose to itemize donations $200 or less. total for the year to date |  [optional] |
|**individualUnitemizedContributionsPeriod** | **BigDecimal** | Unitemized contributions are made individuals whose aggregate contributions total $200 or less per individual per year. Be aware, some filers choose to itemize donations $200 or less and in that case those donations will appear in the itemized total. total for the reporting period |  [optional] |
|**individualUnitemizedContributionsYtd** | **BigDecimal** | Unitemized contributions are made individuals whose aggregate contributions total $200 or less per individual per year. Be aware, some filers choose to itemize donations $200 or less and in that case those donations will appear in the itemized total. total for the year to date |  [optional] |
|**isAmended** | **Boolean** |  False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment.  |  [optional] |
|**loanRepaymentsMadePeriod** | **BigDecimal** |  |  [optional] |
|**loanRepaymentsMadeYtd** | **BigDecimal** |  |  [optional] |
|**loanRepaymentsReceivedPeriod** | **BigDecimal** |  |  [optional] |
|**loanRepaymentsReceivedYtd** | **BigDecimal** |  |  [optional] |
|**loansMadePeriod** | **BigDecimal** |  |  [optional] |
|**loansMadeYtd** | **BigDecimal** |  |  [optional] |
|**meansFiled** | **String** | The method used to file with the FEC, either electronic or on paper. |  [optional] |
|**mostRecent** | **Boolean** |  Report is either new or is the most-recently filed amendment  |  [optional] |
|**mostRecentFileNumber** | **BigDecimal** |  |  [optional] |
|**netContributionsPeriod** | **BigDecimal** |  |  [optional] |
|**netContributionsYtd** | **BigDecimal** |  |  [optional] |
|**netOperatingExpendituresPeriod** | **BigDecimal** |  |  [optional] |
|**netOperatingExpendituresYtd** | **BigDecimal** |  |  [optional] |
|**nonAllocatedFedElectionActivityPeriod** | **BigDecimal** |  |  [optional] |
|**nonAllocatedFedElectionActivityYtd** | **BigDecimal** |  |  [optional] |
|**nonfedShareAllocatedDisbursementsPeriod** | **BigDecimal** |  |  [optional] |
|**offsetsToOperatingExpendituresPeriod** | **BigDecimal** | Offsets to operating expenditures total for the reporting period |  [optional] |
|**offsetsToOperatingExpendituresYtd** | **BigDecimal** | Offsets to operating expenditures total for the year to date |  [optional] |
|**otherDisbursementsPeriod** | **BigDecimal** | Other disbursements total for the reporting period |  [optional] |
|**otherDisbursementsYtd** | **BigDecimal** | Other disbursements total for the year to date |  [optional] |
|**otherFedOperatingExpendituresPeriod** | **BigDecimal** |  |  [optional] |
|**otherFedOperatingExpendituresYtd** | **BigDecimal** |  |  [optional] |
|**otherFedReceiptsPeriod** | **BigDecimal** |  |  [optional] |
|**otherFedReceiptsYtd** | **BigDecimal** |  |  [optional] |
|**otherPoliticalCommitteeContributionsPeriod** | **BigDecimal** | Other committees contributions total for the reporting period |  [optional] |
|**otherPoliticalCommitteeContributionsYtd** | **BigDecimal** | Other committees contributions total for the year to date |  [optional] |
|**pdfUrl** | **String** |  |  [optional] |
|**politicalPartyCommitteeContributionsPeriod** | **BigDecimal** | Party committees contributions total for the reporting period |  [optional] |
|**politicalPartyCommitteeContributionsYtd** | **BigDecimal** | Party committees contributions total for the year to date |  [optional] |
|**previousFileNumber** | **BigDecimal** |  |  [optional] |
|**receiptDate** | **LocalDate** | Date the FEC received the electronic or paper record |  [optional] |
|**refundedIndividualContributionsPeriod** | **BigDecimal** | Individual refunds total for the reporting period |  [optional] |
|**refundedIndividualContributionsYtd** | **BigDecimal** | Individual refunds total for the year to date |  [optional] |
|**refundedOtherPoliticalCommitteeContributionsPeriod** | **BigDecimal** | Other committee refunds total for the reporting period |  [optional] |
|**refundedOtherPoliticalCommitteeContributionsYtd** | **BigDecimal** | Other committee refunds total for the year to date |  [optional] |
|**refundedPoliticalPartyCommitteeContributionsPeriod** | **BigDecimal** | Political party refunds total for the reporting period |  [optional] |
|**refundedPoliticalPartyCommitteeContributionsYtd** | **BigDecimal** | Political party refunds total for the year to date |  [optional] |
|**reportForm** | **String** |  |  [optional] |
|**reportType** | **String** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  |  [optional] |
|**reportTypeFull** | **String** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  |  [optional] |
|**reportYear** | **Integer** |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  |  [optional] |
|**sharedFedActivityNonfedYtd** | **BigDecimal** |  |  [optional] |
|**sharedFedActivityPeriod** | **BigDecimal** |  |  [optional] |
|**sharedFedActivityYtd** | **BigDecimal** |  |  [optional] |
|**sharedFedOperatingExpendituresPeriod** | **BigDecimal** |  |  [optional] |
|**sharedFedOperatingExpendituresYtd** | **BigDecimal** |  |  [optional] |
|**sharedNonfedOperatingExpendituresPeriod** | **BigDecimal** |  |  [optional] |
|**sharedNonfedOperatingExpendituresYtd** | **BigDecimal** |  |  [optional] |
|**subtotalSummaryPagePeriod** | **BigDecimal** |  |  [optional] |
|**subtotalSummaryYtd** | **BigDecimal** |  |  [optional] |
|**totalContributionRefundsPeriod** | **BigDecimal** | Total contribution refunds total for the reporting period |  [optional] |
|**totalContributionRefundsYtd** | **BigDecimal** | Total contribution refunds total for the year to date |  [optional] |
|**totalContributionsPeriod** | **BigDecimal** | Contribution total for the reporting period |  [optional] |
|**totalContributionsYtd** | **BigDecimal** | Contribution total for the year to date |  [optional] |
|**totalDisbursementsPeriod** | **BigDecimal** | Disbursements total for the reporting period |  [optional] |
|**totalDisbursementsYtd** | **BigDecimal** | Disbursements total for the year to date |  [optional] |
|**totalFedDisbursementsPeriod** | **BigDecimal** |  |  [optional] |
|**totalFedDisbursementsYtd** | **BigDecimal** |  |  [optional] |
|**totalFedElectionActivityPeriod** | **BigDecimal** |  |  [optional] |
|**totalFedElectionActivityYtd** | **BigDecimal** |  |  [optional] |
|**totalFedOperatingExpendituresPeriod** | **BigDecimal** |  |  [optional] |
|**totalFedOperatingExpendituresYtd** | **BigDecimal** |  |  [optional] |
|**totalFedReceiptsPeriod** | **BigDecimal** |  |  [optional] |
|**totalFedReceiptsYtd** | **BigDecimal** |  |  [optional] |
|**totalIndividualContributionsPeriod** | **BigDecimal** | Individual contributions total for the reporting period |  [optional] |
|**totalIndividualContributionsYtd** | **BigDecimal** | Individual contributions total for the year to date |  [optional] |
|**totalNonfedTransfersPeriod** | **BigDecimal** |  |  [optional] |
|**totalNonfedTransfersYtd** | **BigDecimal** |  |  [optional] |
|**totalOperatingExpendituresPeriod** | **BigDecimal** |  |  [optional] |
|**totalOperatingExpendituresYtd** | **BigDecimal** |  |  [optional] |
|**totalReceiptsPeriod** | **BigDecimal** | Anything of value (money, goods, services or property) received by a political committee total for the reporting period |  [optional] |
|**totalReceiptsYtd** | **BigDecimal** | Anything of value (money, goods, services or property) received by a political committee total for the year to date |  [optional] |
|**transfersFromAffiliatedPartyPeriod** | **BigDecimal** |  |  [optional] |
|**transfersFromAffiliatedPartyYtd** | **BigDecimal** |  |  [optional] |
|**transfersFromNonfedAccountPeriod** | **BigDecimal** |  |  [optional] |
|**transfersFromNonfedAccountYtd** | **BigDecimal** |  |  [optional] |
|**transfersFromNonfedLevinPeriod** | **BigDecimal** |  |  [optional] |
|**transfersFromNonfedLevinYtd** | **BigDecimal** |  |  [optional] |
|**transfersToAffiliatedCommitteePeriod** | **BigDecimal** |  |  [optional] |
|**transfersToAffilitatedCommitteesYtd** | **BigDecimal** |  |  [optional] |



