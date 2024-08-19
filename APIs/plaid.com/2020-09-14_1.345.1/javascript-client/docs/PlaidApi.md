# ThePlaidApi.PlaidApi

All URIs are relative to *https://production.plaid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsBalanceGet**](PlaidApi.md#accountsBalanceGet) | **POST** /accounts/balance/get | Retrieve real-time balance data
[**accountsGet**](PlaidApi.md#accountsGet) | **POST** /accounts/get | Retrieve accounts
[**applicationGet**](PlaidApi.md#applicationGet) | **POST** /application/get | Retrieve information about a Plaid application
[**assetReportAuditCopyCreate**](PlaidApi.md#assetReportAuditCopyCreate) | **POST** /asset_report/audit_copy/create | Create Asset Report Audit Copy
[**assetReportAuditCopyGet**](PlaidApi.md#assetReportAuditCopyGet) | **POST** /asset_report/audit_copy/get | Retrieve an Asset Report Audit Copy
[**assetReportAuditCopyRemove**](PlaidApi.md#assetReportAuditCopyRemove) | **POST** /asset_report/audit_copy/remove | Remove Asset Report Audit Copy
[**assetReportCreate**](PlaidApi.md#assetReportCreate) | **POST** /asset_report/create | Create an Asset Report
[**assetReportFilter**](PlaidApi.md#assetReportFilter) | **POST** /asset_report/filter | Filter Asset Report
[**assetReportGet**](PlaidApi.md#assetReportGet) | **POST** /asset_report/get | Retrieve an Asset Report
[**assetReportPdfGet**](PlaidApi.md#assetReportPdfGet) | **POST** /asset_report/pdf/get | Retrieve a PDF Asset Report
[**assetReportRefresh**](PlaidApi.md#assetReportRefresh) | **POST** /asset_report/refresh | Refresh an Asset Report
[**assetReportRemove**](PlaidApi.md#assetReportRemove) | **POST** /asset_report/remove | Delete an Asset Report
[**authGet**](PlaidApi.md#authGet) | **POST** /auth/get | Retrieve auth data
[**bankTransferBalanceGet**](PlaidApi.md#bankTransferBalanceGet) | **POST** /bank_transfer/balance/get | Get balance of your Bank Transfer account
[**bankTransferCancel**](PlaidApi.md#bankTransferCancel) | **POST** /bank_transfer/cancel | Cancel a bank transfer
[**bankTransferCreate**](PlaidApi.md#bankTransferCreate) | **POST** /bank_transfer/create | Create a bank transfer
[**bankTransferEventList**](PlaidApi.md#bankTransferEventList) | **POST** /bank_transfer/event/list | List bank transfer events
[**bankTransferEventSync**](PlaidApi.md#bankTransferEventSync) | **POST** /bank_transfer/event/sync | Sync bank transfer events
[**bankTransferGet**](PlaidApi.md#bankTransferGet) | **POST** /bank_transfer/get | Retrieve a bank transfer
[**bankTransferList**](PlaidApi.md#bankTransferList) | **POST** /bank_transfer/list | List bank transfers
[**bankTransferMigrateAccount**](PlaidApi.md#bankTransferMigrateAccount) | **POST** /bank_transfer/migrate_account | Migrate account into Bank Transfers
[**bankTransferSweepGet**](PlaidApi.md#bankTransferSweepGet) | **POST** /bank_transfer/sweep/get | Retrieve a sweep
[**bankTransferSweepList**](PlaidApi.md#bankTransferSweepList) | **POST** /bank_transfer/sweep/list | List sweeps
[**categoriesGet**](PlaidApi.md#categoriesGet) | **POST** /categories/get | Get Categories
[**createPaymentToken**](PlaidApi.md#createPaymentToken) | **POST** /payment_initiation/payment/token/create | Create payment token
[**creditAssetReportFreddieMacGet**](PlaidApi.md#creditAssetReportFreddieMacGet) | **POST** /credit/asset_report/freddie_mac/get | Retrieve an Asset Report with Freddie Mac format. Only Freddie Mac can use this endpoint.
[**creditAuditCopyTokenCreate**](PlaidApi.md#creditAuditCopyTokenCreate) | **POST** /credit/audit_copy_token/create | Create Asset or Income Report Audit Copy Token
[**creditAuditCopyTokenUpdate**](PlaidApi.md#creditAuditCopyTokenUpdate) | **POST** /credit/audit_copy_token/update | Update an Audit Copy Token
[**creditBankEmploymentGet**](PlaidApi.md#creditBankEmploymentGet) | **POST** /beta/credit/v1/bank_employment/get | Retrieve information from the bank accounts used for employment verification
[**creditBankIncomeGet**](PlaidApi.md#creditBankIncomeGet) | **POST** /credit/bank_income/get | Retrieve information from the bank accounts used for income verification
[**creditBankIncomePdfGet**](PlaidApi.md#creditBankIncomePdfGet) | **POST** /credit/bank_income/pdf/get | Retrieve information from the bank accounts used for income verification in PDF format
[**creditBankIncomeRefresh**](PlaidApi.md#creditBankIncomeRefresh) | **POST** /credit/bank_income/refresh | Refresh a user&#39;s bank income information
[**creditEmploymentGet**](PlaidApi.md#creditEmploymentGet) | **POST** /credit/employment/get | Retrieve a summary of an individual&#39;s employment information
[**creditFreddieMacReportsGet**](PlaidApi.md#creditFreddieMacReportsGet) | **POST** /credit/freddie_mac/reports/get | Retrieve an Asset Report with Freddie Mac format (aka VOA - Verification Of Assets), and a Verification Of Employment (VOE) report if this one is available. Only Freddie Mac can use this endpoint.
[**creditPayrollIncomeGet**](PlaidApi.md#creditPayrollIncomeGet) | **POST** /credit/payroll_income/get | Retrieve a user&#39;s payroll information
[**creditPayrollIncomePrecheck**](PlaidApi.md#creditPayrollIncomePrecheck) | **POST** /credit/payroll_income/precheck | Check income verification eligibility and optimize conversion
[**creditPayrollIncomeRefresh**](PlaidApi.md#creditPayrollIncomeRefresh) | **POST** /credit/payroll_income/refresh | Refresh a digital payroll income verification
[**creditRelayCreate**](PlaidApi.md#creditRelayCreate) | **POST** /credit/relay/create | Create a relay token to share an Asset Report with a partner client (beta)
[**creditRelayGet**](PlaidApi.md#creditRelayGet) | **POST** /credit/relay/get | Retrieve the reports associated with a relay token that was shared with you (beta)
[**creditRelayRefresh**](PlaidApi.md#creditRelayRefresh) | **POST** /credit/relay/refresh | Refresh a report of a relay token (beta)
[**creditRelayRemove**](PlaidApi.md#creditRelayRemove) | **POST** /credit/relay/remove | Remove relay token (beta)
[**creditReportAuditCopyRemove**](PlaidApi.md#creditReportAuditCopyRemove) | **POST** /credit/audit_copy_token/remove | Remove an Audit Copy token
[**creditSessionsGet**](PlaidApi.md#creditSessionsGet) | **POST** /credit/sessions/get | Retrieve Link sessions for your user
[**dashboardUserGet**](PlaidApi.md#dashboardUserGet) | **POST** /dashboard_user/get | Retrieve a dashboard user
[**dashboardUserList**](PlaidApi.md#dashboardUserList) | **POST** /dashboard_user/list | List dashboard users
[**depositSwitchAltCreate**](PlaidApi.md#depositSwitchAltCreate) | **POST** /deposit_switch/alt/create | Create a deposit switch without using Plaid Exchange
[**depositSwitchCreate**](PlaidApi.md#depositSwitchCreate) | **POST** /deposit_switch/create | Create a deposit switch
[**depositSwitchGet**](PlaidApi.md#depositSwitchGet) | **POST** /deposit_switch/get | Retrieve a deposit switch
[**depositSwitchTokenCreate**](PlaidApi.md#depositSwitchTokenCreate) | **POST** /deposit_switch/token/create | Create a deposit switch token
[**employersSearch**](PlaidApi.md#employersSearch) | **POST** /employers/search | Search employer database
[**employmentVerificationGet**](PlaidApi.md#employmentVerificationGet) | **POST** /employment/verification/get | (Deprecated) Retrieve a summary of an individual&#39;s employment information
[**fdxNotifications**](PlaidApi.md#fdxNotifications) | **POST** /fdx/notifications | Webhook receiver for fdx notifications
[**identityGet**](PlaidApi.md#identityGet) | **POST** /identity/get | Retrieve identity data
[**identityMatch**](PlaidApi.md#identityMatch) | **POST** /identity/match | Retrieve identity match score
[**identityVerificationCreate**](PlaidApi.md#identityVerificationCreate) | **POST** /identity_verification/create | Create a new identity verification
[**identityVerificationGet**](PlaidApi.md#identityVerificationGet) | **POST** /identity_verification/get | Retrieve Identity Verification
[**identityVerificationList**](PlaidApi.md#identityVerificationList) | **POST** /identity_verification/list | List Identity Verifications
[**identityVerificationRetry**](PlaidApi.md#identityVerificationRetry) | **POST** /identity_verification/retry | Retry an Identity Verification
[**incomeVerificationCreate**](PlaidApi.md#incomeVerificationCreate) | **POST** /income/verification/create | (Deprecated) Create an income verification instance
[**incomeVerificationDocumentsDownload**](PlaidApi.md#incomeVerificationDocumentsDownload) | **POST** /income/verification/documents/download | (Deprecated) Download the original documents used for income verification
[**incomeVerificationPaystubsGet**](PlaidApi.md#incomeVerificationPaystubsGet) | **POST** /income/verification/paystubs/get | (Deprecated) Retrieve information from the paystubs used for income verification
[**incomeVerificationPrecheck**](PlaidApi.md#incomeVerificationPrecheck) | **POST** /income/verification/precheck | (Deprecated) Check digital income verification eligibility and optimize conversion
[**incomeVerificationTaxformsGet**](PlaidApi.md#incomeVerificationTaxformsGet) | **POST** /income/verification/taxforms/get | (Deprecated) Retrieve information from the tax documents used for income verification
[**institutionsGet**](PlaidApi.md#institutionsGet) | **POST** /institutions/get | Get details of all supported institutions
[**institutionsGetById**](PlaidApi.md#institutionsGetById) | **POST** /institutions/get_by_id | Get details of an institution
[**institutionsSearch**](PlaidApi.md#institutionsSearch) | **POST** /institutions/search | Search institutions
[**investmentsHoldingsGet**](PlaidApi.md#investmentsHoldingsGet) | **POST** /investments/holdings/get | Get Investment holdings
[**investmentsTransactionsGet**](PlaidApi.md#investmentsTransactionsGet) | **POST** /investments/transactions/get | Get investment transactions
[**itemAccessTokenInvalidate**](PlaidApi.md#itemAccessTokenInvalidate) | **POST** /item/access_token/invalidate | Invalidate access_token
[**itemActivityList**](PlaidApi.md#itemActivityList) | **POST** /item/activity/list | List a historical log of user consent events
[**itemApplicationList**](PlaidApi.md#itemApplicationList) | **POST** /item/application/list | List a user’s connected applications
[**itemApplicationScopesUpdate**](PlaidApi.md#itemApplicationScopesUpdate) | **POST** /item/application/scopes/update | Update the scopes of access for a particular application
[**itemCreatePublicToken**](PlaidApi.md#itemCreatePublicToken) | **POST** /item/public_token/create | Create public token
[**itemGet**](PlaidApi.md#itemGet) | **POST** /item/get | Retrieve an Item
[**itemImport**](PlaidApi.md#itemImport) | **POST** /item/import | Import Item
[**itemPublicTokenExchange**](PlaidApi.md#itemPublicTokenExchange) | **POST** /item/public_token/exchange | Exchange public token for an access token
[**itemRemove**](PlaidApi.md#itemRemove) | **POST** /item/remove | Remove an Item
[**itemWebhookUpdate**](PlaidApi.md#itemWebhookUpdate) | **POST** /item/webhook/update | Update Webhook URL
[**liabilitiesGet**](PlaidApi.md#liabilitiesGet) | **POST** /liabilities/get | Retrieve Liabilities data
[**linkDeliveryCreate**](PlaidApi.md#linkDeliveryCreate) | **POST** /link_delivery/create | Create Link Delivery session
[**linkDeliveryGet**](PlaidApi.md#linkDeliveryGet) | **POST** /link_delivery/get | Get Link Delivery session
[**linkOauthCorrelationIdExchange**](PlaidApi.md#linkOauthCorrelationIdExchange) | **POST** /link/oauth/correlation_id/exchange | Exchange the Link Correlation Id for a Link Token
[**linkTokenCreate**](PlaidApi.md#linkTokenCreate) | **POST** /link/token/create | Create Link Token
[**linkTokenGet**](PlaidApi.md#linkTokenGet) | **POST** /link/token/get | Get Link Token
[**partnerCustomerCreate**](PlaidApi.md#partnerCustomerCreate) | **POST** /partner/customer/create | Creates a new end customer for a Plaid reseller.
[**partnerCustomerEnable**](PlaidApi.md#partnerCustomerEnable) | **POST** /partner/customer/enable | Enables a Plaid reseller&#39;s end customer in the Production environment.
[**partnerCustomerGet**](PlaidApi.md#partnerCustomerGet) | **POST** /partner/customer/get | Returns a Plaid reseller&#39;s end customer.
[**partnerCustomerOauthInstitutionsGet**](PlaidApi.md#partnerCustomerOauthInstitutionsGet) | **POST** /partner/customer/oauth_institutions/get | Returns OAuth-institution registration information for a given end customer.
[**partnerCustomerRemove**](PlaidApi.md#partnerCustomerRemove) | **POST** /partner/customer/remove | Removes a Plaid reseller&#39;s end customer.
[**paymentInitiationConsentCreate**](PlaidApi.md#paymentInitiationConsentCreate) | **POST** /payment_initiation/consent/create | Create payment consent
[**paymentInitiationConsentGet**](PlaidApi.md#paymentInitiationConsentGet) | **POST** /payment_initiation/consent/get | Get payment consent
[**paymentInitiationConsentPaymentExecute**](PlaidApi.md#paymentInitiationConsentPaymentExecute) | **POST** /payment_initiation/consent/payment/execute | Execute a single payment using consent
[**paymentInitiationConsentRevoke**](PlaidApi.md#paymentInitiationConsentRevoke) | **POST** /payment_initiation/consent/revoke | Revoke payment consent
[**paymentInitiationPaymentCreate**](PlaidApi.md#paymentInitiationPaymentCreate) | **POST** /payment_initiation/payment/create | Create a payment
[**paymentInitiationPaymentGet**](PlaidApi.md#paymentInitiationPaymentGet) | **POST** /payment_initiation/payment/get | Get payment details
[**paymentInitiationPaymentList**](PlaidApi.md#paymentInitiationPaymentList) | **POST** /payment_initiation/payment/list | List payments
[**paymentInitiationPaymentReverse**](PlaidApi.md#paymentInitiationPaymentReverse) | **POST** /payment_initiation/payment/reverse | Reverse an existing payment
[**paymentInitiationRecipientCreate**](PlaidApi.md#paymentInitiationRecipientCreate) | **POST** /payment_initiation/recipient/create | Create payment recipient
[**paymentInitiationRecipientGet**](PlaidApi.md#paymentInitiationRecipientGet) | **POST** /payment_initiation/recipient/get | Get payment recipient
[**paymentInitiationRecipientList**](PlaidApi.md#paymentInitiationRecipientList) | **POST** /payment_initiation/recipient/list | List payment recipients
[**paymentProfileCreate**](PlaidApi.md#paymentProfileCreate) | **POST** /payment_profile/create | Create payment profile
[**paymentProfileGet**](PlaidApi.md#paymentProfileGet) | **POST** /payment_profile/get | Get payment profile
[**paymentProfileRemove**](PlaidApi.md#paymentProfileRemove) | **POST** /payment_profile/remove | Remove payment profile
[**processorApexProcessorTokenCreate**](PlaidApi.md#processorApexProcessorTokenCreate) | **POST** /processor/apex/processor_token/create | Create Apex bank account token
[**processorAuthGet**](PlaidApi.md#processorAuthGet) | **POST** /processor/auth/get | Retrieve Auth data
[**processorBalanceGet**](PlaidApi.md#processorBalanceGet) | **POST** /processor/balance/get | Retrieve Balance data
[**processorBankTransferCreate**](PlaidApi.md#processorBankTransferCreate) | **POST** /processor/bank_transfer/create | Create a bank transfer as a processor
[**processorIdentityGet**](PlaidApi.md#processorIdentityGet) | **POST** /processor/identity/get | Retrieve Identity data
[**processorSignalDecisionReport**](PlaidApi.md#processorSignalDecisionReport) | **POST** /processor/signal/decision/report | Report whether you initiated an ACH transaction
[**processorSignalEvaluate**](PlaidApi.md#processorSignalEvaluate) | **POST** /processor/signal/evaluate | Evaluate a planned ACH transaction
[**processorSignalReturnReport**](PlaidApi.md#processorSignalReturnReport) | **POST** /processor/signal/return/report | Report a return for an ACH transaction
[**processorStripeBankAccountTokenCreate**](PlaidApi.md#processorStripeBankAccountTokenCreate) | **POST** /processor/stripe/bank_account_token/create | Create Stripe bank account token
[**processorTokenCreate**](PlaidApi.md#processorTokenCreate) | **POST** /processor/token/create | Create processor token
[**sandboxBankTransferFireWebhook**](PlaidApi.md#sandboxBankTransferFireWebhook) | **POST** /sandbox/bank_transfer/fire_webhook | Manually fire a Bank Transfer webhook
[**sandboxBankTransferSimulate**](PlaidApi.md#sandboxBankTransferSimulate) | **POST** /sandbox/bank_transfer/simulate | Simulate a bank transfer event in Sandbox
[**sandboxIncomeFireWebhook**](PlaidApi.md#sandboxIncomeFireWebhook) | **POST** /sandbox/income/fire_webhook | Manually fire an Income webhook
[**sandboxItemFireWebhook**](PlaidApi.md#sandboxItemFireWebhook) | **POST** /sandbox/item/fire_webhook | Fire a test webhook
[**sandboxItemResetLogin**](PlaidApi.md#sandboxItemResetLogin) | **POST** /sandbox/item/reset_login | Force a Sandbox Item into an error state
[**sandboxItemSetVerificationStatus**](PlaidApi.md#sandboxItemSetVerificationStatus) | **POST** /sandbox/item/set_verification_status | Set verification status for Sandbox account
[**sandboxOauthSelectAccounts**](PlaidApi.md#sandboxOauthSelectAccounts) | **POST** /sandbox/oauth/select_accounts | Save the selected accounts when connecting to the Platypus Oauth institution
[**sandboxPaymentProfileResetLogin**](PlaidApi.md#sandboxPaymentProfileResetLogin) | **POST** /sandbox/payment_profile/reset_login | Reset the login of a Payment Profile
[**sandboxProcessorTokenCreate**](PlaidApi.md#sandboxProcessorTokenCreate) | **POST** /sandbox/processor_token/create | Create a test Item and processor token
[**sandboxPublicTokenCreate**](PlaidApi.md#sandboxPublicTokenCreate) | **POST** /sandbox/public_token/create | Create a test Item
[**sandboxTransferFireWebhook**](PlaidApi.md#sandboxTransferFireWebhook) | **POST** /sandbox/transfer/fire_webhook | Manually fire a Transfer webhook
[**sandboxTransferRepaymentSimulate**](PlaidApi.md#sandboxTransferRepaymentSimulate) | **POST** /sandbox/transfer/repayment/simulate | Trigger the creation of a repayment
[**sandboxTransferSimulate**](PlaidApi.md#sandboxTransferSimulate) | **POST** /sandbox/transfer/simulate | Simulate a transfer event in Sandbox
[**sandboxTransferSweepSimulate**](PlaidApi.md#sandboxTransferSweepSimulate) | **POST** /sandbox/transfer/sweep/simulate | Simulate creating a sweep
[**sandboxTransferTestClockAdvance**](PlaidApi.md#sandboxTransferTestClockAdvance) | **POST** /sandbox/transfer/test_clock/advance | Advance a test clock
[**sandboxTransferTestClockCreate**](PlaidApi.md#sandboxTransferTestClockCreate) | **POST** /sandbox/transfer/test_clock/create | Create a test clock
[**sandboxTransferTestClockGet**](PlaidApi.md#sandboxTransferTestClockGet) | **POST** /sandbox/transfer/test_clock/get | Get a test clock
[**sandboxTransferTestClockList**](PlaidApi.md#sandboxTransferTestClockList) | **POST** /sandbox/transfer/test_clock/list | List test clocks
[**signalDecisionReport**](PlaidApi.md#signalDecisionReport) | **POST** /signal/decision/report | Report whether you initiated an ACH transaction
[**signalEvaluate**](PlaidApi.md#signalEvaluate) | **POST** /signal/evaluate | Evaluate a planned ACH transaction
[**signalPrepare**](PlaidApi.md#signalPrepare) | **POST** /signal/prepare | Opt-in an Item to Signal
[**signalReturnReport**](PlaidApi.md#signalReturnReport) | **POST** /signal/return/report | Report a return for an ACH transaction
[**transactionsEnhance**](PlaidApi.md#transactionsEnhance) | **POST** /beta/transactions/v1/enhance | enhance locally-held transaction data
[**transactionsEnrich**](PlaidApi.md#transactionsEnrich) | **POST** /transactions/enrich | Enrich locally-held transaction data
[**transactionsGet**](PlaidApi.md#transactionsGet) | **POST** /transactions/get | Get transaction data
[**transactionsRecurringGet**](PlaidApi.md#transactionsRecurringGet) | **POST** /transactions/recurring/get | Fetch recurring transaction streams
[**transactionsRefresh**](PlaidApi.md#transactionsRefresh) | **POST** /transactions/refresh | Refresh transaction data
[**transactionsRulesCreate**](PlaidApi.md#transactionsRulesCreate) | **POST** /beta/transactions/rules/v1/create | Create transaction category rule
[**transactionsRulesList**](PlaidApi.md#transactionsRulesList) | **POST** /beta/transactions/rules/v1/list | Return a list of rules created for the Item associated with the access token.
[**transactionsRulesRemove**](PlaidApi.md#transactionsRulesRemove) | **POST** /beta/transactions/rules/v1/remove | Remove transaction rule
[**transactionsSync**](PlaidApi.md#transactionsSync) | **POST** /transactions/sync | Get incremental transaction updates on an Item
[**transferAuthorizationCreate**](PlaidApi.md#transferAuthorizationCreate) | **POST** /transfer/authorization/create | Create a transfer authorization
[**transferCancel**](PlaidApi.md#transferCancel) | **POST** /transfer/cancel | Cancel a transfer
[**transferCapabilitiesGet**](PlaidApi.md#transferCapabilitiesGet) | **POST** /transfer/capabilities/get | Get RTP eligibility information of a transfer
[**transferConfigurationGet**](PlaidApi.md#transferConfigurationGet) | **POST** /transfer/configuration/get | Get transfer product configuration
[**transferCreate**](PlaidApi.md#transferCreate) | **POST** /transfer/create | Create a transfer
[**transferEventList**](PlaidApi.md#transferEventList) | **POST** /transfer/event/list | List transfer events
[**transferEventSync**](PlaidApi.md#transferEventSync) | **POST** /transfer/event/sync | Sync transfer events
[**transferGet**](PlaidApi.md#transferGet) | **POST** /transfer/get | Retrieve a transfer
[**transferIntentCreate**](PlaidApi.md#transferIntentCreate) | **POST** /transfer/intent/create | Create a transfer intent object to invoke the Transfer UI
[**transferIntentGet**](PlaidApi.md#transferIntentGet) | **POST** /transfer/intent/get | Retrieve more information about a transfer intent
[**transferList**](PlaidApi.md#transferList) | **POST** /transfer/list | List transfers
[**transferMetricsGet**](PlaidApi.md#transferMetricsGet) | **POST** /transfer/metrics/get | Get transfer product usage metrics
[**transferMigrateAccount**](PlaidApi.md#transferMigrateAccount) | **POST** /transfer/migrate_account | Migrate account into Transfers
[**transferOriginatorCreate**](PlaidApi.md#transferOriginatorCreate) | **POST** /transfer/originator/create | Create a new originator
[**transferOriginatorGet**](PlaidApi.md#transferOriginatorGet) | **POST** /transfer/originator/get | Get status of an originator&#39;s onboarding
[**transferOriginatorList**](PlaidApi.md#transferOriginatorList) | **POST** /transfer/originator/list | Get status of all originators&#39; onboarding
[**transferQuestionnaireCreate**](PlaidApi.md#transferQuestionnaireCreate) | **POST** /transfer/questionnaire/create | Generate a Plaid-hosted onboarding UI URL.
[**transferRecurringCancel**](PlaidApi.md#transferRecurringCancel) | **POST** /transfer/recurring/cancel | Cancel a recurring transfer.
[**transferRecurringCreate**](PlaidApi.md#transferRecurringCreate) | **POST** /transfer/recurring/create | Create a recurring transfer
[**transferRecurringGet**](PlaidApi.md#transferRecurringGet) | **POST** /transfer/recurring/get | Retrieve a recurring transfer
[**transferRecurringList**](PlaidApi.md#transferRecurringList) | **POST** /transfer/recurring/list | List recurring transfers
[**transferRefundCancel**](PlaidApi.md#transferRefundCancel) | **POST** /transfer/refund/cancel | Cancel a refund
[**transferRefundCreate**](PlaidApi.md#transferRefundCreate) | **POST** /transfer/refund/create | Create a refund
[**transferRefundGet**](PlaidApi.md#transferRefundGet) | **POST** /transfer/refund/get | Retrieve a refund
[**transferRepaymentList**](PlaidApi.md#transferRepaymentList) | **POST** /transfer/repayment/list | Lists historical repayments
[**transferRepaymentReturnList**](PlaidApi.md#transferRepaymentReturnList) | **POST** /transfer/repayment/return/list | List the returns included in a repayment
[**transferSweepGet**](PlaidApi.md#transferSweepGet) | **POST** /transfer/sweep/get | Retrieve a sweep
[**transferSweepList**](PlaidApi.md#transferSweepList) | **POST** /transfer/sweep/list | List sweeps
[**userCreate**](PlaidApi.md#userCreate) | **POST** /user/create | Create user
[**walletCreate**](PlaidApi.md#walletCreate) | **POST** /wallet/create | Create an e-wallet
[**walletGet**](PlaidApi.md#walletGet) | **POST** /wallet/get | Fetch an e-wallet
[**walletList**](PlaidApi.md#walletList) | **POST** /wallet/list | Fetch a list of e-wallets
[**walletTransactionExecute**](PlaidApi.md#walletTransactionExecute) | **POST** /wallet/transaction/execute | Execute a transaction using an e-wallet
[**walletTransactionGet**](PlaidApi.md#walletTransactionGet) | **POST** /wallet/transaction/get | Fetch an e-wallet transaction
[**walletTransactionList**](PlaidApi.md#walletTransactionList) | **POST** /wallet/transaction/list | List e-wallet transactions
[**watchlistScreeningEntityCreate**](PlaidApi.md#watchlistScreeningEntityCreate) | **POST** /watchlist_screening/entity/create | Create a watchlist screening for an entity
[**watchlistScreeningEntityGet**](PlaidApi.md#watchlistScreeningEntityGet) | **POST** /watchlist_screening/entity/get | Get an entity screening
[**watchlistScreeningEntityHistoryList**](PlaidApi.md#watchlistScreeningEntityHistoryList) | **POST** /watchlist_screening/entity/history/list | List history for entity watchlist screenings
[**watchlistScreeningEntityHitList**](PlaidApi.md#watchlistScreeningEntityHitList) | **POST** /watchlist_screening/entity/hit/list | List hits for entity watchlist screenings
[**watchlistScreeningEntityList**](PlaidApi.md#watchlistScreeningEntityList) | **POST** /watchlist_screening/entity/list | List entity watchlist screenings
[**watchlistScreeningEntityProgramGet**](PlaidApi.md#watchlistScreeningEntityProgramGet) | **POST** /watchlist_screening/entity/program/get | Get entity watchlist screening program
[**watchlistScreeningEntityProgramList**](PlaidApi.md#watchlistScreeningEntityProgramList) | **POST** /watchlist_screening/entity/program/list | List entity watchlist screening programs
[**watchlistScreeningEntityReviewCreate**](PlaidApi.md#watchlistScreeningEntityReviewCreate) | **POST** /watchlist_screening/entity/review/create | Create a review for an entity watchlist screening
[**watchlistScreeningEntityReviewList**](PlaidApi.md#watchlistScreeningEntityReviewList) | **POST** /watchlist_screening/entity/review/list | List reviews for entity watchlist screenings
[**watchlistScreeningEntityUpdate**](PlaidApi.md#watchlistScreeningEntityUpdate) | **POST** /watchlist_screening/entity/update | Update an entity screening
[**watchlistScreeningIndividualCreate**](PlaidApi.md#watchlistScreeningIndividualCreate) | **POST** /watchlist_screening/individual/create | Create a watchlist screening for a person
[**watchlistScreeningIndividualGet**](PlaidApi.md#watchlistScreeningIndividualGet) | **POST** /watchlist_screening/individual/get | Retrieve an individual watchlist screening
[**watchlistScreeningIndividualHistoryList**](PlaidApi.md#watchlistScreeningIndividualHistoryList) | **POST** /watchlist_screening/individual/history/list | List history for individual watchlist screenings
[**watchlistScreeningIndividualHitList**](PlaidApi.md#watchlistScreeningIndividualHitList) | **POST** /watchlist_screening/individual/hit/list | List hits for individual watchlist screening
[**watchlistScreeningIndividualList**](PlaidApi.md#watchlistScreeningIndividualList) | **POST** /watchlist_screening/individual/list | List Individual Watchlist Screenings
[**watchlistScreeningIndividualProgramGet**](PlaidApi.md#watchlistScreeningIndividualProgramGet) | **POST** /watchlist_screening/individual/program/get | Get individual watchlist screening program
[**watchlistScreeningIndividualProgramList**](PlaidApi.md#watchlistScreeningIndividualProgramList) | **POST** /watchlist_screening/individual/program/list | List individual watchlist screening programs
[**watchlistScreeningIndividualReviewCreate**](PlaidApi.md#watchlistScreeningIndividualReviewCreate) | **POST** /watchlist_screening/individual/review/create | Create a review for an individual watchlist screening
[**watchlistScreeningIndividualReviewList**](PlaidApi.md#watchlistScreeningIndividualReviewList) | **POST** /watchlist_screening/individual/review/list | List reviews for individual watchlist screenings
[**watchlistScreeningIndividualUpdate**](PlaidApi.md#watchlistScreeningIndividualUpdate) | **POST** /watchlist_screening/individual/update | Update individual watchlist screening
[**webhookVerificationKeyGet**](PlaidApi.md#webhookVerificationKeyGet) | **POST** /webhook_verification_key/get | Get webhook verification key



## accountsBalanceGet

> AccountsGetResponse accountsBalanceGet(accountsBalanceGetRequest)

Retrieve real-time balance data

The &#x60;/accounts/balance/get&#x60; endpoint returns the real-time balance for each of an Item&#39;s accounts. While other endpoints may return a balance object, only &#x60;/accounts/balance/get&#x60; forces the available and current balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other product, &#x60;balance&#x60; itself is not a product that can be used to initialize Link. As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints; if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let accountsBalanceGetRequest = {"access_token":"string","client_id":"string","options":{"account_ids":["string"]},"secret":"string"}; // AccountsBalanceGetRequest | 
apiInstance.accountsBalanceGet(accountsBalanceGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountsBalanceGetRequest** | [**AccountsBalanceGetRequest**](AccountsBalanceGetRequest.md)|  | 

### Return type

[**AccountsGetResponse**](AccountsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsGet

> AccountsGetResponse accountsGet(accountsGetRequest)

Retrieve accounts

The &#x60;/accounts/get&#x60; endpoint can be used to retrieve a list of accounts associated with any linked Item. Plaid will only return active bank accounts — that is, accounts that are not closed and are capable of carrying a balance. For items that went through the updated account selection pane, this endpoint only returns accounts that were permissioned by the user when they initially created the Item. If a user creates a new account after the initial link, you can capture this event through the [&#x60;NEW_ACCOUNTS_AVAILABLE&#x60;](https://plaid.com/docs/api/items/#new_accounts_available) webhook and then use Link&#39;s [update mode](https://plaid.com/docs/link/update-mode/) to request that the user share this new account with you.  This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, balances returned may not be up-to-date; for realtime balance information, use &#x60;/accounts/balance/get&#x60; instead. Note that some information is nullable.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let accountsGetRequest = {"access_token":"string","client_id":"string","options":{"account_ids":["string"]},"secret":"string"}; // AccountsGetRequest | 
apiInstance.accountsGet(accountsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountsGetRequest** | [**AccountsGetRequest**](AccountsGetRequest.md)|  | 

### Return type

[**AccountsGetResponse**](AccountsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationGet

> ApplicationGetResponse applicationGet(applicationGetRequest)

Retrieve information about a Plaid application

Allows financial institutions to retrieve information about Plaid clients for the purpose of building control-tower experiences

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let applicationGetRequest = new ThePlaidApi.ApplicationGetRequest(); // ApplicationGetRequest | 
apiInstance.applicationGet(applicationGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationGetRequest** | [**ApplicationGetRequest**](ApplicationGetRequest.md)|  | 

### Return type

[**ApplicationGetResponse**](ApplicationGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetReportAuditCopyCreate

> AssetReportAuditCopyCreateResponse assetReportAuditCopyCreate(assetReportAuditCopyCreateRequest)

Create Asset Report Audit Copy

Plaid can provide an Audit Copy of any Asset Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy directly to Fannie Mae on your behalf if you participate in the Day 1 Certainty™ program. An Audit Copy contains the same underlying data as the Asset Report.  To grant access to an Audit Copy, use the &#x60;/asset_report/audit_copy/create&#x60; endpoint to create an &#x60;audit_copy_token&#x60; and then pass that token to the third party who needs access. Each third party has its own &#x60;auditor_id&#x60;, for example &#x60;fannie_mae&#x60;. You’ll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let assetReportAuditCopyCreateRequest = new ThePlaidApi.AssetReportAuditCopyCreateRequest(); // AssetReportAuditCopyCreateRequest | 
apiInstance.assetReportAuditCopyCreate(assetReportAuditCopyCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetReportAuditCopyCreateRequest** | [**AssetReportAuditCopyCreateRequest**](AssetReportAuditCopyCreateRequest.md)|  | 

### Return type

[**AssetReportAuditCopyCreateResponse**](AssetReportAuditCopyCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetReportAuditCopyGet

> AssetReportGetResponse assetReportAuditCopyGet(assetReportAuditCopyGetRequest)

Retrieve an Asset Report Audit Copy

&#x60;/asset_report/audit_copy/get&#x60; allows auditors to get a copy of an Asset Report that was previously shared via the &#x60;/asset_report/audit_copy/create&#x60; endpoint.  The caller of &#x60;/asset_report/audit_copy/create&#x60; must provide the &#x60;audit_copy_token&#x60; to the auditor.  This token can then be used to call &#x60;/asset_report/audit_copy/create&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let assetReportAuditCopyGetRequest = new ThePlaidApi.AssetReportAuditCopyGetRequest(); // AssetReportAuditCopyGetRequest | 
apiInstance.assetReportAuditCopyGet(assetReportAuditCopyGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetReportAuditCopyGetRequest** | [**AssetReportAuditCopyGetRequest**](AssetReportAuditCopyGetRequest.md)|  | 

### Return type

[**AssetReportGetResponse**](AssetReportGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetReportAuditCopyRemove

> AssetReportAuditCopyRemoveResponse assetReportAuditCopyRemove(assetReportAuditCopyRemoveRequest)

Remove Asset Report Audit Copy

The &#x60;/asset_report/audit_copy/remove&#x60; endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the &#x60;audit_copy_token&#x60; associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Asset Report, the Asset Report itself and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let assetReportAuditCopyRemoveRequest = new ThePlaidApi.AssetReportAuditCopyRemoveRequest(); // AssetReportAuditCopyRemoveRequest | 
apiInstance.assetReportAuditCopyRemove(assetReportAuditCopyRemoveRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetReportAuditCopyRemoveRequest** | [**AssetReportAuditCopyRemoveRequest**](AssetReportAuditCopyRemoveRequest.md)|  | 

### Return type

[**AssetReportAuditCopyRemoveResponse**](AssetReportAuditCopyRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetReportCreate

> AssetReportCreateResponse assetReportCreate(assetReportCreateRequest)

Create an Asset Report

The &#x60;/asset_report/create&#x60; endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the &#x60;asset_report_token&#x60; return value to the &#x60;/asset_report/get&#x60; or &#x60;/asset_report/pdf/get&#x60; endpoints.  The Asset Report takes some time to be created and is not available immediately after calling &#x60;/asset_report/create&#x60;. When the Asset Report is ready to be retrieved using &#x60;/asset_report/get&#x60; or &#x60;/asset_report/pdf/get&#x60;, Plaid will fire a &#x60;PRODUCT_READY&#x60; webhook. For full details of the webhook schema, see [Asset Report webhooks](https://plaid.com/docs/api/products/assets/#webhooks).  The &#x60;/asset_report/create&#x60; endpoint creates an Asset Report at a moment in time. Asset Reports are immutable. To get an updated Asset Report, use the &#x60;/asset_report/refresh&#x60; endpoint.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let assetReportCreateRequest = new ThePlaidApi.AssetReportCreateRequest(); // AssetReportCreateRequest | 
apiInstance.assetReportCreate(assetReportCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetReportCreateRequest** | [**AssetReportCreateRequest**](AssetReportCreateRequest.md)|  | 

### Return type

[**AssetReportCreateResponse**](AssetReportCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetReportFilter

> AssetReportFilterResponse assetReportFilter(assetReportFilterRequest)

Filter Asset Report

By default, an Asset Report will contain all of the accounts on a given Item. In some cases, you may not want the Asset Report to contain all accounts. For example, you might have the end user choose which accounts are relevant in Link using the Account Select view, which you can enable in the dashboard. Or, you might always exclude certain account types or subtypes, which you can identify by using the &#x60;/accounts/get&#x60; endpoint. To narrow an Asset Report to only a subset of accounts, use the &#x60;/asset_report/filter&#x60; endpoint.  To exclude certain Accounts from an Asset Report, first use the &#x60;/asset_report/create&#x60; endpoint to create the report, then send the &#x60;asset_report_token&#x60; along with a list of &#x60;account_ids&#x60; to exclude to the &#x60;/asset_report/filter&#x60; endpoint, to create a new Asset Report which contains only a subset of the original Asset Report&#39;s data.  Because Asset Reports are immutable, calling &#x60;/asset_report/filter&#x60; does not alter the original Asset Report in any way; rather, &#x60;/asset_report/filter&#x60; creates a new Asset Report with a new token and id. Asset Reports created via &#x60;/asset_report/filter&#x60; do not contain new Asset data, and are not billed.  Plaid will fire a [&#x60;PRODUCT_READY&#x60;](https://plaid.com/docs/api/products/assets/#product_ready) webhook once generation of the filtered Asset Report has completed.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let assetReportFilterRequest = new ThePlaidApi.AssetReportFilterRequest(); // AssetReportFilterRequest | 
apiInstance.assetReportFilter(assetReportFilterRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetReportFilterRequest** | [**AssetReportFilterRequest**](AssetReportFilterRequest.md)|  | 

### Return type

[**AssetReportFilterResponse**](AssetReportFilterResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetReportGet

> AssetReportGetResponse assetReportGet(assetReportGetRequest)

Retrieve an Asset Report

The &#x60;/asset_report/get&#x60; endpoint retrieves the Asset Report in JSON format. Before calling &#x60;/asset_report/get&#x60;, you must first create the Asset Report using &#x60;/asset_report/create&#x60; (or filter an Asset Report using &#x60;/asset_report/filter&#x60;) and then wait for the [&#x60;PRODUCT_READY&#x60;](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.  By default, an Asset Report includes transaction descriptions as returned by the bank, as opposed to parsed and categorized by Plaid. You can also receive cleaned and categorized transactions, as well as additional insights like merchant name or location information. We call this an Asset Report with Insights. An Asset Report with Insights provides transaction category, location, and merchant information in addition to the transaction strings provided in a standard Asset Report.  If report_type was set to &#x60;VERIFICATION_OF_EMPLOYMENT&#x60; when the Asset Report was created in asset_report/create, debit transactions and transaction amounts won’t be included in the report.  To retrieve an Asset Report with Insights, call the &#x60;/asset_report/get&#x60; endpoint with &#x60;include_insights&#x60; set to &#x60;true&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let assetReportGetRequest = new ThePlaidApi.AssetReportGetRequest(); // AssetReportGetRequest | 
apiInstance.assetReportGet(assetReportGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetReportGetRequest** | [**AssetReportGetRequest**](AssetReportGetRequest.md)|  | 

### Return type

[**AssetReportGetResponse**](AssetReportGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetReportPdfGet

> File assetReportPdfGet(assetReportPDFGetRequest)

Retrieve a PDF Asset Report

The &#x60;/asset_report/pdf/get&#x60; endpoint retrieves the Asset Report in PDF format. Before calling &#x60;/asset_report/pdf/get&#x60;, you must first create the Asset Report using &#x60;/asset_report/create&#x60; (or filter an Asset Report using &#x60;/asset_report/filter&#x60;) and then wait for the [&#x60;PRODUCT_READY&#x60;](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.  The response to &#x60;/asset_report/pdf/get&#x60; is the PDF binary data. The &#x60;request_id&#x60;  is returned in the &#x60;Plaid-Request-ID&#x60; header.  If report_type was set to &#x60;VERIFICATION_OF_EMPLOYMENT&#x60; when the Asset Report was created in asset_report/create, debit transactions and transaction amounts won’t be included in the report.  [View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let assetReportPDFGetRequest = new ThePlaidApi.AssetReportPDFGetRequest(); // AssetReportPDFGetRequest | 
apiInstance.assetReportPdfGet(assetReportPDFGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetReportPDFGetRequest** | [**AssetReportPDFGetRequest**](AssetReportPDFGetRequest.md)|  | 

### Return type

**File**

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf


## assetReportRefresh

> AssetReportRefreshResponse assetReportRefresh(assetReportRefreshRequest)

Refresh an Asset Report

An Asset Report is an immutable snapshot of a user&#39;s assets. In order to \&quot;refresh\&quot; an Asset Report you created previously, you can use the &#x60;/asset_report/refresh&#x60; endpoint to create a new Asset Report based on the old one, but with the most recent data available.  The new Asset Report will contain the same Items as the original Report, as well as the same filters applied by any call to &#x60;/asset_report/filter&#x60;. By default, the new Asset Report will also use the same parameters you submitted with your original &#x60;/asset_report/create&#x60; request, but the original &#x60;days_requested&#x60; value and the values of any parameters in the &#x60;options&#x60; object can be overridden with new values. To change these arguments, simply supply new values for them in your request to &#x60;/asset_report/refresh&#x60;. Submit an empty string (\&quot;\&quot;) for any previously-populated fields you would like set as empty.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let assetReportRefreshRequest = new ThePlaidApi.AssetReportRefreshRequest(); // AssetReportRefreshRequest | 
apiInstance.assetReportRefresh(assetReportRefreshRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetReportRefreshRequest** | [**AssetReportRefreshRequest**](AssetReportRefreshRequest.md)|  | 

### Return type

[**AssetReportRefreshResponse**](AssetReportRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assetReportRemove

> AssetReportRemoveResponse assetReportRemove(assetReportRemoveRequest)

Delete an Asset Report

The &#x60;/item/remove&#x60; endpoint allows you to invalidate an &#x60;access_token&#x60;, meaning you will not be able to create new Asset Reports with it. Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove them specifically.  The &#x60;/asset_report/remove&#x60; endpoint allows you to remove an Asset Report. Removing an Asset Report invalidates its &#x60;asset_report_token&#x60;, meaning you will no longer be able to use it to access Report data or create new Audit Copies. Removing an Asset Report does not affect the underlying Items, but does invalidate any &#x60;audit_copy_tokens&#x60; associated with the Asset Report.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let assetReportRemoveRequest = new ThePlaidApi.AssetReportRemoveRequest(); // AssetReportRemoveRequest | 
apiInstance.assetReportRemove(assetReportRemoveRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetReportRemoveRequest** | [**AssetReportRemoveRequest**](AssetReportRemoveRequest.md)|  | 

### Return type

[**AssetReportRemoveResponse**](AssetReportRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## authGet

> AuthGetResponse authGet(authGetRequest)

Retrieve auth data

The &#x60;/auth/get&#x60; endpoint returns the bank account and bank identification numbers (such as routing numbers, for US accounts) associated with an Item&#39;s checking and savings accounts, along with high-level account data and balances when available.  Note: This request may take some time to complete if &#x60;auth&#x60; was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.  Versioning note: In API version 2017-03-08, the schema of the &#x60;numbers&#x60; object returned by this endpoint is substantially different. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2018-05-22).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let authGetRequest = new ThePlaidApi.AuthGetRequest(); // AuthGetRequest | 
apiInstance.authGet(authGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authGetRequest** | [**AuthGetRequest**](AuthGetRequest.md)|  | 

### Return type

[**AuthGetResponse**](AuthGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankTransferBalanceGet

> BankTransferBalanceGetResponse bankTransferBalanceGet(bankTransferBalanceGetRequest)

Get balance of your Bank Transfer account

Use the &#x60;/bank_transfer/balance/get&#x60; endpoint to see the available balance in your bank transfer account. Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when they are created.  The transactable balance shows the amount in your account that you are able to use for transfers, and is essentially your available balance minus your minimum balance.  Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform configuration.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let bankTransferBalanceGetRequest = new ThePlaidApi.BankTransferBalanceGetRequest(); // BankTransferBalanceGetRequest | 
apiInstance.bankTransferBalanceGet(bankTransferBalanceGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankTransferBalanceGetRequest** | [**BankTransferBalanceGetRequest**](BankTransferBalanceGetRequest.md)|  | 

### Return type

[**BankTransferBalanceGetResponse**](BankTransferBalanceGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankTransferCancel

> BankTransferCancelResponse bankTransferCancel(bankTransferCancelRequest)

Cancel a bank transfer

Use the &#x60;/bank_transfer/cancel&#x60; endpoint to cancel a bank transfer.  A transfer is eligible for cancelation if the &#x60;cancellable&#x60; property returned by &#x60;/bank_transfer/get&#x60; is &#x60;true&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let bankTransferCancelRequest = new ThePlaidApi.BankTransferCancelRequest(); // BankTransferCancelRequest | 
apiInstance.bankTransferCancel(bankTransferCancelRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankTransferCancelRequest** | [**BankTransferCancelRequest**](BankTransferCancelRequest.md)|  | 

### Return type

[**BankTransferCancelResponse**](BankTransferCancelResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankTransferCreate

> BankTransferCreateResponse bankTransferCreate(bankTransferCreateRequest)

Create a bank transfer

Use the &#x60;/bank_transfer/create&#x60; endpoint to initiate a new bank transfer.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let bankTransferCreateRequest = new ThePlaidApi.BankTransferCreateRequest(); // BankTransferCreateRequest | 
apiInstance.bankTransferCreate(bankTransferCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankTransferCreateRequest** | [**BankTransferCreateRequest**](BankTransferCreateRequest.md)|  | 

### Return type

[**BankTransferCreateResponse**](BankTransferCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankTransferEventList

> BankTransferEventListResponse bankTransferEventList(bankTransferEventListRequest)

List bank transfer events

Use the &#x60;/bank_transfer/event/list&#x60; endpoint to get a list of Plaid-initiated ACH or bank transfer events based on specified filter criteria. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://plaid.com/docs/auth/coverage/microdeposit-events/).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let bankTransferEventListRequest = new ThePlaidApi.BankTransferEventListRequest(); // BankTransferEventListRequest | 
apiInstance.bankTransferEventList(bankTransferEventListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankTransferEventListRequest** | [**BankTransferEventListRequest**](BankTransferEventListRequest.md)|  | 

### Return type

[**BankTransferEventListResponse**](BankTransferEventListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankTransferEventSync

> BankTransferEventSyncResponse bankTransferEventSync(bankTransferEventSyncRequest)

Sync bank transfer events

&#x60;/bank_transfer/event/sync&#x60; allows you to request up to the next 25 Plaid-initiated bank transfer events that happened after a specific &#x60;event_id&#x60;. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://www.plaid.com/docs/auth/coverage/microdeposit-events/).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let bankTransferEventSyncRequest = new ThePlaidApi.BankTransferEventSyncRequest(); // BankTransferEventSyncRequest | 
apiInstance.bankTransferEventSync(bankTransferEventSyncRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankTransferEventSyncRequest** | [**BankTransferEventSyncRequest**](BankTransferEventSyncRequest.md)|  | 

### Return type

[**BankTransferEventSyncResponse**](BankTransferEventSyncResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankTransferGet

> BankTransferGetResponse bankTransferGet(bankTransferGetRequest)

Retrieve a bank transfer

The &#x60;/bank_transfer/get&#x60; fetches information about the bank transfer corresponding to the given &#x60;bank_transfer_id&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let bankTransferGetRequest = new ThePlaidApi.BankTransferGetRequest(); // BankTransferGetRequest | 
apiInstance.bankTransferGet(bankTransferGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankTransferGetRequest** | [**BankTransferGetRequest**](BankTransferGetRequest.md)|  | 

### Return type

[**BankTransferGetResponse**](BankTransferGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankTransferList

> BankTransferListResponse bankTransferList(bankTransferListRequest)

List bank transfers

Use the &#x60;/bank_transfer/list&#x60; endpoint to see a list of all your bank transfers and their statuses. Results are paginated; use the &#x60;count&#x60; and &#x60;offset&#x60; query parameters to retrieve the desired bank transfers. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let bankTransferListRequest = new ThePlaidApi.BankTransferListRequest(); // BankTransferListRequest | 
apiInstance.bankTransferList(bankTransferListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankTransferListRequest** | [**BankTransferListRequest**](BankTransferListRequest.md)|  | 

### Return type

[**BankTransferListResponse**](BankTransferListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankTransferMigrateAccount

> BankTransferMigrateAccountResponse bankTransferMigrateAccount(bankTransferMigrateAccountRequest)

Migrate account into Bank Transfers

As an alternative to adding Items via Link, you can also use the &#x60;/bank_transfer/migrate_account&#x60; endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as &#x60;/accounts/balance/get&#x60;, and can only be used with Bank Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to &#x60;/bank_transfer/migrate_account&#x60; is not enabled by default; to obtain access, contact your Plaid Account Manager.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let bankTransferMigrateAccountRequest = new ThePlaidApi.BankTransferMigrateAccountRequest(); // BankTransferMigrateAccountRequest | 
apiInstance.bankTransferMigrateAccount(bankTransferMigrateAccountRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankTransferMigrateAccountRequest** | [**BankTransferMigrateAccountRequest**](BankTransferMigrateAccountRequest.md)|  | 

### Return type

[**BankTransferMigrateAccountResponse**](BankTransferMigrateAccountResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankTransferSweepGet

> BankTransferSweepGetResponse bankTransferSweepGet(bankTransferSweepGetRequest)

Retrieve a sweep

The &#x60;/bank_transfer/sweep/get&#x60; endpoint fetches information about the sweep corresponding to the given &#x60;sweep_id&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let bankTransferSweepGetRequest = new ThePlaidApi.BankTransferSweepGetRequest(); // BankTransferSweepGetRequest | 
apiInstance.bankTransferSweepGet(bankTransferSweepGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankTransferSweepGetRequest** | [**BankTransferSweepGetRequest**](BankTransferSweepGetRequest.md)|  | 

### Return type

[**BankTransferSweepGetResponse**](BankTransferSweepGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bankTransferSweepList

> BankTransferSweepListResponse bankTransferSweepList(bankTransferSweepListRequest)

List sweeps

The &#x60;/bank_transfer/sweep/list&#x60; endpoint fetches information about the sweeps matching the given filters.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let bankTransferSweepListRequest = new ThePlaidApi.BankTransferSweepListRequest(); // BankTransferSweepListRequest | 
apiInstance.bankTransferSweepList(bankTransferSweepListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankTransferSweepListRequest** | [**BankTransferSweepListRequest**](BankTransferSweepListRequest.md)|  | 

### Return type

[**BankTransferSweepListResponse**](BankTransferSweepListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## categoriesGet

> CategoriesGetResponse categoriesGet(body)

Get Categories

Send a request to the &#x60;/categories/get&#x60; endpoint to get detailed information on categories returned by Plaid. This endpoint does not require authentication.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';

let apiInstance = new ThePlaidApi.PlaidApi();
let body = {key: null}; // Object | 
apiInstance.categoriesGet(body, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  | 

### Return type

[**CategoriesGetResponse**](CategoriesGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPaymentToken

> PaymentInitiationPaymentTokenCreateResponse createPaymentToken(paymentInitiationPaymentTokenCreateRequest)

Create payment token

The &#x60;/payment_initiation/payment/token/create&#x60; endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, &#x60;link_token&#x60;-based flow. The recommended flow is to provide the &#x60;payment_id&#x60; to &#x60;/link/token/create&#x60;, which returns a &#x60;link_token&#x60; used to initialize Link.  The &#x60;/payment_initiation/payment/token/create&#x60; is used to create a &#x60;payment_token&#x60;, which can then be used in Link initialization to enter a payment initiation flow. You can only use a &#x60;payment_token&#x60; once. If this attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token. Creating a new payment token does not require end user input.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationPaymentTokenCreateRequest = new ThePlaidApi.PaymentInitiationPaymentTokenCreateRequest(); // PaymentInitiationPaymentTokenCreateRequest | 
apiInstance.createPaymentToken(paymentInitiationPaymentTokenCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationPaymentTokenCreateRequest** | [**PaymentInitiationPaymentTokenCreateRequest**](PaymentInitiationPaymentTokenCreateRequest.md)|  | 

### Return type

[**PaymentInitiationPaymentTokenCreateResponse**](PaymentInitiationPaymentTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditAssetReportFreddieMacGet

> AssetReportFreddieGetResponse creditAssetReportFreddieMacGet(assetReportFreddieGetRequest)

Retrieve an Asset Report with Freddie Mac format. Only Freddie Mac can use this endpoint.

The &#x60;credit/asset_report/freddie_mac/get&#x60; endpoint retrieves the Asset Report in Freddie Mac&#39;s JSON format.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let assetReportFreddieGetRequest = new ThePlaidApi.AssetReportFreddieGetRequest(); // AssetReportFreddieGetRequest | 
apiInstance.creditAssetReportFreddieMacGet(assetReportFreddieGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assetReportFreddieGetRequest** | [**AssetReportFreddieGetRequest**](AssetReportFreddieGetRequest.md)|  | 

### Return type

[**AssetReportFreddieGetResponse**](AssetReportFreddieGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditAuditCopyTokenCreate

> CreditAuditCopyTokenCreateResponse creditAuditCopyTokenCreate(creditAuditCopyTokenCreateRequest)

Create Asset or Income Report Audit Copy Token

Plaid can create an Audit Copy token of an Asset Report and/or Income Report to share with participating Government Sponsored Entity (GSE). If you participate in the Day 1 Certainty™ program, Plaid can supply an Audit Copy token directly to Fannie Mae on your behalf. An Audit Copy token contains the same underlying data as the Asset Report and/or Income Report (result of /credit/payroll_income/get).  Use the &#x60;/credit/audit_copy_token/create&#x60; endpoint to create an &#x60;audit_copy_token&#x60; and then pass that token to the GSE who needs access.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditAuditCopyTokenCreateRequest = new ThePlaidApi.CreditAuditCopyTokenCreateRequest(); // CreditAuditCopyTokenCreateRequest | 
apiInstance.creditAuditCopyTokenCreate(creditAuditCopyTokenCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditAuditCopyTokenCreateRequest** | [**CreditAuditCopyTokenCreateRequest**](CreditAuditCopyTokenCreateRequest.md)|  | 

### Return type

[**CreditAuditCopyTokenCreateResponse**](CreditAuditCopyTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditAuditCopyTokenUpdate

> CreditAuditCopyTokenUpdateResponse creditAuditCopyTokenUpdate(creditAuditCopyTokenUpdateRequest)

Update an Audit Copy Token

The &#x60;/credit/audit_copy_token/update&#x60; endpoint updates an existing  Audit Copy Token by adding the report tokens in the &#x60;report_tokens&#x60; field to the &#x60;audit_copy_token&#x60;. If the Audit Copy Token already contains a report of a certain type, it will be replaced with the token provided in the &#x60;report_tokens&#x60; field.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditAuditCopyTokenUpdateRequest = new ThePlaidApi.CreditAuditCopyTokenUpdateRequest(); // CreditAuditCopyTokenUpdateRequest | 
apiInstance.creditAuditCopyTokenUpdate(creditAuditCopyTokenUpdateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditAuditCopyTokenUpdateRequest** | [**CreditAuditCopyTokenUpdateRequest**](CreditAuditCopyTokenUpdateRequest.md)|  | 

### Return type

[**CreditAuditCopyTokenUpdateResponse**](CreditAuditCopyTokenUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditBankEmploymentGet

> CreditBankEmploymentGetResponse creditBankEmploymentGet(creditBankEmploymentGetRequest)

Retrieve information from the bank accounts used for employment verification

&#x60;/credit/bank_employment/get&#x60; returns the employment report(s) derived from bank transaction data for a specified user.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditBankEmploymentGetRequest = new ThePlaidApi.CreditBankEmploymentGetRequest(); // CreditBankEmploymentGetRequest | 
apiInstance.creditBankEmploymentGet(creditBankEmploymentGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditBankEmploymentGetRequest** | [**CreditBankEmploymentGetRequest**](CreditBankEmploymentGetRequest.md)|  | 

### Return type

[**CreditBankEmploymentGetResponse**](CreditBankEmploymentGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditBankIncomeGet

> CreditBankIncomeGetResponse creditBankIncomeGet(creditBankIncomeGetRequest)

Retrieve information from the bank accounts used for income verification

&#x60;/credit/bank_income/get&#x60; returns the bank income report(s) for a specified user.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditBankIncomeGetRequest = new ThePlaidApi.CreditBankIncomeGetRequest(); // CreditBankIncomeGetRequest | 
apiInstance.creditBankIncomeGet(creditBankIncomeGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditBankIncomeGetRequest** | [**CreditBankIncomeGetRequest**](CreditBankIncomeGetRequest.md)|  | 

### Return type

[**CreditBankIncomeGetResponse**](CreditBankIncomeGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditBankIncomePdfGet

> File creditBankIncomePdfGet(creditBankIncomePDFGetRequest)

Retrieve information from the bank accounts used for income verification in PDF format

&#x60;/credit/bank_income/pdf/get&#x60; returns the most recent bank income report for a specified user in PDF format.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditBankIncomePDFGetRequest = new ThePlaidApi.CreditBankIncomePDFGetRequest(); // CreditBankIncomePDFGetRequest | 
apiInstance.creditBankIncomePdfGet(creditBankIncomePDFGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditBankIncomePDFGetRequest** | [**CreditBankIncomePDFGetRequest**](CreditBankIncomePDFGetRequest.md)|  | 

### Return type

**File**

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf


## creditBankIncomeRefresh

> CreditBankIncomeRefreshResponse creditBankIncomeRefresh(creditBankIncomeRefreshRequest)

Refresh a user&#39;s bank income information

&#x60;/credit/bank_income/refresh&#x60; refreshes the bank income report data for a specific user.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditBankIncomeRefreshRequest = new ThePlaidApi.CreditBankIncomeRefreshRequest(); // CreditBankIncomeRefreshRequest | 
apiInstance.creditBankIncomeRefresh(creditBankIncomeRefreshRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditBankIncomeRefreshRequest** | [**CreditBankIncomeRefreshRequest**](CreditBankIncomeRefreshRequest.md)|  | 

### Return type

[**CreditBankIncomeRefreshResponse**](CreditBankIncomeRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditEmploymentGet

> CreditEmploymentGetResponse creditEmploymentGet(creditEmploymentGetRequest)

Retrieve a summary of an individual&#39;s employment information

&#x60;/credit/employment/get&#x60; returns a list of items with employment information from a user&#39;s payroll provider that was verified by an end user.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditEmploymentGetRequest = new ThePlaidApi.CreditEmploymentGetRequest(); // CreditEmploymentGetRequest | 
apiInstance.creditEmploymentGet(creditEmploymentGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditEmploymentGetRequest** | [**CreditEmploymentGetRequest**](CreditEmploymentGetRequest.md)|  | 

### Return type

[**CreditEmploymentGetResponse**](CreditEmploymentGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditFreddieMacReportsGet

> CreditFreddieMacReportsGetResponse creditFreddieMacReportsGet(creditFreddieMacReportsGetRequest)

Retrieve an Asset Report with Freddie Mac format (aka VOA - Verification Of Assets), and a Verification Of Employment (VOE) report if this one is available. Only Freddie Mac can use this endpoint.

The &#x60;credit/asset_report/freddie_mac/get&#x60; endpoint retrieves the Verification of Assets and Verification of Employment reports.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditFreddieMacReportsGetRequest = new ThePlaidApi.CreditFreddieMacReportsGetRequest(); // CreditFreddieMacReportsGetRequest | 
apiInstance.creditFreddieMacReportsGet(creditFreddieMacReportsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditFreddieMacReportsGetRequest** | [**CreditFreddieMacReportsGetRequest**](CreditFreddieMacReportsGetRequest.md)|  | 

### Return type

[**CreditFreddieMacReportsGetResponse**](CreditFreddieMacReportsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditPayrollIncomeGet

> CreditPayrollIncomeGetResponse creditPayrollIncomeGet(creditPayrollIncomeGetRequest)

Retrieve a user&#39;s payroll information

This endpoint gets payroll income information for a specific user, either as a result of the user connecting to their payroll provider or uploading a pay related document.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditPayrollIncomeGetRequest = new ThePlaidApi.CreditPayrollIncomeGetRequest(); // CreditPayrollIncomeGetRequest | 
apiInstance.creditPayrollIncomeGet(creditPayrollIncomeGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditPayrollIncomeGetRequest** | [**CreditPayrollIncomeGetRequest**](CreditPayrollIncomeGetRequest.md)|  | 

### Return type

[**CreditPayrollIncomeGetResponse**](CreditPayrollIncomeGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditPayrollIncomePrecheck

> CreditPayrollIncomePrecheckResponse creditPayrollIncomePrecheck(creditPayrollIncomePrecheckRequest)

Check income verification eligibility and optimize conversion

&#x60;/credit/payroll_income/precheck&#x60; is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification. If the user is eligible for digital verification, that information will be associated with the user token, and in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.  While all request fields are optional, providing &#x60;employer&#x60; data will increase the chance of receiving a useful result.  When testing in Sandbox, you can control the results by providing special test values in the &#x60;employer&#x60; and &#x60;access_tokens&#x60; fields. &#x60;employer_good&#x60; and &#x60;employer_bad&#x60; will result in &#x60;HIGH&#x60; and &#x60;LOW&#x60; confidence values, respectively. &#x60;employer_multi&#x60; will result in a &#x60;HIGH&#x60; confidence with multiple payroll options. Likewise, &#x60;access_good&#x60; and &#x60;access_bad&#x60; will result in &#x60;HIGH&#x60; and &#x60;LOW&#x60; confidence values, respectively. Any other value for &#x60;employer&#x60; and &#x60;access_tokens&#x60; in Sandbox will result in &#x60;UNKNOWN&#x60; confidence.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditPayrollIncomePrecheckRequest = new ThePlaidApi.CreditPayrollIncomePrecheckRequest(); // CreditPayrollIncomePrecheckRequest | 
apiInstance.creditPayrollIncomePrecheck(creditPayrollIncomePrecheckRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditPayrollIncomePrecheckRequest** | [**CreditPayrollIncomePrecheckRequest**](CreditPayrollIncomePrecheckRequest.md)|  | 

### Return type

[**CreditPayrollIncomePrecheckResponse**](CreditPayrollIncomePrecheckResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditPayrollIncomeRefresh

> CreditPayrollIncomeRefreshResponse creditPayrollIncomeRefresh(creditPayrollIncomeRefreshRequest)

Refresh a digital payroll income verification

&#x60;/credit/payroll_income/refresh&#x60; refreshes a given digital payroll income verification.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditPayrollIncomeRefreshRequest = new ThePlaidApi.CreditPayrollIncomeRefreshRequest(); // CreditPayrollIncomeRefreshRequest | 
apiInstance.creditPayrollIncomeRefresh(creditPayrollIncomeRefreshRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditPayrollIncomeRefreshRequest** | [**CreditPayrollIncomeRefreshRequest**](CreditPayrollIncomeRefreshRequest.md)|  | 

### Return type

[**CreditPayrollIncomeRefreshResponse**](CreditPayrollIncomeRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditRelayCreate

> CreditRelayCreateResponse creditRelayCreate(creditRelayCreateRequest)

Create a relay token to share an Asset Report with a partner client (beta)

Plaid can share an Asset Report directly with a participating third party on your behalf. The shared Asset Report is the exact same Asset Report originally created in &#x60;/asset_report/create&#x60;.  To grant a third party access to an Asset Report, use the &#x60;/credit/relay/create&#x60; endpoint to create a &#x60;relay_token&#x60; and then pass that token to your third party. Each third party has its own &#x60;secondary_client_id&#x60;; for example, &#x60;ce5bd328dcd34123456&#x60;. You&#39;ll need to create a separate &#x60;relay_token&#x60; for each third party that needs access to the report on your behalf.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditRelayCreateRequest = new ThePlaidApi.CreditRelayCreateRequest(); // CreditRelayCreateRequest | 
apiInstance.creditRelayCreate(creditRelayCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditRelayCreateRequest** | [**CreditRelayCreateRequest**](CreditRelayCreateRequest.md)|  | 

### Return type

[**CreditRelayCreateResponse**](CreditRelayCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditRelayGet

> AssetReportGetResponse creditRelayGet(creditRelayGetRequest)

Retrieve the reports associated with a relay token that was shared with you (beta)

&#x60;/credit/relay/get&#x60; allows third parties to receive a report that was shared with them, using a &#x60;relay_token&#x60; that was created by the report owner.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditRelayGetRequest = new ThePlaidApi.CreditRelayGetRequest(); // CreditRelayGetRequest | 
apiInstance.creditRelayGet(creditRelayGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditRelayGetRequest** | [**CreditRelayGetRequest**](CreditRelayGetRequest.md)|  | 

### Return type

[**AssetReportGetResponse**](AssetReportGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditRelayRefresh

> CreditRelayRefreshResponse creditRelayRefresh(creditRelayRefreshRequest)

Refresh a report of a relay token (beta)

The &#x60;/credit/relay/refresh&#x60; endpoint allows third parties to refresh a report that was relayed to them, using a &#x60;relay_token&#x60; that was created by the report owner. A new report will be created with the original report parameters, but with the most recent data available based on the &#x60;days_requested&#x60; value of the original report.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditRelayRefreshRequest = new ThePlaidApi.CreditRelayRefreshRequest(); // CreditRelayRefreshRequest | 
apiInstance.creditRelayRefresh(creditRelayRefreshRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditRelayRefreshRequest** | [**CreditRelayRefreshRequest**](CreditRelayRefreshRequest.md)|  | 

### Return type

[**CreditRelayRefreshResponse**](CreditRelayRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditRelayRemove

> CreditRelayRemoveResponse creditRelayRemove(creditRelayRemoveRequest)

Remove relay token (beta)

The &#x60;/credit/relay/remove&#x60; endpoint allows you to invalidate a &#x60;relay_token&#x60;. The third party holding the token will no longer be able to access or refresh the reports which the &#x60;relay_token&#x60; gives access to. The original report, associated Items, and other relay tokens that provide access to the same report are not affected and will remain accessible after removing the given &#x60;relay_token&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditRelayRemoveRequest = new ThePlaidApi.CreditRelayRemoveRequest(); // CreditRelayRemoveRequest | 
apiInstance.creditRelayRemove(creditRelayRemoveRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditRelayRemoveRequest** | [**CreditRelayRemoveRequest**](CreditRelayRemoveRequest.md)|  | 

### Return type

[**CreditRelayRemoveResponse**](CreditRelayRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditReportAuditCopyRemove

> CreditAuditCopyTokenRemoveResponse creditReportAuditCopyRemove(creditAuditCopyTokenRemoveRequest)

Remove an Audit Copy token

The &#x60;/credit/audit_copy_token/remove&#x60; endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the &#x60;audit_copy_token&#x60; associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Report data and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditAuditCopyTokenRemoveRequest = new ThePlaidApi.CreditAuditCopyTokenRemoveRequest(); // CreditAuditCopyTokenRemoveRequest | 
apiInstance.creditReportAuditCopyRemove(creditAuditCopyTokenRemoveRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditAuditCopyTokenRemoveRequest** | [**CreditAuditCopyTokenRemoveRequest**](CreditAuditCopyTokenRemoveRequest.md)|  | 

### Return type

[**CreditAuditCopyTokenRemoveResponse**](CreditAuditCopyTokenRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## creditSessionsGet

> CreditSessionsGetResponse creditSessionsGet(creditSessionsGetRequest)

Retrieve Link sessions for your user

This endpoint can be used for your end users after they complete the Link flow. This endpoint returns a list of Link sessions that your user completed, where each session includes the results from the Link flow.  These results include details about the Item that was created and some product related metadata (showing, for example, whether the user finished the bank income verification step).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let creditSessionsGetRequest = new ThePlaidApi.CreditSessionsGetRequest(); // CreditSessionsGetRequest | 
apiInstance.creditSessionsGet(creditSessionsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creditSessionsGetRequest** | [**CreditSessionsGetRequest**](CreditSessionsGetRequest.md)|  | 

### Return type

[**CreditSessionsGetResponse**](CreditSessionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dashboardUserGet

> DashboardUserGetResponse dashboardUserGet(dashboardUserGetRequest)

Retrieve a dashboard user

Retrieve information about a dashboard user.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let dashboardUserGetRequest = new ThePlaidApi.DashboardUserGetRequest(); // DashboardUserGetRequest | 
apiInstance.dashboardUserGet(dashboardUserGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboardUserGetRequest** | [**DashboardUserGetRequest**](DashboardUserGetRequest.md)|  | 

### Return type

[**DashboardUserGetResponse**](DashboardUserGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dashboardUserList

> DashboardUserListResponse dashboardUserList(dashboardUserListRequest)

List dashboard users

List all dashboard users associated with your account.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let dashboardUserListRequest = new ThePlaidApi.DashboardUserListRequest(); // DashboardUserListRequest | 
apiInstance.dashboardUserList(dashboardUserListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboardUserListRequest** | [**DashboardUserListRequest**](DashboardUserListRequest.md)|  | 

### Return type

[**DashboardUserListResponse**](DashboardUserListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## depositSwitchAltCreate

> DepositSwitchAltCreateResponse depositSwitchAltCreate(depositSwitchAltCreateRequest)

Create a deposit switch without using Plaid Exchange

This endpoint provides an alternative to &#x60;/deposit_switch/create&#x60; for customers who have not yet fully integrated with Plaid Exchange. Like &#x60;/deposit_switch/create&#x60;, it creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let depositSwitchAltCreateRequest = new ThePlaidApi.DepositSwitchAltCreateRequest(); // DepositSwitchAltCreateRequest | 
apiInstance.depositSwitchAltCreate(depositSwitchAltCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depositSwitchAltCreateRequest** | [**DepositSwitchAltCreateRequest**](DepositSwitchAltCreateRequest.md)|  | 

### Return type

[**DepositSwitchAltCreateResponse**](DepositSwitchAltCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## depositSwitchCreate

> DepositSwitchCreateResponse depositSwitchCreate(depositSwitchCreateRequest)

Create a deposit switch

This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let depositSwitchCreateRequest = new ThePlaidApi.DepositSwitchCreateRequest(); // DepositSwitchCreateRequest | 
apiInstance.depositSwitchCreate(depositSwitchCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depositSwitchCreateRequest** | [**DepositSwitchCreateRequest**](DepositSwitchCreateRequest.md)|  | 

### Return type

[**DepositSwitchCreateResponse**](DepositSwitchCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## depositSwitchGet

> DepositSwitchGetResponse depositSwitchGet(depositSwitchGetRequest)

Retrieve a deposit switch

This endpoint returns information related to how the user has configured their payroll allocation and the state of the switch. You can use this information to build logic related to the user&#39;s direct deposit allocation preferences.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let depositSwitchGetRequest = new ThePlaidApi.DepositSwitchGetRequest(); // DepositSwitchGetRequest | 
apiInstance.depositSwitchGet(depositSwitchGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depositSwitchGetRequest** | [**DepositSwitchGetRequest**](DepositSwitchGetRequest.md)|  | 

### Return type

[**DepositSwitchGetResponse**](DepositSwitchGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## depositSwitchTokenCreate

> DepositSwitchTokenCreateResponse depositSwitchTokenCreate(depositSwitchTokenCreateRequest)

Create a deposit switch token

In order for the end user to take action, you will need to create a public token representing the deposit switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let depositSwitchTokenCreateRequest = new ThePlaidApi.DepositSwitchTokenCreateRequest(); // DepositSwitchTokenCreateRequest | 
apiInstance.depositSwitchTokenCreate(depositSwitchTokenCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **depositSwitchTokenCreateRequest** | [**DepositSwitchTokenCreateRequest**](DepositSwitchTokenCreateRequest.md)|  | 

### Return type

[**DepositSwitchTokenCreateResponse**](DepositSwitchTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## employersSearch

> EmployersSearchResponse employersSearch(employersSearchRequest)

Search employer database

&#x60;/employers/search&#x60; allows you the ability to search Plaid’s database of known employers, for use with Deposit Switch. You can use this endpoint to look up a user&#39;s employer in order to confirm that they are supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.  The data in the employer database is currently limited. As the Deposit Switch and Income products progress through their respective beta periods, more employers are being regularly added. Because the employer database is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let employersSearchRequest = new ThePlaidApi.EmployersSearchRequest(); // EmployersSearchRequest | 
apiInstance.employersSearch(employersSearchRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employersSearchRequest** | [**EmployersSearchRequest**](EmployersSearchRequest.md)|  | 

### Return type

[**EmployersSearchResponse**](EmployersSearchResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## employmentVerificationGet

> EmploymentVerificationGetResponse employmentVerificationGet(employmentVerificationGetRequest)

(Deprecated) Retrieve a summary of an individual&#39;s employment information

&#x60;/employment/verification/get&#x60; returns a list of employments through a user payroll that was verified by an end user.  This endpoint has been deprecated; new integrations should use &#x60;/credit/employment/get&#x60; instead.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let employmentVerificationGetRequest = new ThePlaidApi.EmploymentVerificationGetRequest(); // EmploymentVerificationGetRequest | 
apiInstance.employmentVerificationGet(employmentVerificationGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employmentVerificationGetRequest** | [**EmploymentVerificationGetRequest**](EmploymentVerificationGetRequest.md)|  | 

### Return type

[**EmploymentVerificationGetResponse**](EmploymentVerificationGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fdxNotifications

> fdxNotifications(fDXNotification)

Webhook receiver for fdx notifications

A generic webhook receiver endpoint for FDX Event Notifications

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let fDXNotification = new ThePlaidApi.FDXNotification(); // FDXNotification | 
apiInstance.fdxNotifications(fDXNotification, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fDXNotification** | [**FDXNotification**](FDXNotification.md)|  | 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identityGet

> IdentityGetResponse identityGet(identityGetRequest)

Retrieve identity data

The &#x60;/identity/get&#x60; endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.  This request may take some time to complete if identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.  Note: In API versions 2018-05-22 and earlier, the &#x60;owners&#x60; object is not returned, and instead identity information is returned in the top level &#x60;identity&#x60; object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let identityGetRequest = new ThePlaidApi.IdentityGetRequest(); // IdentityGetRequest | 
apiInstance.identityGet(identityGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identityGetRequest** | [**IdentityGetRequest**](IdentityGetRequest.md)|  | 

### Return type

[**IdentityGetResponse**](IdentityGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identityMatch

> IdentityMatchResponse identityMatch(identityMatchRequest)

Retrieve identity match score

The &#x60;/identity/match&#x60; endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder&#39;s financial institution.  This request may take some time to complete if Identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let identityMatchRequest = new ThePlaidApi.IdentityMatchRequest(); // IdentityMatchRequest | 
apiInstance.identityMatch(identityMatchRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identityMatchRequest** | [**IdentityMatchRequest**](IdentityMatchRequest.md)|  | 

### Return type

[**IdentityMatchResponse**](IdentityMatchResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identityVerificationCreate

> IdentityVerificationCreateResponse identityVerificationCreate(identityVerificationCreateRequest)

Create a new identity verification

Create a new Identity Verification for the user specified by the &#x60;client_user_id&#x60; field. The requirements and behavior of the verification are determined by the &#x60;template_id&#x60; provided. If you don&#39;t know whether the associated user already has an active Identity Verification, you can specify &#x60;\&quot;is_idempotent\&quot;: true&#x60; in the request body. With idempotency enabled, a new Identity Verification will only be created if one does not already exist for the associated &#x60;client_user_id&#x60; and &#x60;template_id&#x60;. If an Identity Verification is found, it will be returned unmodified with an &#x60;200 OK&#x60; HTTP status code. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let identityVerificationCreateRequest = new ThePlaidApi.IdentityVerificationCreateRequest(); // IdentityVerificationCreateRequest | 
apiInstance.identityVerificationCreate(identityVerificationCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identityVerificationCreateRequest** | [**IdentityVerificationCreateRequest**](IdentityVerificationCreateRequest.md)|  | 

### Return type

[**IdentityVerificationCreateResponse**](IdentityVerificationCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identityVerificationGet

> IdentityVerificationGetResponse identityVerificationGet(identityVerificationGetRequest)

Retrieve Identity Verification

Retrieve a previously created identity verification.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let identityVerificationGetRequest = new ThePlaidApi.IdentityVerificationGetRequest(); // IdentityVerificationGetRequest | 
apiInstance.identityVerificationGet(identityVerificationGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identityVerificationGetRequest** | [**IdentityVerificationGetRequest**](IdentityVerificationGetRequest.md)|  | 

### Return type

[**IdentityVerificationGetResponse**](IdentityVerificationGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identityVerificationList

> IdentityVerificationListResponse identityVerificationList(identityVerificationListRequest)

List Identity Verifications

Filter and list Identity Verifications created by your account

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let identityVerificationListRequest = new ThePlaidApi.IdentityVerificationListRequest(); // IdentityVerificationListRequest | 
apiInstance.identityVerificationList(identityVerificationListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identityVerificationListRequest** | [**IdentityVerificationListRequest**](IdentityVerificationListRequest.md)|  | 

### Return type

[**IdentityVerificationListResponse**](IdentityVerificationListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## identityVerificationRetry

> IdentityVerificationRetryResponse identityVerificationRetry(identityVerificationRetryRequest)

Retry an Identity Verification

Allow a customer to retry their identity verification

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let identityVerificationRetryRequest = new ThePlaidApi.IdentityVerificationRetryRequest(); // IdentityVerificationRetryRequest | 
apiInstance.identityVerificationRetry(identityVerificationRetryRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identityVerificationRetryRequest** | [**IdentityVerificationRetryRequest**](IdentityVerificationRetryRequest.md)|  | 

### Return type

[**IdentityVerificationRetryResponse**](IdentityVerificationRetryResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## incomeVerificationCreate

> IncomeVerificationCreateResponse incomeVerificationCreate(incomeVerificationCreateRequest)

(Deprecated) Create an income verification instance

&#x60;/income/verification/create&#x60; begins the income verification process by returning an &#x60;income_verification_id&#x60;. You can then provide the &#x60;income_verification_id&#x60; to &#x60;/link/token/create&#x60; under the &#x60;income_verification&#x60; parameter in order to create a Link instance that will prompt the user to go through the income verification flow. Plaid will fire an &#x60;INCOME&#x60; webhook once the user completes the Payroll Income flow, or when the uploaded documents in the Document Income flow have finished processing. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let incomeVerificationCreateRequest = new ThePlaidApi.IncomeVerificationCreateRequest(); // IncomeVerificationCreateRequest | 
apiInstance.incomeVerificationCreate(incomeVerificationCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incomeVerificationCreateRequest** | [**IncomeVerificationCreateRequest**](IncomeVerificationCreateRequest.md)|  | 

### Return type

[**IncomeVerificationCreateResponse**](IncomeVerificationCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## incomeVerificationDocumentsDownload

> File incomeVerificationDocumentsDownload(incomeVerificationDocumentsDownloadRequest)

(Deprecated) Download the original documents used for income verification

&#x60;/income/verification/documents/download&#x60; provides the ability to download the source documents associated with the verification.  If Document Income was used, the documents will be those the user provided in Link. For Payroll Income, the most recent files available for download from the payroll provider will be available from this endpoint.  The response to &#x60;/income/verification/documents/download&#x60; is a ZIP file in binary data. If a &#x60;document_id&#x60; is passed, a single document will be contained in this file. If not, the response will contain all documents associated with the verification.  The &#x60;request_id&#x60; is returned in the &#x60;Plaid-Request-ID&#x60; header.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let incomeVerificationDocumentsDownloadRequest = new ThePlaidApi.IncomeVerificationDocumentsDownloadRequest(); // IncomeVerificationDocumentsDownloadRequest | 
apiInstance.incomeVerificationDocumentsDownload(incomeVerificationDocumentsDownloadRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incomeVerificationDocumentsDownloadRequest** | [**IncomeVerificationDocumentsDownloadRequest**](IncomeVerificationDocumentsDownloadRequest.md)|  | 

### Return type

**File**

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/zip


## incomeVerificationPaystubsGet

> IncomeVerificationPaystubsGetResponse incomeVerificationPaystubsGet(incomeVerificationPaystubsGetRequest)

(Deprecated) Retrieve information from the paystubs used for income verification

&#x60;/income/verification/paystubs/get&#x60; returns the information collected from the paystubs that were used to verify an end user&#39;s income. It can be called once the status of the verification has been set to &#x60;VERIFICATION_STATUS_PROCESSING_COMPLETE&#x60;, as reported by the &#x60;INCOME: verification_status&#x60; webhook. Attempting to call the endpoint before verification has been completed will result in an error.  This endpoint has been deprecated; new integrations should use &#x60;/credit/payroll_income/get&#x60; instead.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let incomeVerificationPaystubsGetRequest = new ThePlaidApi.IncomeVerificationPaystubsGetRequest(); // IncomeVerificationPaystubsGetRequest | 
apiInstance.incomeVerificationPaystubsGet(incomeVerificationPaystubsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incomeVerificationPaystubsGetRequest** | [**IncomeVerificationPaystubsGetRequest**](IncomeVerificationPaystubsGetRequest.md)|  | 

### Return type

[**IncomeVerificationPaystubsGetResponse**](IncomeVerificationPaystubsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## incomeVerificationPrecheck

> IncomeVerificationPrecheckResponse incomeVerificationPrecheck(incomeVerificationPrecheckRequest)

(Deprecated) Check digital income verification eligibility and optimize conversion

&#x60;/income/verification/precheck&#x60; is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification and returns a &#x60;precheck_id&#x60; that can be provided to &#x60;/link/token/create&#x60;. If the user is eligible for digital verification, providing the &#x60;precheck_id&#x60; in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the &#x60;precheck_id&#x60; can still be provided to &#x60;/link/token/create&#x60; and the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.  While all request fields are optional, providing either &#x60;employer&#x60; or &#x60;transactions_access_tokens&#x60; data will increase the chance of receiving a useful result.  This endpoint has been deprecated; new integrations should use &#x60;/credit/payroll_income/precheck&#x60; instead.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let incomeVerificationPrecheckRequest = new ThePlaidApi.IncomeVerificationPrecheckRequest(); // IncomeVerificationPrecheckRequest | 
apiInstance.incomeVerificationPrecheck(incomeVerificationPrecheckRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incomeVerificationPrecheckRequest** | [**IncomeVerificationPrecheckRequest**](IncomeVerificationPrecheckRequest.md)|  | 

### Return type

[**IncomeVerificationPrecheckResponse**](IncomeVerificationPrecheckResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## incomeVerificationTaxformsGet

> IncomeVerificationTaxformsGetResponse incomeVerificationTaxformsGet(incomeVerificationTaxformsGetRequest)

(Deprecated) Retrieve information from the tax documents used for income verification

&#x60;/income/verification/taxforms/get&#x60; returns the information collected from forms that were used to verify an end user&#39;&#39;s income. It can be called once the status of the verification has been set to &#x60;VERIFICATION_STATUS_PROCESSING_COMPLETE&#x60;, as reported by the &#x60;INCOME: verification_status&#x60; webhook. Attempting to call the endpoint before verification has been completed will result in an error.  This endpoint has been deprecated; new integrations should use &#x60;/credit/payroll_income/get&#x60; instead.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let incomeVerificationTaxformsGetRequest = new ThePlaidApi.IncomeVerificationTaxformsGetRequest(); // IncomeVerificationTaxformsGetRequest | 
apiInstance.incomeVerificationTaxformsGet(incomeVerificationTaxformsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incomeVerificationTaxformsGetRequest** | [**IncomeVerificationTaxformsGetRequest**](IncomeVerificationTaxformsGetRequest.md)|  | 

### Return type

[**IncomeVerificationTaxformsGetResponse**](IncomeVerificationTaxformsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## institutionsGet

> InstitutionsGetResponse institutionsGet(institutionsGetRequest)

Get details of all supported institutions

Returns a JSON response containing details on all financial institutions currently supported by Plaid. Because Plaid supports thousands of institutions, results are paginated.  If there is no overlap between an institution’s enabled products and a client’s enabled products, then the institution will be filtered out from the response. As a result, the number of institutions returned may not match the count specified in the call.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let institutionsGetRequest = new ThePlaidApi.InstitutionsGetRequest(); // InstitutionsGetRequest | 
apiInstance.institutionsGet(institutionsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institutionsGetRequest** | [**InstitutionsGetRequest**](InstitutionsGetRequest.md)|  | 

### Return type

[**InstitutionsGetResponse**](InstitutionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## institutionsGetById

> InstitutionsGetByIdResponse institutionsGetById(institutionsGetByIdRequest)

Get details of an institution

Returns a JSON response containing details on a specified financial institution currently supported by Plaid.  Versioning note: API versions 2019-05-29 and earlier allow use of the &#x60;public_key&#x60; parameter instead of the &#x60;client_id&#x60; and &#x60;secret&#x60; to authenticate to this endpoint. The &#x60;public_key&#x60; has been deprecated; all customers are encouraged to use &#x60;client_id&#x60; and &#x60;secret&#x60; instead. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let institutionsGetByIdRequest = new ThePlaidApi.InstitutionsGetByIdRequest(); // InstitutionsGetByIdRequest | 
apiInstance.institutionsGetById(institutionsGetByIdRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institutionsGetByIdRequest** | [**InstitutionsGetByIdRequest**](InstitutionsGetByIdRequest.md)|  | 

### Return type

[**InstitutionsGetByIdResponse**](InstitutionsGetByIdResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## institutionsSearch

> InstitutionsSearchResponse institutionsSearch(institutionsSearchRequest)

Search institutions

Returns a JSON response containing details for institutions that match the query parameters, up to a maximum of ten institutions per query.  Versioning note: API versions 2019-05-29 and earlier allow use of the &#x60;public_key&#x60; parameter instead of the &#x60;client_id&#x60; and &#x60;secret&#x60; parameters to authenticate to this endpoint. The &#x60;public_key&#x60; parameter has since been deprecated; all customers are encouraged to use &#x60;client_id&#x60; and &#x60;secret&#x60; instead. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let institutionsSearchRequest = new ThePlaidApi.InstitutionsSearchRequest(); // InstitutionsSearchRequest | 
apiInstance.institutionsSearch(institutionsSearchRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institutionsSearchRequest** | [**InstitutionsSearchRequest**](InstitutionsSearchRequest.md)|  | 

### Return type

[**InstitutionsSearchResponse**](InstitutionsSearchResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## investmentsHoldingsGet

> InvestmentsHoldingsGetResponse investmentsHoldingsGet(investmentsHoldingsGetRequest)

Get Investment holdings

The &#x60;/investments/holdings/get&#x60; endpoint allows developers to receive user-authorized stock position data for &#x60;investment&#x60;-type accounts.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let investmentsHoldingsGetRequest = new ThePlaidApi.InvestmentsHoldingsGetRequest(); // InvestmentsHoldingsGetRequest | 
apiInstance.investmentsHoldingsGet(investmentsHoldingsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investmentsHoldingsGetRequest** | [**InvestmentsHoldingsGetRequest**](InvestmentsHoldingsGetRequest.md)|  | 

### Return type

[**InvestmentsHoldingsGetResponse**](InvestmentsHoldingsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## investmentsTransactionsGet

> InvestmentsTransactionsGetResponse investmentsTransactionsGet(investmentsTransactionsGetRequest)

Get investment transactions

The &#x60;/investments/transactions/get&#x60; endpoint allows developers to retrieve up to 24 months of user-authorized transaction data for investment accounts.  Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Due to the potentially large number of investment transactions associated with an Item, results are paginated. Manipulate the count and offset parameters in conjunction with the &#x60;total_investment_transactions&#x60; response body field to fetch all available investment transactions.  Note that Investments does not have a webhook to indicate when initial transaction data has loaded. Instead, if transactions data is not ready when &#x60;/investments/transactions/get&#x60; is first called, Plaid will wait for the data. For this reason, calling &#x60;/investments/transactions/get&#x60; immediately after Link may take up to one to two minutes to return.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let investmentsTransactionsGetRequest = new ThePlaidApi.InvestmentsTransactionsGetRequest(); // InvestmentsTransactionsGetRequest | 
apiInstance.investmentsTransactionsGet(investmentsTransactionsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investmentsTransactionsGetRequest** | [**InvestmentsTransactionsGetRequest**](InvestmentsTransactionsGetRequest.md)|  | 

### Return type

[**InvestmentsTransactionsGetResponse**](InvestmentsTransactionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemAccessTokenInvalidate

> ItemAccessTokenInvalidateResponse itemAccessTokenInvalidate(itemAccessTokenInvalidateRequest)

Invalidate access_token

By default, the &#x60;access_token&#x60; associated with an Item does not expire and should be stored in a persistent, secure manner.  You can use the &#x60;/item/access_token/invalidate&#x60; endpoint to rotate the &#x60;access_token&#x60; associated with an Item. The endpoint returns a new &#x60;access_token&#x60; and immediately invalidates the previous &#x60;access_token&#x60;. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let itemAccessTokenInvalidateRequest = new ThePlaidApi.ItemAccessTokenInvalidateRequest(); // ItemAccessTokenInvalidateRequest | 
apiInstance.itemAccessTokenInvalidate(itemAccessTokenInvalidateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemAccessTokenInvalidateRequest** | [**ItemAccessTokenInvalidateRequest**](ItemAccessTokenInvalidateRequest.md)|  | 

### Return type

[**ItemAccessTokenInvalidateResponse**](ItemAccessTokenInvalidateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemActivityList

> ItemActivityListResponse itemActivityList(itemActivityListRequest)

List a historical log of user consent events

List a historical log of user consent events

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let itemActivityListRequest = new ThePlaidApi.ItemActivityListRequest(); // ItemActivityListRequest | 
apiInstance.itemActivityList(itemActivityListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemActivityListRequest** | [**ItemActivityListRequest**](ItemActivityListRequest.md)|  | 

### Return type

[**ItemActivityListResponse**](ItemActivityListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemApplicationList

> ItemApplicationListResponse itemApplicationList(itemApplicationListRequest)

List a user’s connected applications

List a user’s connected applications

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let itemApplicationListRequest = new ThePlaidApi.ItemApplicationListRequest(); // ItemApplicationListRequest | 
apiInstance.itemApplicationList(itemApplicationListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemApplicationListRequest** | [**ItemApplicationListRequest**](ItemApplicationListRequest.md)|  | 

### Return type

[**ItemApplicationListResponse**](ItemApplicationListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemApplicationScopesUpdate

> ItemApplicationScopesUpdateResponse itemApplicationScopesUpdate(itemApplicationScopesUpdateRequest)

Update the scopes of access for a particular application

Enable consumers to update product access on selected accounts for an application.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let itemApplicationScopesUpdateRequest = new ThePlaidApi.ItemApplicationScopesUpdateRequest(); // ItemApplicationScopesUpdateRequest | 
apiInstance.itemApplicationScopesUpdate(itemApplicationScopesUpdateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemApplicationScopesUpdateRequest** | [**ItemApplicationScopesUpdateRequest**](ItemApplicationScopesUpdateRequest.md)|  | 

### Return type

[**ItemApplicationScopesUpdateResponse**](ItemApplicationScopesUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemCreatePublicToken

> ItemPublicTokenCreateResponse itemCreatePublicToken(itemPublicTokenCreateRequest)

Create public token

Note: As of July 2020, the &#x60;/item/public_token/create&#x60; endpoint is deprecated. Instead, use &#x60;/link/token/create&#x60; with an &#x60;access_token&#x60; to create a Link token for use with [update mode](https://plaid.com/docs/link/update-mode).  If you need your user to take action to restore or resolve an error associated with an Item, generate a public token with the &#x60;/item/public_token/create&#x60; endpoint and then initialize Link with that &#x60;public_token&#x60;.  A &#x60;public_token&#x60; is one-time use and expires after 30 minutes. You use a &#x60;public_token&#x60; to initialize Link in [update mode](https://plaid.com/docs/link/update-mode) for a particular Item. You can generate a &#x60;public_token&#x60; for an Item even if you did not use Link to create the Item originally.  The &#x60;/item/public_token/create&#x60; endpoint is **not** used to create your initial &#x60;public_token&#x60;. If you have not already received an &#x60;access_token&#x60; for a specific Item, use Link to obtain your &#x60;public_token&#x60; instead. See the [Quickstart](https://plaid.com/docs/quickstart) for more information.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let itemPublicTokenCreateRequest = new ThePlaidApi.ItemPublicTokenCreateRequest(); // ItemPublicTokenCreateRequest | 
apiInstance.itemCreatePublicToken(itemPublicTokenCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemPublicTokenCreateRequest** | [**ItemPublicTokenCreateRequest**](ItemPublicTokenCreateRequest.md)|  | 

### Return type

[**ItemPublicTokenCreateResponse**](ItemPublicTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemGet

> ItemGetResponse itemGet(itemGetRequest)

Retrieve an Item

Returns information about the status of an Item.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let itemGetRequest = new ThePlaidApi.ItemGetRequest(); // ItemGetRequest | 
apiInstance.itemGet(itemGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemGetRequest** | [**ItemGetRequest**](ItemGetRequest.md)|  | 

### Return type

[**ItemGetResponse**](ItemGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemImport

> ItemImportResponse itemImport(itemImportRequest)

Import Item

&#x60;/item/import&#x60; creates an Item via your Plaid Exchange Integration and returns an &#x60;access_token&#x60;. As part of an &#x60;/item/import&#x60; request, you will include a User ID (&#x60;user_auth.user_id&#x60;) and Authentication Token (&#x60;user_auth.auth_token&#x60;) that enable data aggregation through your Plaid Exchange API endpoints. These authentication principals are to be chosen by you.  Upon creating an Item via &#x60;/item/import&#x60;, Plaid will automatically begin an extraction of that Item through the Plaid Exchange infrastructure you have already integrated. This will automatically generate the Plaid native account ID for the account the user will switch their direct deposit to (&#x60;target_account_id&#x60;).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let itemImportRequest = new ThePlaidApi.ItemImportRequest(); // ItemImportRequest | 
apiInstance.itemImport(itemImportRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemImportRequest** | [**ItemImportRequest**](ItemImportRequest.md)|  | 

### Return type

[**ItemImportResponse**](ItemImportResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemPublicTokenExchange

> ItemPublicTokenExchangeResponse itemPublicTokenExchange(itemPublicTokenExchangeRequest)

Exchange public token for an access token

Exchange a Link &#x60;public_token&#x60; for an API &#x60;access_token&#x60;. Link hands off the &#x60;public_token&#x60; client-side via the &#x60;onSuccess&#x60; callback once a user has successfully created an Item. The &#x60;public_token&#x60; is ephemeral and expires after 30 minutes. An &#x60;access_token&#x60; does not expire, but can be revoked by calling &#x60;/item/remove&#x60;.  The response also includes an &#x60;item_id&#x60; that should be stored with the &#x60;access_token&#x60;. The &#x60;item_id&#x60; is used to identify an Item in a webhook. The &#x60;item_id&#x60; can also be retrieved by making an &#x60;/item/get&#x60; request.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let itemPublicTokenExchangeRequest = new ThePlaidApi.ItemPublicTokenExchangeRequest(); // ItemPublicTokenExchangeRequest | 
apiInstance.itemPublicTokenExchange(itemPublicTokenExchangeRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemPublicTokenExchangeRequest** | [**ItemPublicTokenExchangeRequest**](ItemPublicTokenExchangeRequest.md)|  | 

### Return type

[**ItemPublicTokenExchangeResponse**](ItemPublicTokenExchangeResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemRemove

> ItemRemoveResponse itemRemove(itemRemoveRequest)

Remove an Item

The &#x60;/item/remove&#x60; endpoint allows you to remove an Item. Once removed, the &#x60;access_token&#x60;, as well as any processor tokens or bank account tokens associated with the Item, is no longer valid and cannot be used to access any data that was associated with the Item.  Note that in the Development environment, issuing an &#x60;/item/remove&#x60;  request will not decrement your live credential count. To increase your credential account in Development, contact Support.  Also note that for certain OAuth-based institutions, an Item removed via &#x60;/item/remove&#x60; may still show as an active connection in the institution&#39;s OAuth permission manager.  API versions 2019-05-29 and earlier return a &#x60;removed&#x60; boolean as part of the response.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let itemRemoveRequest = new ThePlaidApi.ItemRemoveRequest(); // ItemRemoveRequest | 
apiInstance.itemRemove(itemRemoveRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemRemoveRequest** | [**ItemRemoveRequest**](ItemRemoveRequest.md)|  | 

### Return type

[**ItemRemoveResponse**](ItemRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## itemWebhookUpdate

> ItemWebhookUpdateResponse itemWebhookUpdate(itemWebhookUpdateRequest)

Update Webhook URL

The POST &#x60;/item/webhook/update&#x60; allows you to update the webhook URL associated with an Item. This request triggers a [&#x60;WEBHOOK_UPDATE_ACKNOWLEDGED&#x60;](https://plaid.com/docs/api/items/#webhook_update_acknowledged) webhook to the newly specified webhook URL.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let itemWebhookUpdateRequest = new ThePlaidApi.ItemWebhookUpdateRequest(); // ItemWebhookUpdateRequest | 
apiInstance.itemWebhookUpdate(itemWebhookUpdateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemWebhookUpdateRequest** | [**ItemWebhookUpdateRequest**](ItemWebhookUpdateRequest.md)|  | 

### Return type

[**ItemWebhookUpdateResponse**](ItemWebhookUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## liabilitiesGet

> LiabilitiesGetResponse liabilitiesGet(liabilitiesGetRequest)

Retrieve Liabilities data

The &#x60;/liabilities/get&#x60; endpoint returns various details about an Item with loan or credit accounts. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type &#x60;credit&#x60; with account subtype &#x60;credit card&#x60; or &#x60;paypal&#x60;, and account type &#x60;loan&#x60; with account subtype &#x60;student&#x60; or &#x60;mortgage&#x60;. To limit accounts listed in Link to types and subtypes supported by Liabilities, you can use the &#x60;account_filters&#x60; parameter when [creating a Link token](https://plaid.com/docs/api/tokens/#linktokencreate).  The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling &#x60;/liabilities/get&#x60;.  Note: This request may take some time to complete if &#x60;liabilities&#x60; was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the additional data.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let liabilitiesGetRequest = new ThePlaidApi.LiabilitiesGetRequest(); // LiabilitiesGetRequest | 
apiInstance.liabilitiesGet(liabilitiesGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **liabilitiesGetRequest** | [**LiabilitiesGetRequest**](LiabilitiesGetRequest.md)|  | 

### Return type

[**LiabilitiesGetResponse**](LiabilitiesGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## linkDeliveryCreate

> LinkDeliveryCreateResponse linkDeliveryCreate(linkDeliveryCreateRequest)

Create Link Delivery session

Use the &#x60;/link_delivery/create&#x60; endpoint to create a Link Delivery session.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let linkDeliveryCreateRequest = new ThePlaidApi.LinkDeliveryCreateRequest(); // LinkDeliveryCreateRequest | 
apiInstance.linkDeliveryCreate(linkDeliveryCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkDeliveryCreateRequest** | [**LinkDeliveryCreateRequest**](LinkDeliveryCreateRequest.md)|  | 

### Return type

[**LinkDeliveryCreateResponse**](LinkDeliveryCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## linkDeliveryGet

> LinkDeliveryGetResponse linkDeliveryGet(linkDeliveryGetRequest)

Get Link Delivery session

Use the &#x60;/link_delivery/get&#x60; endpoint to get the status of a Link Delivery session.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let linkDeliveryGetRequest = new ThePlaidApi.LinkDeliveryGetRequest(); // LinkDeliveryGetRequest | 
apiInstance.linkDeliveryGet(linkDeliveryGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkDeliveryGetRequest** | [**LinkDeliveryGetRequest**](LinkDeliveryGetRequest.md)|  | 

### Return type

[**LinkDeliveryGetResponse**](LinkDeliveryGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## linkOauthCorrelationIdExchange

> LinkOAuthCorrelationIdExchangeResponse linkOauthCorrelationIdExchange(linkOAuthCorrelationIdExchangeRequest)

Exchange the Link Correlation Id for a Link Token

Exchange an OAuth &#x60;link_correlation_id&#x60; for the corresponding &#x60;link_token&#x60;. The &#x60;link_correlation_id&#x60; is only available for &#39;payment_initiation&#39; products and is provided to the client via the OAuth &#x60;redirect_uri&#x60; as a query parameter. The &#x60;link_correlation_id&#x60; is ephemeral and expires in a brief period, after which it can no longer be exchanged for the &#39;link_token&#39;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let linkOAuthCorrelationIdExchangeRequest = new ThePlaidApi.LinkOAuthCorrelationIdExchangeRequest(); // LinkOAuthCorrelationIdExchangeRequest | 
apiInstance.linkOauthCorrelationIdExchange(linkOAuthCorrelationIdExchangeRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkOAuthCorrelationIdExchangeRequest** | [**LinkOAuthCorrelationIdExchangeRequest**](LinkOAuthCorrelationIdExchangeRequest.md)|  | 

### Return type

[**LinkOAuthCorrelationIdExchangeResponse**](LinkOAuthCorrelationIdExchangeResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## linkTokenCreate

> LinkTokenCreateResponse linkTokenCreate(linkTokenCreateRequest)

Create Link Token

The &#x60;/link/token/create&#x60; endpoint creates a &#x60;link_token&#x60;, which is required as a parameter when initializing Link. Once Link has been initialized, it returns a &#x60;public_token&#x60;, which can then be exchanged for an &#x60;access_token&#x60; via &#x60;/item/public_token/exchange&#x60; as part of the main Link flow.  A &#x60;link_token&#x60; generated by &#x60;/link/token/create&#x60; is also used to initialize other Link flows, such as the update mode flow for tokens with expired credentials, or the Payment Initiation (Europe) flow.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let linkTokenCreateRequest = new ThePlaidApi.LinkTokenCreateRequest(); // LinkTokenCreateRequest | 
apiInstance.linkTokenCreate(linkTokenCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkTokenCreateRequest** | [**LinkTokenCreateRequest**](LinkTokenCreateRequest.md)|  | 

### Return type

[**LinkTokenCreateResponse**](LinkTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## linkTokenGet

> LinkTokenGetResponse linkTokenGet(linkTokenGetRequest)

Get Link Token

The &#x60;/link/token/get&#x60; endpoint gets information about a previously-created &#x60;link_token&#x60; using the &#x60;/link/token/create&#x60; endpoint. It can be useful for debugging purposes.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let linkTokenGetRequest = new ThePlaidApi.LinkTokenGetRequest(); // LinkTokenGetRequest | 
apiInstance.linkTokenGet(linkTokenGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkTokenGetRequest** | [**LinkTokenGetRequest**](LinkTokenGetRequest.md)|  | 

### Return type

[**LinkTokenGetResponse**](LinkTokenGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## partnerCustomerCreate

> PartnerCustomerCreateResponse partnerCustomerCreate(partnerCustomerCreateRequest)

Creates a new end customer for a Plaid reseller.

The &#x60;/partner/customer/create&#x60; endpoint is used by reseller partners to create end customers.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let partnerCustomerCreateRequest = {"address":{"city":"New York","country_code":"US","postal_code":"12345","region":"NY","street":"123 Main St"},"application_name":"Plaid","billing_contact":{"email":"bob.jones@example.com","family_name":"Jones","given_name":"Bob"},"client_id":"7f57eb3d2a9j6480121fx361","company_name":"Plaid","create_link_customization":true,"customer_support_info":{"contact_url":"example.com/contact","email":"support@example.com","link_update_url":"example.com/update","phone_number":"1234567890"},"is_bank_addendum_completed":true,"is_diligence_attested":true,"legal_entity_name":"Plaid","products":["auth","identity"],"redirect_uris":["http://localhost/oauth.html","https://www.example.com/oauth.html","https://*.example.com/oauth.html"],"secret":"79g03eoofwl8240v776r2h667442119","technical_contact":{"email":"alice.smith@example.com","family_name":"Smith","given_name":"Alice"},"website":"plaid.com"}; // PartnerCustomerCreateRequest | 
apiInstance.partnerCustomerCreate(partnerCustomerCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partnerCustomerCreateRequest** | [**PartnerCustomerCreateRequest**](PartnerCustomerCreateRequest.md)|  | 

### Return type

[**PartnerCustomerCreateResponse**](PartnerCustomerCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## partnerCustomerEnable

> PartnerCustomerEnableResponse partnerCustomerEnable(partnerCustomerEnableRequest)

Enables a Plaid reseller&#39;s end customer in the Production environment.

The &#x60;/partner/customer/enable&#x60; endpoint is used by reseller partners to enable an end customer in the Production environment.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let partnerCustomerEnableRequest = {"client_id":"7f57eb3d2a9j6480121fx361","end_customer_client_id":"7f57eb3d2a9j6480121fx361","secret":"79g03eoofwl8240v776r2h667442119"}; // PartnerCustomerEnableRequest | 
apiInstance.partnerCustomerEnable(partnerCustomerEnableRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partnerCustomerEnableRequest** | [**PartnerCustomerEnableRequest**](PartnerCustomerEnableRequest.md)|  | 

### Return type

[**PartnerCustomerEnableResponse**](PartnerCustomerEnableResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## partnerCustomerGet

> PartnerCustomerGetResponse partnerCustomerGet(partnerCustomerGetRequest)

Returns a Plaid reseller&#39;s end customer.

The &#x60;/partner/customer/get&#x60; endpoint is used by reseller partners to retrieve data about a single end customer.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let partnerCustomerGetRequest = {"client_id":"7f57eb3d2a9j6480121fx361","end_customer_client_id":"7f57eb3d2a9j6480121fx361","secret":"79g03eoofwl8240v776r2h667442119"}; // PartnerCustomerGetRequest | 
apiInstance.partnerCustomerGet(partnerCustomerGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partnerCustomerGetRequest** | [**PartnerCustomerGetRequest**](PartnerCustomerGetRequest.md)|  | 

### Return type

[**PartnerCustomerGetResponse**](PartnerCustomerGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## partnerCustomerOauthInstitutionsGet

> PartnerCustomerOAuthInstitutionsGetResponse partnerCustomerOauthInstitutionsGet(partnerCustomerOAuthInstitutionsGetRequest)

Returns OAuth-institution registration information for a given end customer.

The &#x60;/partner/customer/oauth_institutions/get&#x60; endpoint is used by reseller partners to retrieve OAuth-institution registration information about a single end customer. To learn how to set up a webhook to listen to status update events, visit the [reseller documentation](https://plaid.com/docs/account/resellers/#enabling-end-customers).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let partnerCustomerOAuthInstitutionsGetRequest = {"client_id":"7f57eb3d2a9j6480121fx361","end_customer_client_id":"7f57eb3d2a9j6480121fx361","secret":"79g03eoofwl8240v776r2h667442119"}; // PartnerCustomerOAuthInstitutionsGetRequest | 
apiInstance.partnerCustomerOauthInstitutionsGet(partnerCustomerOAuthInstitutionsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partnerCustomerOAuthInstitutionsGetRequest** | [**PartnerCustomerOAuthInstitutionsGetRequest**](PartnerCustomerOAuthInstitutionsGetRequest.md)|  | 

### Return type

[**PartnerCustomerOAuthInstitutionsGetResponse**](PartnerCustomerOAuthInstitutionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## partnerCustomerRemove

> PartnerCustomerRemoveResponse partnerCustomerRemove(partnerCustomerRemoveRequest)

Removes a Plaid reseller&#39;s end customer.

The &#x60;/partner/customer/remove&#x60; endpoint is used by reseller partners to remove an end customer. Removing an end customer will remove it from view in the Plaid Dashboard and deactivate its API keys. This endpoint can only be used to remove an end customer that has not yet been enabled in Production.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let partnerCustomerRemoveRequest = {"client_id":"7f57eb3d2a9j6480121fx361","end_customer_client_id":"7f57eb3d2a9j6480121fx361","secret":"79g03eoofwl8240v776r2h667442119"}; // PartnerCustomerRemoveRequest | 
apiInstance.partnerCustomerRemove(partnerCustomerRemoveRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partnerCustomerRemoveRequest** | [**PartnerCustomerRemoveRequest**](PartnerCustomerRemoveRequest.md)|  | 

### Return type

[**PartnerCustomerRemoveResponse**](PartnerCustomerRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationConsentCreate

> PaymentInitiationConsentCreateResponse paymentInitiationConsentCreate(paymentInitiationConsentCreateRequest)

Create payment consent

The &#x60;/payment_initiation/consent/create&#x60; endpoint is used to create a payment consent, which can be used to initiate payments on behalf of the user. Payment consents are created with &#x60;UNAUTHORISED&#x60; status by default and must be authorised by the user before payments can be initiated.  Consents can be limited in time and scope, and have constraints that describe limitations for payments.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationConsentCreateRequest = new ThePlaidApi.PaymentInitiationConsentCreateRequest(); // PaymentInitiationConsentCreateRequest | 
apiInstance.paymentInitiationConsentCreate(paymentInitiationConsentCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationConsentCreateRequest** | [**PaymentInitiationConsentCreateRequest**](PaymentInitiationConsentCreateRequest.md)|  | 

### Return type

[**PaymentInitiationConsentCreateResponse**](PaymentInitiationConsentCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationConsentGet

> PaymentInitiationConsentGetResponse paymentInitiationConsentGet(paymentInitiationConsentGetRequest)

Get payment consent

The &#x60;/payment_initiation/consent/get&#x60; endpoint can be used to check the status of a payment consent, as well as to receive basic information such as recipient and constraints.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationConsentGetRequest = new ThePlaidApi.PaymentInitiationConsentGetRequest(); // PaymentInitiationConsentGetRequest | 
apiInstance.paymentInitiationConsentGet(paymentInitiationConsentGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationConsentGetRequest** | [**PaymentInitiationConsentGetRequest**](PaymentInitiationConsentGetRequest.md)|  | 

### Return type

[**PaymentInitiationConsentGetResponse**](PaymentInitiationConsentGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationConsentPaymentExecute

> PaymentInitiationConsentPaymentExecuteResponse paymentInitiationConsentPaymentExecute(paymentInitiationConsentPaymentExecuteRequest)

Execute a single payment using consent

The &#x60;/payment_initiation/consent/payment/execute&#x60; endpoint can be used to execute payments using payment consent.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationConsentPaymentExecuteRequest = new ThePlaidApi.PaymentInitiationConsentPaymentExecuteRequest(); // PaymentInitiationConsentPaymentExecuteRequest | 
apiInstance.paymentInitiationConsentPaymentExecute(paymentInitiationConsentPaymentExecuteRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationConsentPaymentExecuteRequest** | [**PaymentInitiationConsentPaymentExecuteRequest**](PaymentInitiationConsentPaymentExecuteRequest.md)|  | 

### Return type

[**PaymentInitiationConsentPaymentExecuteResponse**](PaymentInitiationConsentPaymentExecuteResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationConsentRevoke

> PaymentInitiationConsentRevokeResponse paymentInitiationConsentRevoke(paymentInitiationConsentRevokeRequest)

Revoke payment consent

The &#x60;/payment_initiation/consent/revoke&#x60; endpoint can be used to revoke the payment consent. Once the consent is revoked, it is not possible to initiate payments using it.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationConsentRevokeRequest = new ThePlaidApi.PaymentInitiationConsentRevokeRequest(); // PaymentInitiationConsentRevokeRequest | 
apiInstance.paymentInitiationConsentRevoke(paymentInitiationConsentRevokeRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationConsentRevokeRequest** | [**PaymentInitiationConsentRevokeRequest**](PaymentInitiationConsentRevokeRequest.md)|  | 

### Return type

[**PaymentInitiationConsentRevokeResponse**](PaymentInitiationConsentRevokeResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationPaymentCreate

> PaymentInitiationPaymentCreateResponse paymentInitiationPaymentCreate(paymentInitiationPaymentCreateRequest)

Create a payment

After creating a payment recipient, you can use the &#x60;/payment_initiation/payment/create&#x60; endpoint to create a payment to that recipient.  Payments can be one-time or standing order (recurring) and can be denominated in either EUR, GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency).  If making domestic GBP-denominated payments, your recipient must have been created with BACS numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer, GBP-denominated payments will be sent via the Faster Payments network and for non-Eurozone markets typically via the local payment scheme, but the payment network used will be determined by the institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA Credit Transfer or other local payment schemes will typically arrive in one business day.  Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK. Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or modify a standing order directly on their banking application or website, or by contacting the bank. Standing orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach the recipient’s account, although at least 90% of standing order payments are sent by 6am.  In the Development environment, payments must be below 5 GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency). For details on any payment limits in Production, contact your Plaid Account Manager.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationPaymentCreateRequest = new ThePlaidApi.PaymentInitiationPaymentCreateRequest(); // PaymentInitiationPaymentCreateRequest | 
apiInstance.paymentInitiationPaymentCreate(paymentInitiationPaymentCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationPaymentCreateRequest** | [**PaymentInitiationPaymentCreateRequest**](PaymentInitiationPaymentCreateRequest.md)|  | 

### Return type

[**PaymentInitiationPaymentCreateResponse**](PaymentInitiationPaymentCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationPaymentGet

> PaymentInitiationPaymentGetResponse paymentInitiationPaymentGet(paymentInitiationPaymentGetRequest)

Get payment details

The &#x60;/payment_initiation/payment/get&#x60; endpoint can be used to check the status of a payment, as well as to receive basic information such as recipient and payment amount. In the case of standing orders, the &#x60;/payment_initiation/payment/get&#x60; endpoint will provide information about the status of the overall standing order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationPaymentGetRequest = new ThePlaidApi.PaymentInitiationPaymentGetRequest(); // PaymentInitiationPaymentGetRequest | 
apiInstance.paymentInitiationPaymentGet(paymentInitiationPaymentGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationPaymentGetRequest** | [**PaymentInitiationPaymentGetRequest**](PaymentInitiationPaymentGetRequest.md)|  | 

### Return type

[**PaymentInitiationPaymentGetResponse**](PaymentInitiationPaymentGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationPaymentList

> PaymentInitiationPaymentListResponse paymentInitiationPaymentList(paymentInitiationPaymentListRequest)

List payments

The &#x60;/payment_initiation/payment/list&#x60; endpoint can be used to retrieve all created payments. By default, the 10 most recent payments are returned. You can request more payments and paginate through the results using the optional &#x60;count&#x60; and &#x60;cursor&#x60; parameters.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationPaymentListRequest = new ThePlaidApi.PaymentInitiationPaymentListRequest(); // PaymentInitiationPaymentListRequest | 
apiInstance.paymentInitiationPaymentList(paymentInitiationPaymentListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationPaymentListRequest** | [**PaymentInitiationPaymentListRequest**](PaymentInitiationPaymentListRequest.md)|  | 

### Return type

[**PaymentInitiationPaymentListResponse**](PaymentInitiationPaymentListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationPaymentReverse

> PaymentInitiationPaymentReverseResponse paymentInitiationPaymentReverse(paymentInitiationPaymentReverseRequest)

Reverse an existing payment

Reverse a settled payment from a Plaid virtual account.  The original payment must be in a settled state to be refunded. To refund partially, specify the amount as part of the request. If the amount is not specified, the refund amount will be equal to all of the remaining payment amount that has not been refunded yet.  The refund will go back to the source account that initiated the payment. The original payment must have been initiated to a Plaid virtual account so that this account can be used to initiate the refund. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationPaymentReverseRequest = new ThePlaidApi.PaymentInitiationPaymentReverseRequest(); // PaymentInitiationPaymentReverseRequest | 
apiInstance.paymentInitiationPaymentReverse(paymentInitiationPaymentReverseRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationPaymentReverseRequest** | [**PaymentInitiationPaymentReverseRequest**](PaymentInitiationPaymentReverseRequest.md)|  | 

### Return type

[**PaymentInitiationPaymentReverseResponse**](PaymentInitiationPaymentReverseResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationRecipientCreate

> PaymentInitiationRecipientCreateResponse paymentInitiationRecipientCreate(paymentInitiationRecipientCreateRequest)

Create payment recipient

Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payment Area (SEPA) or a non-Eurozone country [supported](https://plaid.com/global) by Plaid. For a standing order (recurring) payment, the recipient must be in the UK.  It is recommended to use &#x60;bacs&#x60; in the UK and &#x60;iban&#x60; in EU.  The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same &#x60;recipient_id&#x60;. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationRecipientCreateRequest = new ThePlaidApi.PaymentInitiationRecipientCreateRequest(); // PaymentInitiationRecipientCreateRequest | 
apiInstance.paymentInitiationRecipientCreate(paymentInitiationRecipientCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationRecipientCreateRequest** | [**PaymentInitiationRecipientCreateRequest**](PaymentInitiationRecipientCreateRequest.md)|  | 

### Return type

[**PaymentInitiationRecipientCreateResponse**](PaymentInitiationRecipientCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationRecipientGet

> PaymentInitiationRecipientGetResponse paymentInitiationRecipientGet(paymentInitiationRecipientGetRequest)

Get payment recipient

Get details about a payment recipient you have previously created.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationRecipientGetRequest = new ThePlaidApi.PaymentInitiationRecipientGetRequest(); // PaymentInitiationRecipientGetRequest | 
apiInstance.paymentInitiationRecipientGet(paymentInitiationRecipientGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationRecipientGetRequest** | [**PaymentInitiationRecipientGetRequest**](PaymentInitiationRecipientGetRequest.md)|  | 

### Return type

[**PaymentInitiationRecipientGetResponse**](PaymentInitiationRecipientGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentInitiationRecipientList

> PaymentInitiationRecipientListResponse paymentInitiationRecipientList(paymentInitiationRecipientListRequest)

List payment recipients

The &#x60;/payment_initiation/recipient/list&#x60; endpoint list the payment recipients that you have previously created.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentInitiationRecipientListRequest = new ThePlaidApi.PaymentInitiationRecipientListRequest(); // PaymentInitiationRecipientListRequest | 
apiInstance.paymentInitiationRecipientList(paymentInitiationRecipientListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentInitiationRecipientListRequest** | [**PaymentInitiationRecipientListRequest**](PaymentInitiationRecipientListRequest.md)|  | 

### Return type

[**PaymentInitiationRecipientListResponse**](PaymentInitiationRecipientListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentProfileCreate

> PaymentProfileCreateResponse paymentProfileCreate(paymentProfileCreateRequest)

Create payment profile

Use &#x60;/payment_profile/create&#x60; endpoint to create a new payment profile. To initiate the account linking experience, call &#x60;/link/token/create&#x60; and provide the &#x60;payment_profile_token&#x60; in the &#x60;transfer.payment_profile_token&#x60; field. You can then use the &#x60;payment_profile_token&#x60; when creating transfers using &#x60;/transfer/authorization/create&#x60; and &#x60;/transfer/create&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentProfileCreateRequest = new ThePlaidApi.PaymentProfileCreateRequest(); // PaymentProfileCreateRequest | 
apiInstance.paymentProfileCreate(paymentProfileCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentProfileCreateRequest** | [**PaymentProfileCreateRequest**](PaymentProfileCreateRequest.md)|  | 

### Return type

[**PaymentProfileCreateResponse**](PaymentProfileCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentProfileGet

> PaymentProfileGetResponse paymentProfileGet(paymentProfileGetRequest)

Get payment profile

Use &#x60;/payment_profile/get&#x60; endpoint to get the status of a given Payment Profile.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentProfileGetRequest = new ThePlaidApi.PaymentProfileGetRequest(); // PaymentProfileGetRequest | 
apiInstance.paymentProfileGet(paymentProfileGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentProfileGetRequest** | [**PaymentProfileGetRequest**](PaymentProfileGetRequest.md)|  | 

### Return type

[**PaymentProfileGetResponse**](PaymentProfileGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## paymentProfileRemove

> PaymentProfileRemoveResponse paymentProfileRemove(paymentProfileRemoveRequest)

Remove payment profile

Use the &#x60;/payment_profile/remove&#x60; endpoint to remove a given Payment Profile. Once it’s removed, it can no longer be used to create transfers.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let paymentProfileRemoveRequest = new ThePlaidApi.PaymentProfileRemoveRequest(); // PaymentProfileRemoveRequest | 
apiInstance.paymentProfileRemove(paymentProfileRemoveRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paymentProfileRemoveRequest** | [**PaymentProfileRemoveRequest**](PaymentProfileRemoveRequest.md)|  | 

### Return type

[**PaymentProfileRemoveResponse**](PaymentProfileRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## processorApexProcessorTokenCreate

> ProcessorTokenCreateResponse processorApexProcessorTokenCreate(processorApexProcessorTokenCreateRequest)

Create Apex bank account token

Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let processorApexProcessorTokenCreateRequest = new ThePlaidApi.ProcessorApexProcessorTokenCreateRequest(); // ProcessorApexProcessorTokenCreateRequest | 
apiInstance.processorApexProcessorTokenCreate(processorApexProcessorTokenCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processorApexProcessorTokenCreateRequest** | [**ProcessorApexProcessorTokenCreateRequest**](ProcessorApexProcessorTokenCreateRequest.md)|  | 

### Return type

[**ProcessorTokenCreateResponse**](ProcessorTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## processorAuthGet

> ProcessorAuthGetResponse processorAuthGet(processorAuthGetRequest)

Retrieve Auth data

The &#x60;/processor/auth/get&#x60; endpoint returns the bank account and bank identification number (such as the routing number, for US accounts), for a checking or savings account that&#39;&#39;s associated with a given &#x60;processor_token&#x60;. The endpoint also returns high-level account data and balances when available.  Versioning note: API versions 2019-05-29 and earlier use a different schema for the &#x60;numbers&#x60; object returned by this endpoint. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2020-09-14). 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let processorAuthGetRequest = new ThePlaidApi.ProcessorAuthGetRequest(); // ProcessorAuthGetRequest | 
apiInstance.processorAuthGet(processorAuthGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processorAuthGetRequest** | [**ProcessorAuthGetRequest**](ProcessorAuthGetRequest.md)|  | 

### Return type

[**ProcessorAuthGetResponse**](ProcessorAuthGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## processorBalanceGet

> ProcessorBalanceGetResponse processorBalanceGet(processorBalanceGetRequest)

Retrieve Balance data

The &#x60;/processor/balance/get&#x60; endpoint returns the real-time balance for each of an Item&#39;s accounts. While other endpoints may return a balance object, only &#x60;/processor/balance/get&#x60; forces the available and current balance fields to be refreshed rather than cached. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let processorBalanceGetRequest = new ThePlaidApi.ProcessorBalanceGetRequest(); // ProcessorBalanceGetRequest | The `/processor/balance/get` endpoint returns the real-time balance for the account associated with a given `processor_token`.  The current balance is the total amount of funds in the account. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account.  Note that not all institutions calculate the available balance. In the event that available balance is unavailable from the institution, Plaid will return an available balance value of `null`.
apiInstance.processorBalanceGet(processorBalanceGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processorBalanceGetRequest** | [**ProcessorBalanceGetRequest**](ProcessorBalanceGetRequest.md)| The &#x60;/processor/balance/get&#x60; endpoint returns the real-time balance for the account associated with a given &#x60;processor_token&#x60;.  The current balance is the total amount of funds in the account. The available balance is the current balance less any outstanding holds or debits that have not yet posted to the account.  Note that not all institutions calculate the available balance. In the event that available balance is unavailable from the institution, Plaid will return an available balance value of &#x60;null&#x60;. | 

### Return type

[**ProcessorBalanceGetResponse**](ProcessorBalanceGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## processorBankTransferCreate

> ProcessorBankTransferCreateResponse processorBankTransferCreate(processorBankTransferCreateRequest)

Create a bank transfer as a processor

Use the &#x60;/processor/bank_transfer/create&#x60; endpoint to initiate a new bank transfer as a processor

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let processorBankTransferCreateRequest = new ThePlaidApi.ProcessorBankTransferCreateRequest(); // ProcessorBankTransferCreateRequest | 
apiInstance.processorBankTransferCreate(processorBankTransferCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processorBankTransferCreateRequest** | [**ProcessorBankTransferCreateRequest**](ProcessorBankTransferCreateRequest.md)|  | 

### Return type

[**ProcessorBankTransferCreateResponse**](ProcessorBankTransferCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## processorIdentityGet

> ProcessorIdentityGetResponse processorIdentityGet(processorIdentityGetRequest)

Retrieve Identity data

The &#x60;/processor/identity/get&#x60; endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let processorIdentityGetRequest = new ThePlaidApi.ProcessorIdentityGetRequest(); // ProcessorIdentityGetRequest | 
apiInstance.processorIdentityGet(processorIdentityGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processorIdentityGetRequest** | [**ProcessorIdentityGetRequest**](ProcessorIdentityGetRequest.md)|  | 

### Return type

[**ProcessorIdentityGetResponse**](ProcessorIdentityGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## processorSignalDecisionReport

> ProcessorSignalDecisionReportResponse processorSignalDecisionReport(processorSignalDecisionReportRequest)

Report whether you initiated an ACH transaction

After calling &#x60;/processor/signal/evaluate&#x60;, call &#x60;/processor/signal/decision/report&#x60; to report whether the transaction was initiated. This endpoint will return an [&#x60;INVALID_FIELD&#x60;](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for &#x60;initiated&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let processorSignalDecisionReportRequest = new ThePlaidApi.ProcessorSignalDecisionReportRequest(); // ProcessorSignalDecisionReportRequest | 
apiInstance.processorSignalDecisionReport(processorSignalDecisionReportRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processorSignalDecisionReportRequest** | [**ProcessorSignalDecisionReportRequest**](ProcessorSignalDecisionReportRequest.md)|  | 

### Return type

[**ProcessorSignalDecisionReportResponse**](ProcessorSignalDecisionReportResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## processorSignalEvaluate

> ProcessorSignalEvaluateResponse processorSignalEvaluate(processorSignalEvaluateRequest)

Evaluate a planned ACH transaction

Use &#x60;/processor/signal/evaluate&#x60; to evaluate a planned ACH transaction as a processor to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.  In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If &#x60;/processor/signal/evaluate&#x60; is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to our error documentation on [item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).  Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let processorSignalEvaluateRequest = new ThePlaidApi.ProcessorSignalEvaluateRequest(); // ProcessorSignalEvaluateRequest | 
apiInstance.processorSignalEvaluate(processorSignalEvaluateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processorSignalEvaluateRequest** | [**ProcessorSignalEvaluateRequest**](ProcessorSignalEvaluateRequest.md)|  | 

### Return type

[**ProcessorSignalEvaluateResponse**](ProcessorSignalEvaluateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## processorSignalReturnReport

> ProcessorSignalReturnReportResponse processorSignalReturnReport(processorSignalReturnReportRequest)

Report a return for an ACH transaction

Call the &#x60;/processor/signal/return/report&#x60; endpoint to report a returned transaction that was previously sent to the &#x60;/processor/signal/evaluate&#x60; endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let processorSignalReturnReportRequest = new ThePlaidApi.ProcessorSignalReturnReportRequest(); // ProcessorSignalReturnReportRequest | 
apiInstance.processorSignalReturnReport(processorSignalReturnReportRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processorSignalReturnReportRequest** | [**ProcessorSignalReturnReportRequest**](ProcessorSignalReturnReportRequest.md)|  | 

### Return type

[**ProcessorSignalReturnReportResponse**](ProcessorSignalReturnReportResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## processorStripeBankAccountTokenCreate

> ProcessorStripeBankAccountTokenCreateResponse processorStripeBankAccountTokenCreate(processorStripeBankAccountTokenCreateRequest)

Create Stripe bank account token

 Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed guide on integrating Stripe, see [Add Stripe to your app](https://plaid.com/docs/auth/partnerships/stripe/).  Note that the Stripe bank account token is a one-time use token. To store bank account information for later use, you can use a Stripe customer object and create an associated bank account from the token, or you can use a Stripe Custom account and create an associated external bank account from the token. This bank account information should work indefinitely, unless the user&#39;s bank account information changes or they revoke Plaid&#39;s permissions to access their account. Stripe bank account information cannot be modified once the bank account token has been created. If you ever need to change the bank account details used by Stripe for a specific customer, have the user go through Link again and create a new bank account token from the new &#x60;access_token&#x60;.  Bank account tokens can also be revoked, using &#x60;/item/remove&#x60;.&#39;

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let processorStripeBankAccountTokenCreateRequest = new ThePlaidApi.ProcessorStripeBankAccountTokenCreateRequest(); // ProcessorStripeBankAccountTokenCreateRequest | 
apiInstance.processorStripeBankAccountTokenCreate(processorStripeBankAccountTokenCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processorStripeBankAccountTokenCreateRequest** | [**ProcessorStripeBankAccountTokenCreateRequest**](ProcessorStripeBankAccountTokenCreateRequest.md)|  | 

### Return type

[**ProcessorStripeBankAccountTokenCreateResponse**](ProcessorStripeBankAccountTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## processorTokenCreate

> ProcessorTokenCreateResponse processorTokenCreate(processorTokenCreateRequest)

Create processor token

Used to create a token suitable for sending to one of Plaid&#39;s partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see &#x60;/processor/stripe/bank_account_token/create&#x60; for creating tokens for use with Stripe integrations. Once created, a processor token for a given Item cannot be modified or updated. If the account must be linked to a new or different partner resource, create a new Item by having the user go through the Link flow again; a new processor token can then be created from the new &#x60;access_token&#x60;. Processor tokens can also be revoked, using &#x60;/item/remove&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let processorTokenCreateRequest = new ThePlaidApi.ProcessorTokenCreateRequest(); // ProcessorTokenCreateRequest | 
apiInstance.processorTokenCreate(processorTokenCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **processorTokenCreateRequest** | [**ProcessorTokenCreateRequest**](ProcessorTokenCreateRequest.md)|  | 

### Return type

[**ProcessorTokenCreateResponse**](ProcessorTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxBankTransferFireWebhook

> SandboxBankTransferFireWebhookResponse sandboxBankTransferFireWebhook(sandboxBankTransferFireWebhookRequest)

Manually fire a Bank Transfer webhook

Use the &#x60;/sandbox/bank_transfer/fire_webhook&#x60; endpoint to manually trigger a Bank Transfers webhook in the Sandbox environment.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxBankTransferFireWebhookRequest = new ThePlaidApi.SandboxBankTransferFireWebhookRequest(); // SandboxBankTransferFireWebhookRequest | 
apiInstance.sandboxBankTransferFireWebhook(sandboxBankTransferFireWebhookRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxBankTransferFireWebhookRequest** | [**SandboxBankTransferFireWebhookRequest**](SandboxBankTransferFireWebhookRequest.md)|  | 

### Return type

[**SandboxBankTransferFireWebhookResponse**](SandboxBankTransferFireWebhookResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxBankTransferSimulate

> SandboxBankTransferSimulateResponse sandboxBankTransferSimulate(sandboxBankTransferSimulateRequest)

Simulate a bank transfer event in Sandbox

Use the &#x60;/sandbox/bank_transfer/simulate&#x60; endpoint to simulate a bank transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as &#x60;/bank_transfer/event/sync&#x60; or &#x60;/bank_transfer/event/list&#x60;, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxBankTransferSimulateRequest = new ThePlaidApi.SandboxBankTransferSimulateRequest(); // SandboxBankTransferSimulateRequest | 
apiInstance.sandboxBankTransferSimulate(sandboxBankTransferSimulateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxBankTransferSimulateRequest** | [**SandboxBankTransferSimulateRequest**](SandboxBankTransferSimulateRequest.md)|  | 

### Return type

[**SandboxBankTransferSimulateResponse**](SandboxBankTransferSimulateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxIncomeFireWebhook

> SandboxIncomeFireWebhookResponse sandboxIncomeFireWebhook(sandboxIncomeFireWebhookRequest)

Manually fire an Income webhook

Use the &#x60;/sandbox/income/fire_webhook&#x60; endpoint to manually trigger an Income webhook in the Sandbox environment.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxIncomeFireWebhookRequest = new ThePlaidApi.SandboxIncomeFireWebhookRequest(); // SandboxIncomeFireWebhookRequest | 
apiInstance.sandboxIncomeFireWebhook(sandboxIncomeFireWebhookRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxIncomeFireWebhookRequest** | [**SandboxIncomeFireWebhookRequest**](SandboxIncomeFireWebhookRequest.md)|  | 

### Return type

[**SandboxIncomeFireWebhookResponse**](SandboxIncomeFireWebhookResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxItemFireWebhook

> SandboxItemFireWebhookResponse sandboxItemFireWebhook(sandboxItemFireWebhookRequest)

Fire a test webhook

The &#x60;/sandbox/item/fire_webhook&#x60; endpoint is used to test that code correctly handles webhooks. This endpoint can trigger the following webhooks:  &#x60;DEFAULT_UPDATE&#x60;: Transactions update webhook to be fired for a given Sandbox Item. If the Item does not support Transactions, a &#x60;SANDBOX_PRODUCT_NOT_ENABLED&#x60; error will result.  &#x60;NEW_ACCOUNTS_AVAILABLE&#x60;: Webhook to be fired for a given Sandbox Item created with Account Select v2.  &#x60;AUTH_DATA_UPDATE&#x60;: Webhook to be fired for a given Sandbox Item created with Auth as an enabled product.  &#x60;RECURRING_TRANSACTIONS_UPDATE&#x60;: Recurring Transactions webhook to be fired for a given Sandbox Item. If the Item does not support Recurring Transactions, a &#x60;SANDBOX_PRODUCT_NOT_ENABLED&#x60; error will result.  &#x60;SYNC_UPDATES_AVAILABLE&#x60;: Transactions webhook to be fired for a given Sandbox Item.  If the Item does not support Transactions, a &#x60;SANDBOX_PRODUCT_NOT_ENABLED&#x60; error will result.  Note that this endpoint is provided for developer ease-of-use and is not required for testing webhooks; webhooks will also fire in Sandbox under the same conditions that they would in Production or Development.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxItemFireWebhookRequest = new ThePlaidApi.SandboxItemFireWebhookRequest(); // SandboxItemFireWebhookRequest | 
apiInstance.sandboxItemFireWebhook(sandboxItemFireWebhookRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxItemFireWebhookRequest** | [**SandboxItemFireWebhookRequest**](SandboxItemFireWebhookRequest.md)|  | 

### Return type

[**SandboxItemFireWebhookResponse**](SandboxItemFireWebhookResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxItemResetLogin

> SandboxItemResetLoginResponse sandboxItemResetLogin(sandboxItemResetLoginRequest)

Force a Sandbox Item into an error state

&#x60;/sandbox/item/reset_login/&#x60; forces an Item into an &#x60;ITEM_LOGIN_REQUIRED&#x60; state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link&#39;s [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling &#x60;/sandbox/item/reset_login&#x60;, You can then use Plaid Link update mode to restore the Item to a good state. An &#x60;ITEM_LOGIN_REQUIRED&#x60; webhook will also be fired after a call to this endpoint, if one is associated with the Item.   In the Sandbox, Items will transition to an &#x60;ITEM_LOGIN_REQUIRED&#x60; error state automatically after 30 days, even if this endpoint is not called.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxItemResetLoginRequest = new ThePlaidApi.SandboxItemResetLoginRequest(); // SandboxItemResetLoginRequest | 
apiInstance.sandboxItemResetLogin(sandboxItemResetLoginRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxItemResetLoginRequest** | [**SandboxItemResetLoginRequest**](SandboxItemResetLoginRequest.md)|  | 

### Return type

[**SandboxItemResetLoginResponse**](SandboxItemResetLoginResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxItemSetVerificationStatus

> SandboxItemSetVerificationStatusResponse sandboxItemSetVerificationStatus(sandboxItemSetVerificationStatusRequest)

Set verification status for Sandbox account

The &#x60;/sandbox/item/set_verification_status&#x60; endpoint can be used to change the verification status of an Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.  Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your status, contact your account manager or [submit a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access).  For more information on testing Automated Micro-deposits in Sandbox, see [Auth full coverage testing](https://plaid.com/docs/auth/coverage/testing#).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxItemSetVerificationStatusRequest = new ThePlaidApi.SandboxItemSetVerificationStatusRequest(); // SandboxItemSetVerificationStatusRequest | 
apiInstance.sandboxItemSetVerificationStatus(sandboxItemSetVerificationStatusRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxItemSetVerificationStatusRequest** | [**SandboxItemSetVerificationStatusRequest**](SandboxItemSetVerificationStatusRequest.md)|  | 

### Return type

[**SandboxItemSetVerificationStatusResponse**](SandboxItemSetVerificationStatusResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxOauthSelectAccounts

> {String: Object} sandboxOauthSelectAccounts(sandboxOauthSelectAccountsRequest)

Save the selected accounts when connecting to the Platypus Oauth institution

Save the selected accounts when connecting to the Platypus Oauth institution

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxOauthSelectAccountsRequest = new ThePlaidApi.SandboxOauthSelectAccountsRequest(); // SandboxOauthSelectAccountsRequest | 
apiInstance.sandboxOauthSelectAccounts(sandboxOauthSelectAccountsRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxOauthSelectAccountsRequest** | [**SandboxOauthSelectAccountsRequest**](SandboxOauthSelectAccountsRequest.md)|  | 

### Return type

**{String: Object}**

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxPaymentProfileResetLogin

> SandboxPaymentProfileResetLoginResponse sandboxPaymentProfileResetLogin(sandboxPaymentProfileResetLoginRequest)

Reset the login of a Payment Profile

&#x60;/sandbox/payment_profile/reset_login/&#x60; forces a Payment Profile into a state where the login is no longer valid. This makes it easy to test update mode for Payment Profile in the Sandbox environment.   After calling &#x60;/sandbox/payment_profile/reset_login&#x60;, calls to the &#x60;/transfer/authorization/create&#x60; with the Payment Profile will result in a &#x60;decision_rationale&#x60; &#x60;PAYMENT_PROFILE_LOGIN_REQUIRED&#x60;. You can then use update mode for Payment Profile to restore it into a good state.   In order to invoke this endpoint, you must first [create a Payment Profile](https://plaid.com/docs/transfer/add-to-app/#create-a-payment-profile-optional) and [go through the Link flow](https://plaid.com/docs/transfer/add-to-app/#create-a-link-token).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxPaymentProfileResetLoginRequest = new ThePlaidApi.SandboxPaymentProfileResetLoginRequest(); // SandboxPaymentProfileResetLoginRequest | 
apiInstance.sandboxPaymentProfileResetLogin(sandboxPaymentProfileResetLoginRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxPaymentProfileResetLoginRequest** | [**SandboxPaymentProfileResetLoginRequest**](SandboxPaymentProfileResetLoginRequest.md)|  | 

### Return type

[**SandboxPaymentProfileResetLoginResponse**](SandboxPaymentProfileResetLoginResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxProcessorTokenCreate

> SandboxProcessorTokenCreateResponse sandboxProcessorTokenCreate(sandboxProcessorTokenCreateRequest)

Create a test Item and processor token

Use the &#x60;/sandbox/processor_token/create&#x60; endpoint to create a valid &#x60;processor_token&#x60; for an arbitrary institution ID and test credentials. The created &#x60;processor_token&#x60; corresponds to a new Sandbox Item. You can then use this &#x60;processor_token&#x60; with the &#x60;/processor/&#x60; API endpoints in Sandbox. You can also use &#x60;/sandbox/processor_token/create&#x60; with the [&#x60;user_custom&#x60; test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxProcessorTokenCreateRequest = new ThePlaidApi.SandboxProcessorTokenCreateRequest(); // SandboxProcessorTokenCreateRequest | 
apiInstance.sandboxProcessorTokenCreate(sandboxProcessorTokenCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxProcessorTokenCreateRequest** | [**SandboxProcessorTokenCreateRequest**](SandboxProcessorTokenCreateRequest.md)|  | 

### Return type

[**SandboxProcessorTokenCreateResponse**](SandboxProcessorTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxPublicTokenCreate

> SandboxPublicTokenCreateResponse sandboxPublicTokenCreate(sandboxPublicTokenCreateRequest)

Create a test Item

Use the &#x60;/sandbox/public_token/create&#x60; endpoint to create a valid &#x60;public_token&#x60;  for an arbitrary institution ID, initial products, and test credentials. The created &#x60;public_token&#x60; maps to a new Sandbox Item. You can then call &#x60;/item/public_token/exchange&#x60; to exchange the &#x60;public_token&#x60; for an &#x60;access_token&#x60; and perform all API actions. &#x60;/sandbox/public_token/create&#x60; can also be used with the [&#x60;user_custom&#x60; test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data. &#x60;/sandbox/public_token/create&#x60; cannot be used with OAuth institutions.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxPublicTokenCreateRequest = new ThePlaidApi.SandboxPublicTokenCreateRequest(); // SandboxPublicTokenCreateRequest | 
apiInstance.sandboxPublicTokenCreate(sandboxPublicTokenCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxPublicTokenCreateRequest** | [**SandboxPublicTokenCreateRequest**](SandboxPublicTokenCreateRequest.md)|  | 

### Return type

[**SandboxPublicTokenCreateResponse**](SandboxPublicTokenCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxTransferFireWebhook

> SandboxTransferFireWebhookResponse sandboxTransferFireWebhook(sandboxTransferFireWebhookRequest)

Manually fire a Transfer webhook

Use the &#x60;/sandbox/transfer/fire_webhook&#x60; endpoint to manually trigger a Transfer webhook in the Sandbox environment.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxTransferFireWebhookRequest = new ThePlaidApi.SandboxTransferFireWebhookRequest(); // SandboxTransferFireWebhookRequest | 
apiInstance.sandboxTransferFireWebhook(sandboxTransferFireWebhookRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxTransferFireWebhookRequest** | [**SandboxTransferFireWebhookRequest**](SandboxTransferFireWebhookRequest.md)|  | 

### Return type

[**SandboxTransferFireWebhookResponse**](SandboxTransferFireWebhookResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxTransferRepaymentSimulate

> SandboxTransferRepaymentSimulateResponse sandboxTransferRepaymentSimulate(sandboxTransferRepaymentSimulateRequest)

Trigger the creation of a repayment

Use the &#x60;/sandbox/transfer/repayment/simulate&#x60; endpoint to trigger the creation of a repayment. As a side effect of calling this route, a repayment is created that includes all unreimbursed returns of guaranteed transfers. If there are no such returns, an 400 error is returned.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxTransferRepaymentSimulateRequest = new ThePlaidApi.SandboxTransferRepaymentSimulateRequest(); // SandboxTransferRepaymentSimulateRequest | 
apiInstance.sandboxTransferRepaymentSimulate(sandboxTransferRepaymentSimulateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxTransferRepaymentSimulateRequest** | [**SandboxTransferRepaymentSimulateRequest**](SandboxTransferRepaymentSimulateRequest.md)|  | 

### Return type

[**SandboxTransferRepaymentSimulateResponse**](SandboxTransferRepaymentSimulateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxTransferSimulate

> SandboxTransferSimulateResponse sandboxTransferSimulate(sandboxTransferSimulateRequest)

Simulate a transfer event in Sandbox

Use the &#x60;/sandbox/transfer/simulate&#x60; endpoint to simulate a transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as &#x60;/transfer/event/sync&#x60; or &#x60;/transfer/event/list&#x60;, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxTransferSimulateRequest = new ThePlaidApi.SandboxTransferSimulateRequest(); // SandboxTransferSimulateRequest | 
apiInstance.sandboxTransferSimulate(sandboxTransferSimulateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxTransferSimulateRequest** | [**SandboxTransferSimulateRequest**](SandboxTransferSimulateRequest.md)|  | 

### Return type

[**SandboxTransferSimulateResponse**](SandboxTransferSimulateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxTransferSweepSimulate

> SandboxTransferSweepSimulateResponse sandboxTransferSweepSimulate(sandboxTransferSweepSimulateRequest)

Simulate creating a sweep

Use the &#x60;/sandbox/transfer/sweep/simulate&#x60; endpoint to create a sweep and associated events in the Sandbox environment. Upon calling this endpoint, all &#x60;posted&#x60; or &#x60;pending&#x60; transfers with a sweep status of &#x60;unswept&#x60; will become &#x60;swept&#x60;, and all &#x60;returned&#x60; transfers with a sweep status of &#x60;swept&#x60; will become &#x60;return_swept&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxTransferSweepSimulateRequest = new ThePlaidApi.SandboxTransferSweepSimulateRequest(); // SandboxTransferSweepSimulateRequest | 
apiInstance.sandboxTransferSweepSimulate(sandboxTransferSweepSimulateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxTransferSweepSimulateRequest** | [**SandboxTransferSweepSimulateRequest**](SandboxTransferSweepSimulateRequest.md)|  | 

### Return type

[**SandboxTransferSweepSimulateResponse**](SandboxTransferSweepSimulateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxTransferTestClockAdvance

> SandboxTransferTestClockAdvanceResponse sandboxTransferTestClockAdvance(sandboxTransferTestClockAdvanceRequest)

Advance a test clock

Use the &#x60;/sandbox/transfer/test_clock/advance&#x60; endpoint to advance a &#x60;test_clock&#x60; in the Sandbox environment.  A test clock object represents an independent timeline and has a &#x60;virtual_time&#x60; field indicating the current timestamp of the timeline. A test clock can be advanced by incrementing &#x60;virtual_time&#x60;, but may never go back to a lower &#x60;virtual_time&#x60;.  If a test clock is advanced, we will simulate the changes that ought to occur during the time that elapsed. For instance, a client creates a weekly recurring transfer with a test clock set at t. When the client advances the test clock by setting &#x60;virtual_time&#x60; &#x3D; t + 15 days, 2 new originations should be created, along with the webhook events.  The advancement of the test clock from its current &#x60;virtual_time&#x60; should be limited such that there are no more than 20 originations resulting from the advance operation on each &#x60;recurring_transfer&#x60; associated with the &#x60;test_clock&#x60;. For instance, if the recurring transfer associated with this test clock originates once every 4 weeks, you can advance the &#x60;virtual_time&#x60; up to 80 weeks on each API call.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxTransferTestClockAdvanceRequest = new ThePlaidApi.SandboxTransferTestClockAdvanceRequest(); // SandboxTransferTestClockAdvanceRequest | 
apiInstance.sandboxTransferTestClockAdvance(sandboxTransferTestClockAdvanceRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxTransferTestClockAdvanceRequest** | [**SandboxTransferTestClockAdvanceRequest**](SandboxTransferTestClockAdvanceRequest.md)|  | 

### Return type

[**SandboxTransferTestClockAdvanceResponse**](SandboxTransferTestClockAdvanceResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxTransferTestClockCreate

> SandboxTransferTestClockCreateResponse sandboxTransferTestClockCreate(sandboxTransferTestClockCreateRequest)

Create a test clock

Use the &#x60;/sandbox/transfer/test_clock/create&#x60; endpoint to create a &#x60;test_clock&#x60; in the Sandbox environment.  A test clock object represents an independent timeline and has a &#x60;virtual_time&#x60; field indicating the current timestamp of the timeline. Test clocks are used for testing recurring transfers in Sandbox.  A test clock can be associated with up to 5 recurring transfers.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxTransferTestClockCreateRequest = new ThePlaidApi.SandboxTransferTestClockCreateRequest(); // SandboxTransferTestClockCreateRequest | 
apiInstance.sandboxTransferTestClockCreate(sandboxTransferTestClockCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxTransferTestClockCreateRequest** | [**SandboxTransferTestClockCreateRequest**](SandboxTransferTestClockCreateRequest.md)|  | 

### Return type

[**SandboxTransferTestClockCreateResponse**](SandboxTransferTestClockCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxTransferTestClockGet

> SandboxTransferTestClockGetResponse sandboxTransferTestClockGet(sandboxTransferTestClockGetRequest)

Get a test clock

Use the &#x60;/sandbox/transfer/test_clock/get&#x60; endpoint to get a &#x60;test_clock&#x60; in the Sandbox environment.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxTransferTestClockGetRequest = new ThePlaidApi.SandboxTransferTestClockGetRequest(); // SandboxTransferTestClockGetRequest | 
apiInstance.sandboxTransferTestClockGet(sandboxTransferTestClockGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxTransferTestClockGetRequest** | [**SandboxTransferTestClockGetRequest**](SandboxTransferTestClockGetRequest.md)|  | 

### Return type

[**SandboxTransferTestClockGetResponse**](SandboxTransferTestClockGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sandboxTransferTestClockList

> SandboxTransferTestClockListResponse sandboxTransferTestClockList(sandboxTransferTestClockListRequest)

List test clocks

Use the &#x60;/sandbox/transfer/test_clock/list&#x60; endpoint to see a list of all your test clocks in the Sandbox environment, by ascending &#x60;virtual_time&#x60;. Results are paginated; use the &#x60;count&#x60; and &#x60;offset&#x60; query parameters to retrieve the desired test clocks.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let sandboxTransferTestClockListRequest = new ThePlaidApi.SandboxTransferTestClockListRequest(); // SandboxTransferTestClockListRequest | 
apiInstance.sandboxTransferTestClockList(sandboxTransferTestClockListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandboxTransferTestClockListRequest** | [**SandboxTransferTestClockListRequest**](SandboxTransferTestClockListRequest.md)|  | 

### Return type

[**SandboxTransferTestClockListResponse**](SandboxTransferTestClockListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## signalDecisionReport

> SignalDecisionReportResponse signalDecisionReport(signalDecisionReportRequest)

Report whether you initiated an ACH transaction

After calling &#x60;/signal/evaluate&#x60;, call &#x60;/signal/decision/report&#x60; to report whether the transaction was initiated. This endpoint will return an [&#x60;INVALID_FIELD&#x60;](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for &#x60;initiated&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let signalDecisionReportRequest = new ThePlaidApi.SignalDecisionReportRequest(); // SignalDecisionReportRequest | 
apiInstance.signalDecisionReport(signalDecisionReportRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signalDecisionReportRequest** | [**SignalDecisionReportRequest**](SignalDecisionReportRequest.md)|  | 

### Return type

[**SignalDecisionReportResponse**](SignalDecisionReportResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## signalEvaluate

> SignalEvaluateResponse signalEvaluate(signalEvaluateRequest)

Evaluate a planned ACH transaction

Use &#x60;/signal/evaluate&#x60; to evaluate a planned ACH transaction to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.  In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If &#x60;/signal/evaluate&#x60; is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to the error documentation on [Item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).  Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let signalEvaluateRequest = new ThePlaidApi.SignalEvaluateRequest(); // SignalEvaluateRequest | 
apiInstance.signalEvaluate(signalEvaluateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signalEvaluateRequest** | [**SignalEvaluateRequest**](SignalEvaluateRequest.md)|  | 

### Return type

[**SignalEvaluateResponse**](SignalEvaluateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## signalPrepare

> SignalPrepareResponse signalPrepare(signalPrepareRequest)

Opt-in an Item to Signal

When Link is not initialized with Signal, call &#x60;/signal/prepare&#x60; to opt-in that Item to the Signal data collection process, developing a Signal score.  If you are using other Plaid products after Link, e.g. Identity or Assets, call &#x60;/signal/prepare&#x60; after those product calls are complete.  Example flow: Link is initialized with Auth, call &#x60;/auth/get&#x60; for the account and routing number, call &#x60;/identity/get&#x60; to retrieve bank ownership details, then call &#x60;/signal/prepare&#x60; to begin Signal data collection. Later, once you have obtained details about the proposed transaction from the user, call &#x60;/signal/evaluate&#x60; for a Signal score. For more information please see [Recommendations for initializing Link with specific product combinations](https://www.plaid.com/docs/link/initializing-products/#recommendations-for-initializing-link-with-specific-product-combinations).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let signalPrepareRequest = new ThePlaidApi.SignalPrepareRequest(); // SignalPrepareRequest | 
apiInstance.signalPrepare(signalPrepareRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signalPrepareRequest** | [**SignalPrepareRequest**](SignalPrepareRequest.md)|  | 

### Return type

[**SignalPrepareResponse**](SignalPrepareResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## signalReturnReport

> SignalReturnReportResponse signalReturnReport(signalReturnReportRequest)

Report a return for an ACH transaction

Call the &#x60;/signal/return/report&#x60; endpoint to report a returned transaction that was previously sent to the &#x60;/signal/evaluate&#x60; endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let signalReturnReportRequest = new ThePlaidApi.SignalReturnReportRequest(); // SignalReturnReportRequest | 
apiInstance.signalReturnReport(signalReturnReportRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signalReturnReportRequest** | [**SignalReturnReportRequest**](SignalReturnReportRequest.md)|  | 

### Return type

[**SignalReturnReportResponse**](SignalReturnReportResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsEnhance

> TransactionsEnhanceGetResponse transactionsEnhance(transactionsEnhanceGetRequest)

enhance locally-held transaction data

The &#x60;/beta/transactions/v1/enhance&#x60; endpoint enriches raw transaction data provided directly by clients.  The product is currently in beta.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transactionsEnhanceGetRequest = new ThePlaidApi.TransactionsEnhanceGetRequest(); // TransactionsEnhanceGetRequest | 
apiInstance.transactionsEnhance(transactionsEnhanceGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionsEnhanceGetRequest** | [**TransactionsEnhanceGetRequest**](TransactionsEnhanceGetRequest.md)|  | 

### Return type

[**TransactionsEnhanceGetResponse**](TransactionsEnhanceGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsEnrich

> TransactionsEnrichGetResponse transactionsEnrich(transactionsEnrichGetRequest)

Enrich locally-held transaction data

The &#x60;/transactions/enrich&#x60; endpoint enriches raw transaction data generated by your own banking products or retrieved from other non-Plaid sources.  To request access to Enrich, reach out to your Plaid point of contact or send a note to enrich-feedback@plaid.com

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transactionsEnrichGetRequest = new ThePlaidApi.TransactionsEnrichGetRequest(); // TransactionsEnrichGetRequest | 
apiInstance.transactionsEnrich(transactionsEnrichGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionsEnrichGetRequest** | [**TransactionsEnrichGetRequest**](TransactionsEnrichGetRequest.md)|  | 

### Return type

[**TransactionsEnrichGetResponse**](TransactionsEnrichGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsGet

> TransactionsGetResponse transactionsGet(transactionsGetRequest)

Get transaction data

The &#x60;/transactions/get&#x60; endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype &#x60;student&#x60;; coverage may be limited). For transaction history from investments accounts, use the [Investments endpoint](https://plaid.com/docs/api/products/investments/) instead. Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.  Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in &#x60;/transactions/get&#x60;.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).  Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the &#x60;count&#x60; and &#x60;offset&#x60; parameters in conjunction with the &#x60;total_transactions&#x60; response body field to fetch all available transactions.  Data returned by &#x60;/transactions/get&#x60; will be the data available for the Item as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item&#39;s &#x60;status.transactions.last_successful_update&#x60; field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, you can use the &#x60;/transactions/refresh&#x60; endpoint.  Note that data may not be immediately available to &#x60;/transactions/get&#x60;. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with &#x60;transactions&#x60;, or upon the first call to &#x60;/transactions/get&#x60;, if it wasn&#39;t. To be alerted when transaction data is ready to be fetched, listen for the [&#x60;INITIAL_UPDATE&#x60;](https://plaid.com/docs/api/products/transactions/#initial_update) and [&#x60;HISTORICAL_UPDATE&#x60;](https://plaid.com/docs/api/products/transactions/#historical_update) webhooks. If no transaction history is ready when &#x60;/transactions/get&#x60; is called, it will return a &#x60;PRODUCT_NOT_READY&#x60; error.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transactionsGetRequest = new ThePlaidApi.TransactionsGetRequest(); // TransactionsGetRequest | 
apiInstance.transactionsGet(transactionsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionsGetRequest** | [**TransactionsGetRequest**](TransactionsGetRequest.md)|  | 

### Return type

[**TransactionsGetResponse**](TransactionsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsRecurringGet

> TransactionsRecurringGetResponse transactionsRecurringGet(transactionsRecurringGetRequest)

Fetch recurring transaction streams

The &#x60;/transactions/recurring/get&#x60; endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user’s checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.  This endpoint is offered as an add-on to Transactions. To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.  This endpoint can only be called on an Item that has already been initialized with Transactions (either during Link, by specifying it in &#x60;/link/token/create&#x60;; or after Link, by calling &#x60;/transactions/get&#x60; or &#x60;/transactions/sync&#x60;). Once all historical transactions have been fetched, call &#x60;/transactions/recurring/get&#x60; to receive the Recurring Transactions streams and subscribe to the [&#x60;RECURRING_TRANSACTIONS_UPDATE&#x60;](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook. To know when historical transactions have been fetched, if you are using &#x60;/transactions/sync&#x60; listen for the [&#x60;SYNC_UPDATES_AVAILABLE&#x60;](https://plaid.com/docs/api/products/transactions/#SyncUpdatesAvailableWebhook-historical-update-complete) webhook and check that the &#x60;historical_update_complete&#x60; field in the payload is &#x60;true&#x60;. If using &#x60;/transactions/get&#x60;, listen for the [&#x60;HISTORICAL_UPDATE&#x60;](https://plaid.com/docs/api/products/transactions/#historical_update) webhook.  After the initial call, you can call &#x60;/transactions/recurring/get&#x60; endpoint at any point in the future to retrieve the latest summary of recurring streams. Listen to the [&#x60;RECURRING_TRANSACTIONS_UPDATE&#x60;](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook to be notified when new updates are available.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transactionsRecurringGetRequest = new ThePlaidApi.TransactionsRecurringGetRequest(); // TransactionsRecurringGetRequest | 
apiInstance.transactionsRecurringGet(transactionsRecurringGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionsRecurringGetRequest** | [**TransactionsRecurringGetRequest**](TransactionsRecurringGetRequest.md)|  | 

### Return type

[**TransactionsRecurringGetResponse**](TransactionsRecurringGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsRefresh

> TransactionsRefreshResponse transactionsRefresh(transactionsRefreshRequest)

Refresh transaction data

&#x60;/transactions/refresh&#x60; is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled Item. If changes to transactions are discovered after calling &#x60;/transactions/refresh&#x60;, Plaid will fire a webhook: for &#x60;/transactions/sync&#x60; users, [&#x60;SYNC_UPDATES_AVAILABLE&#x60;](https://plaid.com/docs/api/products/transactions/#sync_updates_available) will be fired if there are any transactions updated, added, or removed. For users of both &#x60;/transactions/sync&#x60; and &#x60;/transactions/get&#x60;, [&#x60;TRANSACTIONS_REMOVED&#x60;](https://plaid.com/docs/api/products/transactions/#transactions_removed) will be fired if any removed transactions are detected, and [&#x60;DEFAULT_UPDATE&#x60;](https://plaid.com/docs/api/products/transactions/#default_update) will be fired if any new transactions are detected. New transactions can be fetched by calling &#x60;/transactions/get&#x60; or &#x60;/transactions/sync&#x60;. Note that the &#x60;/transactions/refresh&#x60; endpoint is not supported for Capital One (&#x60;ins_128026&#x60;) and will result in a &#x60;PRODUCT_NOT_SUPPORTED&#x60; error if called on an Item from that institution.  &#x60;/transactions/refresh&#x60; is offered as an add-on to Transactions and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transactionsRefreshRequest = new ThePlaidApi.TransactionsRefreshRequest(); // TransactionsRefreshRequest | 
apiInstance.transactionsRefresh(transactionsRefreshRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionsRefreshRequest** | [**TransactionsRefreshRequest**](TransactionsRefreshRequest.md)|  | 

### Return type

[**TransactionsRefreshResponse**](TransactionsRefreshResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsRulesCreate

> TransactionsRulesCreateResponse transactionsRulesCreate(transactionsRulesCreateRequest)

Create transaction category rule

The &#x60;/transactions/rules/v1/create&#x60; endpoint creates transaction categorization rules.  Rules will be applied on the Item&#39;s transactions returned in &#x60;/transactions/get&#x60; response.  The product is currently in beta. To request access, contact transactions-feedback@plaid.com.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transactionsRulesCreateRequest = {"access_token":"access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175","client_id":"7f57eb3d2a9j6480121fx361","personal_finance_category":"FOOD_AND_DRINK_FAST_FOOD","rule_details":{"field":"NAME","query":"Burger Shack","type":"SUBSTRING_MATCH"},"secret":"79g03eoofwl8240v776r2h667442119"}; // TransactionsRulesCreateRequest | 
apiInstance.transactionsRulesCreate(transactionsRulesCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionsRulesCreateRequest** | [**TransactionsRulesCreateRequest**](TransactionsRulesCreateRequest.md)|  | 

### Return type

[**TransactionsRulesCreateResponse**](TransactionsRulesCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsRulesList

> TransactionsRulesListResponse transactionsRulesList(transactionsRulesListRequest)

Return a list of rules created for the Item associated with the access token.

The &#x60;/transactions/rules/v1/list&#x60; returns a list of transaction rules created for the Item associated with the access token.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transactionsRulesListRequest = {"access_token":"access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175","client_id":"7f57eb3d2a9j6480121fx361","secret":"79g03eoofwl8240v776r2h667442119"}; // TransactionsRulesListRequest | 
apiInstance.transactionsRulesList(transactionsRulesListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionsRulesListRequest** | [**TransactionsRulesListRequest**](TransactionsRulesListRequest.md)|  | 

### Return type

[**TransactionsRulesListResponse**](TransactionsRulesListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsRulesRemove

> TransactionsRulesRemoveResponse transactionsRulesRemove(transactionsRulesRemoveRequest)

Remove transaction rule

The &#x60;/transactions/rules/v1/remove&#x60; endpoint is used to remove a transaction rule.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transactionsRulesRemoveRequest = {"access_token":"access-sandbox-71e02f71-0960-4a27-abd2-5631e04f2175","client_id":"7f57eb3d2a9j6480121fx361","rule_id":"eVBnVMp7zdTJLkRNr33Rs6zr7KNJqBF","secret":"79g03eoofwl8240v776r2h667442119"}; // TransactionsRulesRemoveRequest | 
apiInstance.transactionsRulesRemove(transactionsRulesRemoveRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionsRulesRemoveRequest** | [**TransactionsRulesRemoveRequest**](TransactionsRulesRemoveRequest.md)|  | 

### Return type

[**TransactionsRulesRemoveResponse**](TransactionsRulesRemoveResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionsSync

> TransactionsSyncResponse transactionsSync(transactionsSyncRequest)

Get incremental transaction updates on an Item

This endpoint replaces &#x60;/transactions/get&#x60; and its associated webhooks for most common use-cases.  The &#x60;/transactions/sync&#x60; endpoint allows developers to subscribe to all transactions associated with an Item and get updates synchronously in a stream-like manner, using a cursor to track which updates have already been seen. &#x60;/transactions/sync&#x60; provides the same functionality as &#x60;/transactions/get&#x60; and can be used instead of &#x60;/transactions/get&#x60; to simplify the process of tracking transactions updates.  This endpoint provides user-authorized transaction data for &#x60;credit&#x60;, &#x60;depository&#x60;, and some loan-type accounts (only those with account subtype &#x60;student&#x60;; coverage may be limited). For transaction history from &#x60;investments&#x60; accounts, use &#x60;/investments/transactions/get&#x60; instead.  Returned transactions data is grouped into three types of update, indicating whether the transaction was added, removed, or modified since the last call to the API.  In the first call to &#x60;/transactions/sync&#x60; for an Item, the endpoint will return all historical transactions data associated with that Item up until the time of the API call (as \&quot;adds\&quot;), which then generates a &#x60;next_cursor&#x60; for that Item. In subsequent calls, send the &#x60;next_cursor&#x60; to receive only the changes that have occurred since the previous call.  Due to the potentially large number of transactions associated with an Item, results are paginated. The &#x60;has_more&#x60; field specifies if additional calls are necessary to fetch all available transaction updates. Call &#x60;/transactions/sync&#x60; with the new cursor, pulling all updates, until &#x60;has_more&#x60; is &#x60;false&#x60;.  When retrieving paginated updates, track both the &#x60;next_cursor&#x60; from the latest response and the original cursor from the first call in which &#x60;has_more&#x60; was &#x60;true&#x60;; if a call to &#x60;/transactions/sync&#x60; fails when retrieving a paginated update, which can occur as a result of the [&#x60;TRANSACTIONS_SYNC_MUTATION_DURING_PAGINATION&#x60;](https://plaid.com/docs/errors/transactions/#transactions_sync_mutation_during_pagination) error, the entire pagination request loop must be restarted beginning with the cursor for the first page of the update, rather than retrying only the single request that failed.  Whenever new or updated transaction data becomes available, &#x60;/transactions/sync&#x60; will provide these updates. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item&#39;s &#x60;status.transactions.last_successful_update&#x60; field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, use the &#x60;/transactions/refresh&#x60; endpoint.  Note that for newly created Items, data may not be immediately available to &#x60;/transactions/sync&#x60;. Plaid begins preparing transactions data when the Item is created, but the process can take anywhere from a few seconds to several minutes to complete, depending on the number of transactions available.  To be alerted when new data is available, listen for the [&#x60;SYNC_UPDATES_AVAILABLE&#x60;](https://plaid.com/docs/api/products/transactions/#sync_updates_available) webhook.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transactionsSyncRequest = new ThePlaidApi.TransactionsSyncRequest(); // TransactionsSyncRequest | 
apiInstance.transactionsSync(transactionsSyncRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionsSyncRequest** | [**TransactionsSyncRequest**](TransactionsSyncRequest.md)|  | 

### Return type

[**TransactionsSyncResponse**](TransactionsSyncResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferAuthorizationCreate

> TransferAuthorizationCreateResponse transferAuthorizationCreate(transferAuthorizationCreateRequest)

Create a transfer authorization

Use the &#x60;/transfer/authorization/create&#x60; endpoint to determine transfer failure risk.  In Plaid&#39;s Sandbox environment the decisions will be returned as follows:    - To approve a transfer with null rationale code, make an authorization request with an &#x60;amount&#x60; less than the available balance in the account.    - To approve a transfer with the rationale code &#x60;MANUALLY_VERIFIED_ITEM&#x60;, create an Item in Link through the [Same Day Micro-deposits flow](https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits).    - To approve a transfer with the rationale code &#x60;ITEM_LOGIN_REQUIRED&#x60;, [reset the login for an Item](https://plaid.com/docs/sandbox/#item_login_required).    - To decline a transfer with the rationale code &#x60;NSF&#x60;, the available balance on the account must be less than the authorization &#x60;amount&#x60;. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.    - To decline a transfer with the rationale code &#x60;RISK&#x60;, the available balance on the account must be exactly $0. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.  &#x60;device.ip_address&#x60;, &#x60;device.user_agent&#x60; are required fields.  For [Guarantee](https://www.plaid.com/docs//transfer/guarantee/), the following fields are required : &#x60;idempotency_key&#x60;, &#x60;user.phone_number&#x60; (optional if &#x60;email_address&#x60; provided), &#x60;user.email_address&#x60; (optional if &#x60;phone_number&#x60; provided), &#x60;device.ip_address&#x60;, &#x60;device.user_agent&#x60;, and &#x60;user_present&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferAuthorizationCreateRequest = new ThePlaidApi.TransferAuthorizationCreateRequest(); // TransferAuthorizationCreateRequest | 
apiInstance.transferAuthorizationCreate(transferAuthorizationCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferAuthorizationCreateRequest** | [**TransferAuthorizationCreateRequest**](TransferAuthorizationCreateRequest.md)|  | 

### Return type

[**TransferAuthorizationCreateResponse**](TransferAuthorizationCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferCancel

> TransferCancelResponse transferCancel(transferCancelRequest)

Cancel a transfer

Use the &#x60;/transfer/cancel&#x60; endpoint to cancel a transfer.  A transfer is eligible for cancellation if the &#x60;cancellable&#x60; property returned by &#x60;/transfer/get&#x60; is &#x60;true&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferCancelRequest = new ThePlaidApi.TransferCancelRequest(); // TransferCancelRequest | 
apiInstance.transferCancel(transferCancelRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferCancelRequest** | [**TransferCancelRequest**](TransferCancelRequest.md)|  | 

### Return type

[**TransferCancelResponse**](TransferCancelResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferCapabilitiesGet

> TransferCapabilitiesGetResponse transferCapabilitiesGet(transferCapabilitiesGetRequest)

Get RTP eligibility information of a transfer

Use the &#x60;/transfer/capabilities/get&#x60; endpoint to determine the RTP eligibility information of a transfer.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferCapabilitiesGetRequest = new ThePlaidApi.TransferCapabilitiesGetRequest(); // TransferCapabilitiesGetRequest | 
apiInstance.transferCapabilitiesGet(transferCapabilitiesGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferCapabilitiesGetRequest** | [**TransferCapabilitiesGetRequest**](TransferCapabilitiesGetRequest.md)|  | 

### Return type

[**TransferCapabilitiesGetResponse**](TransferCapabilitiesGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferConfigurationGet

> TransferConfigurationGetResponse transferConfigurationGet(transferConfigurationGetRequest)

Get transfer product configuration

Use the &#x60;/transfer/configuration/get&#x60; endpoint to view your transfer product configurations.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferConfigurationGetRequest = new ThePlaidApi.TransferConfigurationGetRequest(); // TransferConfigurationGetRequest | 
apiInstance.transferConfigurationGet(transferConfigurationGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferConfigurationGetRequest** | [**TransferConfigurationGetRequest**](TransferConfigurationGetRequest.md)|  | 

### Return type

[**TransferConfigurationGetResponse**](TransferConfigurationGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferCreate

> TransferCreateResponse transferCreate(transferCreateRequest)

Create a transfer

Use the &#x60;/transfer/create&#x60; endpoint to initiate a new transfer.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferCreateRequest = new ThePlaidApi.TransferCreateRequest(); // TransferCreateRequest | 
apiInstance.transferCreate(transferCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferCreateRequest** | [**TransferCreateRequest**](TransferCreateRequest.md)|  | 

### Return type

[**TransferCreateResponse**](TransferCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferEventList

> TransferEventListResponse transferEventList(transferEventListRequest)

List transfer events

Use the &#x60;/transfer/event/list&#x60; endpoint to get a list of transfer events based on specified filter criteria.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferEventListRequest = new ThePlaidApi.TransferEventListRequest(); // TransferEventListRequest | 
apiInstance.transferEventList(transferEventListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferEventListRequest** | [**TransferEventListRequest**](TransferEventListRequest.md)|  | 

### Return type

[**TransferEventListResponse**](TransferEventListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferEventSync

> TransferEventSyncResponse transferEventSync(transferEventSyncRequest)

Sync transfer events

&#x60;/transfer/event/sync&#x60; allows you to request up to the next 25 transfer events that happened after a specific &#x60;event_id&#x60;. Use the &#x60;/transfer/event/sync&#x60; endpoint to guarantee you have seen all transfer events. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://www.plaid.com/docs/auth/coverage/microdeposit-events/).

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferEventSyncRequest = new ThePlaidApi.TransferEventSyncRequest(); // TransferEventSyncRequest | 
apiInstance.transferEventSync(transferEventSyncRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferEventSyncRequest** | [**TransferEventSyncRequest**](TransferEventSyncRequest.md)|  | 

### Return type

[**TransferEventSyncResponse**](TransferEventSyncResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferGet

> TransferGetResponse transferGet(transferGetRequest)

Retrieve a transfer

The &#x60;/transfer/get&#x60; endpoint fetches information about the transfer corresponding to the given &#x60;transfer_id&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferGetRequest = new ThePlaidApi.TransferGetRequest(); // TransferGetRequest | 
apiInstance.transferGet(transferGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferGetRequest** | [**TransferGetRequest**](TransferGetRequest.md)|  | 

### Return type

[**TransferGetResponse**](TransferGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferIntentCreate

> TransferIntentCreateResponse transferIntentCreate(transferIntentCreateRequest)

Create a transfer intent object to invoke the Transfer UI

Use the &#x60;/transfer/intent/create&#x60; endpoint to generate a transfer intent object and invoke the Transfer UI.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferIntentCreateRequest = new ThePlaidApi.TransferIntentCreateRequest(); // TransferIntentCreateRequest | 
apiInstance.transferIntentCreate(transferIntentCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferIntentCreateRequest** | [**TransferIntentCreateRequest**](TransferIntentCreateRequest.md)|  | 

### Return type

[**TransferIntentCreateResponse**](TransferIntentCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferIntentGet

> TransferIntentGetResponse transferIntentGet(transferIntentGetRequest)

Retrieve more information about a transfer intent

Use the &#x60;/transfer/intent/get&#x60; endpoint to retrieve more information about a transfer intent.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferIntentGetRequest = new ThePlaidApi.TransferIntentGetRequest(); // TransferIntentGetRequest | 
apiInstance.transferIntentGet(transferIntentGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferIntentGetRequest** | [**TransferIntentGetRequest**](TransferIntentGetRequest.md)|  | 

### Return type

[**TransferIntentGetResponse**](TransferIntentGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferList

> TransferListResponse transferList(transferListRequest)

List transfers

Use the &#x60;/transfer/list&#x60; endpoint to see a list of all your transfers and their statuses. Results are paginated; use the &#x60;count&#x60; and &#x60;offset&#x60; query parameters to retrieve the desired transfers. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferListRequest = new ThePlaidApi.TransferListRequest(); // TransferListRequest | 
apiInstance.transferList(transferListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferListRequest** | [**TransferListRequest**](TransferListRequest.md)|  | 

### Return type

[**TransferListResponse**](TransferListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferMetricsGet

> TransferMetricsGetResponse transferMetricsGet(transferMetricsGetRequest)

Get transfer product usage metrics

Use the &#x60;/transfer/metrics/get&#x60; endpoint to view your transfer product usage metrics.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferMetricsGetRequest = new ThePlaidApi.TransferMetricsGetRequest(); // TransferMetricsGetRequest | 
apiInstance.transferMetricsGet(transferMetricsGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferMetricsGetRequest** | [**TransferMetricsGetRequest**](TransferMetricsGetRequest.md)|  | 

### Return type

[**TransferMetricsGetResponse**](TransferMetricsGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferMigrateAccount

> TransferMigrateAccountResponse transferMigrateAccount(transferMigrateAccountRequest)

Migrate account into Transfers

As an alternative to adding Items via Link, you can also use the &#x60;/transfer/migrate_account&#x60; endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as &#x60;/accounts/balance/get&#x60;, and can only be used with Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to &#x60;/transfer/migrate_account&#x60; is not enabled by default; to obtain access, contact your Plaid Account Manager.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferMigrateAccountRequest = new ThePlaidApi.TransferMigrateAccountRequest(); // TransferMigrateAccountRequest | 
apiInstance.transferMigrateAccount(transferMigrateAccountRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferMigrateAccountRequest** | [**TransferMigrateAccountRequest**](TransferMigrateAccountRequest.md)|  | 

### Return type

[**TransferMigrateAccountResponse**](TransferMigrateAccountResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferOriginatorCreate

> TransferOriginatorCreateResponse transferOriginatorCreate(transferOriginatorCreateRequest)

Create a new originator

Use the &#x60;/transfer/originator/create&#x60; endpoint to create a new originator and return an &#x60;originator_client_id&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferOriginatorCreateRequest = new ThePlaidApi.TransferOriginatorCreateRequest(); // TransferOriginatorCreateRequest | 
apiInstance.transferOriginatorCreate(transferOriginatorCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferOriginatorCreateRequest** | [**TransferOriginatorCreateRequest**](TransferOriginatorCreateRequest.md)|  | 

### Return type

[**TransferOriginatorCreateResponse**](TransferOriginatorCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferOriginatorGet

> TransferOriginatorGetResponse transferOriginatorGet(transferOriginatorGetRequest)

Get status of an originator&#39;s onboarding

The &#x60;/transfer/originator/get&#x60; endpoint gets status updates for an originator&#39;s onboarding process. This information is also available via the Transfer page on the Plaid dashboard.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferOriginatorGetRequest = new ThePlaidApi.TransferOriginatorGetRequest(); // TransferOriginatorGetRequest | 
apiInstance.transferOriginatorGet(transferOriginatorGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferOriginatorGetRequest** | [**TransferOriginatorGetRequest**](TransferOriginatorGetRequest.md)|  | 

### Return type

[**TransferOriginatorGetResponse**](TransferOriginatorGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json, examples
- **Accept**: application/json


## transferOriginatorList

> TransferOriginatorListResponse transferOriginatorList(transferOriginatorListRequest)

Get status of all originators&#39; onboarding

The &#x60;/transfer/originator/list&#x60; endpoint gets status updates for all of your originators&#39; onboarding. This information is also available via the Plaid dashboard.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferOriginatorListRequest = new ThePlaidApi.TransferOriginatorListRequest(); // TransferOriginatorListRequest | 
apiInstance.transferOriginatorList(transferOriginatorListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferOriginatorListRequest** | [**TransferOriginatorListRequest**](TransferOriginatorListRequest.md)|  | 

### Return type

[**TransferOriginatorListResponse**](TransferOriginatorListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferQuestionnaireCreate

> TransferQuestionnaireCreateResponse transferQuestionnaireCreate(transferQuestionnaireCreateRequest)

Generate a Plaid-hosted onboarding UI URL.

The &#x60;/transfer/questionnaire/create&#x60; endpoint generates a Plaid-hosted onboarding UI URL. Redirect the originator to this URL to provide their due diligence information and agree to Plaid’s terms for ACH money movement.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferQuestionnaireCreateRequest = new ThePlaidApi.TransferQuestionnaireCreateRequest(); // TransferQuestionnaireCreateRequest | 
apiInstance.transferQuestionnaireCreate(transferQuestionnaireCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferQuestionnaireCreateRequest** | [**TransferQuestionnaireCreateRequest**](TransferQuestionnaireCreateRequest.md)|  | 

### Return type

[**TransferQuestionnaireCreateResponse**](TransferQuestionnaireCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferRecurringCancel

> TransferRecurringCancelResponse transferRecurringCancel(transferRecurringCancelRequest)

Cancel a recurring transfer.

Use the &#x60;/transfer/recurring/cancel&#x60; endpoint to cancel a recurring transfer.  Scheduled transfer that hasn&#39;t been submitted to bank will be cancelled.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferRecurringCancelRequest = new ThePlaidApi.TransferRecurringCancelRequest(); // TransferRecurringCancelRequest | 
apiInstance.transferRecurringCancel(transferRecurringCancelRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferRecurringCancelRequest** | [**TransferRecurringCancelRequest**](TransferRecurringCancelRequest.md)|  | 

### Return type

[**TransferRecurringCancelResponse**](TransferRecurringCancelResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferRecurringCreate

> TransferRecurringCreateResponse transferRecurringCreate(transferRecurringCreateRequest)

Create a recurring transfer

Use the &#x60;/transfer/recurring/create&#x60; endpoint to initiate a new recurring transfer.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferRecurringCreateRequest = new ThePlaidApi.TransferRecurringCreateRequest(); // TransferRecurringCreateRequest | 
apiInstance.transferRecurringCreate(transferRecurringCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferRecurringCreateRequest** | [**TransferRecurringCreateRequest**](TransferRecurringCreateRequest.md)|  | 

### Return type

[**TransferRecurringCreateResponse**](TransferRecurringCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferRecurringGet

> TransferRecurringGetResponse transferRecurringGet(transferRecurringGetRequest)

Retrieve a recurring transfer

The &#x60;/transfer/recurring/get&#x60; fetches information about the recurring transfer corresponding to the given &#x60;recurring_transfer_id&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferRecurringGetRequest = new ThePlaidApi.TransferRecurringGetRequest(); // TransferRecurringGetRequest | 
apiInstance.transferRecurringGet(transferRecurringGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferRecurringGetRequest** | [**TransferRecurringGetRequest**](TransferRecurringGetRequest.md)|  | 

### Return type

[**TransferRecurringGetResponse**](TransferRecurringGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferRecurringList

> TransferRecurringListResponse transferRecurringList(transferRecurringListRequest)

List recurring transfers

Use the &#x60;/transfer/recurring/list&#x60; endpoint to see a list of all your recurring transfers and their statuses. Results are paginated; use the &#x60;count&#x60; and &#x60;offset&#x60; query parameters to retrieve the desired recurring transfers. 

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferRecurringListRequest = new ThePlaidApi.TransferRecurringListRequest(); // TransferRecurringListRequest | 
apiInstance.transferRecurringList(transferRecurringListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferRecurringListRequest** | [**TransferRecurringListRequest**](TransferRecurringListRequest.md)|  | 

### Return type

[**TransferRecurringListResponse**](TransferRecurringListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferRefundCancel

> TransferRefundCancelResponse transferRefundCancel(transferRefundCancelRequest)

Cancel a refund

Use the &#x60;/transfer/refund/cancel&#x60; endpoint to cancel a refund.  A refund is eligible for cancellation if it has not yet been submitted to the payment network.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferRefundCancelRequest = new ThePlaidApi.TransferRefundCancelRequest(); // TransferRefundCancelRequest | 
apiInstance.transferRefundCancel(transferRefundCancelRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferRefundCancelRequest** | [**TransferRefundCancelRequest**](TransferRefundCancelRequest.md)|  | 

### Return type

[**TransferRefundCancelResponse**](TransferRefundCancelResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferRefundCreate

> TransferRefundCreateResponse transferRefundCreate(transferRefundCreateRequest)

Create a refund

Use the &#x60;/transfer/refund/create&#x60; endpoint to create a refund for a transfer. A transfer can be refunded if the transfer was initiated in the past 180 days.  Processing of the refund will not occur until at least 3 business days following the transfer&#39;s settlement date, plus any hold/settlement delays. This 3-day window helps better protect your business from regular ACH returns. Consumer initiated returns (unauthorized returns) could still happen for about 60 days from the settlement date. If the original transfer is canceled, returned or failed, all pending refunds will automatically be canceled. Processed refunds cannot be revoked.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferRefundCreateRequest = new ThePlaidApi.TransferRefundCreateRequest(); // TransferRefundCreateRequest | 
apiInstance.transferRefundCreate(transferRefundCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferRefundCreateRequest** | [**TransferRefundCreateRequest**](TransferRefundCreateRequest.md)|  | 

### Return type

[**TransferRefundCreateResponse**](TransferRefundCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferRefundGet

> TransferRefundGetResponse transferRefundGet(transferRefundGetRequest)

Retrieve a refund

The &#x60;/transfer/refund/get&#x60; endpoint fetches information about the refund corresponding to the given &#x60;refund_id&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferRefundGetRequest = new ThePlaidApi.TransferRefundGetRequest(); // TransferRefundGetRequest | 
apiInstance.transferRefundGet(transferRefundGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferRefundGetRequest** | [**TransferRefundGetRequest**](TransferRefundGetRequest.md)|  | 

### Return type

[**TransferRefundGetResponse**](TransferRefundGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferRepaymentList

> TransferRepaymentListResponse transferRepaymentList(transferRepaymentListRequest)

Lists historical repayments

The &#x60;/transfer/repayment/list&#x60; endpoint fetches repayments matching the given filters. Repayments are returned in reverse-chronological order (most recent first) starting at the given &#x60;start_time&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferRepaymentListRequest = {"count":1,"start_time":"2022-01-10T12:34:56Z"}; // TransferRepaymentListRequest | 
apiInstance.transferRepaymentList(transferRepaymentListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferRepaymentListRequest** | [**TransferRepaymentListRequest**](TransferRepaymentListRequest.md)|  | 

### Return type

[**TransferRepaymentListResponse**](TransferRepaymentListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferRepaymentReturnList

> TransferRepaymentReturnListResponse transferRepaymentReturnList(transferRepaymentReturnListRequest)

List the returns included in a repayment

The &#x60;/transfer/repayment/return/list&#x60; endpoint retrieves the set of returns that were batched together into the specified repayment. The sum of amounts of returns retrieved by this request equals the amount of the repayment.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferRepaymentReturnListRequest = {"count":1,"repayment_id":"d4bfce70-2470-4298-ae87-5e9b3e18bfaf","start_time":"2022-01-10T12:34:56Z"}; // TransferRepaymentReturnListRequest | 
apiInstance.transferRepaymentReturnList(transferRepaymentReturnListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferRepaymentReturnListRequest** | [**TransferRepaymentReturnListRequest**](TransferRepaymentReturnListRequest.md)|  | 

### Return type

[**TransferRepaymentReturnListResponse**](TransferRepaymentReturnListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferSweepGet

> TransferSweepGetResponse transferSweepGet(transferSweepGetRequest)

Retrieve a sweep

The &#x60;/transfer/sweep/get&#x60; endpoint fetches a sweep corresponding to the given &#x60;sweep_id&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferSweepGetRequest = new ThePlaidApi.TransferSweepGetRequest(); // TransferSweepGetRequest | 
apiInstance.transferSweepGet(transferSweepGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferSweepGetRequest** | [**TransferSweepGetRequest**](TransferSweepGetRequest.md)|  | 

### Return type

[**TransferSweepGetResponse**](TransferSweepGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transferSweepList

> TransferSweepListResponse transferSweepList(transferSweepListRequest)

List sweeps

The &#x60;/transfer/sweep/list&#x60; endpoint fetches sweeps matching the given filters.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let transferSweepListRequest = new ThePlaidApi.TransferSweepListRequest(); // TransferSweepListRequest | 
apiInstance.transferSweepList(transferSweepListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferSweepListRequest** | [**TransferSweepListRequest**](TransferSweepListRequest.md)|  | 

### Return type

[**TransferSweepListResponse**](TransferSweepListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## userCreate

> UserCreateResponse userCreate(userCreateRequest)

Create user

This endpoint should be called for each of your end users before they begin a Plaid income flow. This provides you a single token to access all income data associated with the user. You should only create one per end user.  If you call the endpoint multiple times with the same &#x60;client_user_id&#x60;, the first creation call will succeed and the rest will fail with an error message indicating that the user has been created for the given &#x60;client_user_id&#x60;.  Ensure that you store the &#x60;user_token&#x60; along with your user&#39;s identifier in your database, as it is not possible to retrieve a previously created &#x60;user_token&#x60;.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let userCreateRequest = new ThePlaidApi.UserCreateRequest(); // UserCreateRequest | 
apiInstance.userCreate(userCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userCreateRequest** | [**UserCreateRequest**](UserCreateRequest.md)|  | 

### Return type

[**UserCreateResponse**](UserCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## walletCreate

> WalletCreateResponse walletCreate(walletCreateRequest)

Create an e-wallet

Create an e-wallet. The response is the newly created e-wallet object.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let walletCreateRequest = new ThePlaidApi.WalletCreateRequest(); // WalletCreateRequest | 
apiInstance.walletCreate(walletCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **walletCreateRequest** | [**WalletCreateRequest**](WalletCreateRequest.md)|  | 

### Return type

[**WalletCreateResponse**](WalletCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## walletGet

> WalletGetResponse walletGet(walletGetRequest)

Fetch an e-wallet

Fetch an e-wallet. The response includes the current balance.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let walletGetRequest = new ThePlaidApi.WalletGetRequest(); // WalletGetRequest | 
apiInstance.walletGet(walletGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **walletGetRequest** | [**WalletGetRequest**](WalletGetRequest.md)|  | 

### Return type

[**WalletGetResponse**](WalletGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## walletList

> WalletListResponse walletList(walletListRequest)

Fetch a list of e-wallets

This endpoint lists all e-wallets in descending order of creation.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let walletListRequest = new ThePlaidApi.WalletListRequest(); // WalletListRequest | 
apiInstance.walletList(walletListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **walletListRequest** | [**WalletListRequest**](WalletListRequest.md)|  | 

### Return type

[**WalletListResponse**](WalletListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## walletTransactionExecute

> WalletTransactionExecuteResponse walletTransactionExecute(walletTransactionExecuteRequest)

Execute a transaction using an e-wallet

Execute a transaction using the specified e-wallet. Specify the e-wallet to debit from, the counterparty to credit to, the idempotency key to prevent duplicate transactions, the amount and reference for the transaction. Transactions will settle in seconds to several days, depending on the underlying payment rail.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let walletTransactionExecuteRequest = new ThePlaidApi.WalletTransactionExecuteRequest(); // WalletTransactionExecuteRequest | 
apiInstance.walletTransactionExecute(walletTransactionExecuteRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **walletTransactionExecuteRequest** | [**WalletTransactionExecuteRequest**](WalletTransactionExecuteRequest.md)|  | 

### Return type

[**WalletTransactionExecuteResponse**](WalletTransactionExecuteResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## walletTransactionGet

> WalletTransactionGetResponse walletTransactionGet(walletTransactionGetRequest)

Fetch an e-wallet transaction

Fetch a specific e-wallet transaction

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let walletTransactionGetRequest = new ThePlaidApi.WalletTransactionGetRequest(); // WalletTransactionGetRequest | 
apiInstance.walletTransactionGet(walletTransactionGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **walletTransactionGetRequest** | [**WalletTransactionGetRequest**](WalletTransactionGetRequest.md)|  | 

### Return type

[**WalletTransactionGetResponse**](WalletTransactionGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## walletTransactionList

> WalletTransactionListResponse walletTransactionList(walletTransactionListRequest)

List e-wallet transactions

This endpoint lists the latest transactions of the specified e-wallet. Transactions are returned in descending order by the &#x60;created_at&#x60; time.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let walletTransactionListRequest = new ThePlaidApi.WalletTransactionListRequest(); // WalletTransactionListRequest | 
apiInstance.walletTransactionList(walletTransactionListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **walletTransactionListRequest** | [**WalletTransactionListRequest**](WalletTransactionListRequest.md)|  | 

### Return type

[**WalletTransactionListResponse**](WalletTransactionListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningEntityCreate

> WatchlistScreeningEntityCreateResponse watchlistScreeningEntityCreate(watchlistScreeningEntityCreateRequest)

Create a watchlist screening for an entity

Create a new entity watchlist screening to check your customer against watchlists defined in the associated entity watchlist program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningEntityCreateRequest = new ThePlaidApi.WatchlistScreeningEntityCreateRequest(); // WatchlistScreeningEntityCreateRequest | 
apiInstance.watchlistScreeningEntityCreate(watchlistScreeningEntityCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningEntityCreateRequest** | [**WatchlistScreeningEntityCreateRequest**](WatchlistScreeningEntityCreateRequest.md)|  | 

### Return type

[**WatchlistScreeningEntityCreateResponse**](WatchlistScreeningEntityCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningEntityGet

> WatchlistScreeningEntityGetResponse watchlistScreeningEntityGet(watchlistScreeningEntityGetRequest)

Get an entity screening

Retrieve an entity watchlist screening.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningEntityGetRequest = new ThePlaidApi.WatchlistScreeningEntityGetRequest(); // WatchlistScreeningEntityGetRequest | 
apiInstance.watchlistScreeningEntityGet(watchlistScreeningEntityGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningEntityGetRequest** | [**WatchlistScreeningEntityGetRequest**](WatchlistScreeningEntityGetRequest.md)|  | 

### Return type

[**WatchlistScreeningEntityGetResponse**](WatchlistScreeningEntityGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningEntityHistoryList

> WatchlistScreeningEntityHistoryListResponse watchlistScreeningEntityHistoryList(watchlistScreeningEntityHistoryListRequest)

List history for entity watchlist screenings

List all changes to the entity watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningEntityHistoryListRequest = new ThePlaidApi.WatchlistScreeningEntityHistoryListRequest(); // WatchlistScreeningEntityHistoryListRequest | 
apiInstance.watchlistScreeningEntityHistoryList(watchlistScreeningEntityHistoryListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningEntityHistoryListRequest** | [**WatchlistScreeningEntityHistoryListRequest**](WatchlistScreeningEntityHistoryListRequest.md)|  | 

### Return type

[**WatchlistScreeningEntityHistoryListResponse**](WatchlistScreeningEntityHistoryListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningEntityHitList

> WatchlistScreeningEntityHitListResponse watchlistScreeningEntityHitList(watchlistScreeningEntityHitListRequest)

List hits for entity watchlist screenings

List all hits for the entity watchlist screening.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningEntityHitListRequest = new ThePlaidApi.WatchlistScreeningEntityHitListRequest(); // WatchlistScreeningEntityHitListRequest | 
apiInstance.watchlistScreeningEntityHitList(watchlistScreeningEntityHitListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningEntityHitListRequest** | [**WatchlistScreeningEntityHitListRequest**](WatchlistScreeningEntityHitListRequest.md)|  | 

### Return type

[**WatchlistScreeningEntityHitListResponse**](WatchlistScreeningEntityHitListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningEntityList

> WatchlistScreeningEntityListResponse watchlistScreeningEntityList(watchlistScreeningEntityListRequest)

List entity watchlist screenings

List all entity screenings.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningEntityListRequest = new ThePlaidApi.WatchlistScreeningEntityListRequest(); // WatchlistScreeningEntityListRequest | 
apiInstance.watchlistScreeningEntityList(watchlistScreeningEntityListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningEntityListRequest** | [**WatchlistScreeningEntityListRequest**](WatchlistScreeningEntityListRequest.md)|  | 

### Return type

[**WatchlistScreeningEntityListResponse**](WatchlistScreeningEntityListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningEntityProgramGet

> WatchlistScreeningEntityProgramGetResponse watchlistScreeningEntityProgramGet(watchlistScreeningEntityProgramGetRequest)

Get entity watchlist screening program

Get an entity watchlist screening program

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningEntityProgramGetRequest = new ThePlaidApi.WatchlistScreeningEntityProgramGetRequest(); // WatchlistScreeningEntityProgramGetRequest | 
apiInstance.watchlistScreeningEntityProgramGet(watchlistScreeningEntityProgramGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningEntityProgramGetRequest** | [**WatchlistScreeningEntityProgramGetRequest**](WatchlistScreeningEntityProgramGetRequest.md)|  | 

### Return type

[**WatchlistScreeningEntityProgramGetResponse**](WatchlistScreeningEntityProgramGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningEntityProgramList

> WatchlistScreeningEntityProgramListResponse watchlistScreeningEntityProgramList(watchlistScreeningEntityProgramListRequest)

List entity watchlist screening programs

List all entity watchlist screening programs

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningEntityProgramListRequest = new ThePlaidApi.WatchlistScreeningEntityProgramListRequest(); // WatchlistScreeningEntityProgramListRequest | 
apiInstance.watchlistScreeningEntityProgramList(watchlistScreeningEntityProgramListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningEntityProgramListRequest** | [**WatchlistScreeningEntityProgramListRequest**](WatchlistScreeningEntityProgramListRequest.md)|  | 

### Return type

[**WatchlistScreeningEntityProgramListResponse**](WatchlistScreeningEntityProgramListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningEntityReviewCreate

> WatchlistScreeningEntityReviewCreateResponse watchlistScreeningEntityReviewCreate(watchlistScreeningEntityReviewCreateRequest)

Create a review for an entity watchlist screening

Create a review for an entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningEntityReviewCreateRequest = new ThePlaidApi.WatchlistScreeningEntityReviewCreateRequest(); // WatchlistScreeningEntityReviewCreateRequest | 
apiInstance.watchlistScreeningEntityReviewCreate(watchlistScreeningEntityReviewCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningEntityReviewCreateRequest** | [**WatchlistScreeningEntityReviewCreateRequest**](WatchlistScreeningEntityReviewCreateRequest.md)|  | 

### Return type

[**WatchlistScreeningEntityReviewCreateResponse**](WatchlistScreeningEntityReviewCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningEntityReviewList

> WatchlistScreeningEntityReviewListResponse watchlistScreeningEntityReviewList(watchlistScreeningEntityReviewListRequest)

List reviews for entity watchlist screenings

List all reviews for a particular entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningEntityReviewListRequest = new ThePlaidApi.WatchlistScreeningEntityReviewListRequest(); // WatchlistScreeningEntityReviewListRequest | 
apiInstance.watchlistScreeningEntityReviewList(watchlistScreeningEntityReviewListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningEntityReviewListRequest** | [**WatchlistScreeningEntityReviewListRequest**](WatchlistScreeningEntityReviewListRequest.md)|  | 

### Return type

[**WatchlistScreeningEntityReviewListResponse**](WatchlistScreeningEntityReviewListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningEntityUpdate

> WatchlistScreeningEntityUpdateResponse watchlistScreeningEntityUpdate(watchlistScreeningEntityUpdateRequest)

Update an entity screening

Update an entity watchlist screening.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningEntityUpdateRequest = new ThePlaidApi.WatchlistScreeningEntityUpdateRequest(); // WatchlistScreeningEntityUpdateRequest | The entity screening was successfully updated.
apiInstance.watchlistScreeningEntityUpdate(watchlistScreeningEntityUpdateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningEntityUpdateRequest** | [**WatchlistScreeningEntityUpdateRequest**](WatchlistScreeningEntityUpdateRequest.md)| The entity screening was successfully updated. | 

### Return type

[**WatchlistScreeningEntityUpdateResponse**](WatchlistScreeningEntityUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningIndividualCreate

> WatchlistScreeningIndividualCreateResponse watchlistScreeningIndividualCreate(watchlistScreeningIndividualCreateRequest)

Create a watchlist screening for a person

Create a new Watchlist Screening to check your customer against watchlists defined in the associated Watchlist Program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningIndividualCreateRequest = new ThePlaidApi.WatchlistScreeningIndividualCreateRequest(); // WatchlistScreeningIndividualCreateRequest | 
apiInstance.watchlistScreeningIndividualCreate(watchlistScreeningIndividualCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningIndividualCreateRequest** | [**WatchlistScreeningIndividualCreateRequest**](WatchlistScreeningIndividualCreateRequest.md)|  | 

### Return type

[**WatchlistScreeningIndividualCreateResponse**](WatchlistScreeningIndividualCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningIndividualGet

> WatchlistScreeningIndividualGetResponse watchlistScreeningIndividualGet(watchlistScreeningIndividualGetRequest)

Retrieve an individual watchlist screening

Retrieve a previously created individual watchlist screening

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningIndividualGetRequest = new ThePlaidApi.WatchlistScreeningIndividualGetRequest(); // WatchlistScreeningIndividualGetRequest | 
apiInstance.watchlistScreeningIndividualGet(watchlistScreeningIndividualGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningIndividualGetRequest** | [**WatchlistScreeningIndividualGetRequest**](WatchlistScreeningIndividualGetRequest.md)|  | 

### Return type

[**WatchlistScreeningIndividualGetResponse**](WatchlistScreeningIndividualGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningIndividualHistoryList

> WatchlistScreeningIndividualHistoryListResponse watchlistScreeningIndividualHistoryList(watchlistScreeningIndividualHistoryListRequest)

List history for individual watchlist screenings

List all changes to the individual watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningIndividualHistoryListRequest = new ThePlaidApi.WatchlistScreeningIndividualHistoryListRequest(); // WatchlistScreeningIndividualHistoryListRequest | 
apiInstance.watchlistScreeningIndividualHistoryList(watchlistScreeningIndividualHistoryListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningIndividualHistoryListRequest** | [**WatchlistScreeningIndividualHistoryListRequest**](WatchlistScreeningIndividualHistoryListRequest.md)|  | 

### Return type

[**WatchlistScreeningIndividualHistoryListResponse**](WatchlistScreeningIndividualHistoryListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningIndividualHitList

> WatchlistScreeningIndividualHitListResponse watchlistScreeningIndividualHitList(watchlistScreeningIndividualHitListRequest)

List hits for individual watchlist screening

List all hits found by Plaid for a particular individual watchlist screening.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningIndividualHitListRequest = new ThePlaidApi.WatchlistScreeningIndividualHitListRequest(); // WatchlistScreeningIndividualHitListRequest | 
apiInstance.watchlistScreeningIndividualHitList(watchlistScreeningIndividualHitListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningIndividualHitListRequest** | [**WatchlistScreeningIndividualHitListRequest**](WatchlistScreeningIndividualHitListRequest.md)|  | 

### Return type

[**WatchlistScreeningIndividualHitListResponse**](WatchlistScreeningIndividualHitListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningIndividualList

> WatchlistScreeningIndividualListResponse watchlistScreeningIndividualList(watchlistScreeningIndividualListRequest)

List Individual Watchlist Screenings

List previously created watchlist screenings for individuals

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningIndividualListRequest = new ThePlaidApi.WatchlistScreeningIndividualListRequest(); // WatchlistScreeningIndividualListRequest | 
apiInstance.watchlistScreeningIndividualList(watchlistScreeningIndividualListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningIndividualListRequest** | [**WatchlistScreeningIndividualListRequest**](WatchlistScreeningIndividualListRequest.md)|  | 

### Return type

[**WatchlistScreeningIndividualListResponse**](WatchlistScreeningIndividualListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningIndividualProgramGet

> WatchlistScreeningIndividualProgramGetResponse watchlistScreeningIndividualProgramGet(watchlistScreeningIndividualProgramGetRequest)

Get individual watchlist screening program

Get an individual watchlist screening program

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningIndividualProgramGetRequest = new ThePlaidApi.WatchlistScreeningIndividualProgramGetRequest(); // WatchlistScreeningIndividualProgramGetRequest | 
apiInstance.watchlistScreeningIndividualProgramGet(watchlistScreeningIndividualProgramGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningIndividualProgramGetRequest** | [**WatchlistScreeningIndividualProgramGetRequest**](WatchlistScreeningIndividualProgramGetRequest.md)|  | 

### Return type

[**WatchlistScreeningIndividualProgramGetResponse**](WatchlistScreeningIndividualProgramGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningIndividualProgramList

> WatchlistScreeningIndividualProgramListResponse watchlistScreeningIndividualProgramList(watchlistScreeningIndividualProgramListRequest)

List individual watchlist screening programs

List all individual watchlist screening programs

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningIndividualProgramListRequest = new ThePlaidApi.WatchlistScreeningIndividualProgramListRequest(); // WatchlistScreeningIndividualProgramListRequest | 
apiInstance.watchlistScreeningIndividualProgramList(watchlistScreeningIndividualProgramListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningIndividualProgramListRequest** | [**WatchlistScreeningIndividualProgramListRequest**](WatchlistScreeningIndividualProgramListRequest.md)|  | 

### Return type

[**WatchlistScreeningIndividualProgramListResponse**](WatchlistScreeningIndividualProgramListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningIndividualReviewCreate

> WatchlistScreeningIndividualReviewCreateResponse watchlistScreeningIndividualReviewCreate(watchlistScreeningIndividualReviewCreateRequest)

Create a review for an individual watchlist screening

Create a review for the individual watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningIndividualReviewCreateRequest = new ThePlaidApi.WatchlistScreeningIndividualReviewCreateRequest(); // WatchlistScreeningIndividualReviewCreateRequest | 
apiInstance.watchlistScreeningIndividualReviewCreate(watchlistScreeningIndividualReviewCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningIndividualReviewCreateRequest** | [**WatchlistScreeningIndividualReviewCreateRequest**](WatchlistScreeningIndividualReviewCreateRequest.md)|  | 

### Return type

[**WatchlistScreeningIndividualReviewCreateResponse**](WatchlistScreeningIndividualReviewCreateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningIndividualReviewList

> WatchlistScreeningIndividualReviewListResponse watchlistScreeningIndividualReviewList(watchlistScreeningIndividualReviewListRequest)

List reviews for individual watchlist screenings

List all reviews for the individual watchlist screening.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningIndividualReviewListRequest = new ThePlaidApi.WatchlistScreeningIndividualReviewListRequest(); // WatchlistScreeningIndividualReviewListRequest | 
apiInstance.watchlistScreeningIndividualReviewList(watchlistScreeningIndividualReviewListRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningIndividualReviewListRequest** | [**WatchlistScreeningIndividualReviewListRequest**](WatchlistScreeningIndividualReviewListRequest.md)|  | 

### Return type

[**WatchlistScreeningIndividualReviewListResponse**](WatchlistScreeningIndividualReviewListResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## watchlistScreeningIndividualUpdate

> WatchlistScreeningIndividualUpdateResponse watchlistScreeningIndividualUpdate(watchlistScreeningIndividualUpdateRequest)

Update individual watchlist screening

Update a specific individual watchlist screening. This endpoint can be used to add additional customer information, correct outdated information, add a reference id, assign the individual to a reviewer, and update which program it is associated with. Please note that you may not update &#x60;search_terms&#x60; and &#x60;status&#x60; at the same time since editing &#x60;search_terms&#x60; may trigger an automatic &#x60;status&#x60; change.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let watchlistScreeningIndividualUpdateRequest = new ThePlaidApi.WatchlistScreeningIndividualUpdateRequest(); // WatchlistScreeningIndividualUpdateRequest | 
apiInstance.watchlistScreeningIndividualUpdate(watchlistScreeningIndividualUpdateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watchlistScreeningIndividualUpdateRequest** | [**WatchlistScreeningIndividualUpdateRequest**](WatchlistScreeningIndividualUpdateRequest.md)|  | 

### Return type

[**WatchlistScreeningIndividualUpdateResponse**](WatchlistScreeningIndividualUpdateResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webhookVerificationKeyGet

> WebhookVerificationKeyGetResponse webhookVerificationKeyGet(webhookVerificationKeyGetRequest)

Get webhook verification key

Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity of any incoming webhooks to your application. A message signature is included in the &#x60;Plaid-Verification&#x60; header.  The &#x60;/webhook_verification_key/get&#x60; endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

### Example

```javascript
import ThePlaidApi from 'the_plaid_api';
let defaultClient = ThePlaidApi.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: plaidVersion
let plaidVersion = defaultClient.authentications['plaidVersion'];
plaidVersion.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//plaidVersion.apiKeyPrefix = 'Token';
// Configure API key authorization: secret
let secret = defaultClient.authentications['secret'];
secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//secret.apiKeyPrefix = 'Token';

let apiInstance = new ThePlaidApi.PlaidApi();
let webhookVerificationKeyGetRequest = new ThePlaidApi.WebhookVerificationKeyGetRequest(); // WebhookVerificationKeyGetRequest | 
apiInstance.webhookVerificationKeyGet(webhookVerificationKeyGetRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhookVerificationKeyGetRequest** | [**WebhookVerificationKeyGetRequest**](WebhookVerificationKeyGetRequest.md)|  | 

### Return type

[**WebhookVerificationKeyGetResponse**](WebhookVerificationKeyGetResponse.md)

### Authorization

[clientId](../README.md#clientId), [plaidVersion](../README.md#plaidVersion), [secret](../README.md#secret)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

