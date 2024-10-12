# ProductFinderApi.FeeChargeDetailInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationFrequency** | **String** | How frequently the fee/charge is applied to the account | 
**calculationFrequency** | **String** | How frequently the fee/charge is calculated | 
**feeAmount** | **String** | Fee Amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate) | [optional] 
**feeApplicableRange** | **Object** | Range or amounts or rates for which the fee/charge applies | [optional] 
**feeCategory** | **String** | Categorisation of fees and charges into standard categories. | 
**feeRate** | **String** | Rate charged for Fee/Charge (where it is charged in terms of a rate rather than an amount) | [optional] 
**feeRateType** | **String** | Rate type for Fee/Charge (where it is charged in terms of a rate rather than an amount) | [optional] 
**feeType** | **String** | Fee/Charge Type | 
**includedInMonthlyChargeIndicator** | **Boolean** | Indicates that fee/charge is already included in the monthly charge. | [optional] 
**negotiableIndicator** | **Boolean** | Fee/charge which is usually negotiable rather than a fixed amount | [optional] 
**notes** | **[String]** | Optional additional notes to supplement the fee/charge details. | [optional] 
**otherApplicationFrequency** | **Object** | Other application frequencies not covered in the standard code list | [optional] 
**otherCalculationFrequency** | **Object** | Other calculation frequency which is not available in standard code set. | [optional] 
**otherFeeCategory** | **Object** |  | [optional] 
**otherFeeRateType** | **Object** | Other fee rate type which is not available in the standard code set | [optional] 
**otherFeeType** | **Object** | Other Fee/charge type which is not available in the standard code set | [optional] 



## Enum: ApplicationFrequencyEnum


* `OnClosing` (value: `"OnClosing"`)

* `OnOpening` (value: `"OnOpening"`)

* `ChargingPeriod` (value: `"ChargingPeriod"`)

* `Daily` (value: `"Daily"`)

* `PerItem` (value: `"PerItem"`)

* `Monthly` (value: `"Monthly"`)

* `OnAnniversary` (value: `"OnAnniversary"`)

* `Other` (value: `"Other"`)

* `PerHundredPounds` (value: `"PerHundredPounds"`)

* `PerHour` (value: `"PerHour"`)

* `PerOccurrence` (value: `"PerOccurrence"`)

* `PerSheet` (value: `"PerSheet"`)

* `PerTransaction` (value: `"PerTransaction"`)

* `PerTransactionAmount` (value: `"PerTransactionAmount"`)

* `PerTransactionPercentage` (value: `"PerTransactionPercentage"`)

* `Quarterly` (value: `"Quarterly"`)

* `SixMonthly` (value: `"SixMonthly"`)

* `StatementMonthly` (value: `"StatementMonthly"`)

* `Weekly` (value: `"Weekly"`)

* `Yearly` (value: `"Yearly"`)





## Enum: CalculationFrequencyEnum


* `OnClosing` (value: `"OnClosing"`)

* `OnOpening` (value: `"OnOpening"`)

* `ChargingPeriod` (value: `"ChargingPeriod"`)

* `Daily` (value: `"Daily"`)

* `PerItem` (value: `"PerItem"`)

* `Monthly` (value: `"Monthly"`)

* `OnAnniversary` (value: `"OnAnniversary"`)

* `Other` (value: `"Other"`)

* `PerHundredPounds` (value: `"PerHundredPounds"`)

* `PerHour` (value: `"PerHour"`)

* `PerOccurrence` (value: `"PerOccurrence"`)

* `PerSheet` (value: `"PerSheet"`)

* `PerTransaction` (value: `"PerTransaction"`)

* `PerTransactionAmount` (value: `"PerTransactionAmount"`)

* `PerTransactionPercentage` (value: `"PerTransactionPercentage"`)

* `Quarterly` (value: `"Quarterly"`)

* `SixMonthly` (value: `"SixMonthly"`)

* `StatementMonthly` (value: `"StatementMonthly"`)

* `Weekly` (value: `"Weekly"`)

* `Yearly` (value: `"Yearly"`)





## Enum: FeeCategoryEnum


* `Auto` (value: `"Auto"`)

* `ATM` (value: `"ATM"`)

* `BankersDrafts` (value: `"BankersDrafts"`)

* `Card` (value: `"Card"`)

