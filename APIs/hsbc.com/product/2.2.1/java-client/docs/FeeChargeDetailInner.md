

# FeeChargeDetailInner

Other fees/charges details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationFrequency** | [**ApplicationFrequencyEnum**](#ApplicationFrequencyEnum) | How frequently the fee/charge is applied to the account |  |
|**calculationFrequency** | [**CalculationFrequencyEnum**](#CalculationFrequencyEnum) | How frequently the fee/charge is calculated |  |
|**feeAmount** | **String** | Fee Amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate) |  [optional] |
|**feeApplicableRange** | **Object** | Range or amounts or rates for which the fee/charge applies |  [optional] |
|**feeCategory** | [**FeeCategoryEnum**](#FeeCategoryEnum) | Categorisation of fees and charges into standard categories. |  |
|**feeRate** | **String** | Rate charged for Fee/Charge (where it is charged in terms of a rate rather than an amount) |  [optional] |
|**feeRateType** | [**FeeRateTypeEnum**](#FeeRateTypeEnum) | Rate type for Fee/Charge (where it is charged in terms of a rate rather than an amount) |  [optional] |
|**feeType** | [**FeeTypeEnum**](#FeeTypeEnum) | Fee/Charge Type |  |
|**includedInMonthlyChargeIndicator** | **Boolean** | Indicates that fee/charge is already included in the monthly charge. |  [optional] |
|**negotiableIndicator** | **Boolean** | Fee/charge which is usually negotiable rather than a fixed amount |  [optional] |
|**notes** | **List&lt;String&gt;** | Optional additional notes to supplement the fee/charge details. |  [optional] |
|**otherApplicationFrequency** | **Object** | Other application frequencies not covered in the standard code list |  [optional] |
|**otherCalculationFrequency** | **Object** | Other calculation frequency which is not available in standard code set. |  [optional] |
|**otherFeeCategory** | **Object** |  |  [optional] |
|**otherFeeRateType** | **Object** | Other fee rate type which is not available in the standard code set |  [optional] |
|**otherFeeType** | **Object** | Other Fee/charge type which is not available in the standard code set |  [optional] |



## Enum: ApplicationFrequencyEnum

| Name | Value |
|---- | -----|
| ON_CLOSING | &quot;OnClosing&quot; |
| ON_OPENING | &quot;OnOpening&quot; |
| CHARGING_PERIOD | &quot;ChargingPeriod&quot; |
| DAILY | &quot;Daily&quot; |
| PER_ITEM | &quot;PerItem&quot; |
| MONTHLY | &quot;Monthly&quot; |
| ON_ANNIVERSARY | &quot;OnAnniversary&quot; |
| OTHER | &quot;Other&quot; |
| PER_HUNDRED_POUNDS | &quot;PerHundredPounds&quot; |
| PER_HOUR | &quot;PerHour&quot; |
| PER_OCCURRENCE | &quot;PerOccurrence&quot; |
| PER_SHEET | &quot;PerSheet&quot; |
| PER_TRANSACTION | &quot;PerTransaction&quot; |
| PER_TRANSACTION_AMOUNT | &quot;PerTransactionAmount&quot; |
| PER_TRANSACTION_PERCENTAGE | &quot;PerTransactionPercentage&quot; |
| QUARTERLY | &quot;Quarterly&quot; |
| SIX_MONTHLY | &quot;SixMonthly&quot; |
| STATEMENT_MONTHLY | &quot;StatementMonthly&quot; |
| WEEKLY | &quot;Weekly&quot; |
| YEARLY | &quot;Yearly&quot; |



## Enum: CalculationFrequencyEnum

| Name | Value |
|---- | -----|
| ON_CLOSING | &quot;OnClosing&quot; |
| ON_OPENING | &quot;OnOpening&quot; |
| CHARGING_PERIOD | &quot;ChargingPeriod&quot; |
| DAILY | &quot;Daily&quot; |
| PER_ITEM | &quot;PerItem&quot; |
| MONTHLY | &quot;Monthly&quot; |
| ON_ANNIVERSARY | &quot;OnAnniversary&quot; |
| OTHER | &quot;Other&quot; |
| PER_HUNDRED_POUNDS | &quot;PerHundredPounds&quot; |
| PER_HOUR | &quot;PerHour&quot; |
| PER_OCCURRENCE | &quot;PerOccurrence&quot; |
| PER_SHEET | &quot;PerSheet&quot; |
| PER_TRANSACTION | &quot;PerTransaction&quot; |
| PER_TRANSACTION_AMOUNT | &quot;PerTransactionAmount&quot; |
| PER_TRANSACTION_PERCENTAGE | &quot;PerTransactionPercentage&quot; |
| QUARTERLY | &quot;Quarterly&quot; |
| SIX_MONTHLY | &quot;SixMonthly&quot; |
| STATEMENT_MONTHLY | &quot;StatementMonthly&quot; |
| WEEKLY | &quot;Weekly&quot; |
| YEARLY | &quot;Yearly&quot; |



## Enum: FeeCategoryEnum

| Name | Value |
|---- | -----|
| AUTO | &quot;Auto&quot; |
| ATM | &quot;ATM&quot; |
| BANKERS_DRAFTS | &quot;BankersDrafts&quot; |
| CARD | &quot;Card&quot; |
| CHEQUE | &quot;Cheque&quot; |
| COUNTER_SERVICES | &quot;CounterServices&quot; |
| DIRECT_DEBIT | &quot;DirectDebit&quot; |
| DEEDS | &quot;Deeds&quot; |
| FOREIGN | &quot;Foreign&quot; |
| FX | &quot;FX&quot; |
| INTERNATIONAL | &quot;International&quot; |
| INVESTIGATION | &quot;Investigation&quot; |
| LEGAL | &quot;Legal&quot; |
| LOAN | &quot;Loan&quot; |
| NIGHT_SAFE | &quot;NightSafe&quot; |
| ONLINE | &quot;Online&quot; |
| OTHER | &quot;Other&quot; |
| POST_OFFICE | &quot;PostOffice&quot; |
| PAYMENT_SCHEME | &quot;PaymentScheme&quot; |
| REPORT | &quot;Report&quot; |
| SAFEKEEPING | &quot;Safekeeping&quot; |
| SERVICING | &quot;Servicing&quot; |
| TRANSACTION | &quot;Transaction&quot; |



## Enum: FeeRateTypeEnum

| Name | Value |
|---- | -----|
| GROSS | &quot;Gross&quot; |
| OTHER | &quot;Other&quot; |



## Enum: FeeTypeEnum

| Name | Value |
|---- | -----|
| ATM_DEPOS_ATM_PAID_IN | &quot;ATMDeposATMPaidIn&quot; |
| REPORT_CERT_BALANCE | &quot;ReportCertBalance&quot; |
| ATM_ABROAD_CON_VISA_DEBIT | &quot;ATMAbroadConVisaDebit&quot; |
| ATM_CARDNET_ENV_IN | &quot;ATMCardnetEnvIn&quot; |
| ATM_CASH_GROUP_ATM_DEBIT_CARD | &quot;ATMCashGroupATMDebitCard&quot; |
| ATM_CASH_NON_GROUP_ATM_DEBITCARD | &quot;ATMCashNonGroupATMDebitcard&quot; |
| ATM_CON_GROUP_ATM | &quot;ATMConGroupATM&quot; |
| ATM_ABROAD | &quot;ATMAbroad&quot; |
| ATM_FOREIGN_CASH_DEB_CARD | &quot;ATMForeignCashDebCard&quot; |
| ATM_ABROAD_GOLD_VISA_DEBIT | &quot;ATMAbroadGoldVisaDebit&quot; |
| ATM_NON_STERLING_WITHDRAWAL | &quot;ATMNonSterlingWithdrawal&quot; |
| ATM_ABROAD_VISA_DEBIT | &quot;ATMAbroadVisaDebit&quot; |
| ATM_WITHDRAW_CASH | &quot;ATMWithdrawCash&quot; |
| BACSON_LINE_ANCILLIARY | &quot;BACSOnLineAncilliary&quot; |
| BACS_BATCH | &quot;BACSBatch&quot; |
| BACSON_LINE_FILE | &quot;BACSOnLineFile&quot; |
| BACS_ITEM | &quot;BACSItem&quot; |
| BACS_BULK_BATCH | &quot;BACSBulkBatch&quot; |
| BACSON_LINE_OVERLIMIT | &quot;BACSOnLineOverlimit&quot; |
| BACSON_LINE_PAYMENT | &quot;BACSOnLinePayment&quot; |
| BACSON_LINE_SERVICE | &quot;BACSOnLineService&quot; |
| BACS_BULK_INTERNET | &quot;BACSBulkInternet&quot; |
| BACSTEL_DIR_DEB_SMART_CARD | &quot;BACSTELDirDebSmartCard&quot; |
| BACSTEL_DIR_DEB_WEB_INIT | &quot;BACSTELDirDebWebInit&quot; |
| BACSTE_LIR_DEB_WEB_INIT | &quot;BACSTELirDebWebInit&quot; |
| BACSTEL_DIR_DEB_OVERLIMIT | &quot;BACSTELDirDebOverlimit&quot; |
| BACSTEL_DIR_DEB_PAYMENT | &quot;BACSTELDirDebPayment&quot; |
| BACSTEL_DIR_DEB_SERVICE | &quot;BACSTELDirDebService&quot; |
| BACSTEL_DIR_DEB_ANCILLIARY | &quot;BACSTELDirDebAncilliary&quot; |
| BACSTEL_ANCILLIARY | &quot;BACSTELAncilliary&quot; |
| BACSTEL_SMART_CARD | &quot;BACSTELSmartCard&quot; |
| BACSTEL_FILE | &quot;BACSTELFile&quot; |
| BACSTEL_OVERLIMIT | &quot;BACSTELOverlimit&quot; |
| BACSTEL_PAYMENT | &quot;BACSTELPayment&quot; |
| BACSTEL_SERVICE | &quot;BACSTELService&quot; |
| CHAPS_OUT_BRANCH | &quot;CHAPSOutBranch&quot; |
| CHAPS_OUT_ONLINE_DEPOSIT_ACC | &quot;CHAPSOutOnlineDepositAcc&quot; |
| CHAPSIN | &quot;CHAPSIn&quot; |
| CHAPS_OUT_POST | &quot;CHAPSOutPost&quot; |
| CHAPS_OUT | &quot;CHAPSOut&quot; |
| CHAPS_OUT_ONLINE | &quot;CHAPSOutOnline&quot; |
| CHAPS_OUT_MANUAL | &quot;CHAPSOutManual&quot; |
| CARD_CARD_REPLACEMENT | &quot;CardCardReplacement&quot; |
| DRAFTS_BANKERS | &quot;DraftsBankers&quot; |
| DRAFTS_CANCELLATION | &quot;DraftsCancellation&quot; |
| CARD_GUARANTEED | &quot;CardGuaranteed&quot; |
| DRAFTS_INTL_PAYABLE_ABROAD | &quot;DraftsIntlPayableAbroad&quot; |
| DRAFTS_INTL_STOPPED_CANCELLED | &quot;DraftsIntlStoppedCancelled&quot; |
| EURO_CHQ_X_LESS | &quot;EuroChqXLess&quot; |
| EURO_CHQ_X_PLUS | &quot;EuroChqXPlus&quot; |
| FPS_OUT | &quot;FPSOut&quot; |
| FPS_OUT_OWN | &quot;FPSOutOwn&quot; |
| FPSIN_BRANCH | &quot;FPSInBranch&quot; |
| LEGAL_ARTICLES_REPORT | &quot;LegalArticlesReport&quot; |
| LEGAL_SEALING | &quot;LegalSealing&quot; |
| LEGAL_BOND_AND_GUARANTEE | &quot;LegalBondAndGuarantee&quot; |
| LEGAL_CO_SEARCH | &quot;LegalCoSearch&quot; |
| LEGAL_DEPOSIT_ASSIGNMENT | &quot;LegalDepositAssignment&quot; |
| LEGAL_GUARANTEE_PREP | &quot;LegalGuaranteePrep&quot; |
| LEGAL_LIFE_POLICY_PREP_CO | &quot;LegalLifePolicyPrepCo&quot; |
| LEGAL_LIFE_POLICY_PREP_PERSONAL | &quot;LegalLifePolicyPrepPersonal&quot; |
| LEGAL_PRIORITY_PARI_PASSU | &quot;LegalPriorityPariPassu&quot; |
| LEGAL_SUBORDINATION_AGREEMENT | &quot;LegalSubordinationAgreement&quot; |
| DIR_DEB_DIRECT_DEBIT_ADMIN | &quot;DirDebDirectDebitAdmin&quot; |
| DIR_DEB_DIRECT_DEBIT_CANCEL | &quot;DirDebDirectDebitCancel&quot; |
| INTL_PAY_BIB_FOREIGN_LIMIT | &quot;IntlPayBIBForeignLimit&quot; |
| INTL_PAY_CREDIT_TRANS_CUST | &quot;IntlPayCreditTransCust&quot; |
| INTL_PAY_CREDIT_TRANS_NON_CUST | &quot;IntlPayCreditTransNonCust&quot; |
| INTL_PAY_EXPRESS_MONEY_MOVER | &quot;IntlPayExpressMoneyMover&quot; |
| INTL_PAY_EEA_PAY_URGENT | &quot;IntlPayEEAPayUrgent&quot; |
| INTL_PAY_IRISH_PAY_URGENT | &quot;IntlPayIrishPayUrgent&quot; |
| INTL_PAY_EEA_PAY | &quot;IntlPayEEAPay&quot; |
| INTL_PAY_FX_PAYMENT_IN | &quot;IntlPayFXPaymentIn&quot; |
| INTL_PAY_FOREIGN_IN1_C_PLUS | &quot;IntlPayForeignIn1CPlus&quot; |
| INTL_PAY_FOREIGN_CHARGE | &quot;IntlPayForeignCharge&quot; |
| INTL_PAY_FOREIGN_INTERNET | &quot;IntlPayForeignInternet&quot; |
| INTL_PAY_FOREIGN_IN_SUB1_C | &quot;IntlPayForeignInSub1C&quot; |
| INTL_PAY_PURCHASE_NON_STERLING | &quot;IntlPayPurchaseNonSterling&quot; |
| INTL_PAY_PAYMENT_TRACING | &quot;IntlPayPaymentTracing&quot; |
| INTL_PAY_STANDARD_MONEY_MOVER | &quot;IntlPayStandardMoneyMover&quot; |
| INTL_PAY_MT101_TRANSACTION | &quot;IntlPayMT101Transaction&quot; |
| INTL_PAY_WORLDPAY_PAYMENT | &quot;IntlPayWorldpayPayment&quot; |
| INV_PAY_BANK_DETAILS_WRONG | &quot;InvPayBankDetailsWrong&quot; |
| INV_PAY_FOREIGN_BCNR | &quot;InvPayForeignBCNR&quot; |
| INV_PAY_FOREIGN_RECALL | &quot;InvPayForeignRecall&quot; |
| INV_GENERAL_INQ | &quot;InvGeneralInq&quot; |
| INV_OLD_INSTRUCTION | &quot;InvOldInstruction&quot; |
| INV_PAY_RETURN_DEBIT_XV_LESS | &quot;InvPayReturnDebitXVLess&quot; |
| INV_PAY_RETURN_DEBIT_XV_PLUS | &quot;InvPayReturnDebitXVPlus&quot; |
| INV_PAY_STOP_PAYMENT | &quot;InvPayStopPayment&quot; |
| INV_PAY_STANDING_ORD_UNPAID | &quot;InvPayStandingOrdUnpaid&quot; |
| SAFE_KEEP_ACCESS | &quot;SafeKeepAccess&quot; |
| SAFE_KEEP_DEED_MEDIUM | &quot;SafeKeepDeedMedium&quot; |
| SAFE_KEEPING_ENVELOPE | &quot;SafeKeepingEnvelope&quot; |
| SAFE_KEEPING_INSPECTION | &quot;SafeKeepingInspection&quot; |
| SAFE_KEEPING_LARGE_ITEM | &quot;SafeKeepingLargeItem&quot; |
| SAFE_KEEP_MULTIPLE_ITEMS | &quot;SafeKeepMultipleItems&quot; |
| SAFE_KEEPING_PARCEL | &quot;SafeKeepingParcel&quot; |
| SAFE_KEEP_DEED_SMALL | &quot;SafeKeepDeedSmall&quot; |
| SAFE_KEEP_ONE_ITEM | &quot;SafeKeepOneItem&quot; |
| LOAN_ARRANGEMENT | &quot;LoanArrangement&quot; |
| NIGHT_SAFE_NIGHT_SAFE_BANK_OPEN | &quot;NightSafeNightSafeBankOpen&quot; |
| NIGHT_SAFE_CREDIT_SUB5_K | &quot;NightSafeCreditSub5K&quot; |
| NIGHT_SAFE_NIGHT_SAFE | &quot;NightSafeNightSafe&quot; |
| NIGHT_SAFE_NIGHT_SAFE_PAID_IN | &quot;NightSafeNightSafePaidIn&quot; |
| PO_POST_OFFICE_COUNTER_CREDIT | &quot;POPostOfficeCounterCredit&quot; |
| PO_POST_OFFICE_CASH_CREDIT | &quot;POPostOfficeCashCredit&quot; |
| PO_POST_OFFICE_CASH_OUT | &quot;POPostOfficeCashOut&quot; |
| PO_POST_OFFICE_WITHDRAWAL | &quot;POPostOfficeWithdrawal&quot; |
| CHQ_BOOK_THEFT_LOSS_ALL_STOPPED | &quot;ChqBookTheftLossAllStopped&quot; |
| CHQ_ISSUED_CURRENCY_ACC | &quot;ChqIssuedCurrencyAcc&quot; |
| CHQ_COPY | &quot;ChqCopy&quot; |
| CHQ_DRAFT | &quot;ChqDraft&quot; |
| CHQ_IN | &quot;ChqIn&quot; |
| CHQ_SPECIAL_CHQ_CLEARANCE | &quot;ChqSpecialChqClearance&quot; |
| CHQ_OUT_ISSUED | &quot;ChqOutIssued&quot; |
| CHQ_SPECIAL_CHQ_PRESENTATION | &quot;ChqSpecialChqPresentation&quot; |
| CHQ_COUNTER_CHEQUE | &quot;ChqCounterCheque&quot; |
| CHQ_CHEQUESWITH_STATEMENT | &quot;ChqChequeswithStatement&quot; |
| CHQ_STOPPED | &quot;ChqStopped&quot; |
| CHQ_TRANS | &quot;ChqTrans&quot; |
| CHQ_DRAFT_FX | &quot;ChqDraftFX&quot; |
| CHQ_FOREIGN_COURIER | &quot;ChqForeignCourier&quot; |
| CHQ_FOREIGN_NEG_TEN_THOU | &quot;ChqForeignNegTenThou&quot; |
| CHQ_FOREIGN_NEG_HUNDRED | &quot;ChqForeignNegHundred&quot; |
| CHEQUE_FOREIGN_BANK_DIVI | &quot;ChequeForeignBankDivi&quot; |
| CHQ_FOREIGN_NEG_FIFTY_THOU | &quot;ChqForeignNegFiftyThou&quot; |
| CHQ_PENSION_CHEQUE | &quot;ChqPensionCheque&quot; |
| CHEQUE_FOREIGN_OTHER_DIVI | &quot;ChequeForeignOtherDivi&quot; |
| CHQ_FOREIGN_NEG_FIVE_THOU | &quot;ChqForeignNegFiveThou&quot; |
| CHQ_FOREIGN_NEG_MAX | &quot;ChqForeignNegMax&quot; |
| CHQ_FOREIGN_GBPMMD_PLUS | &quot;ChqForeignGBPMMDPlus&quot; |
| CHQ_GIFT_CHEQUE | &quot;ChqGiftCheque&quot; |
| CHQ_COUNTER_LODGEMENT | &quot;ChqCounterLodgement&quot; |
| CHQ_CASH_DROP_LODGEMENT | &quot;ChqCashDropLodgement&quot; |
| CHQ_FOREIGN | &quot;ChqForeign&quot; |
| CHQ_CHEQUE_PHOTOCOPY | &quot;ChqChequePhotocopy&quot; |
| CHQ_POST_OFFICE_CREDIT | &quot;ChqPostOfficeCredit&quot; |
| CHQ_POST_OFFICE_CHEQUE_COLLECTED | &quot;ChqPostOfficeChequeCollected&quot; |
| CHQ_CHEQUE_RETRIEVAL | &quot;ChqChequeRetrieval&quot; |
| CHQ_RECONCILLIATION_PER_TRANS | &quot;ChqReconcilliationPerTrans&quot; |
| CHQ_SPECIAL_PRESENTATION_COUNT | &quot;ChqSpecialPresentationCount&quot; |
| CHQ_SPECIAL_PRESENTATION_PTT | &quot;ChqSpecialPresentationPTT&quot; |
| CHQ_DRAFT_STERLING | &quot;ChqDraftSterling&quot; |
| CHQ_UNPAID_CHARGE | &quot;ChqUnpaidCharge&quot; |
| CHQ_UNPAID_TRANS_IN | &quot;ChqUnpaidTransIn&quot; |
| CHQ_UNPAID_TRANS_OUT | &quot;ChqUnpaidTransOut&quot; |
| CHQ_UNPAID_CHEQUE | &quot;ChqUnpaidCheque&quot; |
| REPORT_AUDIT_LETTER | &quot;ReportAuditLetter&quot; |
| REPORT_FAX_ADVICE_ADDITIONAL | &quot;ReportFAXAdviceAdditional&quot; |
| REPORT_TEL_ADVICE_ADDITIONAL | &quot;ReportTelAdviceAdditional&quot; |
| REPORT_CREDIT_HISTORY | &quot;ReportCreditHistory&quot; |
| REPORT_CERT_INTEREST_DUPLICATE | &quot;ReportCertInterestDuplicate&quot; |
| REPORT_CERT_INTEREST | &quot;ReportCertInterest&quot; |
| REPORT_CREDIT_HISTORY_ADDITIONAL_IN_YEAR | &quot;ReportCreditHistoryAdditionalInYear&quot; |
| REPORT_FOREIGN_STATUS_ENQ_ELEC | &quot;ReportForeignStatusEnqElec&quot; |
| REPORT_FOREIGN_STATUS_ENQ | &quot;ReportForeignStatusEnq&quot; |
| REPORT_STATEMENT_CHQ_DAILY | &quot;ReportStatementChqDaily&quot; |
| REPORT_STATEMENT_CHQ_FORTNIGHTLY | &quot;ReportStatementChqFortnightly&quot; |
| REPORT_STATEMENT_CHQ_MONTHLY | &quot;ReportStatementChqMonthly&quot; |
| REPORT_STATEMENT_CHQ_WEEKLY | &quot;ReportStatementChqWeekly&quot; |
| REPORT_STATEMENT_AND_DIVI_CHQ | &quot;ReportStatementAndDiviChq&quot; |
| REPORT_REFERRAL_ITEM | &quot;ReportReferralItem&quot; |
| REPORT_STATEMENT_BY_ATM | &quot;ReportStatementByATM&quot; |
| REPORT_STATEMENT_BY_BRANCH | &quot;ReportStatementByBranch&quot; |
| REPORT_STATEMENT_COPY_REGULAR | &quot;ReportStatementCopyRegular&quot; |
| REPORT_STATEMENT_DAILY | &quot;ReportStatementDaily&quot; |
| REPORT_STATUS_ENQUIRY | &quot;ReportStatusEnquiry&quot; |
| REPORT_STATEMENT_FREQUENT | &quot;ReportStatementFrequent&quot; |
| REPORT_STATEMENT_MONTHLY | &quot;ReportStatementMonthly&quot; |
| REPORT_STATEMENT_COPY1 | &quot;ReportStatementCopy1&quot; |
| REPORT_STATEMENT_TO_BRANCH | &quot;ReportStatementToBranch&quot; |
| REPORT_SMS_TEXT_MINI_STATEMENTOR_ALERT | &quot;ReportSMSTextMiniStatementorAlert&quot; |
| REPORT_STATEMENT_FORTNIGHTLY | &quot;ReportStatementFortnightly&quot; |
| REPORT_SMS_TEXT_MINI_STATEMENT_WO_M | &quot;ReportSMSTextMiniStatementWoM&quot; |
| REPORT_SMS_TEXT_ALERT_BALANCE | &quot;ReportSMSTextAlertBalance&quot; |
| REPORT_SMS_TEXT_ALERT | &quot;ReportSMSTextAlert&quot; |
| REPORT_TAX_CERT | &quot;ReportTaxCert&quot; |
| REPORT_WEEKLY_STATEMENT | &quot;ReportWeeklyStatement&quot; |
| SEPA_BRANCH | &quot;SEPABranch&quot; |
| SEPA_CREDIT | &quot;SEPACredit&quot; |
| SEPA_DIRECT_DEBIT | &quot;SEPADirectDebit&quot; |
| SEPAIN | &quot;SEPAIn&quot; |
| SEPA_EURO | &quot;SEPAEuro&quot; |
| SEPA_OUT | &quot;SEPAOut&quot; |
| SEPA_UNPAID | &quot;SEPAUnpaid&quot; |
| SEPA_WINBITS_TRANSACTION | &quot;SEPAWinbitsTransaction&quot; |
| TRANS_BILL_PAYMENT_BRANCH | &quot;TransBillPaymentBranch&quot; |
| TRANS_BILL_COLLECT | &quot;TransBillCollect&quot; |
| TRANS_TELEPHONE_BILL_PAYMENT | &quot;TransTelephoneBillPayment&quot; |
| TRANS_BANK_PAYMENT | &quot;TransBankPayment&quot; |
| TRANS_BILL_PAYMENT_TELEPHONE | &quot;TransBillPaymentTelephone&quot; |
| TRANS_CORRESPONDENT_BANK_FEE | &quot;TransCorrespondentBankFee&quot; |
| TRANS_CREDIT_TRANSFER_UK_DIFFERENT | &quot;TransCreditTransferUKDifferent&quot; |
| TRANS_CREDIT_TRANSFER_UK_SAME | &quot;TransCreditTransferUKSame&quot; |
| TRANS_CREDIT | &quot;TransCredit&quot; |
| TRANS_CREDIT_TRANSFER | &quot;TransCreditTransfer&quot; |
| TRANS_BRANCH_CREDIT | &quot;TransBranchCredit&quot; |
| TRANS_DEBIT | &quot;TransDebit&quot; |
| TRANS_DEB_CARD_DEB | &quot;TransDebCardDeb&quot; |
| TRANS_UK_DIR_DEB | &quot;TransUKDirDeb&quot; |
| TRANS_MANUAL_DEB | &quot;TransManualDeb&quot; |
| TITLE_DEEDS | &quot;TitleDeeds&quot; |
| TRANS_BUY_FOREIGN_WITH_GBP | &quot;TransBuyForeignWithGBP&quot; |
| TRANS_GOOD_VALUE_REQ | &quot;TransGoodValueReq&quot; |
| TRANS_SWIFT_OUT_UK_FOREIGN | &quot;TransSWIFTOutUKForeign&quot; |
| TRANS_INCONPLETE_INSTRUCTION | &quot;TransInconpleteInstruction&quot; |
| TRANS_MANUAL_ENTRIES | &quot;TransManualEntries&quot; |
| TRANS_MANUAL_TRANS | &quot;TransManualTrans&quot; |
| TRANS_NON_STERLING | &quot;TransNonSterling&quot; |
| OTHER | &quot;Other&quot; |
| TRANS_POS_SALE_FOREIGN | &quot;TransPOSSaleForeign&quot; |
| TRANS_PRI_PAYMENT_POST | &quot;TransPriPaymentPost&quot; |
| TRANS_POS_SALE_UK | &quot;TransPOSSaleUK&quot; |
| TRANS_RECONCILIATION_PER_TRANS | &quot;TransReconciliationPerTrans&quot; |
| TRANS_STANDING_ORD_ADMIN | &quot;TransStandingOrdAdmin&quot; |
| TRANS_STANDING_ORD | &quot;TransStandingOrd&quot; |
| TRANS_STANDING_ORD_MAN_PAY | &quot;TransStandingOrdManPay&quot; |
| TRANS_TEL_BUSI_PRI_PAYMENT_FOREIGN_TO_UK_ACC | &quot;TransTelBusiPriPaymentForeignToUKAcc&quot; |
| TRANS_TELE_ITEM | &quot;TransTeleItem&quot; |
| TRANS_TEL_BUSI_PRI_PAYMENT_TO_GRP_ACC | &quot;TransTelBusiPriPaymentToGrpAcc&quot; |
| TRANS_TRANSFER_EX_GROUP | &quot;TransTransferExGroup&quot; |
| TRANS_TEL_BUSI_PRI_PAYMENT_TO_NON_GRP_ACC | &quot;TransTelBusiPriPaymentToNonGrpAcc&quot; |
| TRANS_SWIFT_OUT_NON_EEA_STERLING | &quot;TransSWIFTOutNonEEASterling&quot; |
| AUTO_AUTO_CREDIT | &quot;AutoAutoCredit&quot; |
| AUTO_AUTOMATED_ENTRIES | &quot;AutoAutomatedEntries&quot; |
| AUTO_AUTO_CREDIT_PHONE_INET | &quot;AutoAutoCreditPhoneInet&quot; |
| AUTO_AUTOMATED_TRANS | &quot;AutoAutomatedTrans&quot; |
| AUTO_DEBIT_CARD_COMMERCIAL | &quot;AutoDebitCardCommercial&quot; |
| AUTO_FPS_AUTO_CREDIT | &quot;AutoFPSAutoCredit&quot; |
| VISA_TRAVELLERS_CHQOR_CURRENCY | &quot;VisaTravellersChqorCurrency&quot; |
| ONLINE_INTERNET_BILL_PAYMENT | &quot;OnlineInternetBillPayment&quot; |
| ONLINE_BUSINESS_ONLINE_EURO_PAYMENT | &quot;OnlineBusinessOnlineEuroPayment&quot; |
| ONLINE_BUSINESS_ONLINE_URGENT_EURO_PAYMENT | &quot;OnlineBusinessOnlineUrgentEuroPayment&quot; |
| ONLINE_BUSINESS_ONLINE_FOREIGN_PAYMENT | &quot;OnlineBusinessOnlineForeignPayment&quot; |
| ONLINE_INTERBANK_TRANSFER | &quot;OnlineInterbankTransfer&quot; |
| ONLINE_INTERBANK_PER_TRANSFER | &quot;OnlineInterbankPerTransfer&quot; |
| ONLINE_INTERBRANCH_TRANSFER | &quot;OnlineInterbranchTransfer&quot; |
| ONLINE_INTERBRANCH_PER_TRANSFER | &quot;OnlineInterbranchPerTransfer&quot; |
| ONLINE_SUBSCRIPTION_MONTHLY | &quot;OnlineSubscriptionMonthly&quot; |
| ONLINE_BANKING_PAYMENT | &quot;OnlineBankingPayment&quot; |
| ONLINE_REPLACEMENT_CARD_READER | &quot;OnlineReplacementCardReader&quot; |
| ONLINE_PAYMENTIN_GB_PTO_UK | &quot;OnlinePaymentinGBPtoUK&quot; |
| ONLINE_URGENT_PAYMENT | &quot;OnlineUrgentPayment&quot; |
| ONLINE_PAYMENTIN_US_DTO_US | &quot;OnlinePaymentinUSDtoUS&quot; |
| ONLINE_BULK_DIRECT_DEB_STERLING | &quot;OnlineBulkDirectDebSterling&quot; |
| FOREIGN_CHQ_SENT | &quot;ForeignChqSent&quot; |
| FOREIGN_CHQ_SELF | &quot;ForeignChqSelf&quot; |
| FOREIGN_CHQ_ENCASHMENT | &quot;ForeignChqEncashment&quot; |
| FOREIGN_FX_INWARDS_CUST | &quot;ForeignFXInwardsCust&quot; |
| FOREIGN_FX_TRANSFERS_ROI | &quot;ForeignFXTransfersROI&quot; |
| FOREIGN_FX_FORWARD_TRANS | &quot;ForeignFXForwardTrans&quot; |
| FOREIGN_EX_MAINTENANCE | &quot;ForeignExMaintenance&quot; |
| FOREIGN_FX_INWARDS_NON_CUST | &quot;ForeignFXInwardsNonCust&quot; |
| FOREIGN_FX_OUTWARDS | &quot;ForeignFXOutwards&quot; |
| FOREIGN_PURCHASE | &quot;ForeignPurchase&quot; |
| FOREIGN_STATUS_REP | &quot;ForeignStatusRep&quot; |
| FOREIGN_CHQ_DRAFT | &quot;ForeignChqDraft&quot; |
| FOREIGN_CHQ_C_LESS | &quot;ForeignChqCLess&quot; |
| FOREIGN_CHQ_M_LESS | &quot;ForeignChqMLess&quot; |
| FOREIGN_CHQ_OTHER | &quot;ForeignChqOther&quot; |
| FOREIGN_CHQ_M_PLUS | &quot;ForeignChqMPlus&quot; |
| FOREIGN_CHQ_CCC | &quot;ForeignChqCCC&quot; |
| SERVICE_C_ACCOUNT_FEE | &quot;ServiceCAccountFee&quot; |
| SERVICE_C_ACCOUNT_FEE_MONTHLY | &quot;ServiceCAccountFeeMonthly&quot; |
| SERVICE_C_ACCOUNT_FEE_QUARTERLY | &quot;ServiceCAccountFeeQuarterly&quot; |
| SERVICE_C_FIXED_TARIFF | &quot;ServiceCFixedTariff&quot; |
| SERVICE_C_BUSI_DEP_ACC_BREAKAGE | &quot;ServiceCBusiDepAccBreakage&quot; |
| SERVICE_C_MONITOR_DAILY | &quot;ServiceCMonitorDaily&quot; |
| SERVICE_C_MINIMUM_MONTHLY_FEE | &quot;ServiceCMinimumMonthlyFee&quot; |
| SERVICE_C_MONITOR_MONTHLY | &quot;ServiceCMonitorMonthly&quot; |
| SERVICE_C_MONITOR_WEEKLY | &quot;ServiceCMonitorWeekly&quot; |
| SERVICE_CMT940_ACCOUNT_FIRST | &quot;ServiceCMT940AccountFirst&quot; |
| SERVICE_CMT940_ACCOUNT_SUBSEQUENT | &quot;ServiceCMT940AccountSubsequent&quot; |
| SERVICE_C_OTHER | &quot;ServiceCOther&quot; |
| COUNTER_COIN_HANDLING | &quot;CounterCoinHandling&quot; |
| COUNTER_CASH_IN | &quot;CounterCashIn&quot; |
| COUNTER_CASH_IN_NOT_US | &quot;CounterCashInNotUs&quot; |
| COUNTER_CASH_OUT | &quot;CounterCashOut&quot; |
| COUNTER_CASH_X | &quot;CounterCashX&quot; |
| COUNTER_FOREIGN_NOTE_HANDLING | &quot;CounterForeignNoteHandling&quot; |
| COUNTER_CASH_FEE_RATE | &quot;CounterCashFeeRate&quot; |
| COUNTER_FOREIGN_CASH_OUT_TX | &quot;CounterForeignCashOutTx&quot; |
| COUNTER_COUNTER_LODGEMENT | &quot;CounterCounterLodgement&quot; |
| COUNTER_CASH_DROP_LODGEMENT | &quot;CounterCashDropLodgement&quot; |
| COUNTER_NOTES_LODGED | &quot;CounterNotesLodged&quot; |
| COUNTER_NOTES_OUT | &quot;CounterNotesOut&quot; |
| COUNTER_CASH_IN_OWN | &quot;CounterCashInOwn&quot; |
| COUNTER_CASH_FEE_PERCENT | &quot;CounterCashFeePercent&quot; |



