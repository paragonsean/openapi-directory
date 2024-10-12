

# ScheduleE


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionCode** | **String** |  |  [optional] |
|**actionCodeFull** | **String** |  |  [optional] |
|**amendmentIndicator** | **String** | Amendent types:     -N   new     -A   amendment     -T   terminated     -C   consolidated     -M   multi-candidate     -S   secondary  NULL might be new or amendment. If amendment indicator is null and the filings is the first or first in a chain treat it as if it was a new. If it is not the first or first in a chain then treat the filing as an amendment.  |  [optional] |
|**amendmentNumber** | **Integer** |  Number of times the report has been amended.  |  [optional] |
|**backReferenceScheduleName** | **String** |  |  [optional] |
|**backReferenceTransactionId** | **String** |  |  [optional] |
|**candidate** | **String** |  |  [optional] |
|**candidateFirstName** | **String** |  |  [optional] |
|**candidateId** | **String** |  |  [optional] |
|**candidateLastName** | **String** |  |  [optional] |
|**candidateMiddleName** | **String** |  |  [optional] |
|**candidateName** | **String** | Name of candidate running for office |  [optional] |
|**candidateOffice** | **String** | Federal office candidate runs for: H, S or P |  [optional] |
|**candidateOfficeDistrict** | **String** | Two-digit US House distirict of the office the candidate is running for. Presidential, Senate and House at-large candidates will have District 00. |  [optional] |
|**candidateOfficeState** | **String** | US state or territory |  [optional] |
|**candidateParty** | **String** | Three-letter code for the party affiliated with a candidate or committee. For example, DEM for Democratic Party and REP for Republican Party. |  [optional] |
|**candidatePrefix** | **String** |  |  [optional] |
|**candidateSuffix** | **String** |  |  [optional] |
|**categoryCode** | **String** |  |  [optional] |
|**categoryCodeFull** | **String** |  |  [optional] |
|**committee** | [**CommitteeHistory**](CommitteeHistory.md) |  |  [optional] |
|**committeeId** | **String** |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  |  [optional] |
|**conduitCommitteeCity** | **String** |  |  [optional] |
|**conduitCommitteeId** | **String** |  |  [optional] |
|**conduitCommitteeName** | **String** |  |  [optional] |
|**conduitCommitteeState** | **String** |  |  [optional] |
|**conduitCommitteeStreet1** | **String** |  |  [optional] |
|**conduitCommitteeStreet2** | **String** |  |  [optional] |
|**conduitCommitteeZip** | **Integer** |  |  [optional] |
|**disseminationDate** | **LocalDate** |  |  [optional] |
|**electionType** | **String** | Election type  Convention, Primary, General, Special, Runoff etc.  |  [optional] |
|**electionTypeFull** | **String** | Election type  Convention, Primary, General, Special, Runoff etc.  |  [optional] |
|**expenditureAmount** | **BigDecimal** |  |  [optional] |
|**expenditureDate** | **LocalDate** |  |  [optional] |
|**expenditureDescription** | **String** |  |  [optional] |
|**fileNumber** | **Integer** |  |  [optional] |
|**filerFirstName** | **String** |  |  [optional] |
|**filerLastName** | **String** |  |  [optional] |
|**filerMiddleName** | **String** |  |  [optional] |
|**filerPrefix** | **String** |  |  [optional] |
|**filerSuffix** | **String** |  |  [optional] |
|**filingDate** | **LocalDate** |  |  [optional] |
|**filingForm** | **String** |  |  [optional] |
|**imageNumber** | **String** |  |  [optional] |
|**independentSignDate** | **LocalDate** |  |  [optional] |
|**independentSignName** | **String** |  |  [optional] |
|**isNotice** | **Boolean** |  |  [optional] |
|**lineNumber** | **String** |  |  [optional] |
|**linkId** | **Integer** |  |  [optional] |
|**memoCode** | **String** |  |  [optional] |
|**memoCodeFull** | **String** |  |  [optional] |
|**memoText** | **String** |  |  [optional] |
|**memoedSubtotal** | **Boolean** |  |  [optional] |
|**mostRecent** | **Boolean** |  Report is either new or is the most-recently filed amendment  |  [optional] |
|**notaryCommissionExpirationDate** | **LocalDate** |  |  [optional] |
|**notarySignDate** | **LocalDate** |  |  [optional] |
|**notarySignName** | **String** |  |  [optional] |
|**officeTotalYtd** | **BigDecimal** |  |  [optional] |
|**originalSubId** | **String** |  |  [optional] |
|**payeeCity** | **String** |  |  [optional] |
|**payeeFirstName** | **String** |  |  [optional] |
|**payeeLastName** | **String** |  |  [optional] |
|**payeeMiddleName** | **String** |  |  [optional] |
|**payeeName** | **String** |  |  [optional] |
|**payeePrefix** | **String** |  |  [optional] |
|**payeeState** | **String** |  |  [optional] |
|**payeeStreet1** | **String** |  |  [optional] |
|**payeeStreet2** | **String** |  |  [optional] |
|**payeeSuffix** | **String** |  |  [optional] |
|**payeeZip** | **String** |  |  [optional] |
|**pdfUrl** | **String** |  |  [optional] |
|**previousFileNumber** | **Integer** |  |  [optional] |
|**reportType** | **String** | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  |  [optional] |
|**reportYear** | **Integer** |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  |  [optional] |
|**scheduleType** | **String** |  |  [optional] |
|**scheduleTypeFull** | **String** |  |  [optional] |
|**subId** | **String** |  |  [optional] |
|**supportOpposeIndicator** | **String** |  |  [optional] |
|**transactionId** | **String** |  |  [optional] |