* `Cheque` (value: `"Cheque"`)

* `CounterServices` (value: `"CounterServices"`)

* `DirectDebit` (value: `"DirectDebit"`)

* `Deeds` (value: `"Deeds"`)

* `Foreign` (value: `"Foreign"`)

* `FX` (value: `"FX"`)

* `International` (value: `"International"`)

* `Investigation` (value: `"Investigation"`)

* `Legal` (value: `"Legal"`)

* `Loan` (value: `"Loan"`)

* `NightSafe` (value: `"NightSafe"`)

* `Online` (value: `"Online"`)

* `Other` (value: `"Other"`)

* `PostOffice` (value: `"PostOffice"`)

* `PaymentScheme` (value: `"PaymentScheme"`)

* `Report` (value: `"Report"`)

* `Safekeeping` (value: `"Safekeeping"`)

* `Servicing` (value: `"Servicing"`)

* `Transaction` (value: `"Transaction"`)





## Enum: FeeRateTypeEnum


* `Gross` (value: `"Gross"`)

* `Other` (value: `"Other"`)





## Enum: FeeTypeEnum


* `ATMDeposATMPaidIn` (value: `"ATMDeposATMPaidIn"`)

* `ReportCertBalance` (value: `"ReportCertBalance"`)

* `ATMAbroadConVisaDebit` (value: `"ATMAbroadConVisaDebit"`)

* `ATMCardnetEnvIn` (value: `"ATMCardnetEnvIn"`)

* `ATMCashGroupATMDebitCard` (value: `"ATMCashGroupATMDebitCard"`)

* `ATMCashNonGroupATMDebitcard` (value: `"ATMCashNonGroupATMDebitcard"`)

* `ATMConGroupATM` (value: `"ATMConGroupATM"`)

* `ATMAbroad` (value: `"ATMAbroad"`)

* `ATMForeignCashDebCard` (value: `"ATMForeignCashDebCard"`)

* `ATMAbroadGoldVisaDebit` (value: `"ATMAbroadGoldVisaDebit"`)

* `ATMNonSterlingWithdrawal` (value: `"ATMNonSterlingWithdrawal"`)

* `ATMAbroadVisaDebit` (value: `"ATMAbroadVisaDebit"`)

* `ATMWithdrawCash` (value: `"ATMWithdrawCash"`)

* `BACSOnLineAncilliary` (value: `"BACSOnLineAncilliary"`)

* `BACSBatch` (value: `"BACSBatch"`)

* `BACSOnLineFile` (value: `"BACSOnLineFile"`)

* `BACSItem` (value: `"BACSItem"`)

* `BACSBulkBatch` (value: `"BACSBulkBatch"`)

* `BACSOnLineOverlimit` (value: `"BACSOnLineOverlimit"`)

* `BACSOnLinePayment` (value: `"BACSOnLinePayment"`)

* `BACSOnLineService` (value: `"BACSOnLineService"`)

* `BACSBulkInternet` (value: `"BACSBulkInternet"`)

* `BACSTELDirDebSmartCard` (value: `"BACSTELDirDebSmartCard"`)

* `BACSTELDirDebWebInit` (value: `"BACSTELDirDebWebInit"`)

* `BACSTELirDebWebInit` (value: `"BACSTELirDebWebInit"`)

* `BACSTELDirDebOverlimit` (value: `"BACSTELDirDebOverlimit"`)

* `BACSTELDirDebPayment` (value: `"BACSTELDirDebPayment"`)

* `BACSTELDirDebService` (value: `"BACSTELDirDebService"`)

* `BACSTELDirDebAncilliary` (value: `"BACSTELDirDebAncilliary"`)

* `BACSTELAncilliary` (value: `"BACSTELAncilliary"`)

* `BACSTELSmartCard` (value: `"BACSTELSmartCard"`)

* `BACSTELFile` (value: `"BACSTELFile"`)

* `BACSTELOverlimit` (value: `"BACSTELOverlimit"`)

* `BACSTELPayment` (value: `"BACSTELPayment"`)

* `BACSTELService` (value: `"BACSTELService"`)

* `CHAPSOutBranch` (value: `"CHAPSOutBranch"`)

* `CHAPSOutOnlineDepositAcc` (value: `"CHAPSOutOnlineDepositAcc"`)

* `CHAPSIn` (value: `"CHAPSIn"`)

