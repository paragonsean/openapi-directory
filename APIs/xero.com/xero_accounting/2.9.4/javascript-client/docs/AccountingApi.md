# XeroAccountingApi.AccountingApi

All URIs are relative to *https://api.xero.com/api.xro/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAccount**](AccountingApi.md#createAccount) | **PUT** /Accounts | Creates a new chart of accounts
[**createAccountAttachmentByFileName**](AccountingApi.md#createAccountAttachmentByFileName) | **PUT** /Accounts/{AccountID}/Attachments/{FileName} | Creates an attachment on a specific account
[**createBankTransactionAttachmentByFileName**](AccountingApi.md#createBankTransactionAttachmentByFileName) | **PUT** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Creates an attachment for a specific bank transaction by filename
[**createBankTransactionHistoryRecord**](AccountingApi.md#createBankTransactionHistoryRecord) | **PUT** /BankTransactions/{BankTransactionID}/History | Creates a history record for a specific bank transactions
[**createBankTransactions**](AccountingApi.md#createBankTransactions) | **PUT** /BankTransactions | Creates one or more spent or received money transaction
[**createBankTransfer**](AccountingApi.md#createBankTransfer) | **PUT** /BankTransfers | Creates a bank transfer
[**createBankTransferAttachmentByFileName**](AccountingApi.md#createBankTransferAttachmentByFileName) | **PUT** /BankTransfers/{BankTransferID}/Attachments/{FileName} | 
[**createBankTransferHistoryRecord**](AccountingApi.md#createBankTransferHistoryRecord) | **PUT** /BankTransfers/{BankTransferID}/History | Creates a history record for a specific bank transfer
[**createBatchPayment**](AccountingApi.md#createBatchPayment) | **PUT** /BatchPayments | Creates one or many batch payments for invoices
[**createBatchPaymentHistoryRecord**](AccountingApi.md#createBatchPaymentHistoryRecord) | **PUT** /BatchPayments/{BatchPaymentID}/History | Creates a history record for a specific batch payment
[**createBrandingThemePaymentServices**](AccountingApi.md#createBrandingThemePaymentServices) | **POST** /BrandingThemes/{BrandingThemeID}/PaymentServices | Creates a new custom payment service for a specific branding theme
[**createContactAttachmentByFileName**](AccountingApi.md#createContactAttachmentByFileName) | **PUT** /Contacts/{ContactID}/Attachments/{FileName} | 
[**createContactGroup**](AccountingApi.md#createContactGroup) | **PUT** /ContactGroups | Creates a contact group
[**createContactGroupContacts**](AccountingApi.md#createContactGroupContacts) | **PUT** /ContactGroups/{ContactGroupID}/Contacts | Creates contacts to a specific contact group
[**createContactHistory**](AccountingApi.md#createContactHistory) | **PUT** /Contacts/{ContactID}/History | Creates a new history record for a specific contact
[**createContacts**](AccountingApi.md#createContacts) | **PUT** /Contacts | Creates multiple contacts (bulk) in a Xero organisation
[**createCreditNoteAllocation**](AccountingApi.md#createCreditNoteAllocation) | **PUT** /CreditNotes/{CreditNoteID}/Allocations | Creates allocation for a specific credit note
[**createCreditNoteAttachmentByFileName**](AccountingApi.md#createCreditNoteAttachmentByFileName) | **PUT** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Creates an attachment for a specific credit note
[**createCreditNoteHistory**](AccountingApi.md#createCreditNoteHistory) | **PUT** /CreditNotes/{CreditNoteID}/History | Retrieves history records of a specific credit note
[**createCreditNotes**](AccountingApi.md#createCreditNotes) | **PUT** /CreditNotes | Creates a new credit note
[**createCurrency**](AccountingApi.md#createCurrency) | **PUT** /Currencies | Create a new currency for a Xero organisation
[**createEmployees**](AccountingApi.md#createEmployees) | **PUT** /Employees | Creates new employees used in Xero payrun
[**createExpenseClaimHistory**](AccountingApi.md#createExpenseClaimHistory) | **PUT** /ExpenseClaims/{ExpenseClaimID}/History | Creates a history record for a specific expense claim
[**createExpenseClaims**](AccountingApi.md#createExpenseClaims) | **PUT** /ExpenseClaims | Creates expense claims
[**createInvoiceAttachmentByFileName**](AccountingApi.md#createInvoiceAttachmentByFileName) | **PUT** /Invoices/{InvoiceID}/Attachments/{FileName} | Creates an attachment for a specific invoice or purchase bill by filename
[**createInvoiceHistory**](AccountingApi.md#createInvoiceHistory) | **PUT** /Invoices/{InvoiceID}/History | Creates a history record for a specific invoice
[**createInvoices**](AccountingApi.md#createInvoices) | **PUT** /Invoices | Creates one or more sales invoices or purchase bills
[**createItemHistory**](AccountingApi.md#createItemHistory) | **PUT** /Items/{ItemID}/History | Creates a history record for a specific item
[**createItems**](AccountingApi.md#createItems) | **PUT** /Items | Creates one or more items
[**createLinkedTransaction**](AccountingApi.md#createLinkedTransaction) | **PUT** /LinkedTransactions | Creates linked transactions (billable expenses)
[**createManualJournalAttachmentByFileName**](AccountingApi.md#createManualJournalAttachmentByFileName) | **PUT** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Creates a specific attachment for a specific manual journal by file name
[**createManualJournalHistoryRecord**](AccountingApi.md#createManualJournalHistoryRecord) | **PUT** /ManualJournals/{ManualJournalID}/History | Creates a history record for a specific manual journal
[**createManualJournals**](AccountingApi.md#createManualJournals) | **PUT** /ManualJournals | Creates one or more manual journals
[**createOverpaymentAllocations**](AccountingApi.md#createOverpaymentAllocations) | **PUT** /Overpayments/{OverpaymentID}/Allocations | Creates a single allocation for a specific overpayment
[**createOverpaymentHistory**](AccountingApi.md#createOverpaymentHistory) | **PUT** /Overpayments/{OverpaymentID}/History | Creates a history record for a specific overpayment
[**createPayment**](AccountingApi.md#createPayment) | **POST** /Payments | Creates a single payment for invoice or credit notes
[**createPaymentHistory**](AccountingApi.md#createPaymentHistory) | **PUT** /Payments/{PaymentID}/History | Creates a history record for a specific payment
[**createPaymentService**](AccountingApi.md#createPaymentService) | **PUT** /PaymentServices | Creates a payment service
[**createPayments**](AccountingApi.md#createPayments) | **PUT** /Payments | Creates multiple payments for invoices or credit notes
[**createPrepaymentAllocations**](AccountingApi.md#createPrepaymentAllocations) | **PUT** /Prepayments/{PrepaymentID}/Allocations | Allows you to create an Allocation for prepayments
[**createPrepaymentHistory**](AccountingApi.md#createPrepaymentHistory) | **PUT** /Prepayments/{PrepaymentID}/History | Creates a history record for a specific prepayment
[**createPurchaseOrderAttachmentByFileName**](AccountingApi.md#createPurchaseOrderAttachmentByFileName) | **PUT** /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName} | Creates attachment for a specific purchase order
[**createPurchaseOrderHistory**](AccountingApi.md#createPurchaseOrderHistory) | **PUT** /PurchaseOrders/{PurchaseOrderID}/History | Creates a history record for a specific purchase orders
[**createPurchaseOrders**](AccountingApi.md#createPurchaseOrders) | **PUT** /PurchaseOrders | Creates one or more purchase orders
[**createQuoteAttachmentByFileName**](AccountingApi.md#createQuoteAttachmentByFileName) | **PUT** /Quotes/{QuoteID}/Attachments/{FileName} | Creates attachment for a specific quote
[**createQuoteHistory**](AccountingApi.md#createQuoteHistory) | **PUT** /Quotes/{QuoteID}/History | Creates a history record for a specific quote
[**createQuotes**](AccountingApi.md#createQuotes) | **PUT** /Quotes | Create one or more quotes
[**createReceipt**](AccountingApi.md#createReceipt) | **PUT** /Receipts | Creates draft expense claim receipts for any user
[**createReceiptAttachmentByFileName**](AccountingApi.md#createReceiptAttachmentByFileName) | **PUT** /Receipts/{ReceiptID}/Attachments/{FileName} | Creates an attachment on a specific expense claim receipts by file name
[**createReceiptHistory**](AccountingApi.md#createReceiptHistory) | **PUT** /Receipts/{ReceiptID}/History | Creates a history record for a specific receipt
[**createRepeatingInvoiceAttachmentByFileName**](AccountingApi.md#createRepeatingInvoiceAttachmentByFileName) | **PUT** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Creates an attachment from a specific repeating invoices by file name
[**createRepeatingInvoiceHistory**](AccountingApi.md#createRepeatingInvoiceHistory) | **PUT** /RepeatingInvoices/{RepeatingInvoiceID}/History | Creates a  history record for a specific repeating invoice
[**createTaxRates**](AccountingApi.md#createTaxRates) | **PUT** /TaxRates | Creates one or more tax rates
[**createTrackingCategory**](AccountingApi.md#createTrackingCategory) | **PUT** /TrackingCategories | Create tracking categories
[**createTrackingOptions**](AccountingApi.md#createTrackingOptions) | **PUT** /TrackingCategories/{TrackingCategoryID}/Options | Creates options for a specific tracking category
[**deleteAccount**](AccountingApi.md#deleteAccount) | **DELETE** /Accounts/{AccountID} | Deletes a chart of accounts
[**deleteContactGroupContact**](AccountingApi.md#deleteContactGroupContact) | **DELETE** /ContactGroups/{ContactGroupID}/Contacts/{ContactID} | Deletes a specific contact from a contact group using a unique contact Id
[**deleteContactGroupContacts**](AccountingApi.md#deleteContactGroupContacts) | **DELETE** /ContactGroups/{ContactGroupID}/Contacts | Deletes all contacts from a specific contact group
[**deleteItem**](AccountingApi.md#deleteItem) | **DELETE** /Items/{ItemID} | Deletes a specific item
[**deleteLinkedTransaction**](AccountingApi.md#deleteLinkedTransaction) | **DELETE** /LinkedTransactions/{LinkedTransactionID} | Deletes a specific linked transactions (billable expenses)
[**deletePayment**](AccountingApi.md#deletePayment) | **POST** /Payments/{PaymentID} | Updates a specific payment for invoices and credit notes
[**deleteTrackingCategory**](AccountingApi.md#deleteTrackingCategory) | **DELETE** /TrackingCategories/{TrackingCategoryID} | Deletes a specific tracking category
[**deleteTrackingOptions**](AccountingApi.md#deleteTrackingOptions) | **DELETE** /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} | Deletes a specific option for a specific tracking category
[**emailInvoice**](AccountingApi.md#emailInvoice) | **POST** /Invoices/{InvoiceID}/Email | Sends a copy of a specific invoice to related contact via email
[**getAccount**](AccountingApi.md#getAccount) | **GET** /Accounts/{AccountID} | Retrieves a single chart of accounts by using a unique account Id
[**getAccountAttachmentByFileName**](AccountingApi.md#getAccountAttachmentByFileName) | **GET** /Accounts/{AccountID}/Attachments/{FileName} | Retrieves an attachment for a specific account by filename
[**getAccountAttachmentById**](AccountingApi.md#getAccountAttachmentById) | **GET** /Accounts/{AccountID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific account using a unique attachment Id
[**getAccountAttachments**](AccountingApi.md#getAccountAttachments) | **GET** /Accounts/{AccountID}/Attachments | Retrieves attachments for a specific accounts by using a unique account Id
[**getAccounts**](AccountingApi.md#getAccounts) | **GET** /Accounts | Retrieves the full chart of accounts
[**getBankTransaction**](AccountingApi.md#getBankTransaction) | **GET** /BankTransactions/{BankTransactionID} | Retrieves a single spent or received money transaction by using a unique bank transaction Id
[**getBankTransactionAttachmentByFileName**](AccountingApi.md#getBankTransactionAttachmentByFileName) | **GET** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Retrieves a specific attachment from a specific bank transaction by filename
[**getBankTransactionAttachmentById**](AccountingApi.md#getBankTransactionAttachmentById) | **GET** /BankTransactions/{BankTransactionID}/Attachments/{AttachmentID} | Retrieves specific attachments from a specific BankTransaction using a unique attachment Id
[**getBankTransactionAttachments**](AccountingApi.md#getBankTransactionAttachments) | **GET** /BankTransactions/{BankTransactionID}/Attachments | Retrieves any attachments from a specific bank transactions
[**getBankTransactions**](AccountingApi.md#getBankTransactions) | **GET** /BankTransactions | Retrieves any spent or received money transactions
[**getBankTransactionsHistory**](AccountingApi.md#getBankTransactionsHistory) | **GET** /BankTransactions/{BankTransactionID}/History | Retrieves history from a specific bank transaction using a unique bank transaction Id
[**getBankTransfer**](AccountingApi.md#getBankTransfer) | **GET** /BankTransfers/{BankTransferID} | Retrieves specific bank transfers by using a unique bank transfer Id
[**getBankTransferAttachmentByFileName**](AccountingApi.md#getBankTransferAttachmentByFileName) | **GET** /BankTransfers/{BankTransferID}/Attachments/{FileName} | Retrieves a specific attachment on a specific bank transfer by file name
[**getBankTransferAttachmentById**](AccountingApi.md#getBankTransferAttachmentById) | **GET** /BankTransfers/{BankTransferID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific bank transfer using a unique attachment ID
[**getBankTransferAttachments**](AccountingApi.md#getBankTransferAttachments) | **GET** /BankTransfers/{BankTransferID}/Attachments | Retrieves attachments from a specific bank transfer
[**getBankTransferHistory**](AccountingApi.md#getBankTransferHistory) | **GET** /BankTransfers/{BankTransferID}/History | Retrieves history from a specific bank transfer using a unique bank transfer Id
[**getBankTransfers**](AccountingApi.md#getBankTransfers) | **GET** /BankTransfers | Retrieves all bank transfers
[**getBatchPaymentHistory**](AccountingApi.md#getBatchPaymentHistory) | **GET** /BatchPayments/{BatchPaymentID}/History | Retrieves history from a specific batch payment
[**getBatchPayments**](AccountingApi.md#getBatchPayments) | **GET** /BatchPayments | Retrieves either one or many batch payments for invoices
[**getBrandingTheme**](AccountingApi.md#getBrandingTheme) | **GET** /BrandingThemes/{BrandingThemeID} | Retrieves a specific branding theme using a unique branding theme Id
[**getBrandingThemePaymentServices**](AccountingApi.md#getBrandingThemePaymentServices) | **GET** /BrandingThemes/{BrandingThemeID}/PaymentServices | Retrieves the payment services for a specific branding theme
[**getBrandingThemes**](AccountingApi.md#getBrandingThemes) | **GET** /BrandingThemes | Retrieves all the branding themes
[**getContact**](AccountingApi.md#getContact) | **GET** /Contacts/{ContactID} | Retrieves a specific contacts in a Xero organisation using a unique contact Id
[**getContactAttachmentByFileName**](AccountingApi.md#getContactAttachmentByFileName) | **GET** /Contacts/{ContactID}/Attachments/{FileName} | Retrieves a specific attachment from a specific contact by file name
[**getContactAttachmentById**](AccountingApi.md#getContactAttachmentById) | **GET** /Contacts/{ContactID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific contact using a unique attachment Id
[**getContactAttachments**](AccountingApi.md#getContactAttachments) | **GET** /Contacts/{ContactID}/Attachments | Retrieves attachments for a specific contact in a Xero organisation
[**getContactByContactNumber**](AccountingApi.md#getContactByContactNumber) | **GET** /Contacts/{ContactNumber} | Retrieves a specific contact by contact number in a Xero organisation
[**getContactCISSettings**](AccountingApi.md#getContactCISSettings) | **GET** /Contacts/{ContactID}/CISSettings | Retrieves CIS settings for a specific contact in a Xero organisation
[**getContactGroup**](AccountingApi.md#getContactGroup) | **GET** /ContactGroups/{ContactGroupID} | Retrieves a specific contact group by using a unique contact group Id
[**getContactGroups**](AccountingApi.md#getContactGroups) | **GET** /ContactGroups | Retrieves the contact Id and name of all the contacts in a contact group
[**getContactHistory**](AccountingApi.md#getContactHistory) | **GET** /Contacts/{ContactID}/History | Retrieves history records for a specific contact
[**getContacts**](AccountingApi.md#getContacts) | **GET** /Contacts | Retrieves all contacts in a Xero organisation
[**getCreditNote**](AccountingApi.md#getCreditNote) | **GET** /CreditNotes/{CreditNoteID} | Retrieves a specific credit note using a unique credit note Id
[**getCreditNoteAsPdf**](AccountingApi.md#getCreditNoteAsPdf) | **GET** /CreditNotes/{CreditNoteID}/pdf | Retrieves credit notes as PDF files
[**getCreditNoteAttachmentByFileName**](AccountingApi.md#getCreditNoteAttachmentByFileName) | **GET** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Retrieves a specific attachment on a specific credit note by file name
[**getCreditNoteAttachmentById**](AccountingApi.md#getCreditNoteAttachmentById) | **GET** /CreditNotes/{CreditNoteID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific credit note using a unique attachment Id
[**getCreditNoteAttachments**](AccountingApi.md#getCreditNoteAttachments) | **GET** /CreditNotes/{CreditNoteID}/Attachments | Retrieves attachments for a specific credit notes
[**getCreditNoteHistory**](AccountingApi.md#getCreditNoteHistory) | **GET** /CreditNotes/{CreditNoteID}/History | Retrieves history records of a specific credit note
[**getCreditNotes**](AccountingApi.md#getCreditNotes) | **GET** /CreditNotes | Retrieves any credit notes
[**getCurrencies**](AccountingApi.md#getCurrencies) | **GET** /Currencies | Retrieves currencies for your Xero organisation
[**getEmployee**](AccountingApi.md#getEmployee) | **GET** /Employees/{EmployeeID} | Retrieves a specific employee used in Xero payrun using a unique employee Id
[**getEmployees**](AccountingApi.md#getEmployees) | **GET** /Employees | Retrieves employees used in Xero payrun
[**getExpenseClaim**](AccountingApi.md#getExpenseClaim) | **GET** /ExpenseClaims/{ExpenseClaimID} | Retrieves a specific expense claim using a unique expense claim Id
[**getExpenseClaimHistory**](AccountingApi.md#getExpenseClaimHistory) | **GET** /ExpenseClaims/{ExpenseClaimID}/History | Retrieves history records of a specific expense claim
[**getExpenseClaims**](AccountingApi.md#getExpenseClaims) | **GET** /ExpenseClaims | Retrieves expense claims
[**getInvoice**](AccountingApi.md#getInvoice) | **GET** /Invoices/{InvoiceID} | Retrieves a specific sales invoice or purchase bill using a unique invoice Id
[**getInvoiceAsPdf**](AccountingApi.md#getInvoiceAsPdf) | **GET** /Invoices/{InvoiceID}/pdf | Retrieves invoices or purchase bills as PDF files
[**getInvoiceAttachmentByFileName**](AccountingApi.md#getInvoiceAttachmentByFileName) | **GET** /Invoices/{InvoiceID}/Attachments/{FileName} | Retrieves an attachment from a specific invoice or purchase bill by filename
[**getInvoiceAttachmentById**](AccountingApi.md#getInvoiceAttachmentById) | **GET** /Invoices/{InvoiceID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific invoices or purchase bills by using a unique attachment Id
[**getInvoiceAttachments**](AccountingApi.md#getInvoiceAttachments) | **GET** /Invoices/{InvoiceID}/Attachments | Retrieves attachments for a specific invoice or purchase bill
[**getInvoiceHistory**](AccountingApi.md#getInvoiceHistory) | **GET** /Invoices/{InvoiceID}/History | Retrieves history records for a specific invoice
[**getInvoiceReminders**](AccountingApi.md#getInvoiceReminders) | **GET** /InvoiceReminders/Settings | Retrieves invoice reminder settings
[**getInvoices**](AccountingApi.md#getInvoices) | **GET** /Invoices | Retrieves sales invoices or purchase bills
[**getItem**](AccountingApi.md#getItem) | **GET** /Items/{ItemID} | Retrieves a specific item using a unique item Id
[**getItemHistory**](AccountingApi.md#getItemHistory) | **GET** /Items/{ItemID}/History | Retrieves history for a specific item
[**getItems**](AccountingApi.md#getItems) | **GET** /Items | Retrieves items
[**getJournal**](AccountingApi.md#getJournal) | **GET** /Journals/{JournalID} | Retrieves a specific journal using a unique journal Id.
[**getJournals**](AccountingApi.md#getJournals) | **GET** /Journals | Retrieves journals
[**getLinkedTransaction**](AccountingApi.md#getLinkedTransaction) | **GET** /LinkedTransactions/{LinkedTransactionID} | Retrieves a specific linked transaction (billable expenses) using a unique linked transaction Id
[**getLinkedTransactions**](AccountingApi.md#getLinkedTransactions) | **GET** /LinkedTransactions | Retrieves linked transactions (billable expenses)
[**getManualJournal**](AccountingApi.md#getManualJournal) | **GET** /ManualJournals/{ManualJournalID} | Retrieves a specific manual journal
[**getManualJournalAttachmentByFileName**](AccountingApi.md#getManualJournalAttachmentByFileName) | **GET** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Retrieves a specific attachment from a specific manual journal by file name
[**getManualJournalAttachmentById**](AccountingApi.md#getManualJournalAttachmentById) | **GET** /ManualJournals/{ManualJournalID}/Attachments/{AttachmentID} | Allows you to retrieve a specific attachment from a specific manual journal using a unique attachment Id
[**getManualJournalAttachments**](AccountingApi.md#getManualJournalAttachments) | **GET** /ManualJournals/{ManualJournalID}/Attachments | Retrieves attachment for a specific manual journal
[**getManualJournals**](AccountingApi.md#getManualJournals) | **GET** /ManualJournals | Retrieves manual journals
[**getManualJournalsHistory**](AccountingApi.md#getManualJournalsHistory) | **GET** /ManualJournals/{ManualJournalID}/History | Retrieves history for a specific manual journal
[**getOnlineInvoice**](AccountingApi.md#getOnlineInvoice) | **GET** /Invoices/{InvoiceID}/OnlineInvoice | Retrieves a URL to an online invoice
[**getOrganisationActions**](AccountingApi.md#getOrganisationActions) | **GET** /Organisation/Actions | Retrieves a list of the key actions your app has permission to perform in the connected Xero organisation.
[**getOrganisationCISSettings**](AccountingApi.md#getOrganisationCISSettings) | **GET** /Organisation/{OrganisationID}/CISSettings | Retrieves the CIS settings for the Xero organistaion.
[**getOrganisations**](AccountingApi.md#getOrganisations) | **GET** /Organisation | Retrieves Xero organisation details
[**getOverpayment**](AccountingApi.md#getOverpayment) | **GET** /Overpayments/{OverpaymentID} | Retrieves a specific overpayment using a unique overpayment Id
[**getOverpaymentHistory**](AccountingApi.md#getOverpaymentHistory) | **GET** /Overpayments/{OverpaymentID}/History | Retrieves history records of a specific overpayment
[**getOverpayments**](AccountingApi.md#getOverpayments) | **GET** /Overpayments | Retrieves overpayments
[**getPayment**](AccountingApi.md#getPayment) | **GET** /Payments/{PaymentID} | Retrieves a specific payment for invoices and credit notes using a unique payment Id
[**getPaymentHistory**](AccountingApi.md#getPaymentHistory) | **GET** /Payments/{PaymentID}/History | Retrieves history records of a specific payment
[**getPaymentServices**](AccountingApi.md#getPaymentServices) | **GET** /PaymentServices | Retrieves payment services
[**getPayments**](AccountingApi.md#getPayments) | **GET** /Payments | Retrieves payments for invoices and credit notes
[**getPrepayment**](AccountingApi.md#getPrepayment) | **GET** /Prepayments/{PrepaymentID} | Allows you to retrieve a specified prepayments
[**getPrepaymentHistory**](AccountingApi.md#getPrepaymentHistory) | **GET** /Prepayments/{PrepaymentID}/History | Retrieves history record for a specific prepayment
[**getPrepayments**](AccountingApi.md#getPrepayments) | **GET** /Prepayments | Retrieves prepayments
[**getPurchaseOrder**](AccountingApi.md#getPurchaseOrder) | **GET** /PurchaseOrders/{PurchaseOrderID} | Retrieves a specific purchase order using a unique purchase order Id
[**getPurchaseOrderAsPdf**](AccountingApi.md#getPurchaseOrderAsPdf) | **GET** /PurchaseOrders/{PurchaseOrderID}/pdf | Retrieves specific purchase order as PDF files using a unique purchase order Id
[**getPurchaseOrderAttachmentByFileName**](AccountingApi.md#getPurchaseOrderAttachmentByFileName) | **GET** /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName} | Retrieves a specific attachment for a specific purchase order by filename
[**getPurchaseOrderAttachmentById**](AccountingApi.md#getPurchaseOrderAttachmentById) | **GET** /PurchaseOrders/{PurchaseOrderID}/Attachments/{AttachmentID} | Retrieves specific attachment for a specific purchase order using a unique attachment Id
[**getPurchaseOrderAttachments**](AccountingApi.md#getPurchaseOrderAttachments) | **GET** /PurchaseOrders/{PurchaseOrderID}/Attachments | Retrieves attachments for a specific purchase order
[**getPurchaseOrderByNumber**](AccountingApi.md#getPurchaseOrderByNumber) | **GET** /PurchaseOrders/{PurchaseOrderNumber} | Retrieves a specific purchase order using purchase order number
[**getPurchaseOrderHistory**](AccountingApi.md#getPurchaseOrderHistory) | **GET** /PurchaseOrders/{PurchaseOrderID}/History | Retrieves history for a specific purchase order
[**getPurchaseOrders**](AccountingApi.md#getPurchaseOrders) | **GET** /PurchaseOrders | Retrieves purchase orders
[**getQuote**](AccountingApi.md#getQuote) | **GET** /Quotes/{QuoteID} | Retrieves a specific quote using a unique quote Id
[**getQuoteAsPdf**](AccountingApi.md#getQuoteAsPdf) | **GET** /Quotes/{QuoteID}/pdf | Retrieves a specific quote as a PDF file using a unique quote Id
[**getQuoteAttachmentByFileName**](AccountingApi.md#getQuoteAttachmentByFileName) | **GET** /Quotes/{QuoteID}/Attachments/{FileName} | Retrieves a specific attachment from a specific quote by filename
[**getQuoteAttachmentById**](AccountingApi.md#getQuoteAttachmentById) | **GET** /Quotes/{QuoteID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific quote using a unique attachment Id
[**getQuoteAttachments**](AccountingApi.md#getQuoteAttachments) | **GET** /Quotes/{QuoteID}/Attachments | Retrieves attachments for a specific quote
[**getQuoteHistory**](AccountingApi.md#getQuoteHistory) | **GET** /Quotes/{QuoteID}/History | Retrieves history records of a specific quote
[**getQuotes**](AccountingApi.md#getQuotes) | **GET** /Quotes | Retrieves sales quotes
[**getReceipt**](AccountingApi.md#getReceipt) | **GET** /Receipts/{ReceiptID} | Retrieves a specific draft expense claim receipt by using a unique receipt Id
[**getReceiptAttachmentByFileName**](AccountingApi.md#getReceiptAttachmentByFileName) | **GET** /Receipts/{ReceiptID}/Attachments/{FileName} | Retrieves a specific attachment from a specific expense claim receipts by file name
[**getReceiptAttachmentById**](AccountingApi.md#getReceiptAttachmentById) | **GET** /Receipts/{ReceiptID}/Attachments/{AttachmentID} | Retrieves a specific attachments from a specific expense claim receipts by using a unique attachment Id
[**getReceiptAttachments**](AccountingApi.md#getReceiptAttachments) | **GET** /Receipts/{ReceiptID}/Attachments | Retrieves attachments for a specific expense claim receipt
[**getReceiptHistory**](AccountingApi.md#getReceiptHistory) | **GET** /Receipts/{ReceiptID}/History | Retrieves a history record for a specific receipt
[**getReceipts**](AccountingApi.md#getReceipts) | **GET** /Receipts | Retrieves draft expense claim receipts for any user
[**getRepeatingInvoice**](AccountingApi.md#getRepeatingInvoice) | **GET** /RepeatingInvoices/{RepeatingInvoiceID} | Retrieves a specific repeating invoice by using a unique repeating invoice Id
[**getRepeatingInvoiceAttachmentByFileName**](AccountingApi.md#getRepeatingInvoiceAttachmentByFileName) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Retrieves a specific attachment from a specific repeating invoices by file name
[**getRepeatingInvoiceAttachmentById**](AccountingApi.md#getRepeatingInvoiceAttachmentById) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific repeating invoice
[**getRepeatingInvoiceAttachments**](AccountingApi.md#getRepeatingInvoiceAttachments) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments | Retrieves attachments from a specific repeating invoice
[**getRepeatingInvoiceHistory**](AccountingApi.md#getRepeatingInvoiceHistory) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/History | Retrieves history record for a specific repeating invoice
[**getRepeatingInvoices**](AccountingApi.md#getRepeatingInvoices) | **GET** /RepeatingInvoices | Retrieves repeating invoices
[**getReportAgedPayablesByContact**](AccountingApi.md#getReportAgedPayablesByContact) | **GET** /Reports/AgedPayablesByContact | Retrieves report for aged payables by contact
[**getReportAgedReceivablesByContact**](AccountingApi.md#getReportAgedReceivablesByContact) | **GET** /Reports/AgedReceivablesByContact | Retrieves report for aged receivables by contact
[**getReportBASorGST**](AccountingApi.md#getReportBASorGST) | **GET** /Reports/{ReportID} | Retrieves a specific report for BAS using a unique report Id (only valid for AU orgs)
[**getReportBASorGSTList**](AccountingApi.md#getReportBASorGSTList) | **GET** /Reports | Retrieves report for BAS (only valid for AU orgs)
[**getReportBalanceSheet**](AccountingApi.md#getReportBalanceSheet) | **GET** /Reports/BalanceSheet | Retrieves report for balancesheet
[**getReportBankSummary**](AccountingApi.md#getReportBankSummary) | **GET** /Reports/BankSummary | Retrieves report for bank summary
[**getReportBudgetSummary**](AccountingApi.md#getReportBudgetSummary) | **GET** /Reports/BudgetSummary | Retrieves report for budget summary
[**getReportExecutiveSummary**](AccountingApi.md#getReportExecutiveSummary) | **GET** /Reports/ExecutiveSummary | Retrieves report for executive summary
[**getReportProfitAndLoss**](AccountingApi.md#getReportProfitAndLoss) | **GET** /Reports/ProfitAndLoss | Retrieves report for profit and loss
[**getReportTenNinetyNine**](AccountingApi.md#getReportTenNinetyNine) | **GET** /Reports/TenNinetyNine | Retrieve reports for 1099
[**getReportTrialBalance**](AccountingApi.md#getReportTrialBalance) | **GET** /Reports/TrialBalance | Retrieves report for trial balance
[**getTaxRates**](AccountingApi.md#getTaxRates) | **GET** /TaxRates | Retrieves tax rates
[**getTrackingCategories**](AccountingApi.md#getTrackingCategories) | **GET** /TrackingCategories | Retrieves tracking categories and options
[**getTrackingCategory**](AccountingApi.md#getTrackingCategory) | **GET** /TrackingCategories/{TrackingCategoryID} | Retrieves specific tracking categories and options using a unique tracking category Id
[**getUser**](AccountingApi.md#getUser) | **GET** /Users/{UserID} | Retrieves a specific user
[**getUsers**](AccountingApi.md#getUsers) | **GET** /Users | Retrieves users
[**postSetup**](AccountingApi.md#postSetup) | **POST** /Setup | Sets the chart of accounts, the conversion date and conversion balances
[**updateAccount**](AccountingApi.md#updateAccount) | **POST** /Accounts/{AccountID} | Updates a chart of accounts
[**updateAccountAttachmentByFileName**](AccountingApi.md#updateAccountAttachmentByFileName) | **POST** /Accounts/{AccountID}/Attachments/{FileName} | Updates attachment on a specific account by filename
[**updateBankTransaction**](AccountingApi.md#updateBankTransaction) | **POST** /BankTransactions/{BankTransactionID} | Updates a single spent or received money transaction
[**updateBankTransactionAttachmentByFileName**](AccountingApi.md#updateBankTransactionAttachmentByFileName) | **POST** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Updates a specific attachment from a specific bank transaction by filename
[**updateBankTransferAttachmentByFileName**](AccountingApi.md#updateBankTransferAttachmentByFileName) | **POST** /BankTransfers/{BankTransferID}/Attachments/{FileName} | 
[**updateContact**](AccountingApi.md#updateContact) | **POST** /Contacts/{ContactID} | Updates a specific contact in a Xero organisation
[**updateContactAttachmentByFileName**](AccountingApi.md#updateContactAttachmentByFileName) | **POST** /Contacts/{ContactID}/Attachments/{FileName} | 
[**updateContactGroup**](AccountingApi.md#updateContactGroup) | **POST** /ContactGroups/{ContactGroupID} | Updates a specific contact group
[**updateCreditNote**](AccountingApi.md#updateCreditNote) | **POST** /CreditNotes/{CreditNoteID} | Updates a specific credit note
[**updateCreditNoteAttachmentByFileName**](AccountingApi.md#updateCreditNoteAttachmentByFileName) | **POST** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Updates attachments on a specific credit note by file name
[**updateExpenseClaim**](AccountingApi.md#updateExpenseClaim) | **POST** /ExpenseClaims/{ExpenseClaimID} | Updates a specific expense claims
[**updateInvoice**](AccountingApi.md#updateInvoice) | **POST** /Invoices/{InvoiceID} | Updates a specific sales invoices or purchase bills
[**updateInvoiceAttachmentByFileName**](AccountingApi.md#updateInvoiceAttachmentByFileName) | **POST** /Invoices/{InvoiceID}/Attachments/{FileName} | Updates an attachment from a specific invoices or purchase bill by filename
[**updateItem**](AccountingApi.md#updateItem) | **POST** /Items/{ItemID} | Updates a specific item
[**updateLinkedTransaction**](AccountingApi.md#updateLinkedTransaction) | **POST** /LinkedTransactions/{LinkedTransactionID} | Updates a specific linked transactions (billable expenses)
[**updateManualJournal**](AccountingApi.md#updateManualJournal) | **POST** /ManualJournals/{ManualJournalID} | Updates a specific manual journal
[**updateManualJournalAttachmentByFileName**](AccountingApi.md#updateManualJournalAttachmentByFileName) | **POST** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Updates a specific attachment from a specific manual journal by file name
[**updateOrCreateBankTransactions**](AccountingApi.md#updateOrCreateBankTransactions) | **POST** /BankTransactions | Updates or creates one or more spent or received money transaction
[**updateOrCreateContacts**](AccountingApi.md#updateOrCreateContacts) | **POST** /Contacts | Updates or creates one or more contacts in a Xero organisation
[**updateOrCreateCreditNotes**](AccountingApi.md#updateOrCreateCreditNotes) | **POST** /CreditNotes | Updates or creates one or more credit notes
[**updateOrCreateEmployees**](AccountingApi.md#updateOrCreateEmployees) | **POST** /Employees | Creates a single new employees used in Xero payrun
[**updateOrCreateInvoices**](AccountingApi.md#updateOrCreateInvoices) | **POST** /Invoices | Updates or creates one or more sales invoices or purchase bills
[**updateOrCreateItems**](AccountingApi.md#updateOrCreateItems) | **POST** /Items | Updates or creates one or more items
[**updateOrCreateManualJournals**](AccountingApi.md#updateOrCreateManualJournals) | **POST** /ManualJournals | Updates or creates a single manual journal
[**updateOrCreatePurchaseOrders**](AccountingApi.md#updateOrCreatePurchaseOrders) | **POST** /PurchaseOrders | Updates or creates one or more purchase orders
[**updateOrCreateQuotes**](AccountingApi.md#updateOrCreateQuotes) | **POST** /Quotes | Updates or creates one or more quotes
[**updatePurchaseOrder**](AccountingApi.md#updatePurchaseOrder) | **POST** /PurchaseOrders/{PurchaseOrderID} | Updates a specific purchase order
[**updatePurchaseOrderAttachmentByFileName**](AccountingApi.md#updatePurchaseOrderAttachmentByFileName) | **POST** /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName} | Updates a specific attachment for a specific purchase order by filename
[**updateQuote**](AccountingApi.md#updateQuote) | **POST** /Quotes/{QuoteID} | Updates a specific quote
[**updateQuoteAttachmentByFileName**](AccountingApi.md#updateQuoteAttachmentByFileName) | **POST** /Quotes/{QuoteID}/Attachments/{FileName} | Updates a specific attachment from a specific quote by filename
[**updateReceipt**](AccountingApi.md#updateReceipt) | **POST** /Receipts/{ReceiptID} | Updates a specific draft expense claim receipts
[**updateReceiptAttachmentByFileName**](AccountingApi.md#updateReceiptAttachmentByFileName) | **POST** /Receipts/{ReceiptID}/Attachments/{FileName} | Updates a specific attachment on a specific expense claim receipts by file name
[**updateRepeatingInvoiceAttachmentByFileName**](AccountingApi.md#updateRepeatingInvoiceAttachmentByFileName) | **POST** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Updates a specific attachment from a specific repeating invoices by file name
[**updateTaxRate**](AccountingApi.md#updateTaxRate) | **POST** /TaxRates | Updates tax rates
[**updateTrackingCategory**](AccountingApi.md#updateTrackingCategory) | **POST** /TrackingCategories/{TrackingCategoryID} | Updates a specific tracking category
[**updateTrackingOptions**](AccountingApi.md#updateTrackingOptions) | **POST** /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} | Updates a specific option for a specific tracking category



## createAccount

> Accounts createAccount(xeroTenantId, account)

Creates a new chart of accounts

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let account = { "Code":"123456", "Name":"Foobar", "Type":"EXPENSE", "Description":"Hello World" }; // Account | Account object in body of request
apiInstance.createAccount(xeroTenantId, account, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **account** | [**Account**](Account.md)| Account object in body of request | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAccountAttachmentByFileName

> Attachments createAccountAttachmentByFileName(xeroTenantId, accountID, fileName, body)

Creates an attachment on a specific account

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let accountID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Account object
let fileName = "xero-dev.jpg"; // String | Name of the attachment
let body = null; // Blob | Byte array of file in body of request
apiInstance.createAccountAttachmentByFileName(xeroTenantId, accountID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **accountID** | **String**| Unique identifier for Account object | 
 **fileName** | **String**| Name of the attachment | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createBankTransactionAttachmentByFileName

> Attachments createBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, body)

Creates an attachment for a specific bank transaction by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transaction
let fileName = "xero-dev.jpg"; // String | The name of the file being attached
let body = null; // Blob | Byte array of file in body of request
apiInstance.createBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactionID** | **String**| Xero generated unique identifier for a bank transaction | 
 **fileName** | **String**| The name of the file being attached | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createBankTransactionHistoryRecord

> HistoryRecords createBankTransactionHistoryRecord(xeroTenantId, bankTransactionID, historyRecords)

Creates a history record for a specific bank transactions

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transaction
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createBankTransactionHistoryRecord(xeroTenantId, bankTransactionID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactionID** | **String**| Xero generated unique identifier for a bank transaction | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBankTransactions

> BankTransactions createBankTransactions(xeroTenantId, bankTransactions, opts)

Creates one or more spent or received money transaction

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactions = { bankTransactions: [{ type: BankTransaction.TypeEnum.SPEND, contact: { contactID: "00000000-0000-0000-0000-000000000000" }, lineItems: [{ description: "Foobar", quantity: 1.0, unitAmount: 20.0, accountCode: "000" } ], bankAccount: { code: "000" }}]}; // BankTransactions | BankTransactions with an array of BankTransaction objects in body of request
let opts = {
  'summarizeErrors': true, // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.createBankTransactions(xeroTenantId, bankTransactions, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactions** | [**BankTransactions**](BankTransactions.md)| BankTransactions with an array of BankTransaction objects in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBankTransfer

> BankTransfers createBankTransfer(xeroTenantId, bankTransfers)

Creates a bank transfer

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransfers = { "BankTransfers": [ { "FromBankAccount": { "Code": "090", "Name": "My Savings", "AccountID": "00000000-0000-0000-0000-000000000000", "Type": "BANK", "BankAccountNumber": "123455", "Status": "ACTIVE", "BankAccountType": "BANK", "CurrencyCode": "USD", "TaxType": "NONE", "EnablePaymentsToAccount": false, "ShowInExpenseClaims": false, "Class": "ASSET", "ReportingCode": "ASS", "ReportingCodeName": "Assets", "HasAttachments": false, "UpdatedDateUTC": "2016-10-17T13:45:33.993-07:00" }, "ToBankAccount": { "Code": "088", "Name": "Business Wells Fargo", "AccountID": "00000000-0000-0000-0000-000000000000", "Type": "BANK", "BankAccountNumber": "123455", "Status": "ACTIVE", "BankAccountType": "BANK", "CurrencyCode": "USD", "TaxType": "NONE", "EnablePaymentsToAccount": false, "ShowInExpenseClaims": false, "Class": "ASSET", "ReportingCode": "ASS", "ReportingCodeName": "Assets", "HasAttachments": false, "UpdatedDateUTC": "2016-06-03T08:31:14.517-07:00" }, "Amount": "50.00" } ] }; // BankTransfers | BankTransfers with array of BankTransfer objects in request body
apiInstance.createBankTransfer(xeroTenantId, bankTransfers, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransfers** | [**BankTransfers**](BankTransfers.md)| BankTransfers with array of BankTransfer objects in request body | 

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBankTransferAttachmentByFileName

> Attachments createBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, body)



### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransferID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transfer
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Bank Transfer
let body = null; // Blob | Byte array of file in body of request
apiInstance.createBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransferID** | **String**| Xero generated unique identifier for a bank transfer | 
 **fileName** | **String**| The name of the file being attached to a Bank Transfer | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createBankTransferHistoryRecord

> HistoryRecords createBankTransferHistoryRecord(xeroTenantId, bankTransferID, historyRecords)

Creates a history record for a specific bank transfer

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransferID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transfer
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createBankTransferHistoryRecord(xeroTenantId, bankTransferID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransferID** | **String**| Xero generated unique identifier for a bank transfer | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBatchPayment

> BatchPayments createBatchPayment(xeroTenantId, batchPayments, opts)

Creates one or many batch payments for invoices

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let batchPayments = { "BatchPayments": [ { "Account": { "AccountID": "00000000-0000-0000-0000-000000000000" }, "Reference": "ref", "Date": "2018-08-01", "Payments": [ { "Account": { "Code": "001" }, "Date": "2019-12-31", "Amount": 500, "Invoice": { "InvoiceID": "00000000-0000-0000-0000-000000000000", "LineItems": [], "Contact": {}, "Type": "ACCPAY" } } ] } ] }; // BatchPayments | BatchPayments with an array of Payments in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.createBatchPayment(xeroTenantId, batchPayments, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **batchPayments** | [**BatchPayments**](BatchPayments.md)| BatchPayments with an array of Payments in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**BatchPayments**](BatchPayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBatchPaymentHistoryRecord

> HistoryRecords createBatchPaymentHistoryRecord(xeroTenantId, batchPaymentID, historyRecords)

Creates a history record for a specific batch payment

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let batchPaymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for BatchPayment
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createBatchPaymentHistoryRecord(xeroTenantId, batchPaymentID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **batchPaymentID** | **String**| Unique identifier for BatchPayment | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBrandingThemePaymentServices

> PaymentServices createBrandingThemePaymentServices(xeroTenantId, brandingThemeID, paymentService)

Creates a new custom payment service for a specific branding theme

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let brandingThemeID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Branding Theme
let paymentService = {   "PaymentServiceID": "00000000-0000-0000-0000-000000000000", "PaymentServiceName": "ACME Payments", "PaymentServiceUrl": "https://www.payupnow.com/", "PayNowText": "Pay Now" }; // PaymentService | PaymentService object in body of request
apiInstance.createBrandingThemePaymentServices(xeroTenantId, brandingThemeID, paymentService, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **brandingThemeID** | **String**| Unique identifier for a Branding Theme | 
 **paymentService** | [**PaymentService**](PaymentService.md)| PaymentService object in body of request | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContactAttachmentByFileName

> Attachments createContactAttachmentByFileName(xeroTenantId, contactID, fileName, body)



### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
let fileName = "xero-dev.jpg"; // String | Name for the file you are attaching
let body = null; // Blob | Byte array of file in body of request
apiInstance.createContactAttachmentByFileName(xeroTenantId, contactID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactID** | **String**| Unique identifier for a Contact | 
 **fileName** | **String**| Name for the file you are attaching | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createContactGroup

> ContactGroups createContactGroup(xeroTenantId, contactGroups)

Creates a contact group

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactGroups = { "ContactGroups": [{ "Name": "VIPs" }]}; // ContactGroups | ContactGroups with an array of names in request body
apiInstance.createContactGroup(xeroTenantId, contactGroups, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactGroups** | [**ContactGroups**](ContactGroups.md)| ContactGroups with an array of names in request body | 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContactGroupContacts

> Contacts createContactGroupContacts(xeroTenantId, contactGroupID, contacts)

Creates contacts to a specific contact group

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactGroupID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact Group
let contacts = { "Contacts": [ { "ContactID": "a3675fc4-f8dd-4f03-ba5b-f1870566bcd7" }, { "ContactID": "4e1753b9-018a-4775-b6aa-1bc7871cfee3" } ] }; // Contacts | Contacts with array of contacts specifying the ContactID to be added to ContactGroup in body of request
apiInstance.createContactGroupContacts(xeroTenantId, contactGroupID, contacts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactGroupID** | **String**| Unique identifier for a Contact Group | 
 **contacts** | [**Contacts**](Contacts.md)| Contacts with array of contacts specifying the ContactID to be added to ContactGroup in body of request | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContactHistory

> HistoryRecords createContactHistory(xeroTenantId, contactID, historyRecords)

Creates a new history record for a specific contact

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createContactHistory(xeroTenantId, contactID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactID** | **String**| Unique identifier for a Contact | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContacts

> Contacts createContacts(xeroTenantId, contacts, opts)

Creates multiple contacts (bulk) in a Xero organisation

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contacts = { "Id": "e997d6d7-6dad-4458-beb8-d9c1bf7f2edf", "Status": "OK", "ProviderName": "Xero API Partner", "DateTimeUTC": "/Date(1551399321121)/", "Contacts": [ { "ContactID": "3ff6d40c-af9a-40a3-89ce-3c1556a25591", "ContactStatus": "ACTIVE", "Name": "Foo9987", "EmailAddress": "sid32476@blah.com", "BankAccountDetails": "", "Addresses": [ { "AddressType": "STREET", "City": "", "Region": "", "PostalCode": "", "Country": "" }, { "AddressType": "POBOX", "City": "", "Region": "", "PostalCode": "", "Country": "" } ], "Phones": [ { "PhoneType": "DEFAULT", "PhoneNumber": "", "PhoneAreaCode": "", "PhoneCountryCode": "" }, { "PhoneType": "DDI", "PhoneNumber": "", "PhoneAreaCode": "", "PhoneCountryCode": "" }, { "PhoneType": "FAX", "PhoneNumber": "", "PhoneAreaCode": "", "PhoneCountryCode": "" }, { "PhoneType": "MOBILE", "PhoneNumber": "555-1212", "PhoneAreaCode": "415", "PhoneCountryCode": "" } ], "UpdatedDateUTC": "/Date(1551399321043+0000)/", "ContactGroups": [], "IsSupplier": false, "IsCustomer": false, "SalesTrackingCategories": [], "PurchasesTrackingCategories": [], "PaymentTerms": { "Bills": { "Day": 15, "Type": "OFCURRENTMONTH" }, "Sales": { "Day": 10, "Type": "DAYSAFTERBILLMONTH" } }, "ContactPersons": [], "HasValidationErrors": false } ] }; // Contacts | Contacts with an array of Contact objects to create in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.createContacts(xeroTenantId, contacts, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contacts** | [**Contacts**](Contacts.md)| Contacts with an array of Contact objects to create in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCreditNoteAllocation

> Allocations createCreditNoteAllocation(xeroTenantId, creditNoteID, allocations, opts)

Creates allocation for a specific credit note

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
let allocations = { "Allocations": [ { "Invoice": { "LineItems": [], "InvoiceID": "c45720a1-ade3-4a38-a064-d15489be6841" }, "Amount": 1, "Date": "2019-03-05" } ] }; // Allocations | Allocations with array of Allocation object in body of request.
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.createCreditNoteAllocation(xeroTenantId, creditNoteID, allocations, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 
 **allocations** | [**Allocations**](Allocations.md)| Allocations with array of Allocation object in body of request. | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**Allocations**](Allocations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCreditNoteAttachmentByFileName

> Attachments createCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, body, opts)

Creates an attachment for a specific credit note

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
let fileName = "xero-dev.jpg"; // String | Name of the file you are attaching to Credit Note
let body = null; // Blob | Byte array of file in body of request
let opts = {
  'includeOnline': true // Boolean | Allows an attachment to be seen by the end customer within their online invoice
};
apiInstance.createCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, body, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 
 **fileName** | **String**| Name of the file you are attaching to Credit Note | 
 **body** | **Blob**| Byte array of file in body of request | 
 **includeOnline** | **Boolean**| Allows an attachment to be seen by the end customer within their online invoice | [optional] [default to false]

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createCreditNoteHistory

> HistoryRecords createCreditNoteHistory(xeroTenantId, creditNoteID, historyRecords)

Retrieves history records of a specific credit note

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createCreditNoteHistory(xeroTenantId, creditNoteID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCreditNotes

> CreditNotes createCreditNotes(xeroTenantId, creditNotes, opts)

Creates a new credit note

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNotes = {   "CreditNotes":[   {   "Type":"ACCPAYCREDIT", "Contact":{   "ContactID":"430fa14a-f945-44d3-9f97-5df5e28441b8" }, "Date":"2019-01-05", "LineItems":[   {   "Description":"Foobar", "Quantity":2.0, "UnitAmount":20.0, "AccountCode":"400" } ] } ] }; // CreditNotes | Credit Notes with array of CreditNote object in body of request
let opts = {
  'summarizeErrors': true, // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.createCreditNotes(xeroTenantId, creditNotes, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNotes** | [**CreditNotes**](CreditNotes.md)| Credit Notes with array of CreditNote object in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCurrency

> Currencies createCurrency(xeroTenantId, currency)

Create a new currency for a Xero organisation

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let currency = { "Code": "USD", "Description": "United States Dollar" }; // Currency | Currency object in the body of request
apiInstance.createCurrency(xeroTenantId, currency, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **currency** | [**Currency**](Currency.md)| Currency object in the body of request | 

### Return type

[**Currencies**](Currencies.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEmployees

> Employees createEmployees(xeroTenantId, employees, opts)

Creates new employees used in Xero payrun

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let employees = { "Employees": [ { "FirstName": "Nick", "LastName": "Fury", "ExternalLink": { "Url": "http://twitter.com/#!/search/Nick+Fury" } } ] }; // Employees | Employees with array of Employee object in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.createEmployees(xeroTenantId, employees, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **employees** | [**Employees**](Employees.md)| Employees with array of Employee object in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createExpenseClaimHistory

> HistoryRecords createExpenseClaimHistory(xeroTenantId, expenseClaimID, historyRecords)

Creates a history record for a specific expense claim

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let expenseClaimID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ExpenseClaim
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createExpenseClaimHistory(xeroTenantId, expenseClaimID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **expenseClaimID** | **String**| Unique identifier for a ExpenseClaim | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createExpenseClaims

> ExpenseClaims createExpenseClaims(xeroTenantId, expenseClaims)

Creates expense claims

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let expenseClaims = { "ExpenseClaims": [ { "Status": "SUBMITTED", "User": { "UserID": "d1164823-0ac1-41ad-987b-b4e30fe0b273" }, "Receipts": [ { "Lineitems": [], "ReceiptID": "dc1c7f6d-0a4c-402f-acac-551d62ce5816" } ] } ] }; // ExpenseClaims | ExpenseClaims with array of ExpenseClaim object in body of request
apiInstance.createExpenseClaims(xeroTenantId, expenseClaims, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **expenseClaims** | [**ExpenseClaims**](ExpenseClaims.md)| ExpenseClaims with array of ExpenseClaim object in body of request | 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createInvoiceAttachmentByFileName

> Attachments createInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, body, opts)

Creates an attachment for a specific invoice or purchase bill by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
let fileName = "xero-dev.jpg"; // String | Name of the file you are attaching
let body = null; // Blob | Byte array of file in body of request
let opts = {
  'includeOnline': true // Boolean | Allows an attachment to be seen by the end customer within their online invoice
};
apiInstance.createInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, body, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 
 **fileName** | **String**| Name of the file you are attaching | 
 **body** | **Blob**| Byte array of file in body of request | 
 **includeOnline** | **Boolean**| Allows an attachment to be seen by the end customer within their online invoice | [optional] [default to false]

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createInvoiceHistory

> HistoryRecords createInvoiceHistory(xeroTenantId, invoiceID, historyRecords)

Creates a history record for a specific invoice

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createInvoiceHistory(xeroTenantId, invoiceID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createInvoices

> Invoices createInvoices(xeroTenantId, invoices, opts)

Creates one or more sales invoices or purchase bills

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoices = { "Invoices": [ { "Type": "ACCREC", "Contact": { "ContactID": "430fa14a-f945-44d3-9f97-5df5e28441b8" }, "LineItems": [ { "Description": "Acme Tires", "Quantity": 2, "UnitAmount": 20, "AccountCode": "200", "TaxType": "NONE", "LineAmount": 40 } ], "Date": "2019-03-11", "DueDate": "2018-12-10", "Reference": "Website Design", "Status": "AUTHORISED" } ] }; // Invoices | Invoices with an array of invoice objects in body of request
let opts = {
  'summarizeErrors': true, // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.createInvoices(xeroTenantId, invoices, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoices** | [**Invoices**](Invoices.md)| Invoices with an array of invoice objects in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createItemHistory

> HistoryRecords createItemHistory(xeroTenantId, itemID, historyRecords)

Creates a history record for a specific item

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let itemID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Item
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createItemHistory(xeroTenantId, itemID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **itemID** | **String**| Unique identifier for an Item | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createItems

> Items createItems(xeroTenantId, items, opts)

Creates one or more items

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let items = { "Items": [ { "Code": "code123", "Name": "Item Name XYZ", "Description": "Foobar", "InventoryAssetAccountCode": "140", "PurchaseDetails": { "COGSAccountCode": "500" } } ] }; // Items | Items with an array of Item objects in body of request
let opts = {
  'summarizeErrors': true, // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.createItems(xeroTenantId, items, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **items** | [**Items**](Items.md)| Items with an array of Item objects in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLinkedTransaction

> LinkedTransactions createLinkedTransaction(xeroTenantId, linkedTransaction)

Creates linked transactions (billable expenses)

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let linkedTransaction = { "LinkedTransactions": [ { "SourceTransactionID": "a848644a-f20f-4630-98c3-386bd7505631", "SourceLineItemID": "b0df260d-3cc8-4ced-9bd6-41924f624ed3" } ] }; // LinkedTransaction | LinkedTransaction object in body of request
apiInstance.createLinkedTransaction(xeroTenantId, linkedTransaction, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **linkedTransaction** | [**LinkedTransaction**](LinkedTransaction.md)| LinkedTransaction object in body of request | 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createManualJournalAttachmentByFileName

> Attachments createManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, body)

Creates a specific attachment for a specific manual journal by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournalID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ManualJournal
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to a ManualJournal
let body = null; // Blob | Byte array of file in body of request
apiInstance.createManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournalID** | **String**| Unique identifier for a ManualJournal | 
 **fileName** | **String**| The name of the file being attached to a ManualJournal | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createManualJournalHistoryRecord

> HistoryRecords createManualJournalHistoryRecord(xeroTenantId, manualJournalID, historyRecords)

Creates a history record for a specific manual journal

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournalID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a manual journal
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createManualJournalHistoryRecord(xeroTenantId, manualJournalID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournalID** | **String**| Xero generated unique identifier for a manual journal | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createManualJournals

> ManualJournals createManualJournals(xeroTenantId, manualJournals, opts)

Creates one or more manual journals

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournals = { "ManualJournals": [ { "Narration": "Journal Desc", "JournalLines": [ { "LineAmount": 100, "AccountCode": "400", "Description": "Money Movement" }, { "LineAmount": -100, "AccountCode": "400", "Description": "Prepayment of things", "Tracking": [ { "Name": "North", "Option": "Region" } ] } ], "Date": "2019-03-14" } ] }; // ManualJournals | ManualJournals array with ManualJournal object in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.createManualJournals(xeroTenantId, manualJournals, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournals** | [**ManualJournals**](ManualJournals.md)| ManualJournals array with ManualJournal object in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOverpaymentAllocations

> Allocations createOverpaymentAllocations(xeroTenantId, overpaymentID, allocations, opts)

Creates a single allocation for a specific overpayment

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let overpaymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Overpayment
let allocations = { "Allocations": [ { "Invoice": { "InvoiceID": "00000000-0000-0000-0000-000000000000", "LineItems": [], "Contact": {}, "Type": "ACCPAY" }, "Amount": 10.00, "Date": "2019-03-12" } ] }; // Allocations | Allocations array with Allocation object in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.createOverpaymentAllocations(xeroTenantId, overpaymentID, allocations, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **overpaymentID** | **String**| Unique identifier for a Overpayment | 
 **allocations** | [**Allocations**](Allocations.md)| Allocations array with Allocation object in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**Allocations**](Allocations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOverpaymentHistory

> HistoryRecords createOverpaymentHistory(xeroTenantId, overpaymentID, historyRecords)

Creates a history record for a specific overpayment

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let overpaymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Overpayment
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createOverpaymentHistory(xeroTenantId, overpaymentID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **overpaymentID** | **String**| Unique identifier for a Overpayment | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPayment

> Payments createPayment(xeroTenantId, payment)

Creates a single payment for invoice or credit notes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let payment = { "Payments": [ { "Invoice": { "LineItems": [], "InvoiceID": "00000000-0000-0000-0000-000000000000" }, "Account": { "Code": "970" }, "Date": "2019-03-12", "Amount": 1 } ] }; // Payment | Request body with a single Payment object
apiInstance.createPayment(xeroTenantId, payment, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **payment** | [**Payment**](Payment.md)| Request body with a single Payment object | 

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPaymentHistory

> HistoryRecords createPaymentHistory(xeroTenantId, paymentID, historyRecords)

Creates a history record for a specific payment

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let paymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Payment
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createPaymentHistory(xeroTenantId, paymentID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **paymentID** | **String**| Unique identifier for a Payment | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPaymentService

> PaymentServices createPaymentService(xeroTenantId, paymentServices)

Creates a payment service

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let paymentServices = { "PaymentServices": [ { "PaymentServiceName": "PayUpNow", "PaymentServiceUrl": "https://www.payupnow.com/", "PayNowText": "Time To Pay" } ] }; // PaymentServices | PaymentServices array with PaymentService object in body of request
apiInstance.createPaymentService(xeroTenantId, paymentServices, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **paymentServices** | [**PaymentServices**](PaymentServices.md)| PaymentServices array with PaymentService object in body of request | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPayments

> Payments createPayments(xeroTenantId, payments, opts)

Creates multiple payments for invoices or credit notes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let payments = { "Payments": [ { "Invoice": { "LineItems": [], "InvoiceID": "00000000-0000-0000-0000-000000000000" }, "Account": { "Code": "970" }, "Date": "2019-03-12", "Amount": 1 } ] }; // Payments | Payments array with Payment object in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.createPayments(xeroTenantId, payments, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **payments** | [**Payments**](Payments.md)| Payments array with Payment object in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPrepaymentAllocations

> Allocations createPrepaymentAllocations(xeroTenantId, prepaymentID, allocations, opts)

Allows you to create an Allocation for prepayments

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let prepaymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Prepayment
let allocations = { "Allocations": [ { "Invoice": { "LineItems": [], "InvoiceID": "00000000-0000-0000-0000-000000000000" }, "Amount": 1, "Date": "2019-01-10" } ] }; // Allocations | Allocations with an array of Allocation object in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.createPrepaymentAllocations(xeroTenantId, prepaymentID, allocations, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **prepaymentID** | **String**| Unique identifier for Prepayment | 
 **allocations** | [**Allocations**](Allocations.md)| Allocations with an array of Allocation object in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**Allocations**](Allocations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPrepaymentHistory

> HistoryRecords createPrepaymentHistory(xeroTenantId, prepaymentID, historyRecords)

Creates a history record for a specific prepayment

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let prepaymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a PrePayment
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createPrepaymentHistory(xeroTenantId, prepaymentID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **prepaymentID** | **String**| Unique identifier for a PrePayment | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPurchaseOrderAttachmentByFileName

> Attachments createPurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, body)

Creates attachment for a specific purchase order

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Purchase Order object
let fileName = "xero-dev.png"; // String | Name of the attachment
let body = null; // Blob | Byte array of file in body of request
apiInstance.createPurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderID** | **String**| Unique identifier for Purchase Order object | 
 **fileName** | **String**| Name of the attachment | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createPurchaseOrderHistory

> HistoryRecords createPurchaseOrderHistory(xeroTenantId, purchaseOrderID, historyRecords)

Creates a history record for a specific purchase orders

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a PurchaseOrder
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createPurchaseOrderHistory(xeroTenantId, purchaseOrderID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderID** | **String**| Unique identifier for a PurchaseOrder | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPurchaseOrders

> PurchaseOrders createPurchaseOrders(xeroTenantId, purchaseOrders, opts)

Creates one or more purchase orders

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrders = { "PurchaseOrders": [ { "Contact": { "ContactID": "00000000-0000-0000-0000-000000000000" }, "LineItems": [ { "Description": "Foobar", "Quantity": 1, "UnitAmount": 20, "AccountCode": "710" } ], "Date": "2019-03-13" } ] }; // PurchaseOrders | PurchaseOrders with an array of PurchaseOrder object in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.createPurchaseOrders(xeroTenantId, purchaseOrders, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrders** | [**PurchaseOrders**](PurchaseOrders.md)| PurchaseOrders with an array of PurchaseOrder object in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createQuoteAttachmentByFileName

> Attachments createQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, body)

Creates attachment for a specific quote

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Quote object
let fileName = "xero-dev.jpg"; // String | Name of the attachment
let body = null; // Blob | Byte array of file in body of request
apiInstance.createQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quoteID** | **String**| Unique identifier for Quote object | 
 **fileName** | **String**| Name of the attachment | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createQuoteHistory

> HistoryRecords createQuoteHistory(xeroTenantId, quoteID, historyRecords)

Creates a history record for a specific quote

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Quote
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createQuoteHistory(xeroTenantId, quoteID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quoteID** | **String**| Unique identifier for an Quote | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createQuotes

> Quotes createQuotes(xeroTenantId, quotes, opts)

Create one or more quotes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quotes = { "Quotes": [ { "Contact": { "ContactID": "00000000-0000-0000-0000-000000000000" }, "LineItems": [ { "Description": "Foobar", "Quantity": 1, "UnitAmount": 20, "AccountCode": "12775" } ], "Date": "2020-02-01" } ] }; // Quotes | Quotes with an array of Quote object in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.createQuotes(xeroTenantId, quotes, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quotes** | [**Quotes**](Quotes.md)| Quotes with an array of Quote object in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createReceipt

> Receipts createReceipt(xeroTenantId, receipts, opts)

Creates draft expense claim receipts for any user

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let receipts = { "Receipts": [ { "Contact": { "ContactID": "00000000-0000-0000-0000-000000000000" }, "Lineitems": [ { "Description": "Foobar", "Quantity": 2, "UnitAmount": 20, "AccountCode": "400", "TaxType": "NONE", "LineAmount": 40 } ], "User": { "UserID": "00000000-0000-0000-0000-000000000000" }, "LineAmountTypes": "NoTax", "Status": "DRAFT" } ] }; // Receipts | Receipts with an array of Receipt object in body of request
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.createReceipt(xeroTenantId, receipts, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **receipts** | [**Receipts**](Receipts.md)| Receipts with an array of Receipt object in body of request | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createReceiptAttachmentByFileName

> Attachments createReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, body)

Creates an attachment on a specific expense claim receipts by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let receiptID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Receipt
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to the Receipt
let body = null; // Blob | Byte array of file in body of request
apiInstance.createReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **receiptID** | **String**| Unique identifier for a Receipt | 
 **fileName** | **String**| The name of the file being attached to the Receipt | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createReceiptHistory

> HistoryRecords createReceiptHistory(xeroTenantId, receiptID, historyRecords)

Creates a history record for a specific receipt

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let receiptID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Receipt
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createReceiptHistory(xeroTenantId, receiptID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **receiptID** | **String**| Unique identifier for a Receipt | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRepeatingInvoiceAttachmentByFileName

> Attachments createRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, body)

Creates an attachment from a specific repeating invoices by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let repeatingInvoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Repeating Invoice
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Repeating Invoice
let body = null; // Blob | Byte array of file in body of request
apiInstance.createRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **repeatingInvoiceID** | **String**| Unique identifier for a Repeating Invoice | 
 **fileName** | **String**| The name of the file being attached to a Repeating Invoice | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## createRepeatingInvoiceHistory

> HistoryRecords createRepeatingInvoiceHistory(xeroTenantId, repeatingInvoiceID, historyRecords)

Creates a  history record for a specific repeating invoice

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let repeatingInvoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Repeating Invoice
let historyRecords = {   "HistoryRecords": [   {   "Details": "Hello World" } ] }; // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
apiInstance.createRepeatingInvoiceHistory(xeroTenantId, repeatingInvoiceID, historyRecords, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **repeatingInvoiceID** | **String**| Unique identifier for a Repeating Invoice | 
 **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTaxRates

> TaxRates createTaxRates(xeroTenantId, taxRates)

Creates one or more tax rates

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let taxRates = { "TaxRates": [ { "Name": "CA State Tax", "TaxComponents": [ { "Name": "State Tax", "Rate": 2.25 } ] } ] }; // TaxRates | TaxRates array with TaxRate object in body of request
apiInstance.createTaxRates(xeroTenantId, taxRates, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **taxRates** | [**TaxRates**](TaxRates.md)| TaxRates array with TaxRate object in body of request | 

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTrackingCategory

> TrackingCategories createTrackingCategory(xeroTenantId, trackingCategory)

Create tracking categories

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let trackingCategory = { name: "FooBar" }; // TrackingCategory | TrackingCategory object in body of request
apiInstance.createTrackingCategory(xeroTenantId, trackingCategory, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **trackingCategory** | [**TrackingCategory**](TrackingCategory.md)| TrackingCategory object in body of request | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTrackingOptions

> TrackingOptions createTrackingOptions(xeroTenantId, trackingCategoryID, trackingOption)

Creates options for a specific tracking category

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let trackingCategoryID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a TrackingCategory
let trackingOption = { name: " Bar" }; // TrackingOption | TrackingOption object in body of request
apiInstance.createTrackingOptions(xeroTenantId, trackingCategoryID, trackingOption, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **trackingCategoryID** | **String**| Unique identifier for a TrackingCategory | 
 **trackingOption** | [**TrackingOption**](TrackingOption.md)| TrackingOption object in body of request | 

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccount

> Accounts deleteAccount(xeroTenantId, accountID)

Deletes a chart of accounts

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let accountID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for retrieving single object
apiInstance.deleteAccount(xeroTenantId, accountID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **accountID** | **String**| Unique identifier for retrieving single object | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteContactGroupContact

> deleteContactGroupContact(xeroTenantId, contactGroupID, contactID)

Deletes a specific contact from a contact group using a unique contact Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactGroupID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact Group
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
apiInstance.deleteContactGroupContact(xeroTenantId, contactGroupID, contactID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactGroupID** | **String**| Unique identifier for a Contact Group | 
 **contactID** | **String**| Unique identifier for a Contact | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteContactGroupContacts

> deleteContactGroupContacts(xeroTenantId, contactGroupID)

Deletes all contacts from a specific contact group

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactGroupID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact Group
apiInstance.deleteContactGroupContacts(xeroTenantId, contactGroupID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactGroupID** | **String**| Unique identifier for a Contact Group | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteItem

> deleteItem(xeroTenantId, itemID)

Deletes a specific item

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let itemID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Item
apiInstance.deleteItem(xeroTenantId, itemID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **itemID** | **String**| Unique identifier for an Item | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLinkedTransaction

> deleteLinkedTransaction(xeroTenantId, linkedTransactionID)

Deletes a specific linked transactions (billable expenses)

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let linkedTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a LinkedTransaction
apiInstance.deleteLinkedTransaction(xeroTenantId, linkedTransactionID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **linkedTransactionID** | **String**| Unique identifier for a LinkedTransaction | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePayment

> Payments deletePayment(xeroTenantId, paymentID, paymentDelete)

Updates a specific payment for invoices and credit notes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let paymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Payment
let paymentDelete = {   "Payments":[   {   "Status":"DELETED" } ] }; // PaymentDelete | 
apiInstance.deletePayment(xeroTenantId, paymentID, paymentDelete, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **paymentID** | **String**| Unique identifier for a Payment | 
 **paymentDelete** | [**PaymentDelete**](PaymentDelete.md)|  | 

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTrackingCategory

> TrackingCategories deleteTrackingCategory(xeroTenantId, trackingCategoryID)

Deletes a specific tracking category

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let trackingCategoryID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a TrackingCategory
apiInstance.deleteTrackingCategory(xeroTenantId, trackingCategoryID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **trackingCategoryID** | **String**| Unique identifier for a TrackingCategory | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTrackingOptions

> TrackingOptions deleteTrackingOptions(xeroTenantId, trackingCategoryID, trackingOptionID)

Deletes a specific option for a specific tracking category

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let trackingCategoryID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a TrackingCategory
let trackingOptionID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Tracking Option
apiInstance.deleteTrackingOptions(xeroTenantId, trackingCategoryID, trackingOptionID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **trackingCategoryID** | **String**| Unique identifier for a TrackingCategory | 
 **trackingOptionID** | **String**| Unique identifier for a Tracking Option | 

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## emailInvoice

> emailInvoice(xeroTenantId, invoiceID, requestEmpty)

Sends a copy of a specific invoice to related contact via email

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
let requestEmpty = {}; // RequestEmpty | 
apiInstance.emailInvoice(xeroTenantId, invoiceID, requestEmpty, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 
 **requestEmpty** | [**RequestEmpty**](RequestEmpty.md)|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccount

> Accounts getAccount(xeroTenantId, accountID)

Retrieves a single chart of accounts by using a unique account Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let accountID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for retrieving single object
apiInstance.getAccount(xeroTenantId, accountID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **accountID** | **String**| Unique identifier for retrieving single object | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccountAttachmentByFileName

> File getAccountAttachmentByFileName(xeroTenantId, accountID, fileName, contentType)

Retrieves an attachment for a specific account by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let accountID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Account object
let fileName = "xero-dev.jpg"; // String | Name of the attachment
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getAccountAttachmentByFileName(xeroTenantId, accountID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **accountID** | **String**| Unique identifier for Account object | 
 **fileName** | **String**| Name of the attachment | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getAccountAttachmentById

> File getAccountAttachmentById(xeroTenantId, accountID, attachmentID, contentType)

Retrieves a specific attachment from a specific account using a unique attachment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let accountID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Account object
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Attachment object
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getAccountAttachmentById(xeroTenantId, accountID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **accountID** | **String**| Unique identifier for Account object | 
 **attachmentID** | **String**| Unique identifier for Attachment object | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getAccountAttachments

> Attachments getAccountAttachments(xeroTenantId, accountID)

Retrieves attachments for a specific accounts by using a unique account Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let accountID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Account object
apiInstance.getAccountAttachments(xeroTenantId, accountID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **accountID** | **String**| Unique identifier for Account object | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccounts

> Accounts getAccounts(xeroTenantId, opts)

Retrieves the full chart of accounts

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;", // String | Filter by an any element
  'order': "Name ASC" // String | Order by an any element
};
apiInstance.getAccounts(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBankTransaction

> BankTransactions getBankTransaction(xeroTenantId, bankTransactionID, opts)

Retrieves a single spent or received money transaction by using a unique bank transaction Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transaction
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getBankTransaction(xeroTenantId, bankTransactionID, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactionID** | **String**| Xero generated unique identifier for a bank transaction | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBankTransactionAttachmentByFileName

> File getBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, contentType)

Retrieves a specific attachment from a specific bank transaction by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transaction
let fileName = "xero-dev.jpg"; // String | The name of the file being attached
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactionID** | **String**| Xero generated unique identifier for a bank transaction | 
 **fileName** | **String**| The name of the file being attached | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getBankTransactionAttachmentById

> File getBankTransactionAttachmentById(xeroTenantId, bankTransactionID, attachmentID, contentType)

Retrieves specific attachments from a specific BankTransaction using a unique attachment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transaction
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for an attachment
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getBankTransactionAttachmentById(xeroTenantId, bankTransactionID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactionID** | **String**| Xero generated unique identifier for a bank transaction | 
 **attachmentID** | **String**| Xero generated unique identifier for an attachment | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getBankTransactionAttachments

> Attachments getBankTransactionAttachments(xeroTenantId, bankTransactionID)

Retrieves any attachments from a specific bank transactions

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transaction
apiInstance.getBankTransactionAttachments(xeroTenantId, bankTransactionID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactionID** | **String**| Xero generated unique identifier for a bank transaction | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBankTransactions

> BankTransactions getBankTransactions(xeroTenantId, opts)

Retrieves any spent or received money transactions

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"AUTHORISED\"", // String | Filter by an any element
  'order': "Type ASC", // String | Order by an any element
  'page': 1, // Number | Up to 100 bank transactions will be returned in a single API call with line items details
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getBankTransactions(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| Up to 100 bank transactions will be returned in a single API call with line items details | [optional] 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBankTransactionsHistory

> HistoryRecords getBankTransactionsHistory(xeroTenantId, bankTransactionID)

Retrieves history from a specific bank transaction using a unique bank transaction Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transaction
apiInstance.getBankTransactionsHistory(xeroTenantId, bankTransactionID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactionID** | **String**| Xero generated unique identifier for a bank transaction | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBankTransfer

> BankTransfers getBankTransfer(xeroTenantId, bankTransferID)

Retrieves specific bank transfers by using a unique bank transfer Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransferID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transfer
apiInstance.getBankTransfer(xeroTenantId, bankTransferID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransferID** | **String**| Xero generated unique identifier for a bank transfer | 

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBankTransferAttachmentByFileName

> File getBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, contentType)

Retrieves a specific attachment on a specific bank transfer by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransferID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transfer
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Bank Transfer
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransferID** | **String**| Xero generated unique identifier for a bank transfer | 
 **fileName** | **String**| The name of the file being attached to a Bank Transfer | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getBankTransferAttachmentById

> File getBankTransferAttachmentById(xeroTenantId, bankTransferID, attachmentID, contentType)

Retrieves a specific attachment from a specific bank transfer using a unique attachment ID

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransferID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transfer
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for an Attachment to a bank transfer
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getBankTransferAttachmentById(xeroTenantId, bankTransferID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransferID** | **String**| Xero generated unique identifier for a bank transfer | 
 **attachmentID** | **String**| Xero generated unique identifier for an Attachment to a bank transfer | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getBankTransferAttachments

> Attachments getBankTransferAttachments(xeroTenantId, bankTransferID)

Retrieves attachments from a specific bank transfer

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransferID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transfer
apiInstance.getBankTransferAttachments(xeroTenantId, bankTransferID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransferID** | **String**| Xero generated unique identifier for a bank transfer | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBankTransferHistory

> HistoryRecords getBankTransferHistory(xeroTenantId, bankTransferID)

Retrieves history from a specific bank transfer using a unique bank transfer Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransferID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transfer
apiInstance.getBankTransferHistory(xeroTenantId, bankTransferID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransferID** | **String**| Xero generated unique identifier for a bank transfer | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBankTransfers

> BankTransfers getBankTransfers(xeroTenantId, opts)

Retrieves all bank transfers

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "HasAttachments==true", // String | Filter by an any element
  'order': "Amount ASC" // String | Order by an any element
};
apiInstance.getBankTransfers(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBatchPaymentHistory

> HistoryRecords getBatchPaymentHistory(xeroTenantId, batchPaymentID)

Retrieves history from a specific batch payment

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let batchPaymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for BatchPayment
apiInstance.getBatchPaymentHistory(xeroTenantId, batchPaymentID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **batchPaymentID** | **String**| Unique identifier for BatchPayment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBatchPayments

> BatchPayments getBatchPayments(xeroTenantId, opts)

Retrieves either one or many batch payments for invoices

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"AUTHORISED\"", // String | Filter by an any element
  'order': "Date ASC" // String | Order by an any element
};
apiInstance.getBatchPayments(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 

### Return type

[**BatchPayments**](BatchPayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBrandingTheme

> BrandingThemes getBrandingTheme(xeroTenantId, brandingThemeID)

Retrieves a specific branding theme using a unique branding theme Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let brandingThemeID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Branding Theme
apiInstance.getBrandingTheme(xeroTenantId, brandingThemeID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **brandingThemeID** | **String**| Unique identifier for a Branding Theme | 

### Return type

[**BrandingThemes**](BrandingThemes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBrandingThemePaymentServices

> PaymentServices getBrandingThemePaymentServices(xeroTenantId, brandingThemeID)

Retrieves the payment services for a specific branding theme

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let brandingThemeID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Branding Theme
apiInstance.getBrandingThemePaymentServices(xeroTenantId, brandingThemeID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **brandingThemeID** | **String**| Unique identifier for a Branding Theme | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBrandingThemes

> BrandingThemes getBrandingThemes(xeroTenantId)

Retrieves all the branding themes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
apiInstance.getBrandingThemes(xeroTenantId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 

### Return type

[**BrandingThemes**](BrandingThemes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContact

> Contacts getContact(xeroTenantId, contactID)

Retrieves a specific contacts in a Xero organisation using a unique contact Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
apiInstance.getContact(xeroTenantId, contactID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactID** | **String**| Unique identifier for a Contact | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactAttachmentByFileName

> File getContactAttachmentByFileName(xeroTenantId, contactID, fileName, contentType)

Retrieves a specific attachment from a specific contact by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
let fileName = "xero-dev.jpg"; // String | Name for the file you are attaching
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getContactAttachmentByFileName(xeroTenantId, contactID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactID** | **String**| Unique identifier for a Contact | 
 **fileName** | **String**| Name for the file you are attaching | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getContactAttachmentById

> File getContactAttachmentById(xeroTenantId, contactID, attachmentID, contentType)

Retrieves a specific attachment from a specific contact using a unique attachment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Attachment
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getContactAttachmentById(xeroTenantId, contactID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactID** | **String**| Unique identifier for a Contact | 
 **attachmentID** | **String**| Unique identifier for a Attachment | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getContactAttachments

> Attachments getContactAttachments(xeroTenantId, contactID)

Retrieves attachments for a specific contact in a Xero organisation

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
apiInstance.getContactAttachments(xeroTenantId, contactID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactID** | **String**| Unique identifier for a Contact | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactByContactNumber

> Contacts getContactByContactNumber(xeroTenantId, contactNumber)

Retrieves a specific contact by contact number in a Xero organisation

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactNumber = "SB2"; // String | This field is read only on the Xero contact screen, used to identify contacts in external systems (max length = 50).
apiInstance.getContactByContactNumber(xeroTenantId, contactNumber, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactNumber** | **String**| This field is read only on the Xero contact screen, used to identify contacts in external systems (max length &#x3D; 50). | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactCISSettings

> CISSettings getContactCISSettings(xeroTenantId, contactID)

Retrieves CIS settings for a specific contact in a Xero organisation

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
apiInstance.getContactCISSettings(xeroTenantId, contactID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactID** | **String**| Unique identifier for a Contact | 

### Return type

[**CISSettings**](CISSettings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactGroup

> ContactGroups getContactGroup(xeroTenantId, contactGroupID)

Retrieves a specific contact group by using a unique contact group Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactGroupID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact Group
apiInstance.getContactGroup(xeroTenantId, contactGroupID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactGroupID** | **String**| Unique identifier for a Contact Group | 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactGroups

> ContactGroups getContactGroups(xeroTenantId, opts)

Retrieves the contact Id and name of all the contacts in a contact group

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "Name ASC" // String | Order by an any element
};
apiInstance.getContactGroups(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactHistory

> HistoryRecords getContactHistory(xeroTenantId, contactID)

Retrieves history records for a specific contact

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
apiInstance.getContactHistory(xeroTenantId, contactID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactID** | **String**| Unique identifier for a Contact | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContacts

> Contacts getContacts(xeroTenantId, opts)

Retrieves all contacts in a Xero organisation

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "ContactStatus==&quot;ACTIVE&quot;", // String | Filter by an any element
  'order': "Name ASC", // String | Order by an any element
  'iDs': ["null"], // [String] | Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call.
  'page': 1, // Number | e.g. page=1 - Up to 100 contacts will be returned in a single API call.
  'includeArchived': true // Boolean | e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response
};
apiInstance.getContacts(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **iDs** | [**[String]**](String.md)| Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call. | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 - Up to 100 contacts will be returned in a single API call. | [optional] 
 **includeArchived** | **Boolean**| e.g. includeArchived&#x3D;true - Contacts with a status of ARCHIVED will be included in the response | [optional] 

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCreditNote

> CreditNotes getCreditNote(xeroTenantId, creditNoteID, opts)

Retrieves a specific credit note using a unique credit note Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getCreditNote(xeroTenantId, creditNoteID, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCreditNoteAsPdf

> File getCreditNoteAsPdf(xeroTenantId, creditNoteID)

Retrieves credit notes as PDF files

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
apiInstance.getCreditNoteAsPdf(xeroTenantId, creditNoteID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf


## getCreditNoteAttachmentByFileName

> File getCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, contentType)

Retrieves a specific attachment on a specific credit note by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
let fileName = "xero-dev.jpg"; // String | Name of the file you are attaching to Credit Note
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 
 **fileName** | **String**| Name of the file you are attaching to Credit Note | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getCreditNoteAttachmentById

> File getCreditNoteAttachmentById(xeroTenantId, creditNoteID, attachmentID, contentType)

Retrieves a specific attachment from a specific credit note using a unique attachment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Attachment
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getCreditNoteAttachmentById(xeroTenantId, creditNoteID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 
 **attachmentID** | **String**| Unique identifier for a Attachment | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getCreditNoteAttachments

> Attachments getCreditNoteAttachments(xeroTenantId, creditNoteID)

Retrieves attachments for a specific credit notes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
apiInstance.getCreditNoteAttachments(xeroTenantId, creditNoteID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCreditNoteHistory

> HistoryRecords getCreditNoteHistory(xeroTenantId, creditNoteID)

Retrieves history records of a specific credit note

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
apiInstance.getCreditNoteHistory(xeroTenantId, creditNoteID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCreditNotes

> CreditNotes getCreditNotes(xeroTenantId, opts)

Retrieves any credit notes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"DRAFT\"", // String | Filter by an any element
  'order': "CreditNoteNumber ASC", // String | Order by an any element
  'page': 1, // Number | e.g. page=1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getCreditNotes(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note | [optional] 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCurrencies

> Currencies getCurrencies(xeroTenantId, opts)

Retrieves currencies for your Xero organisation

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'where': "Code==\"USD\"", // String | Filter by an any element
  'order': "Code ASC" // String | Order by an any element
};
apiInstance.getCurrencies(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 

### Return type

[**Currencies**](Currencies.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployee

> Employees getEmployee(xeroTenantId, employeeID)

Retrieves a specific employee used in Xero payrun using a unique employee Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let employeeID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Employee
apiInstance.getEmployee(xeroTenantId, employeeID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **employeeID** | **String**| Unique identifier for a Employee | 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployees

> Employees getEmployees(xeroTenantId, opts)

Retrieves employees used in Xero payrun

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "LastName ASC" // String | Order by an any element
};
apiInstance.getEmployees(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExpenseClaim

> ExpenseClaims getExpenseClaim(xeroTenantId, expenseClaimID)

Retrieves a specific expense claim using a unique expense claim Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let expenseClaimID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ExpenseClaim
apiInstance.getExpenseClaim(xeroTenantId, expenseClaimID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **expenseClaimID** | **String**| Unique identifier for a ExpenseClaim | 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExpenseClaimHistory

> HistoryRecords getExpenseClaimHistory(xeroTenantId, expenseClaimID)

Retrieves history records of a specific expense claim

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let expenseClaimID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ExpenseClaim
apiInstance.getExpenseClaimHistory(xeroTenantId, expenseClaimID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **expenseClaimID** | **String**| Unique identifier for a ExpenseClaim | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExpenseClaims

> ExpenseClaims getExpenseClaims(xeroTenantId, opts)

Retrieves expense claims

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"SUBMITTED\"", // String | Filter by an any element
  'order': "Status ASC" // String | Order by an any element
};
apiInstance.getExpenseClaims(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoice

> Invoices getInvoice(xeroTenantId, invoiceID, opts)

Retrieves a specific sales invoice or purchase bill using a unique invoice Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getInvoice(xeroTenantId, invoiceID, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceAsPdf

> File getInvoiceAsPdf(xeroTenantId, invoiceID)

Retrieves invoices or purchase bills as PDF files

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
apiInstance.getInvoiceAsPdf(xeroTenantId, invoiceID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf


## getInvoiceAttachmentByFileName

> File getInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, contentType)

Retrieves an attachment from a specific invoice or purchase bill by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
let fileName = "xero-dev.jpg"; // String | Name of the file you are attaching
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 
 **fileName** | **String**| Name of the file you are attaching | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getInvoiceAttachmentById

> File getInvoiceAttachmentById(xeroTenantId, invoiceID, attachmentID, contentType)

Retrieves a specific attachment from a specific invoices or purchase bills by using a unique attachment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Attachment
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getInvoiceAttachmentById(xeroTenantId, invoiceID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 
 **attachmentID** | **String**| Unique identifier for an Attachment | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getInvoiceAttachments

> Attachments getInvoiceAttachments(xeroTenantId, invoiceID)

Retrieves attachments for a specific invoice or purchase bill

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
apiInstance.getInvoiceAttachments(xeroTenantId, invoiceID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceHistory

> HistoryRecords getInvoiceHistory(xeroTenantId, invoiceID)

Retrieves history records for a specific invoice

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
apiInstance.getInvoiceHistory(xeroTenantId, invoiceID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoiceReminders

> InvoiceReminders getInvoiceReminders(xeroTenantId)

Retrieves invoice reminder settings

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
apiInstance.getInvoiceReminders(xeroTenantId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 

### Return type

[**InvoiceReminders**](InvoiceReminders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvoices

> Invoices getInvoices(xeroTenantId, opts)

Retrieves sales invoices or purchase bills

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"DRAFT\"", // String | Filter by an any element
  'order': "InvoiceNumber ASC", // String | Order by an any element
  'iDs': ["null"], // [String] | Filter by a comma-separated list of InvoicesIDs.
  'invoiceNumbers': ["null"], // [String] | Filter by a comma-separated list of InvoiceNumbers.
  'contactIDs': ["null"], // [String] | Filter by a comma-separated list of ContactIDs.
  'statuses': ["null"], // [String] | Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter.
  'page': 1, // Number | e.g. page=1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice
  'includeArchived': true, // Boolean | e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response
  'createdByMyApp': false, // Boolean | When set to true you'll only retrieve Invoices created by your app
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getInvoices(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **iDs** | [**[String]**](String.md)| Filter by a comma-separated list of InvoicesIDs. | [optional] 
 **invoiceNumbers** | [**[String]**](String.md)| Filter by a comma-separated list of InvoiceNumbers. | [optional] 
 **contactIDs** | [**[String]**](String.md)| Filter by a comma-separated list of ContactIDs. | [optional] 
 **statuses** | [**[String]**](String.md)| Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice | [optional] 
 **includeArchived** | **Boolean**| e.g. includeArchived&#x3D;true - Contacts with a status of ARCHIVED will be included in the response | [optional] 
 **createdByMyApp** | **Boolean**| When set to true you&#39;ll only retrieve Invoices created by your app | [optional] 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItem

> Items getItem(xeroTenantId, itemID, opts)

Retrieves a specific item using a unique item Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let itemID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Item
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getItem(xeroTenantId, itemID, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **itemID** | **String**| Unique identifier for an Item | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemHistory

> HistoryRecords getItemHistory(xeroTenantId, itemID)

Retrieves history for a specific item

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let itemID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Item
apiInstance.getItemHistory(xeroTenantId, itemID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **itemID** | **String**| Unique identifier for an Item | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItems

> Items getItems(xeroTenantId, opts)

Retrieves items

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "IsSold==true", // String | Filter by an any element
  'order': "Code ASC", // String | Order by an any element
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getItems(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJournal

> Journals getJournal(xeroTenantId, journalID)

Retrieves a specific journal using a unique journal Id.

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let journalID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Journal
apiInstance.getJournal(xeroTenantId, journalID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **journalID** | **String**| Unique identifier for a Journal | 

### Return type

[**Journals**](Journals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJournals

> Journals getJournals(xeroTenantId, opts)

Retrieves journals

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'offset': 10, // Number | Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned
  'paymentsOnly': true // Boolean | Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default.
};
apiInstance.getJournals(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **offset** | **Number**| Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned | [optional] 
 **paymentsOnly** | **Boolean**| Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default. | [optional] 

### Return type

[**Journals**](Journals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinkedTransaction

> LinkedTransactions getLinkedTransaction(xeroTenantId, linkedTransactionID)

Retrieves a specific linked transaction (billable expenses) using a unique linked transaction Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let linkedTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a LinkedTransaction
apiInstance.getLinkedTransaction(xeroTenantId, linkedTransactionID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **linkedTransactionID** | **String**| Unique identifier for a LinkedTransaction | 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinkedTransactions

> LinkedTransactions getLinkedTransactions(xeroTenantId, opts)

Retrieves linked transactions (billable expenses)

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'page': 1, // Number | Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page=1.
  'linkedTransactionID': "00000000-0000-0000-0000-000000000000", // String | The Xero identifier for an Linked Transaction
  'sourceTransactionID': "00000000-0000-0000-0000-000000000000", // String | Filter by the SourceTransactionID. Get the linked transactions created from a particular ACCPAY invoice
  'contactID': "00000000-0000-0000-0000-000000000000", // String | Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer.
  'status': "APPROVED", // String | Filter by the combination of ContactID and Status. Get  the linked transactions associated to a  customer and with a status
  'targetTransactionID': "00000000-0000-0000-0000-000000000000" // String | Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice
};
apiInstance.getLinkedTransactions(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **page** | **Number**| Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page&#x3D;1. | [optional] 
 **linkedTransactionID** | **String**| The Xero identifier for an Linked Transaction | [optional] 
 **sourceTransactionID** | **String**| Filter by the SourceTransactionID. Get the linked transactions created from a particular ACCPAY invoice | [optional] 
 **contactID** | **String**| Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer. | [optional] 
 **status** | **String**| Filter by the combination of ContactID and Status. Get  the linked transactions associated to a  customer and with a status | [optional] 
 **targetTransactionID** | **String**| Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice | [optional] 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManualJournal

> ManualJournals getManualJournal(xeroTenantId, manualJournalID)

Retrieves a specific manual journal

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournalID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ManualJournal
apiInstance.getManualJournal(xeroTenantId, manualJournalID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournalID** | **String**| Unique identifier for a ManualJournal | 

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManualJournalAttachmentByFileName

> File getManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, contentType)

Retrieves a specific attachment from a specific manual journal by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournalID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ManualJournal
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to a ManualJournal
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournalID** | **String**| Unique identifier for a ManualJournal | 
 **fileName** | **String**| The name of the file being attached to a ManualJournal | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getManualJournalAttachmentById

> File getManualJournalAttachmentById(xeroTenantId, manualJournalID, attachmentID, contentType)

Allows you to retrieve a specific attachment from a specific manual journal using a unique attachment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournalID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ManualJournal
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Attachment
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getManualJournalAttachmentById(xeroTenantId, manualJournalID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournalID** | **String**| Unique identifier for a ManualJournal | 
 **attachmentID** | **String**| Unique identifier for a Attachment | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getManualJournalAttachments

> Attachments getManualJournalAttachments(xeroTenantId, manualJournalID)

Retrieves attachment for a specific manual journal

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournalID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ManualJournal
apiInstance.getManualJournalAttachments(xeroTenantId, manualJournalID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournalID** | **String**| Unique identifier for a ManualJournal | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManualJournals

> ManualJournals getManualJournals(xeroTenantId, opts)

Retrieves manual journals

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"DRAFT\"", // String | Filter by an any element
  'order': "Date ASC", // String | Order by an any element
  'page': 1 // Number | e.g. page=1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment
};
apiInstance.getManualJournals(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment | [optional] 

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManualJournalsHistory

> HistoryRecords getManualJournalsHistory(xeroTenantId, manualJournalID)

Retrieves history for a specific manual journal

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournalID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a manual journal
apiInstance.getManualJournalsHistory(xeroTenantId, manualJournalID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournalID** | **String**| Xero generated unique identifier for a manual journal | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOnlineInvoice

> OnlineInvoices getOnlineInvoice(xeroTenantId, invoiceID)

Retrieves a URL to an online invoice

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
apiInstance.getOnlineInvoice(xeroTenantId, invoiceID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 

### Return type

[**OnlineInvoices**](OnlineInvoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationActions

> Actions getOrganisationActions(xeroTenantId)

Retrieves a list of the key actions your app has permission to perform in the connected Xero organisation.

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
apiInstance.getOrganisationActions(xeroTenantId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 

### Return type

[**Actions**](Actions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisationCISSettings

> CISOrgSettings getOrganisationCISSettings(xeroTenantId, organisationID)

Retrieves the CIS settings for the Xero organistaion.

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let organisationID = "00000000-0000-0000-0000-000000000000"; // String | The unique Xero identifier for an organisation
apiInstance.getOrganisationCISSettings(xeroTenantId, organisationID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **organisationID** | **String**| The unique Xero identifier for an organisation | 

### Return type

[**CISOrgSettings**](CISOrgSettings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganisations

> Organisations getOrganisations(xeroTenantId)

Retrieves Xero organisation details

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
apiInstance.getOrganisations(xeroTenantId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 

### Return type

[**Organisations**](Organisations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOverpayment

> Overpayments getOverpayment(xeroTenantId, overpaymentID)

Retrieves a specific overpayment using a unique overpayment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let overpaymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Overpayment
apiInstance.getOverpayment(xeroTenantId, overpaymentID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **overpaymentID** | **String**| Unique identifier for a Overpayment | 

### Return type

[**Overpayments**](Overpayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOverpaymentHistory

> HistoryRecords getOverpaymentHistory(xeroTenantId, overpaymentID)

Retrieves history records of a specific overpayment

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let overpaymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Overpayment
apiInstance.getOverpaymentHistory(xeroTenantId, overpaymentID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **overpaymentID** | **String**| Unique identifier for a Overpayment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOverpayments

> Overpayments getOverpayments(xeroTenantId, opts)

Retrieves overpayments

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"AUTHORISED\"", // String | Filter by an any element
  'order': "Status ASC", // String | Order by an any element
  'page': 1, // Number | e.g. page=1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getOverpayments(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment | [optional] 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Overpayments**](Overpayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayment

> Payments getPayment(xeroTenantId, paymentID)

Retrieves a specific payment for invoices and credit notes using a unique payment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let paymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Payment
apiInstance.getPayment(xeroTenantId, paymentID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **paymentID** | **String**| Unique identifier for a Payment | 

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPaymentHistory

> HistoryRecords getPaymentHistory(xeroTenantId, paymentID)

Retrieves history records of a specific payment

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let paymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Payment
apiInstance.getPaymentHistory(xeroTenantId, paymentID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **paymentID** | **String**| Unique identifier for a Payment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPaymentServices

> PaymentServices getPaymentServices(xeroTenantId)

Retrieves payment services

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
apiInstance.getPaymentServices(xeroTenantId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayments

> Payments getPayments(xeroTenantId, opts)

Retrieves payments for invoices and credit notes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"AUTHORISED\"", // String | Filter by an any element
  'order': "Amount ASC", // String | Order by an any element
  'page': 1 // Number | Up to 100 payments will be returned in a single API call
};
apiInstance.getPayments(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| Up to 100 payments will be returned in a single API call | [optional] 

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPrepayment

> Prepayments getPrepayment(xeroTenantId, prepaymentID)

Allows you to retrieve a specified prepayments

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let prepaymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a PrePayment
apiInstance.getPrepayment(xeroTenantId, prepaymentID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **prepaymentID** | **String**| Unique identifier for a PrePayment | 

### Return type

[**Prepayments**](Prepayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPrepaymentHistory

> HistoryRecords getPrepaymentHistory(xeroTenantId, prepaymentID)

Retrieves history record for a specific prepayment

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let prepaymentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a PrePayment
apiInstance.getPrepaymentHistory(xeroTenantId, prepaymentID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **prepaymentID** | **String**| Unique identifier for a PrePayment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPrepayments

> Prepayments getPrepayments(xeroTenantId, opts)

Retrieves prepayments

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"AUTHORISED\"", // String | Filter by an any element
  'order': "Reference ASC", // String | Order by an any element
  'page': 1, // Number | e.g. page=1 – Up to 100 prepayments will be returned in a single API call with line items shown for each overpayment
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getPrepayments(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 prepayments will be returned in a single API call with line items shown for each overpayment | [optional] 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Prepayments**](Prepayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPurchaseOrder

> PurchaseOrders getPurchaseOrder(xeroTenantId, purchaseOrderID)

Retrieves a specific purchase order using a unique purchase order Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a PurchaseOrder
apiInstance.getPurchaseOrder(xeroTenantId, purchaseOrderID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderID** | **String**| Unique identifier for a PurchaseOrder | 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPurchaseOrderAsPdf

> File getPurchaseOrderAsPdf(xeroTenantId, purchaseOrderID)

Retrieves specific purchase order as PDF files using a unique purchase order Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Purchase Order
apiInstance.getPurchaseOrderAsPdf(xeroTenantId, purchaseOrderID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderID** | **String**| Unique identifier for an Purchase Order | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf


## getPurchaseOrderAttachmentByFileName

> File getPurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, contentType)

Retrieves a specific attachment for a specific purchase order by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Purchase Order object
let fileName = "xero-dev.jpg"; // String | Name of the attachment
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getPurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderID** | **String**| Unique identifier for Purchase Order object | 
 **fileName** | **String**| Name of the attachment | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getPurchaseOrderAttachmentById

> File getPurchaseOrderAttachmentById(xeroTenantId, purchaseOrderID, attachmentID, contentType)

Retrieves specific attachment for a specific purchase order using a unique attachment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Purchase Order object
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Attachment object
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getPurchaseOrderAttachmentById(xeroTenantId, purchaseOrderID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderID** | **String**| Unique identifier for Purchase Order object | 
 **attachmentID** | **String**| Unique identifier for Attachment object | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getPurchaseOrderAttachments

> Attachments getPurchaseOrderAttachments(xeroTenantId, purchaseOrderID)

Retrieves attachments for a specific purchase order

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Purchase Orders object
apiInstance.getPurchaseOrderAttachments(xeroTenantId, purchaseOrderID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderID** | **String**| Unique identifier for Purchase Orders object | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPurchaseOrderByNumber

> PurchaseOrders getPurchaseOrderByNumber(xeroTenantId, purchaseOrderNumber)

Retrieves a specific purchase order using purchase order number

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderNumber = "PO1234"; // String | Unique identifier for a PurchaseOrder
apiInstance.getPurchaseOrderByNumber(xeroTenantId, purchaseOrderNumber, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderNumber** | **String**| Unique identifier for a PurchaseOrder | 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPurchaseOrderHistory

> HistoryRecords getPurchaseOrderHistory(xeroTenantId, purchaseOrderID)

Retrieves history for a specific purchase order

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a PurchaseOrder
apiInstance.getPurchaseOrderHistory(xeroTenantId, purchaseOrderID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderID** | **String**| Unique identifier for a PurchaseOrder | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPurchaseOrders

> PurchaseOrders getPurchaseOrders(xeroTenantId, opts)

Retrieves purchase orders

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'status': "SUBMITTED", // String | Filter by purchase order status
  'dateFrom': "2019-12-01", // String | Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31
  'dateTo': "2019-12-31", // String | Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31
  'order': "PurchaseOrderNumber ASC", // String | Order by an any element
  'page': 1 // Number | To specify a page, append the page parameter to the URL e.g. ?page=1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page=2 and continuing this process until no more results are returned.
};
apiInstance.getPurchaseOrders(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **status** | **String**| Filter by purchase order status | [optional] 
 **dateFrom** | **String**| Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom&#x3D;2015-12-01&amp;DateTo&#x3D;2015-12-31 | [optional] 
 **dateTo** | **String**| Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom&#x3D;2015-12-01&amp;DateTo&#x3D;2015-12-31 | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| To specify a page, append the page parameter to the URL e.g. ?page&#x3D;1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page&#x3D;2 and continuing this process until no more results are returned. | [optional] 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQuote

> Quotes getQuote(xeroTenantId, quoteID)

Retrieves a specific quote using a unique quote Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Quote
apiInstance.getQuote(xeroTenantId, quoteID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quoteID** | **String**| Unique identifier for an Quote | 

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQuoteAsPdf

> File getQuoteAsPdf(xeroTenantId, quoteID)

Retrieves a specific quote as a PDF file using a unique quote Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Quote
apiInstance.getQuoteAsPdf(xeroTenantId, quoteID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quoteID** | **String**| Unique identifier for an Quote | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf


## getQuoteAttachmentByFileName

> File getQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, contentType)

Retrieves a specific attachment from a specific quote by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Quote object
let fileName = "xero-dev.jpg"; // String | Name of the attachment
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quoteID** | **String**| Unique identifier for Quote object | 
 **fileName** | **String**| Name of the attachment | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getQuoteAttachmentById

> File getQuoteAttachmentById(xeroTenantId, quoteID, attachmentID, contentType)

Retrieves a specific attachment from a specific quote using a unique attachment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Quote object
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Attachment object
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getQuoteAttachmentById(xeroTenantId, quoteID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quoteID** | **String**| Unique identifier for Quote object | 
 **attachmentID** | **String**| Unique identifier for Attachment object | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getQuoteAttachments

> Attachments getQuoteAttachments(xeroTenantId, quoteID)

Retrieves attachments for a specific quote

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Quote object
apiInstance.getQuoteAttachments(xeroTenantId, quoteID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quoteID** | **String**| Unique identifier for Quote object | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQuoteHistory

> HistoryRecords getQuoteHistory(xeroTenantId, quoteID)

Retrieves history records of a specific quote

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Quote
apiInstance.getQuoteHistory(xeroTenantId, quoteID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quoteID** | **String**| Unique identifier for an Quote | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQuotes

> Quotes getQuotes(xeroTenantId, opts)

Retrieves sales quotes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'dateFrom': new Date("2013-10-20"), // Date | Filter for quotes after a particular date
  'dateTo': new Date("2013-10-20"), // Date | Filter for quotes before a particular date
  'expiryDateFrom': new Date("2013-10-20"), // Date | Filter for quotes expiring after a particular date
  'expiryDateTo': new Date("2013-10-20"), // Date | Filter for quotes before a particular date
  'contactID': "00000000-0000-0000-0000-000000000000", // String | Filter for quotes belonging to a particular contact
  'status': "DRAFT", // String | Filter for quotes of a particular Status
  'page': 1, // Number | e.g. page=1 – Up to 100 Quotes will be returned in a single API call with line items shown for each quote
  'order': "Status ASC", // String | Order by an any element
  'quoteNumber': "QU-0001" // String | Filter by quote number (e.g. GET https://.../Quotes?QuoteNumber=QU-0001)
};
apiInstance.getQuotes(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **dateFrom** | **Date**| Filter for quotes after a particular date | [optional] 
 **dateTo** | **Date**| Filter for quotes before a particular date | [optional] 
 **expiryDateFrom** | **Date**| Filter for quotes expiring after a particular date | [optional] 
 **expiryDateTo** | **Date**| Filter for quotes before a particular date | [optional] 
 **contactID** | **String**| Filter for quotes belonging to a particular contact | [optional] 
 **status** | **String**| Filter for quotes of a particular Status | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 Quotes will be returned in a single API call with line items shown for each quote | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **quoteNumber** | **String**| Filter by quote number (e.g. GET https://.../Quotes?QuoteNumber&#x3D;QU-0001) | [optional] 

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReceipt

> Receipts getReceipt(xeroTenantId, receiptID, opts)

Retrieves a specific draft expense claim receipt by using a unique receipt Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let receiptID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Receipt
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getReceipt(xeroTenantId, receiptID, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **receiptID** | **String**| Unique identifier for a Receipt | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReceiptAttachmentByFileName

> File getReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, contentType)

Retrieves a specific attachment from a specific expense claim receipts by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let receiptID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Receipt
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to the Receipt
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **receiptID** | **String**| Unique identifier for a Receipt | 
 **fileName** | **String**| The name of the file being attached to the Receipt | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getReceiptAttachmentById

> File getReceiptAttachmentById(xeroTenantId, receiptID, attachmentID, contentType)

Retrieves a specific attachments from a specific expense claim receipts by using a unique attachment Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let receiptID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Receipt
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Attachment
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getReceiptAttachmentById(xeroTenantId, receiptID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **receiptID** | **String**| Unique identifier for a Receipt | 
 **attachmentID** | **String**| Unique identifier for a Attachment | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getReceiptAttachments

> Attachments getReceiptAttachments(xeroTenantId, receiptID)

Retrieves attachments for a specific expense claim receipt

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let receiptID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Receipt
apiInstance.getReceiptAttachments(xeroTenantId, receiptID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **receiptID** | **String**| Unique identifier for a Receipt | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReceiptHistory

> HistoryRecords getReceiptHistory(xeroTenantId, receiptID)

Retrieves a history record for a specific receipt

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let receiptID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Receipt
apiInstance.getReceiptHistory(xeroTenantId, receiptID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **receiptID** | **String**| Unique identifier for a Receipt | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReceipts

> Receipts getReceipts(xeroTenantId, opts)

Retrieves draft expense claim receipts for any user

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "Status==\"DRAFT\"", // String | Filter by an any element
  'order': "ReceiptNumber ASC", // String | Order by an any element
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.getReceipts(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepeatingInvoice

> RepeatingInvoices getRepeatingInvoice(xeroTenantId, repeatingInvoiceID)

Retrieves a specific repeating invoice by using a unique repeating invoice Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let repeatingInvoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Repeating Invoice
apiInstance.getRepeatingInvoice(xeroTenantId, repeatingInvoiceID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **repeatingInvoiceID** | **String**| Unique identifier for a Repeating Invoice | 

### Return type

[**RepeatingInvoices**](RepeatingInvoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepeatingInvoiceAttachmentByFileName

> File getRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, contentType)

Retrieves a specific attachment from a specific repeating invoices by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let repeatingInvoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Repeating Invoice
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Repeating Invoice
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **repeatingInvoiceID** | **String**| Unique identifier for a Repeating Invoice | 
 **fileName** | **String**| The name of the file being attached to a Repeating Invoice | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getRepeatingInvoiceAttachmentById

> File getRepeatingInvoiceAttachmentById(xeroTenantId, repeatingInvoiceID, attachmentID, contentType)

Retrieves a specific attachment from a specific repeating invoice

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let repeatingInvoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Repeating Invoice
let attachmentID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Attachment
let contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
apiInstance.getRepeatingInvoiceAttachmentById(xeroTenantId, repeatingInvoiceID, attachmentID, contentType, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **repeatingInvoiceID** | **String**| Unique identifier for a Repeating Invoice | 
 **attachmentID** | **String**| Unique identifier for a Attachment | 
 **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**File**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getRepeatingInvoiceAttachments

> Attachments getRepeatingInvoiceAttachments(xeroTenantId, repeatingInvoiceID)

Retrieves attachments from a specific repeating invoice

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let repeatingInvoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Repeating Invoice
apiInstance.getRepeatingInvoiceAttachments(xeroTenantId, repeatingInvoiceID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **repeatingInvoiceID** | **String**| Unique identifier for a Repeating Invoice | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepeatingInvoiceHistory

> HistoryRecords getRepeatingInvoiceHistory(xeroTenantId, repeatingInvoiceID)

Retrieves history record for a specific repeating invoice

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let repeatingInvoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Repeating Invoice
apiInstance.getRepeatingInvoiceHistory(xeroTenantId, repeatingInvoiceID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **repeatingInvoiceID** | **String**| Unique identifier for a Repeating Invoice | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepeatingInvoices

> RepeatingInvoices getRepeatingInvoices(xeroTenantId, opts)

Retrieves repeating invoices

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'where': "Status==\"DRAFT\"", // String | Filter by an any element
  'order': "Total ASC" // String | Order by an any element
};
apiInstance.getRepeatingInvoices(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 

### Return type

[**RepeatingInvoices**](RepeatingInvoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportAgedPayablesByContact

> ReportWithRows getReportAgedPayablesByContact(xeroTenantId, contactId, opts)

Retrieves report for aged payables by contact

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactId = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
let opts = {
  'date': new Date("2013-10-20"), // Date | The date of the Aged Payables By Contact report
  'fromDate': new Date("2013-10-20"), // Date | The from date of the Aged Payables By Contact report
  'toDate': new Date("2013-10-20") // Date | The to date of the Aged Payables By Contact report
};
apiInstance.getReportAgedPayablesByContact(xeroTenantId, contactId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactId** | **String**| Unique identifier for a Contact | 
 **date** | **Date**| The date of the Aged Payables By Contact report | [optional] 
 **fromDate** | **Date**| The from date of the Aged Payables By Contact report | [optional] 
 **toDate** | **Date**| The to date of the Aged Payables By Contact report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportAgedReceivablesByContact

> ReportWithRows getReportAgedReceivablesByContact(xeroTenantId, contactId, opts)

Retrieves report for aged receivables by contact

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactId = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
let opts = {
  'date': new Date("2013-10-20"), // Date | The date of the Aged Receivables By Contact report
  'fromDate': new Date("2013-10-20"), // Date | The from date of the Aged Receivables By Contact report
  'toDate': new Date("2013-10-20") // Date | The to date of the Aged Receivables By Contact report
};
apiInstance.getReportAgedReceivablesByContact(xeroTenantId, contactId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactId** | **String**| Unique identifier for a Contact | 
 **date** | **Date**| The date of the Aged Receivables By Contact report | [optional] 
 **fromDate** | **Date**| The from date of the Aged Receivables By Contact report | [optional] 
 **toDate** | **Date**| The to date of the Aged Receivables By Contact report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportBASorGST

> ReportWithRows getReportBASorGST(xeroTenantId, reportID)

Retrieves a specific report for BAS using a unique report Id (only valid for AU orgs)

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let reportID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Report
apiInstance.getReportBASorGST(xeroTenantId, reportID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **reportID** | **String**| Unique identifier for a Report | 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportBASorGSTList

> ReportWithRows getReportBASorGSTList(xeroTenantId)

Retrieves report for BAS (only valid for AU orgs)

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
apiInstance.getReportBASorGSTList(xeroTenantId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportBalanceSheet

> ReportWithRows getReportBalanceSheet(xeroTenantId, opts)

Retrieves report for balancesheet

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'date': new Date("2019-11-01"), // Date | The date of the Balance Sheet report
  'periods': 3, // Number | The number of periods for the Balance Sheet report
  'timeframe': "MONTH", // String | The period size to compare to (MONTH, QUARTER, YEAR)
  'trackingOptionID1': "00000000-0000-0000-0000-000000000000", // String | The tracking option 1 for the Balance Sheet report
  'trackingOptionID2': "00000000-0000-0000-0000-000000000000", // String | The tracking option 2 for the Balance Sheet report
  'standardLayout': true, // Boolean | The standard layout boolean for the Balance Sheet report
  'paymentsOnly': false // Boolean | return a cash basis for the Balance Sheet report
};
apiInstance.getReportBalanceSheet(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **date** | **Date**| The date of the Balance Sheet report | [optional] 
 **periods** | **Number**| The number of periods for the Balance Sheet report | [optional] 
 **timeframe** | **String**| The period size to compare to (MONTH, QUARTER, YEAR) | [optional] 
 **trackingOptionID1** | **String**| The tracking option 1 for the Balance Sheet report | [optional] 
 **trackingOptionID2** | **String**| The tracking option 2 for the Balance Sheet report | [optional] 
 **standardLayout** | **Boolean**| The standard layout boolean for the Balance Sheet report | [optional] 
 **paymentsOnly** | **Boolean**| return a cash basis for the Balance Sheet report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportBankSummary

> ReportWithRows getReportBankSummary(xeroTenantId, opts)

Retrieves report for bank summary

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'fromDate': new Date("2019-11-01"), // Date | The from date for the Bank Summary report e.g. 2018-03-31
  'toDate': new Date("2019-11-30") // Date | The to date for the Bank Summary report e.g. 2018-03-31
};
apiInstance.getReportBankSummary(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **fromDate** | **Date**| The from date for the Bank Summary report e.g. 2018-03-31 | [optional] 
 **toDate** | **Date**| The to date for the Bank Summary report e.g. 2018-03-31 | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportBudgetSummary

> ReportWithRows getReportBudgetSummary(xeroTenantId, opts)

Retrieves report for budget summary

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'date': new Date("2019-03-31"), // Date | The date for the Bank Summary report e.g. 2018-03-31
  'period': 2, // Number | The number of periods to compare (integer between 1 and 12)
  'timeframe': 3 // Number | The period size to compare to (1=month, 3=quarter, 12=year)
};
apiInstance.getReportBudgetSummary(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **date** | **Date**| The date for the Bank Summary report e.g. 2018-03-31 | [optional] 
 **period** | **Number**| The number of periods to compare (integer between 1 and 12) | [optional] 
 **timeframe** | **Number**| The period size to compare to (1&#x3D;month, 3&#x3D;quarter, 12&#x3D;year) | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportExecutiveSummary

> ReportWithRows getReportExecutiveSummary(xeroTenantId, opts)

Retrieves report for executive summary

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'date': new Date("2019-03-31") // Date | The date for the Bank Summary report e.g. 2018-03-31
};
apiInstance.getReportExecutiveSummary(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **date** | **Date**| The date for the Bank Summary report e.g. 2018-03-31 | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportProfitAndLoss

> ReportWithRows getReportProfitAndLoss(xeroTenantId, opts)

Retrieves report for profit and loss

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'fromDate': new Date("2019-03-01"), // Date | The from date for the ProfitAndLoss report e.g. 2018-03-31
  'toDate': new Date("2019-03-31"), // Date | The to date for the ProfitAndLoss report e.g. 2018-03-31
  'periods': 3, // Number | The number of periods to compare (integer between 1 and 12)
  'timeframe': "MONTH", // String | The period size to compare to (MONTH, QUARTER, YEAR)
  'trackingCategoryID': "00000000-0000-0000-0000-000000000000", // String | The trackingCategory 1 for the ProfitAndLoss report
  'trackingCategoryID2': "00000000-0000-0000-0000-000000000000", // String | The trackingCategory 2 for the ProfitAndLoss report
  'trackingOptionID': "00000000-0000-0000-0000-000000000000", // String | The tracking option 1 for the ProfitAndLoss report
  'trackingOptionID2': "00000000-0000-0000-0000-000000000000", // String | The tracking option 2 for the ProfitAndLoss report
  'standardLayout': true, // Boolean | Return the standard layout for the ProfitAndLoss report
  'paymentsOnly': false // Boolean | Return cash only basis for the ProfitAndLoss report
};
apiInstance.getReportProfitAndLoss(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **fromDate** | **Date**| The from date for the ProfitAndLoss report e.g. 2018-03-31 | [optional] 
 **toDate** | **Date**| The to date for the ProfitAndLoss report e.g. 2018-03-31 | [optional] 
 **periods** | **Number**| The number of periods to compare (integer between 1 and 12) | [optional] 
 **timeframe** | **String**| The period size to compare to (MONTH, QUARTER, YEAR) | [optional] 
 **trackingCategoryID** | **String**| The trackingCategory 1 for the ProfitAndLoss report | [optional] 
 **trackingCategoryID2** | **String**| The trackingCategory 2 for the ProfitAndLoss report | [optional] 
 **trackingOptionID** | **String**| The tracking option 1 for the ProfitAndLoss report | [optional] 
 **trackingOptionID2** | **String**| The tracking option 2 for the ProfitAndLoss report | [optional] 
 **standardLayout** | **Boolean**| Return the standard layout for the ProfitAndLoss report | [optional] 
 **paymentsOnly** | **Boolean**| Return cash only basis for the ProfitAndLoss report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportTenNinetyNine

> Reports getReportTenNinetyNine(xeroTenantId, opts)

Retrieve reports for 1099

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'reportYear': "2019" // String | The year of the 1099 report
};
apiInstance.getReportTenNinetyNine(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **reportYear** | **String**| The year of the 1099 report | [optional] 

### Return type

[**Reports**](Reports.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportTrialBalance

> ReportWithRows getReportTrialBalance(xeroTenantId, opts)

Retrieves report for trial balance

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'date': new Date("2019-10-31"), // Date | The date for the Trial Balance report e.g. 2018-03-31
  'paymentsOnly': true // Boolean | Return cash only basis for the Trial Balance report
};
apiInstance.getReportTrialBalance(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **date** | **Date**| The date for the Trial Balance report e.g. 2018-03-31 | [optional] 
 **paymentsOnly** | **Boolean**| Return cash only basis for the Trial Balance report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTaxRates

> TaxRates getTaxRates(xeroTenantId, opts)

Retrieves tax rates

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "Name ASC", // String | Order by an any element
  'taxType': "INPUT" // String | Filter by tax type
};
apiInstance.getTaxRates(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **taxType** | **String**| Filter by tax type | [optional] 

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrackingCategories

> TrackingCategories getTrackingCategories(xeroTenantId, opts)

Retrieves tracking categories and options

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "Name ASC", // String | Order by an any element
  'includeArchived': true // Boolean | e.g. includeArchived=true - Categories and options with a status of ARCHIVED will be included in the response
};
apiInstance.getTrackingCategories(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **includeArchived** | **Boolean**| e.g. includeArchived&#x3D;true - Categories and options with a status of ARCHIVED will be included in the response | [optional] 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrackingCategory

> TrackingCategories getTrackingCategory(xeroTenantId, trackingCategoryID)

Retrieves specific tracking categories and options using a unique tracking category Id

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let trackingCategoryID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a TrackingCategory
apiInstance.getTrackingCategory(xeroTenantId, trackingCategoryID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **trackingCategoryID** | **String**| Unique identifier for a TrackingCategory | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUser

> Users getUser(xeroTenantId, userID)

Retrieves a specific user

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let userID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a User
apiInstance.getUser(xeroTenantId, userID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **userID** | **String**| Unique identifier for a User | 

### Return type

[**Users**](Users.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsers

> Users getUsers(xeroTenantId, opts)

Retrieves users

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': new Date("2020-02-06T12:17:43.202-08:00"), // Date | Only records created or modified since this timestamp will be returned
  'where': "IsSubscriber==true", // String | Filter by an any element
  'order': "LastName ASC" // String | Order by an any element
};
apiInstance.getUsers(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **Date**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 

### Return type

[**Users**](Users.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postSetup

> ImportSummaryObject postSetup(xeroTenantId, setup)

Sets the chart of accounts, the conversion date and conversion balances

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let setup = { "ConversionDate": {}, "ConversionBalances": [], "Accounts": [ { "Code": "200", "Name": "Sales", "Type": "SALES", "ReportingCode": "REV.TRA.GOO" }, { "Code": "400", "Name": "Advertising", "Type": "OVERHEADS", "ReportingCode": "EXP" }, { "Code": "610", "Name": "Accounts Receivable", "Type": "CURRENT", "SystemAccount": "DEBTORS", "ReportingCode": "ASS.CUR.REC.TRA" }, { "Code": "800", "Name": "Accounts Payable", "Type": "CURRLIAB", "SystemAccount": "CREDITORS", "ReportingCode": "LIA.CUR.PAY" } ] }; // Setup | Object including an accounts array, a conversion balances array and a conversion date object in body of request
apiInstance.postSetup(xeroTenantId, setup, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **setup** | [**Setup**](Setup.md)| Object including an accounts array, a conversion balances array and a conversion date object in body of request | 

### Return type

[**ImportSummaryObject**](ImportSummaryObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAccount

> Accounts updateAccount(xeroTenantId, accountID, accounts)

Updates a chart of accounts

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let accountID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for retrieving single object
let accounts = {   "Accounts":[   {   "Code":"123456", "Name":"BarFoo", "AccountID":"99ce6032-0678-4aa0-8148-240c75fee33a", "Type":"EXPENSE", "Description":"GoodBye World", "TaxType":"INPUT", "EnablePaymentsToAccount":false, "ShowInExpenseClaims":false, "Class":"EXPENSE", "ReportingCode":"EXP", "ReportingCodeName":"Expense", "UpdatedDateUTC":"2019-02-21T16:29:47.96-08:00" } ] }; // Accounts | Request of type Accounts array with one Account
apiInstance.updateAccount(xeroTenantId, accountID, accounts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **accountID** | **String**| Unique identifier for retrieving single object | 
 **accounts** | [**Accounts**](Accounts.md)| Request of type Accounts array with one Account | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAccountAttachmentByFileName

> Attachments updateAccountAttachmentByFileName(xeroTenantId, accountID, fileName, body)

Updates attachment on a specific account by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let accountID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Account object
let fileName = "xero-dev.jpg"; // String | Name of the attachment
let body = null; // Blob | Byte array of file in body of request
apiInstance.updateAccountAttachmentByFileName(xeroTenantId, accountID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **accountID** | **String**| Unique identifier for Account object | 
 **fileName** | **String**| Name of the attachment | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateBankTransaction

> BankTransactions updateBankTransaction(xeroTenantId, bankTransactionID, bankTransactions, opts)

Updates a single spent or received money transaction

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transaction
let bankTransactions = { "BankTransactions": [ { "Type": "SPEND", "Contact": { "ContactID": "00000000-0000-0000-0000-000000000000", "ContactStatus": "ACTIVE", "Name": "Buzz Lightyear", "FirstName": "Buzz", "LastName": "Lightyear", "EmailAddress": "buzz.Lightyear@email.com", "ContactPersons": [], "BankAccountDetails": "", "Addresses": [ { "AddressType": "STREET", "City": "", "Region": "", "PostalCode": "", "Country": "" }, { "AddressType": "POBOX", "AddressLine1": "", "AddressLine2": "", "AddressLine3": "", "AddressLine4": "", "City": "Palo Alto", "Region": "CA", "PostalCode": "94020", "Country": "United States" } ], "Phones": [ { "PhoneType": "DEFAULT", "PhoneNumber": "847-1294", "PhoneAreaCode": "(626)", "PhoneCountryCode": "" }, { "PhoneType": "DDI", "PhoneNumber": "", "PhoneAreaCode": "", "PhoneCountryCode": "" }, { "PhoneType": "FAX", "PhoneNumber": "", "PhoneAreaCode": "", "PhoneCountryCode": "" }, { "PhoneType": "MOBILE", "PhoneNumber": "", "PhoneAreaCode": "", "PhoneCountryCode": "" } ], "UpdatedDateUTC": "2017-08-21T13:49:04.227-07:00", "ContactGroups": [] }, "Lineitems": [], "BankAccount": { "Code": "088", "Name": "Business Wells Fargo", "AccountID": "00000000-0000-0000-0000-000000000000" }, "IsReconciled": false, "Date": "2019-02-25", "Reference": "You just updated", "CurrencyCode": "USD", "CurrencyRate": 1, "Status": "AUTHORISED", "LineAmountTypes": "Inclusive", "TotalTax": 1.74, "BankTransactionID": "00000000-0000-0000-0000-000000000000", "UpdatedDateUTC": "2019-02-26T12:39:27.813-08:00" } ] }; // BankTransactions | 
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.updateBankTransaction(xeroTenantId, bankTransactionID, bankTransactions, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactionID** | **String**| Xero generated unique identifier for a bank transaction | 
 **bankTransactions** | [**BankTransactions**](BankTransactions.md)|  | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBankTransactionAttachmentByFileName

> Attachments updateBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, body)

Updates a specific attachment from a specific bank transaction by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transaction
let fileName = "xero-dev.jpg"; // String | The name of the file being attached
let body = null; // Blob | Byte array of file in body of request
apiInstance.updateBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactionID** | **String**| Xero generated unique identifier for a bank transaction | 
 **fileName** | **String**| The name of the file being attached | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateBankTransferAttachmentByFileName

> Attachments updateBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, body)



### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransferID = "00000000-0000-0000-0000-000000000000"; // String | Xero generated unique identifier for a bank transfer
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Bank Transfer
let body = null; // Blob | Byte array of file in body of request
apiInstance.updateBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransferID** | **String**| Xero generated unique identifier for a bank transfer | 
 **fileName** | **String**| The name of the file being attached to a Bank Transfer | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateContact

> Contacts updateContact(xeroTenantId, contactID, contacts)

Updates a specific contact in a Xero organisation

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
let contacts = { "Contacts": [{ "ContactID": "00000000-0000-0000-0000-000000000000", "Name": "Thanos" }]}; // Contacts | an array of Contacts containing single Contact object with properties to update
apiInstance.updateContact(xeroTenantId, contactID, contacts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactID** | **String**| Unique identifier for a Contact | 
 **contacts** | [**Contacts**](Contacts.md)| an array of Contacts containing single Contact object with properties to update | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateContactAttachmentByFileName

> Attachments updateContactAttachmentByFileName(xeroTenantId, contactID, fileName, body)



### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact
let fileName = "xero-dev.jpg"; // String | Name for the file you are attaching
let body = null; // Blob | Byte array of file in body of request
apiInstance.updateContactAttachmentByFileName(xeroTenantId, contactID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactID** | **String**| Unique identifier for a Contact | 
 **fileName** | **String**| Name for the file you are attaching | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateContactGroup

> ContactGroups updateContactGroup(xeroTenantId, contactGroupID, contactGroups)

Updates a specific contact group

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contactGroupID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Contact Group
let contactGroups = {   "ContactGroups":[   {   "Name":"Suppliers" } ] }; // ContactGroups | an array of Contact groups with Name of specific group to update
apiInstance.updateContactGroup(xeroTenantId, contactGroupID, contactGroups, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contactGroupID** | **String**| Unique identifier for a Contact Group | 
 **contactGroups** | [**ContactGroups**](ContactGroups.md)| an array of Contact groups with Name of specific group to update | 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCreditNote

> CreditNotes updateCreditNote(xeroTenantId, creditNoteID, creditNotes, opts)

Updates a specific credit note

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
let creditNotes = { "CreditNotes": [ { "Type": "ACCPAYCREDIT", "Contact": { "ContactID": "430fa14a-f945-44d3-9f97-5df5e28441b8" }, "Date": "2019-01-05", "Status": "AUTHORISED", "Reference": "HelloWorld", "LineItems": [ { "Description": "Foobar", "Quantity": 2, "UnitAmount": 20, "AccountCode": "400" } ] } ] }; // CreditNotes | an array of Credit Notes containing credit note details to update
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.updateCreditNote(xeroTenantId, creditNoteID, creditNotes, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 
 **creditNotes** | [**CreditNotes**](CreditNotes.md)| an array of Credit Notes containing credit note details to update | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCreditNoteAttachmentByFileName

> Attachments updateCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, body)

Updates attachments on a specific credit note by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Credit Note
let fileName = "xero-dev.jpg"; // String | Name of the file you are attaching to Credit Note
let body = null; // Blob | Byte array of file in body of request
apiInstance.updateCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNoteID** | **String**| Unique identifier for a Credit Note | 
 **fileName** | **String**| Name of the file you are attaching to Credit Note | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateExpenseClaim

> ExpenseClaims updateExpenseClaim(xeroTenantId, expenseClaimID, expenseClaims)

Updates a specific expense claims

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let expenseClaimID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ExpenseClaim
let expenseClaims = { "ExpenseClaims": [ { "Status": "SUBMITTED", "User": { "UserID": "d1164823-0ac1-41ad-987b-b4e30fe0b273" }, "Receipts": [ { "Lineitems": [], "ReceiptID": "dc1c7f6d-0a4c-402f-acac-551d62ce5816" } ] } ] }; // ExpenseClaims | 
apiInstance.updateExpenseClaim(xeroTenantId, expenseClaimID, expenseClaims, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **expenseClaimID** | **String**| Unique identifier for a ExpenseClaim | 
 **expenseClaims** | [**ExpenseClaims**](ExpenseClaims.md)|  | 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInvoice

> Invoices updateInvoice(xeroTenantId, invoiceID, invoices, opts)

Updates a specific sales invoices or purchase bills

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
let invoices = { "Invoices": [{ Reference: "May the force be with you", "InvoiceID": "00000000-0000-0000-0000-000000000000", "LineItems": [], "Contact": {}, "Type": "ACCPAY" }]}; // Invoices | 
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.updateInvoice(xeroTenantId, invoiceID, invoices, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 
 **invoices** | [**Invoices**](Invoices.md)|  | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInvoiceAttachmentByFileName

> Attachments updateInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, body)

Updates an attachment from a specific invoices or purchase bill by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Invoice
let fileName = "xero-dev.jpg"; // String | Name of the file you are attaching
let body = null; // Blob | Byte array of file in body of request
apiInstance.updateInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoiceID** | **String**| Unique identifier for an Invoice | 
 **fileName** | **String**| Name of the file you are attaching | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateItem

> Items updateItem(xeroTenantId, itemID, items, opts)

Updates a specific item

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let itemID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Item
let items = { "Items": [ { "Code": "ItemCode123", "Description": "Description 123" } ] }; // Items | 
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.updateItem(xeroTenantId, itemID, items, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **itemID** | **String**| Unique identifier for an Item | 
 **items** | [**Items**](Items.md)|  | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLinkedTransaction

> LinkedTransactions updateLinkedTransaction(xeroTenantId, linkedTransactionID, linkedTransactions)

Updates a specific linked transactions (billable expenses)

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let linkedTransactionID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a LinkedTransaction
let linkedTransactions = { "LinkedTransactions": [ { "SourceTransactionID": "00000000-0000-0000-0000-000000000000", "SourceLineItemID": "00000000-0000-0000-0000-000000000000" } ] }; // LinkedTransactions | 
apiInstance.updateLinkedTransaction(xeroTenantId, linkedTransactionID, linkedTransactions, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **linkedTransactionID** | **String**| Unique identifier for a LinkedTransaction | 
 **linkedTransactions** | [**LinkedTransactions**](LinkedTransactions.md)|  | 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateManualJournal

> ManualJournals updateManualJournal(xeroTenantId, manualJournalID, manualJournals)

Updates a specific manual journal

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournalID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ManualJournal
let manualJournals = { "ManualJournals": [ { "Narration": "Hello Xero", "ManualJournalID": "00000000-0000-0000-0000-000000000000", "JournalLines": [] } ] }; // ManualJournals | 
apiInstance.updateManualJournal(xeroTenantId, manualJournalID, manualJournals, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournalID** | **String**| Unique identifier for a ManualJournal | 
 **manualJournals** | [**ManualJournals**](ManualJournals.md)|  | 

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateManualJournalAttachmentByFileName

> Attachments updateManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, body)

Updates a specific attachment from a specific manual journal by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournalID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a ManualJournal
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to a ManualJournal
let body = null; // Blob | Byte array of file in body of request
apiInstance.updateManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournalID** | **String**| Unique identifier for a ManualJournal | 
 **fileName** | **String**| The name of the file being attached to a ManualJournal | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateOrCreateBankTransactions

> BankTransactions updateOrCreateBankTransactions(xeroTenantId, bankTransactions, opts)

Updates or creates one or more spent or received money transaction

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let bankTransactions = { "BankTransactions": [ { "Type": "SPEND", "Contact": { "ContactID": "00000000-0000-0000-0000-000000000000" }, "Lineitems": [ { "Description": "Foobar", "Quantity": 1, "UnitAmount": 20, "AccountCode": "400" } ], "BankAccount": { "Code": "088" } } ] }; // BankTransactions | 
let opts = {
  'summarizeErrors': true, // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.updateOrCreateBankTransactions(xeroTenantId, bankTransactions, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **bankTransactions** | [**BankTransactions**](BankTransactions.md)|  | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrCreateContacts

> Contacts updateOrCreateContacts(xeroTenantId, contacts, opts)

Updates or creates one or more contacts in a Xero organisation

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let contacts = { "Contacts": [ { "Name": "Bruce Banner", "EmailAddress": "hulk@avengers.com", "Phones": [ { "PhoneType": "MOBILE", "PhoneNumber": "555-1212", "PhoneAreaCode": "415" } ], "PaymentTerms": { "Bills": { "Day": 15, "Type": "OFCURRENTMONTH" }, "Sales": { "Day": 10, "Type": "DAYSAFTERBILLMONTH" } } } ] }; // Contacts | 
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.updateOrCreateContacts(xeroTenantId, contacts, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **contacts** | [**Contacts**](Contacts.md)|  | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrCreateCreditNotes

> CreditNotes updateOrCreateCreditNotes(xeroTenantId, creditNotes, opts)

Updates or creates one or more credit notes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let creditNotes = {   "CreditNotes":[   {   "Type":"ACCPAYCREDIT", "Contact":{   "ContactID":"430fa14a-f945-44d3-9f97-5df5e28441b8" }, "Date":"2019-01-05", "Status":"AUTHORISED", "Reference": "HelloWorld", "LineItems":[   {   "Description":"Foobar", "Quantity":2.0, "UnitAmount":20.0, "AccountCode":"400" } ] } ] }; // CreditNotes | an array of Credit Notes with a single CreditNote object.
let opts = {
  'summarizeErrors': true, // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.updateOrCreateCreditNotes(xeroTenantId, creditNotes, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **creditNotes** | [**CreditNotes**](CreditNotes.md)| an array of Credit Notes with a single CreditNote object. | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrCreateEmployees

> Employees updateOrCreateEmployees(xeroTenantId, employees, opts)

Creates a single new employees used in Xero payrun

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let employees = { "Employees": [ { "FirstName": "Nick", "LastName": "Fury", "ExternalLink": { "Url": "http://twitter.com/#!/search/Nick+Fury" } } ] }; // Employees | Employees with array of Employee object in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.updateOrCreateEmployees(xeroTenantId, employees, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **employees** | [**Employees**](Employees.md)| Employees with array of Employee object in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrCreateInvoices

> Invoices updateOrCreateInvoices(xeroTenantId, invoices, opts)

Updates or creates one or more sales invoices or purchase bills

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let invoices = { "Invoices": [ { "Type": "ACCREC", "Contact": { "ContactID": "430fa14a-f945-44d3-9f97-5df5e28441b8" }, "LineItems": [ { "Description": "Acme Tires", "Quantity": 2, "UnitAmount": 20, "AccountCode": "200", "TaxType": "NONE", "LineAmount": 40 } ], "Date": "2019-03-11", "DueDate": "2018-12-10", "Reference": "Website Design", "Status": "AUTHORISED" } ] }; // Invoices | 
let opts = {
  'summarizeErrors': true, // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.updateOrCreateInvoices(xeroTenantId, invoices, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **invoices** | [**Invoices**](Invoices.md)|  | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrCreateItems

> Items updateOrCreateItems(xeroTenantId, items, opts)

Updates or creates one or more items

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let items = { "Items": [ { "Code": "ItemCode123", "Name": "ItemName XYZ", "Description": "Item Description ABC" } ] }; // Items | 
let opts = {
  'summarizeErrors': true, // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.updateOrCreateItems(xeroTenantId, items, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **items** | [**Items**](Items.md)|  | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrCreateManualJournals

> ManualJournals updateOrCreateManualJournals(xeroTenantId, manualJournals, opts)

Updates or creates a single manual journal

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let manualJournals = { "ManualJournals": [ { "Narration": "Journal Desc", "JournalLines": [ { "LineAmount": 100, "AccountCode": "400", "Description": "Money Movement" }, { "LineAmount": -100, "AccountCode": "400", "Description": "Prepayment of things", "Tracking": [ { "Name": "North", "Option": "Region" } ] } ], "Date": "2019-03-14" } ] }; // ManualJournals | ManualJournals array with ManualJournal object in body of request
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.updateOrCreateManualJournals(xeroTenantId, manualJournals, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **manualJournals** | [**ManualJournals**](ManualJournals.md)| ManualJournals array with ManualJournal object in body of request | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrCreatePurchaseOrders

> PurchaseOrders updateOrCreatePurchaseOrders(xeroTenantId, purchaseOrders, opts)

Updates or creates one or more purchase orders

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrders = { "PurchaseOrders": [ { "Contact": { "ContactID": "00000000-0000-0000-0000-000000000000" }, "LineItems": [ { "Description": "Foobar", "Quantity": 1, "UnitAmount": 20, "AccountCode": "710" } ], "Date": "2019-03-13" } ] }; // PurchaseOrders | 
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.updateOrCreatePurchaseOrders(xeroTenantId, purchaseOrders, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrders** | [**PurchaseOrders**](PurchaseOrders.md)|  | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrCreateQuotes

> Quotes updateOrCreateQuotes(xeroTenantId, quotes, opts)

Updates or creates one or more quotes

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quotes = { "Quotes": [ { "Contact": { "ContactID": "00000000-0000-0000-0000-000000000000" }, "LineItems": [ { "Description": "Foobar", "Quantity": 1, "UnitAmount": 20, "AccountCode": "12775" } ], "Date": "2020-02-01" } ] }; // Quotes | 
let opts = {
  'summarizeErrors': true // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
};
apiInstance.updateOrCreateQuotes(xeroTenantId, quotes, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quotes** | [**Quotes**](Quotes.md)|  | 
 **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false]

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePurchaseOrder

> PurchaseOrders updatePurchaseOrder(xeroTenantId, purchaseOrderID, purchaseOrders)

Updates a specific purchase order

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a PurchaseOrder
let purchaseOrders = { "PurchaseOrders": [ { "AttentionTo": "Peter Parker", "LineItems": [], "Contact": {} } ] }; // PurchaseOrders | 
apiInstance.updatePurchaseOrder(xeroTenantId, purchaseOrderID, purchaseOrders, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderID** | **String**| Unique identifier for a PurchaseOrder | 
 **purchaseOrders** | [**PurchaseOrders**](PurchaseOrders.md)|  | 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePurchaseOrderAttachmentByFileName

> Attachments updatePurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, body)

Updates a specific attachment for a specific purchase order by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let purchaseOrderID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Purchase Order object
let fileName = "xero-dev.png"; // String | Name of the attachment
let body = null; // Blob | Byte array of file in body of request
apiInstance.updatePurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **purchaseOrderID** | **String**| Unique identifier for Purchase Order object | 
 **fileName** | **String**| Name of the attachment | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateQuote

> Quotes updateQuote(xeroTenantId, quoteID, quotes)

Updates a specific quote

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for an Quote
let quotes = { "Quotes": [ { "Reference": "I am an update", "Contact": { "ContactID": "00000000-0000-0000-0000-000000000000" }, "Date": "2020-02-01" } ] }; // Quotes | 
apiInstance.updateQuote(xeroTenantId, quoteID, quotes, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quoteID** | **String**| Unique identifier for an Quote | 
 **quotes** | [**Quotes**](Quotes.md)|  | 

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateQuoteAttachmentByFileName

> Attachments updateQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, body)

Updates a specific attachment from a specific quote by filename

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let quoteID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for Quote object
let fileName = "xero-dev.jpg"; // String | Name of the attachment
let body = null; // Blob | Byte array of file in body of request
apiInstance.updateQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **quoteID** | **String**| Unique identifier for Quote object | 
 **fileName** | **String**| Name of the attachment | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateReceipt

> Receipts updateReceipt(xeroTenantId, receiptID, receipts, opts)

Updates a specific draft expense claim receipts

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let receiptID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Receipt
let receipts = { "Receipts": [ { "Lineitems": [], "User": { "UserID": "00000000-0000-0000-0000-000000000000" }, "Reference": "Foobar" } ] }; // Receipts | 
let opts = {
  'unitdp': 4 // Number | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
};
apiInstance.updateReceipt(xeroTenantId, receiptID, receipts, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **receiptID** | **String**| Unique identifier for a Receipt | 
 **receipts** | [**Receipts**](Receipts.md)|  | 
 **unitdp** | **Number**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateReceiptAttachmentByFileName

> Attachments updateReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, body)

Updates a specific attachment on a specific expense claim receipts by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let receiptID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Receipt
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to the Receipt
let body = null; // Blob | Byte array of file in body of request
apiInstance.updateReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **receiptID** | **String**| Unique identifier for a Receipt | 
 **fileName** | **String**| The name of the file being attached to the Receipt | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateRepeatingInvoiceAttachmentByFileName

> Attachments updateRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, body)

Updates a specific attachment from a specific repeating invoices by file name

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let repeatingInvoiceID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Repeating Invoice
let fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Repeating Invoice
let body = null; // Blob | Byte array of file in body of request
apiInstance.updateRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, body, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **repeatingInvoiceID** | **String**| Unique identifier for a Repeating Invoice | 
 **fileName** | **String**| The name of the file being attached to a Repeating Invoice | 
 **body** | **Blob**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateTaxRate

> TaxRates updateTaxRate(xeroTenantId, taxRates)

Updates tax rates

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let taxRates = { "TaxRates": [ { "Name": "State Tax NY", "TaxComponents": [ { "Name": "State Tax", "Rate": 2.25 } ], "Status": "DELETED", "ReportTaxType": "INPUT" } ] }; // TaxRates | 
apiInstance.updateTaxRate(xeroTenantId, taxRates, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **taxRates** | [**TaxRates**](TaxRates.md)|  | 

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTrackingCategory

> TrackingCategories updateTrackingCategory(xeroTenantId, trackingCategoryID, trackingCategory)

Updates a specific tracking category

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let trackingCategoryID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a TrackingCategory
let trackingCategory = { "Name": "Avengers" }; // TrackingCategory | 
apiInstance.updateTrackingCategory(xeroTenantId, trackingCategoryID, trackingCategory, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **trackingCategoryID** | **String**| Unique identifier for a TrackingCategory | 
 **trackingCategory** | [**TrackingCategory**](TrackingCategory.md)|  | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTrackingOptions

> TrackingOptions updateTrackingOptions(xeroTenantId, trackingCategoryID, trackingOptionID, trackingOption)

Updates a specific option for a specific tracking category

### Example

```javascript
import XeroAccountingApi from 'xero_accounting_api';
let defaultClient = XeroAccountingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroAccountingApi.AccountingApi();
let xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
let trackingCategoryID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a TrackingCategory
let trackingOptionID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Tracking Option
let trackingOption = { name: "Vision" }; // TrackingOption | 
apiInstance.updateTrackingOptions(xeroTenantId, trackingCategoryID, trackingOptionID, trackingOption, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **trackingCategoryID** | **String**| Unique identifier for a TrackingCategory | 
 **trackingOptionID** | **String**| Unique identifier for a Tracking Option | 
 **trackingOption** | [**TrackingOption**](TrackingOption.md)|  | 

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