* `CHAPSOutPost` (value: `"CHAPSOutPost"`)

* `CHAPSOut` (value: `"CHAPSOut"`)

* `CHAPSOutOnline` (value: `"CHAPSOutOnline"`)

* `CHAPSOutManual` (value: `"CHAPSOutManual"`)

* `CardCardReplacement` (value: `"CardCardReplacement"`)

* `DraftsBankers` (value: `"DraftsBankers"`)

* `DraftsCancellation` (value: `"DraftsCancellation"`)

* `CardGuaranteed` (value: `"CardGuaranteed"`)

* `DraftsIntlPayableAbroad` (value: `"DraftsIntlPayableAbroad"`)

* `DraftsIntlStoppedCancelled` (value: `"DraftsIntlStoppedCancelled"`)

* `EuroChqXLess` (value: `"EuroChqXLess"`)

* `EuroChqXPlus` (value: `"EuroChqXPlus"`)

* `FPSOut` (value: `"FPSOut"`)

* `FPSOutOwn` (value: `"FPSOutOwn"`)

* `FPSInBranch` (value: `"FPSInBranch"`)

* `LegalArticlesReport` (value: `"LegalArticlesReport"`)

* `LegalSealing` (value: `"LegalSealing"`)

* `LegalBondAndGuarantee` (value: `"LegalBondAndGuarantee"`)

* `LegalCoSearch` (value: `"LegalCoSearch"`)

* `LegalDepositAssignment` (value: `"LegalDepositAssignment"`)

* `LegalGuaranteePrep` (value: `"LegalGuaranteePrep"`)

* `LegalLifePolicyPrepCo` (value: `"LegalLifePolicyPrepCo"`)

* `LegalLifePolicyPrepPersonal` (value: `"LegalLifePolicyPrepPersonal"`)

* `LegalPriorityPariPassu` (value: `"LegalPriorityPariPassu"`)

* `LegalSubordinationAgreement` (value: `"LegalSubordinationAgreement"`)

* `DirDebDirectDebitAdmin` (value: `"DirDebDirectDebitAdmin"`)

* `DirDebDirectDebitCancel` (value: `"DirDebDirectDebitCancel"`)

* `IntlPayBIBForeignLimit` (value: `"IntlPayBIBForeignLimit"`)

* `IntlPayCreditTransCust` (value: `"IntlPayCreditTransCust"`)

* `IntlPayCreditTransNonCust` (value: `"IntlPayCreditTransNonCust"`)

* `IntlPayExpressMoneyMover` (value: `"IntlPayExpressMoneyMover"`)

* `IntlPayEEAPayUrgent` (value: `"IntlPayEEAPayUrgent"`)

* `IntlPayIrishPayUrgent` (value: `"IntlPayIrishPayUrgent"`)

* `IntlPayEEAPay` (value: `"IntlPayEEAPay"`)

* `IntlPayFXPaymentIn` (value: `"IntlPayFXPaymentIn"`)

* `IntlPayForeignIn1CPlus` (value: `"IntlPayForeignIn1CPlus"`)

* `IntlPayForeignCharge` (value: `"IntlPayForeignCharge"`)

* `IntlPayForeignInternet` (value: `"IntlPayForeignInternet"`)

* `IntlPayForeignInSub1C` (value: `"IntlPayForeignInSub1C"`)

* `IntlPayPurchaseNonSterling` (value: `"IntlPayPurchaseNonSterling"`)

* `IntlPayPaymentTracing` (value: `"IntlPayPaymentTracing"`)

* `IntlPayStandardMoneyMover` (value: `"IntlPayStandardMoneyMover"`)

* `IntlPayMT101Transaction` (value: `"IntlPayMT101Transaction"`)

* `IntlPayWorldpayPayment` (value: `"IntlPayWorldpayPayment"`)

* `InvPayBankDetailsWrong` (value: `"InvPayBankDetailsWrong"`)

* `InvPayForeignBCNR` (value: `"InvPayForeignBCNR"`)

* `InvPayForeignRecall` (value: `"InvPayForeignRecall"`)

* `InvGeneralInq` (value: `"InvGeneralInq"`)

* `InvOldInstruction` (value: `"InvOldInstruction"`)

* `InvPayReturnDebitXVLess` (value: `"InvPayReturnDebitXVLess"`)

* `InvPayReturnDebitXVPlus` (value: `"InvPayReturnDebitXVPlus"`)

* `InvPayStopPayment` (value: `"InvPayStopPayment"`)

* `InvPayStandingOrdUnpaid` (value: `"InvPayStandingOrdUnpaid"`)

* `SafeKeepAccess` (value: `"SafeKeepAccess"`)

* `SafeKeepDeedMedium` (value: `"SafeKeepDeedMedium"`)

* `SafeKeepingEnvelope` (value: `"SafeKeepingEnvelope"`)

* `SafeKeepingInspection` (value: `"SafeKeepingInspection"`)

* `SafeKeepingLargeItem` (value: `"SafeKeepingLargeItem"`)

* `SafeKeepMultipleItems` (value: `"SafeKeepMultipleItems"`)

* `SafeKeepingParcel` (value: `"SafeKeepingParcel"`)

* `SafeKeepDeedSmall` (value: `"SafeKeepDeedSmall"`)

* `SafeKeepOneItem` (value: `"SafeKeepOneItem"`)

* `LoanArrangement` (value: `"LoanArrangement"`)

* `NightSafeNightSafeBankOpen` (value: `"NightSafeNightSafeBankOpen"`)

* `NightSafeCreditSub5K` (value: `"NightSafeCreditSub5K"`)

* `NightSafeNightSafe` (value: `"NightSafeNightSafe"`)

* `NightSafeNightSafePaidIn` (value: `"NightSafeNightSafePaidIn"`)

* `POPostOfficeCounterCredit` (value: `"POPostOfficeCounterCredit"`)

* `POPostOfficeCashCredit` (value: `"POPostOfficeCashCredit"`)

* `POPostOfficeCashOut` (value: `"POPostOfficeCashOut"`)

* `POPostOfficeWithdrawal` (value: `"POPostOfficeWithdrawal"`)

* `ChqBookTheftLossAllStopped` (value: `"ChqBookTheftLossAllStopped"`)

* `ChqIssuedCurrencyAcc` (value: `"ChqIssuedCurrencyAcc"`)

* `ChqCopy` (value: `"ChqCopy"`)

* `ChqDraft` (value: `"ChqDraft"`)

* `ChqIn` (value: `"ChqIn"`)

* `ChqSpecialChqClearance` (value: `"ChqSpecialChqClearance"`)

* `ChqOutIssued` (value: `"ChqOutIssued"`)

* `ChqSpecialChqPresentation` (value: `"ChqSpecialChqPresentation"`)

* `ChqCounterCheque` (value: `"ChqCounterCheque"`)

* `ChqChequeswithStatement` (value: `"ChqChequeswithStatement"`)

* `ChqStopped` (value: `"ChqStopped"`)

* `ChqTrans` (value: `"ChqTrans"`)

* `ChqDraftFX` (value: `"ChqDraftFX"`)

* `ChqForeignCourier` (value: `"ChqForeignCourier"`)

* `ChqForeignNegTenThou` (value: `"ChqForeignNegTenThou"`)

* `ChqForeignNegHundred` (value: `"ChqForeignNegHundred"`)

* `ChequeForeignBankDivi` (value: `"ChequeForeignBankDivi"`)

* `ChqForeignNegFiftyThou` (value: `"ChqForeignNegFiftyThou"`)

* `ChqPensionCheque` (value: `"ChqPensionCheque"`)

* `ChequeForeignOtherDivi` (value: `"ChequeForeignOtherDivi"`)

* `ChqForeignNegFiveThou` (value: `"ChqForeignNegFiveThou"`)

* `ChqForeignNegMax` (value: `"ChqForeignNegMax"`)

* `ChqForeignGBPMMDPlus` (value: `"ChqForeignGBPMMDPlus"`)

* `ChqGiftCheque` (value: `"ChqGiftCheque"`)

* `ChqCounterLodgement` (value: `"ChqCounterLodgement"`)

* `ChqCashDropLodgement` (value: `"ChqCashDropLodgement"`)

* `ChqForeign` (value: `"ChqForeign"`)

* `ChqChequePhotocopy` (value: `"ChqChequePhotocopy"`)

* `ChqPostOfficeCredit` (value: `"ChqPostOfficeCredit"`)

* `ChqPostOfficeChequeCollected` (value: `"ChqPostOfficeChequeCollected"`)

* `ChqChequeRetrieval` (value: `"ChqChequeRetrieval"`)

* `ChqReconcilliationPerTrans` (value: `"ChqReconcilliationPerTrans"`)

* `ChqSpecialPresentationCount` (value: `"ChqSpecialPresentationCount"`)

* `ChqSpecialPresentationPTT` (value: `"ChqSpecialPresentationPTT"`)

* `ChqDraftSterling` (value: `"ChqDraftSterling"`)

* `ChqUnpaidCharge` (value: `"ChqUnpaidCharge"`)

* `ChqUnpaidTransIn` (value: `"ChqUnpaidTransIn"`)

* `ChqUnpaidTransOut` (value: `"ChqUnpaidTransOut"`)

* `ChqUnpaidCheque` (value: `"ChqUnpaidCheque"`)

* `ReportAuditLetter` (value: `"ReportAuditLetter"`)

* `ReportFAXAdviceAdditional` (value: `"ReportFAXAdviceAdditional"`)

* `ReportTelAdviceAdditional` (value: `"ReportTelAdviceAdditional"`)

* `ReportCreditHistory` (value: `"ReportCreditHistory"`)

* `ReportCertInterestDuplicate` (value: `"ReportCertInterestDuplicate"`)

* `ReportCertInterest` (value: `"ReportCertInterest"`)

* `ReportCreditHistoryAdditionalInYear` (value: `"ReportCreditHistoryAdditionalInYear"`)

* `ReportForeignStatusEnqElec` (value: `"ReportForeignStatusEnqElec"`)

* `ReportForeignStatusEnq` (value: `"ReportForeignStatusEnq"`)

* `ReportStatementChqDaily` (value: `"ReportStatementChqDaily"`)

* `ReportStatementChqFortnightly` (value: `"ReportStatementChqFortnightly"`)

* `ReportStatementChqMonthly` (value: `"ReportStatementChqMonthly"`)

* `ReportStatementChqWeekly` (value: `"ReportStatementChqWeekly"`)

* `ReportStatementAndDiviChq` (value: `"ReportStatementAndDiviChq"`)

* `ReportReferralItem` (value: `"ReportReferralItem"`)

* `ReportStatementByATM` (value: `"ReportStatementByATM"`)

* `ReportStatementByBranch` (value: `"ReportStatementByBranch"`)

* `ReportStatementCopyRegular` (value: `"ReportStatementCopyRegular"`)

* `ReportStatementDaily` (value: `"ReportStatementDaily"`)

* `ReportStatusEnquiry` (value: `"ReportStatusEnquiry"`)

* `ReportStatementFrequent` (value: `"ReportStatementFrequent"`)

* `ReportStatementMonthly` (value: `"ReportStatementMonthly"`)

* `ReportStatementCopy1` (value: `"ReportStatementCopy1"`)

* `ReportStatementToBranch` (value: `"ReportStatementToBranch"`)

* `ReportSMSTextMiniStatementorAlert` (value: `"ReportSMSTextMiniStatementorAlert"`)

* `ReportStatementFortnightly` (value: `"ReportStatementFortnightly"`)

* `ReportSMSTextMiniStatementWoM` (value: `"ReportSMSTextMiniStatementWoM"`)

* `ReportSMSTextAlertBalance` (value: `"ReportSMSTextAlertBalance"`)

* `ReportSMSTextAlert` (value: `"ReportSMSTextAlert"`)

* `ReportTaxCert` (value: `"ReportTaxCert"`)

* `ReportWeeklyStatement` (value: `"ReportWeeklyStatement"`)

* `SEPABranch` (value: `"SEPABranch"`)

* `SEPACredit` (value: `"SEPACredit"`)

* `SEPADirectDebit` (value: `"SEPADirectDebit"`)

* `SEPAIn` (value: `"SEPAIn"`)

* `SEPAEuro` (value: `"SEPAEuro"`)

* `SEPAOut` (value: `"SEPAOut"`)

* `SEPAUnpaid` (value: `"SEPAUnpaid"`)

* `SEPAWinbitsTransaction` (value: `"SEPAWinbitsTransaction"`)

* `TransBillPaymentBranch` (value: `"TransBillPaymentBranch"`)

* `TransBillCollect` (value: `"TransBillCollect"`)

* `TransTelephoneBillPayment` (value: `"TransTelephoneBillPayment"`)

* `TransBankPayment` (value: `"TransBankPayment"`)

* `TransBillPaymentTelephone` (value: `"TransBillPaymentTelephone"`)

* `TransCorrespondentBankFee` (value: `"TransCorrespondentBankFee"`)

* `TransCreditTransferUKDifferent` (value: `"TransCreditTransferUKDifferent"`)

* `TransCreditTransferUKSame` (value: `"TransCreditTransferUKSame"`)

* `TransCredit` (value: `"TransCredit"`)

* `TransCreditTransfer` (value: `"TransCreditTransfer"`)

* `TransBranchCredit` (value: `"TransBranchCredit"`)

* `TransDebit` (value: `"TransDebit"`)

* `TransDebCardDeb` (value: `"TransDebCardDeb"`)

* `TransUKDirDeb` (value: `"TransUKDirDeb"`)

* `TransManualDeb` (value: `"TransManualDeb"`)

* `TitleDeeds` (value: `"TitleDeeds"`)

* `TransBuyForeignWithGBP` (value: `"TransBuyForeignWithGBP"`)

* `TransGoodValueReq` (value: `"TransGoodValueReq"`)

* `TransSWIFTOutUKForeign` (value: `"TransSWIFTOutUKForeign"`)

* `TransInconpleteInstruction` (value: `"TransInconpleteInstruction"`)

* `TransManualEntries` (value: `"TransManualEntries"`)

* `TransManualTrans` (value: `"TransManualTrans"`)

* `TransNonSterling` (value: `"TransNonSterling"`)

* `Other` (value: `"Other"`)

* `TransPOSSaleForeign` (value: `"TransPOSSaleForeign"`)

* `TransPriPaymentPost` (value: `"TransPriPaymentPost"`)

* `TransPOSSaleUK` (value: `"TransPOSSaleUK"`)

* `TransReconciliationPerTrans` (value: `"TransReconciliationPerTrans"`)

* `TransStandingOrdAdmin` (value: `"TransStandingOrdAdmin"`)

* `TransStandingOrd` (value: `"TransStandingOrd"`)

* `TransStandingOrdManPay` (value: `"TransStandingOrdManPay"`)

* `TransTelBusiPriPaymentForeignToUKAcc` (value: `"TransTelBusiPriPaymentForeignToUKAcc"`)

* `TransTeleItem` (value: `"TransTeleItem"`)

* `TransTelBusiPriPaymentToGrpAcc` (value: `"TransTelBusiPriPaymentToGrpAcc"`)

* `TransTransferExGroup` (value: `"TransTransferExGroup"`)

* `TransTelBusiPriPaymentToNonGrpAcc` (value: `"TransTelBusiPriPaymentToNonGrpAcc"`)

* `TransSWIFTOutNonEEASterling` (value: `"TransSWIFTOutNonEEASterling"`)

* `AutoAutoCredit` (value: `"AutoAutoCredit"`)

* `AutoAutomatedEntries` (value: `"AutoAutomatedEntries"`)

* `AutoAutoCreditPhoneInet` (value: `"AutoAutoCreditPhoneInet"`)

* `AutoAutomatedTrans` (value: `"AutoAutomatedTrans"`)

* `AutoDebitCardCommercial` (value: `"AutoDebitCardCommercial"`)

* `AutoFPSAutoCredit` (value: `"AutoFPSAutoCredit"`)

* `VisaTravellersChqorCurrency` (value: `"VisaTravellersChqorCurrency"`)

* `OnlineInternetBillPayment` (value: `"OnlineInternetBillPayment"`)

* `OnlineBusinessOnlineEuroPayment` (value: `"OnlineBusinessOnlineEuroPayment"`)

* `OnlineBusinessOnlineUrgentEuroPayment` (value: `"OnlineBusinessOnlineUrgentEuroPayment"`)

* `OnlineBusinessOnlineForeignPayment` (value: `"OnlineBusinessOnlineForeignPayment"`)

* `OnlineInterbankTransfer` (value: `"OnlineInterbankTransfer"`)

* `OnlineInterbankPerTransfer` (value: `"OnlineInterbankPerTransfer"`)

* `OnlineInterbranchTransfer` (value: `"OnlineInterbranchTransfer"`)

* `OnlineInterbranchPerTransfer` (value: `"OnlineInterbranchPerTransfer"`)

* `OnlineSubscriptionMonthly` (value: `"OnlineSubscriptionMonthly"`)

* `OnlineBankingPayment` (value: `"OnlineBankingPayment"`)

* `OnlineReplacementCardReader` (value: `"OnlineReplacementCardReader"`)

* `OnlinePaymentinGBPtoUK` (value: `"OnlinePaymentinGBPtoUK"`)

* `OnlineUrgentPayment` (value: `"OnlineUrgentPayment"`)

* `OnlinePaymentinUSDtoUS` (value: `"OnlinePaymentinUSDtoUS"`)

* `OnlineBulkDirectDebSterling` (value: `"OnlineBulkDirectDebSterling"`)

* `ForeignChqSent` (value: `"ForeignChqSent"`)

* `ForeignChqSelf` (value: `"ForeignChqSelf"`)

* `ForeignChqEncashment` (value: `"ForeignChqEncashment"`)

* `ForeignFXInwardsCust` (value: `"ForeignFXInwardsCust"`)

* `ForeignFXTransfersROI` (value: `"ForeignFXTransfersROI"`)

* `ForeignFXForwardTrans` (value: `"ForeignFXForwardTrans"`)

* `ForeignExMaintenance` (value: `"ForeignExMaintenance"`)

* `ForeignFXInwardsNonCust` (value: `"ForeignFXInwardsNonCust"`)

* `ForeignFXOutwards` (value: `"ForeignFXOutwards"`)

* `ForeignPurchase` (value: `"ForeignPurchase"`)

* `ForeignStatusRep` (value: `"ForeignStatusRep"`)

* `ForeignChqDraft` (value: `"ForeignChqDraft"`)

* `ForeignChqCLess` (value: `"ForeignChqCLess"`)

* `ForeignChqMLess` (value: `"ForeignChqMLess"`)

* `ForeignChqOther` (value: `"ForeignChqOther"`)

* `ForeignChqMPlus` (value: `"ForeignChqMPlus"`)

* `ForeignChqCCC` (value: `"ForeignChqCCC"`)

* `ServiceCAccountFee` (value: `"ServiceCAccountFee"`)

* `ServiceCAccountFeeMonthly` (value: `"ServiceCAccountFeeMonthly"`)

* `ServiceCAccountFeeQuarterly` (value: `"ServiceCAccountFeeQuarterly"`)

* `ServiceCFixedTariff` (value: `"ServiceCFixedTariff"`)

* `ServiceCBusiDepAccBreakage` (value: `"ServiceCBusiDepAccBreakage"`)

* `ServiceCMonitorDaily` (value: `"ServiceCMonitorDaily"`)

* `ServiceCMinimumMonthlyFee` (value: `"ServiceCMinimumMonthlyFee"`)

* `ServiceCMonitorMonthly` (value: `"ServiceCMonitorMonthly"`)

* `ServiceCMonitorWeekly` (value: `"ServiceCMonitorWeekly"`)

* `ServiceCMT940AccountFirst` (value: `"ServiceCMT940AccountFirst"`)

* `ServiceCMT940AccountSubsequent` (value: `"ServiceCMT940AccountSubsequent"`)

* `ServiceCOther` (value: `"ServiceCOther"`)

* `CounterCoinHandling` (value: `"CounterCoinHandling"`)

* `CounterCashIn` (value: `"CounterCashIn"`)

* `CounterCashInNotUs` (value: `"CounterCashInNotUs"`)

* `CounterCashOut` (value: `"CounterCashOut"`)

* `CounterCashX` (value: `"CounterCashX"`)

* `CounterForeignNoteHandling` (value: `"CounterForeignNoteHandling"`)

* `CounterCashFeeRate` (value: `"CounterCashFeeRate"`)

* `CounterForeignCashOutTx` (value: `"CounterForeignCashOutTx"`)

* `CounterCounterLodgement` (value: `"CounterCounterLodgement"`)

* `CounterCashDropLodgement` (value: `"CounterCashDropLodgement"`)

* `CounterNotesLodged` (value: `"CounterNotesLodged"`)

* `CounterNotesOut` (value: `"CounterNotesOut"`)

* `CounterCashInOwn` (value: `"CounterCashInOwn"`)

* `CounterCashFeePercent` (value: `"CounterCashFeePercent"`)




