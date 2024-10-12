# AccountingApi

All URIs are relative to *https://api.xero.com/api.xro/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAccount**](AccountingApi.md#createAccount) | **PUT** /Accounts | Creates a new chart of accounts |
| [**createAccountAttachmentByFileName**](AccountingApi.md#createAccountAttachmentByFileName) | **PUT** /Accounts/{AccountID}/Attachments/{FileName} | Creates an attachment on a specific account |
| [**createBankTransactionAttachmentByFileName**](AccountingApi.md#createBankTransactionAttachmentByFileName) | **PUT** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Creates an attachment for a specific bank transaction by filename |
| [**createBankTransactionHistoryRecord**](AccountingApi.md#createBankTransactionHistoryRecord) | **PUT** /BankTransactions/{BankTransactionID}/History | Creates a history record for a specific bank transactions |
| [**createBankTransactions**](AccountingApi.md#createBankTransactions) | **PUT** /BankTransactions | Creates one or more spent or received money transaction |
| [**createBankTransfer**](AccountingApi.md#createBankTransfer) | **PUT** /BankTransfers | Creates a bank transfer |
| [**createBankTransferAttachmentByFileName**](AccountingApi.md#createBankTransferAttachmentByFileName) | **PUT** /BankTransfers/{BankTransferID}/Attachments/{FileName} |  |
| [**createBankTransferHistoryRecord**](AccountingApi.md#createBankTransferHistoryRecord) | **PUT** /BankTransfers/{BankTransferID}/History | Creates a history record for a specific bank transfer |
| [**createBatchPayment**](AccountingApi.md#createBatchPayment) | **PUT** /BatchPayments | Creates one or many batch payments for invoices |
| [**createBatchPaymentHistoryRecord**](AccountingApi.md#createBatchPaymentHistoryRecord) | **PUT** /BatchPayments/{BatchPaymentID}/History | Creates a history record for a specific batch payment |
| [**createBrandingThemePaymentServices**](AccountingApi.md#createBrandingThemePaymentServices) | **POST** /BrandingThemes/{BrandingThemeID}/PaymentServices | Creates a new custom payment service for a specific branding theme |
| [**createContactAttachmentByFileName**](AccountingApi.md#createContactAttachmentByFileName) | **PUT** /Contacts/{ContactID}/Attachments/{FileName} |  |
| [**createContactGroup**](AccountingApi.md#createContactGroup) | **PUT** /ContactGroups | Creates a contact group |
| [**createContactGroupContacts**](AccountingApi.md#createContactGroupContacts) | **PUT** /ContactGroups/{ContactGroupID}/Contacts | Creates contacts to a specific contact group |
| [**createContactHistory**](AccountingApi.md#createContactHistory) | **PUT** /Contacts/{ContactID}/History | Creates a new history record for a specific contact |
| [**createContacts**](AccountingApi.md#createContacts) | **PUT** /Contacts | Creates multiple contacts (bulk) in a Xero organisation |
| [**createCreditNoteAllocation**](AccountingApi.md#createCreditNoteAllocation) | **PUT** /CreditNotes/{CreditNoteID}/Allocations | Creates allocation for a specific credit note |
| [**createCreditNoteAttachmentByFileName**](AccountingApi.md#createCreditNoteAttachmentByFileName) | **PUT** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Creates an attachment for a specific credit note |
| [**createCreditNoteHistory**](AccountingApi.md#createCreditNoteHistory) | **PUT** /CreditNotes/{CreditNoteID}/History | Retrieves history records of a specific credit note |
| [**createCreditNotes**](AccountingApi.md#createCreditNotes) | **PUT** /CreditNotes | Creates a new credit note |
| [**createCurrency**](AccountingApi.md#createCurrency) | **PUT** /Currencies | Create a new currency for a Xero organisation |
| [**createEmployees**](AccountingApi.md#createEmployees) | **PUT** /Employees | Creates new employees used in Xero payrun |
| [**createExpenseClaimHistory**](AccountingApi.md#createExpenseClaimHistory) | **PUT** /ExpenseClaims/{ExpenseClaimID}/History | Creates a history record for a specific expense claim |
| [**createExpenseClaims**](AccountingApi.md#createExpenseClaims) | **PUT** /ExpenseClaims | Creates expense claims |
| [**createInvoiceAttachmentByFileName**](AccountingApi.md#createInvoiceAttachmentByFileName) | **PUT** /Invoices/{InvoiceID}/Attachments/{FileName} | Creates an attachment for a specific invoice or purchase bill by filename |
| [**createInvoiceHistory**](AccountingApi.md#createInvoiceHistory) | **PUT** /Invoices/{InvoiceID}/History | Creates a history record for a specific invoice |
| [**createInvoices**](AccountingApi.md#createInvoices) | **PUT** /Invoices | Creates one or more sales invoices or purchase bills |
| [**createItemHistory**](AccountingApi.md#createItemHistory) | **PUT** /Items/{ItemID}/History | Creates a history record for a specific item |
| [**createItems**](AccountingApi.md#createItems) | **PUT** /Items | Creates one or more items |
| [**createLinkedTransaction**](AccountingApi.md#createLinkedTransaction) | **PUT** /LinkedTransactions | Creates linked transactions (billable expenses) |
| [**createManualJournalAttachmentByFileName**](AccountingApi.md#createManualJournalAttachmentByFileName) | **PUT** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Creates a specific attachment for a specific manual journal by file name |
| [**createManualJournalHistoryRecord**](AccountingApi.md#createManualJournalHistoryRecord) | **PUT** /ManualJournals/{ManualJournalID}/History | Creates a history record for a specific manual journal |
| [**createManualJournals**](AccountingApi.md#createManualJournals) | **PUT** /ManualJournals | Creates one or more manual journals |
| [**createOverpaymentAllocations**](AccountingApi.md#createOverpaymentAllocations) | **PUT** /Overpayments/{OverpaymentID}/Allocations | Creates a single allocation for a specific overpayment |
| [**createOverpaymentHistory**](AccountingApi.md#createOverpaymentHistory) | **PUT** /Overpayments/{OverpaymentID}/History | Creates a history record for a specific overpayment |
| [**createPayment**](AccountingApi.md#createPayment) | **POST** /Payments | Creates a single payment for invoice or credit notes |
| [**createPaymentHistory**](AccountingApi.md#createPaymentHistory) | **PUT** /Payments/{PaymentID}/History | Creates a history record for a specific payment |
| [**createPaymentService**](AccountingApi.md#createPaymentService) | **PUT** /PaymentServices | Creates a payment service |
| [**createPayments**](AccountingApi.md#createPayments) | **PUT** /Payments | Creates multiple payments for invoices or credit notes |
| [**createPrepaymentAllocations**](AccountingApi.md#createPrepaymentAllocations) | **PUT** /Prepayments/{PrepaymentID}/Allocations | Allows you to create an Allocation for prepayments |
| [**createPrepaymentHistory**](AccountingApi.md#createPrepaymentHistory) | **PUT** /Prepayments/{PrepaymentID}/History | Creates a history record for a specific prepayment |
| [**createPurchaseOrderAttachmentByFileName**](AccountingApi.md#createPurchaseOrderAttachmentByFileName) | **PUT** /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName} | Creates attachment for a specific purchase order |
| [**createPurchaseOrderHistory**](AccountingApi.md#createPurchaseOrderHistory) | **PUT** /PurchaseOrders/{PurchaseOrderID}/History | Creates a history record for a specific purchase orders |
| [**createPurchaseOrders**](AccountingApi.md#createPurchaseOrders) | **PUT** /PurchaseOrders | Creates one or more purchase orders |
| [**createQuoteAttachmentByFileName**](AccountingApi.md#createQuoteAttachmentByFileName) | **PUT** /Quotes/{QuoteID}/Attachments/{FileName} | Creates attachment for a specific quote |
| [**createQuoteHistory**](AccountingApi.md#createQuoteHistory) | **PUT** /Quotes/{QuoteID}/History | Creates a history record for a specific quote |
| [**createQuotes**](AccountingApi.md#createQuotes) | **PUT** /Quotes | Create one or more quotes |
| [**createReceipt**](AccountingApi.md#createReceipt) | **PUT** /Receipts | Creates draft expense claim receipts for any user |
| [**createReceiptAttachmentByFileName**](AccountingApi.md#createReceiptAttachmentByFileName) | **PUT** /Receipts/{ReceiptID}/Attachments/{FileName} | Creates an attachment on a specific expense claim receipts by file name |
| [**createReceiptHistory**](AccountingApi.md#createReceiptHistory) | **PUT** /Receipts/{ReceiptID}/History | Creates a history record for a specific receipt |
| [**createRepeatingInvoiceAttachmentByFileName**](AccountingApi.md#createRepeatingInvoiceAttachmentByFileName) | **PUT** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Creates an attachment from a specific repeating invoices by file name |
| [**createRepeatingInvoiceHistory**](AccountingApi.md#createRepeatingInvoiceHistory) | **PUT** /RepeatingInvoices/{RepeatingInvoiceID}/History | Creates a  history record for a specific repeating invoice |
| [**createTaxRates**](AccountingApi.md#createTaxRates) | **PUT** /TaxRates | Creates one or more tax rates |
| [**createTrackingCategory**](AccountingApi.md#createTrackingCategory) | **PUT** /TrackingCategories | Create tracking categories |
| [**createTrackingOptions**](AccountingApi.md#createTrackingOptions) | **PUT** /TrackingCategories/{TrackingCategoryID}/Options | Creates options for a specific tracking category |
| [**deleteAccount**](AccountingApi.md#deleteAccount) | **DELETE** /Accounts/{AccountID} | Deletes a chart of accounts |
| [**deleteContactGroupContact**](AccountingApi.md#deleteContactGroupContact) | **DELETE** /ContactGroups/{ContactGroupID}/Contacts/{ContactID} | Deletes a specific contact from a contact group using a unique contact Id |
| [**deleteContactGroupContacts**](AccountingApi.md#deleteContactGroupContacts) | **DELETE** /ContactGroups/{ContactGroupID}/Contacts | Deletes all contacts from a specific contact group |
| [**deleteItem**](AccountingApi.md#deleteItem) | **DELETE** /Items/{ItemID} | Deletes a specific item |
| [**deleteLinkedTransaction**](AccountingApi.md#deleteLinkedTransaction) | **DELETE** /LinkedTransactions/{LinkedTransactionID} | Deletes a specific linked transactions (billable expenses) |
| [**deletePayment**](AccountingApi.md#deletePayment) | **POST** /Payments/{PaymentID} | Updates a specific payment for invoices and credit notes |
| [**deleteTrackingCategory**](AccountingApi.md#deleteTrackingCategory) | **DELETE** /TrackingCategories/{TrackingCategoryID} | Deletes a specific tracking category |
| [**deleteTrackingOptions**](AccountingApi.md#deleteTrackingOptions) | **DELETE** /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} | Deletes a specific option for a specific tracking category |
| [**emailInvoice**](AccountingApi.md#emailInvoice) | **POST** /Invoices/{InvoiceID}/Email | Sends a copy of a specific invoice to related contact via email |
| [**getAccount**](AccountingApi.md#getAccount) | **GET** /Accounts/{AccountID} | Retrieves a single chart of accounts by using a unique account Id |
| [**getAccountAttachmentByFileName**](AccountingApi.md#getAccountAttachmentByFileName) | **GET** /Accounts/{AccountID}/Attachments/{FileName} | Retrieves an attachment for a specific account by filename |
| [**getAccountAttachmentById**](AccountingApi.md#getAccountAttachmentById) | **GET** /Accounts/{AccountID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific account using a unique attachment Id |
| [**getAccountAttachments**](AccountingApi.md#getAccountAttachments) | **GET** /Accounts/{AccountID}/Attachments | Retrieves attachments for a specific accounts by using a unique account Id |
| [**getAccounts**](AccountingApi.md#getAccounts) | **GET** /Accounts | Retrieves the full chart of accounts |
| [**getBankTransaction**](AccountingApi.md#getBankTransaction) | **GET** /BankTransactions/{BankTransactionID} | Retrieves a single spent or received money transaction by using a unique bank transaction Id |
| [**getBankTransactionAttachmentByFileName**](AccountingApi.md#getBankTransactionAttachmentByFileName) | **GET** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Retrieves a specific attachment from a specific bank transaction by filename |
| [**getBankTransactionAttachmentById**](AccountingApi.md#getBankTransactionAttachmentById) | **GET** /BankTransactions/{BankTransactionID}/Attachments/{AttachmentID} | Retrieves specific attachments from a specific BankTransaction using a unique attachment Id |
| [**getBankTransactionAttachments**](AccountingApi.md#getBankTransactionAttachments) | **GET** /BankTransactions/{BankTransactionID}/Attachments | Retrieves any attachments from a specific bank transactions |
| [**getBankTransactions**](AccountingApi.md#getBankTransactions) | **GET** /BankTransactions | Retrieves any spent or received money transactions |
| [**getBankTransactionsHistory**](AccountingApi.md#getBankTransactionsHistory) | **GET** /BankTransactions/{BankTransactionID}/History | Retrieves history from a specific bank transaction using a unique bank transaction Id |
| [**getBankTransfer**](AccountingApi.md#getBankTransfer) | **GET** /BankTransfers/{BankTransferID} | Retrieves specific bank transfers by using a unique bank transfer Id |
| [**getBankTransferAttachmentByFileName**](AccountingApi.md#getBankTransferAttachmentByFileName) | **GET** /BankTransfers/{BankTransferID}/Attachments/{FileName} | Retrieves a specific attachment on a specific bank transfer by file name |
| [**getBankTransferAttachmentById**](AccountingApi.md#getBankTransferAttachmentById) | **GET** /BankTransfers/{BankTransferID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific bank transfer using a unique attachment ID |
| [**getBankTransferAttachments**](AccountingApi.md#getBankTransferAttachments) | **GET** /BankTransfers/{BankTransferID}/Attachments | Retrieves attachments from a specific bank transfer |
| [**getBankTransferHistory**](AccountingApi.md#getBankTransferHistory) | **GET** /BankTransfers/{BankTransferID}/History | Retrieves history from a specific bank transfer using a unique bank transfer Id |
| [**getBankTransfers**](AccountingApi.md#getBankTransfers) | **GET** /BankTransfers | Retrieves all bank transfers |
| [**getBatchPaymentHistory**](AccountingApi.md#getBatchPaymentHistory) | **GET** /BatchPayments/{BatchPaymentID}/History | Retrieves history from a specific batch payment |
| [**getBatchPayments**](AccountingApi.md#getBatchPayments) | **GET** /BatchPayments | Retrieves either one or many batch payments for invoices |
| [**getBrandingTheme**](AccountingApi.md#getBrandingTheme) | **GET** /BrandingThemes/{BrandingThemeID} | Retrieves a specific branding theme using a unique branding theme Id |
| [**getBrandingThemePaymentServices**](AccountingApi.md#getBrandingThemePaymentServices) | **GET** /BrandingThemes/{BrandingThemeID}/PaymentServices | Retrieves the payment services for a specific branding theme |
| [**getBrandingThemes**](AccountingApi.md#getBrandingThemes) | **GET** /BrandingThemes | Retrieves all the branding themes |
| [**getContact**](AccountingApi.md#getContact) | **GET** /Contacts/{ContactID} | Retrieves a specific contacts in a Xero organisation using a unique contact Id |
| [**getContactAttachmentByFileName**](AccountingApi.md#getContactAttachmentByFileName) | **GET** /Contacts/{ContactID}/Attachments/{FileName} | Retrieves a specific attachment from a specific contact by file name |
| [**getContactAttachmentById**](AccountingApi.md#getContactAttachmentById) | **GET** /Contacts/{ContactID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific contact using a unique attachment Id |
| [**getContactAttachments**](AccountingApi.md#getContactAttachments) | **GET** /Contacts/{ContactID}/Attachments | Retrieves attachments for a specific contact in a Xero organisation |
| [**getContactByContactNumber**](AccountingApi.md#getContactByContactNumber) | **GET** /Contacts/{ContactNumber} | Retrieves a specific contact by contact number in a Xero organisation |
| [**getContactCISSettings**](AccountingApi.md#getContactCISSettings) | **GET** /Contacts/{ContactID}/CISSettings | Retrieves CIS settings for a specific contact in a Xero organisation |
| [**getContactGroup**](AccountingApi.md#getContactGroup) | **GET** /ContactGroups/{ContactGroupID} | Retrieves a specific contact group by using a unique contact group Id |
| [**getContactGroups**](AccountingApi.md#getContactGroups) | **GET** /ContactGroups | Retrieves the contact Id and name of all the contacts in a contact group |
| [**getContactHistory**](AccountingApi.md#getContactHistory) | **GET** /Contacts/{ContactID}/History | Retrieves history records for a specific contact |
| [**getContacts**](AccountingApi.md#getContacts) | **GET** /Contacts | Retrieves all contacts in a Xero organisation |
| [**getCreditNote**](AccountingApi.md#getCreditNote) | **GET** /CreditNotes/{CreditNoteID} | Retrieves a specific credit note using a unique credit note Id |
| [**getCreditNoteAsPdf**](AccountingApi.md#getCreditNoteAsPdf) | **GET** /CreditNotes/{CreditNoteID}/pdf | Retrieves credit notes as PDF files |
| [**getCreditNoteAttachmentByFileName**](AccountingApi.md#getCreditNoteAttachmentByFileName) | **GET** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Retrieves a specific attachment on a specific credit note by file name |
| [**getCreditNoteAttachmentById**](AccountingApi.md#getCreditNoteAttachmentById) | **GET** /CreditNotes/{CreditNoteID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific credit note using a unique attachment Id |
| [**getCreditNoteAttachments**](AccountingApi.md#getCreditNoteAttachments) | **GET** /CreditNotes/{CreditNoteID}/Attachments | Retrieves attachments for a specific credit notes |
| [**getCreditNoteHistory**](AccountingApi.md#getCreditNoteHistory) | **GET** /CreditNotes/{CreditNoteID}/History | Retrieves history records of a specific credit note |
| [**getCreditNotes**](AccountingApi.md#getCreditNotes) | **GET** /CreditNotes | Retrieves any credit notes |
| [**getCurrencies**](AccountingApi.md#getCurrencies) | **GET** /Currencies | Retrieves currencies for your Xero organisation |
| [**getEmployee**](AccountingApi.md#getEmployee) | **GET** /Employees/{EmployeeID} | Retrieves a specific employee used in Xero payrun using a unique employee Id |
| [**getEmployees**](AccountingApi.md#getEmployees) | **GET** /Employees | Retrieves employees used in Xero payrun |
| [**getExpenseClaim**](AccountingApi.md#getExpenseClaim) | **GET** /ExpenseClaims/{ExpenseClaimID} | Retrieves a specific expense claim using a unique expense claim Id |
| [**getExpenseClaimHistory**](AccountingApi.md#getExpenseClaimHistory) | **GET** /ExpenseClaims/{ExpenseClaimID}/History | Retrieves history records of a specific expense claim |
| [**getExpenseClaims**](AccountingApi.md#getExpenseClaims) | **GET** /ExpenseClaims | Retrieves expense claims |
| [**getInvoice**](AccountingApi.md#getInvoice) | **GET** /Invoices/{InvoiceID} | Retrieves a specific sales invoice or purchase bill using a unique invoice Id |
| [**getInvoiceAsPdf**](AccountingApi.md#getInvoiceAsPdf) | **GET** /Invoices/{InvoiceID}/pdf | Retrieves invoices or purchase bills as PDF files |
| [**getInvoiceAttachmentByFileName**](AccountingApi.md#getInvoiceAttachmentByFileName) | **GET** /Invoices/{InvoiceID}/Attachments/{FileName} | Retrieves an attachment from a specific invoice or purchase bill by filename |
| [**getInvoiceAttachmentById**](AccountingApi.md#getInvoiceAttachmentById) | **GET** /Invoices/{InvoiceID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific invoices or purchase bills by using a unique attachment Id |
| [**getInvoiceAttachments**](AccountingApi.md#getInvoiceAttachments) | **GET** /Invoices/{InvoiceID}/Attachments | Retrieves attachments for a specific invoice or purchase bill |
| [**getInvoiceHistory**](AccountingApi.md#getInvoiceHistory) | **GET** /Invoices/{InvoiceID}/History | Retrieves history records for a specific invoice |
| [**getInvoiceReminders**](AccountingApi.md#getInvoiceReminders) | **GET** /InvoiceReminders/Settings | Retrieves invoice reminder settings |
| [**getInvoices**](AccountingApi.md#getInvoices) | **GET** /Invoices | Retrieves sales invoices or purchase bills |
| [**getItem**](AccountingApi.md#getItem) | **GET** /Items/{ItemID} | Retrieves a specific item using a unique item Id |
| [**getItemHistory**](AccountingApi.md#getItemHistory) | **GET** /Items/{ItemID}/History | Retrieves history for a specific item |
| [**getItems**](AccountingApi.md#getItems) | **GET** /Items | Retrieves items |
| [**getJournal**](AccountingApi.md#getJournal) | **GET** /Journals/{JournalID} | Retrieves a specific journal using a unique journal Id. |
| [**getJournals**](AccountingApi.md#getJournals) | **GET** /Journals | Retrieves journals |
| [**getLinkedTransaction**](AccountingApi.md#getLinkedTransaction) | **GET** /LinkedTransactions/{LinkedTransactionID} | Retrieves a specific linked transaction (billable expenses) using a unique linked transaction Id |
| [**getLinkedTransactions**](AccountingApi.md#getLinkedTransactions) | **GET** /LinkedTransactions | Retrieves linked transactions (billable expenses) |
| [**getManualJournal**](AccountingApi.md#getManualJournal) | **GET** /ManualJournals/{ManualJournalID} | Retrieves a specific manual journal |
| [**getManualJournalAttachmentByFileName**](AccountingApi.md#getManualJournalAttachmentByFileName) | **GET** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Retrieves a specific attachment from a specific manual journal by file name |
| [**getManualJournalAttachmentById**](AccountingApi.md#getManualJournalAttachmentById) | **GET** /ManualJournals/{ManualJournalID}/Attachments/{AttachmentID} | Allows you to retrieve a specific attachment from a specific manual journal using a unique attachment Id |
| [**getManualJournalAttachments**](AccountingApi.md#getManualJournalAttachments) | **GET** /ManualJournals/{ManualJournalID}/Attachments | Retrieves attachment for a specific manual journal |
| [**getManualJournals**](AccountingApi.md#getManualJournals) | **GET** /ManualJournals | Retrieves manual journals |
| [**getManualJournalsHistory**](AccountingApi.md#getManualJournalsHistory) | **GET** /ManualJournals/{ManualJournalID}/History | Retrieves history for a specific manual journal |
| [**getOnlineInvoice**](AccountingApi.md#getOnlineInvoice) | **GET** /Invoices/{InvoiceID}/OnlineInvoice | Retrieves a URL to an online invoice |
| [**getOrganisationActions**](AccountingApi.md#getOrganisationActions) | **GET** /Organisation/Actions | Retrieves a list of the key actions your app has permission to perform in the connected Xero organisation. |
| [**getOrganisationCISSettings**](AccountingApi.md#getOrganisationCISSettings) | **GET** /Organisation/{OrganisationID}/CISSettings | Retrieves the CIS settings for the Xero organistaion. |
| [**getOrganisations**](AccountingApi.md#getOrganisations) | **GET** /Organisation | Retrieves Xero organisation details |
| [**getOverpayment**](AccountingApi.md#getOverpayment) | **GET** /Overpayments/{OverpaymentID} | Retrieves a specific overpayment using a unique overpayment Id |
| [**getOverpaymentHistory**](AccountingApi.md#getOverpaymentHistory) | **GET** /Overpayments/{OverpaymentID}/History | Retrieves history records of a specific overpayment |
| [**getOverpayments**](AccountingApi.md#getOverpayments) | **GET** /Overpayments | Retrieves overpayments |
| [**getPayment**](AccountingApi.md#getPayment) | **GET** /Payments/{PaymentID} | Retrieves a specific payment for invoices and credit notes using a unique payment Id |
| [**getPaymentHistory**](AccountingApi.md#getPaymentHistory) | **GET** /Payments/{PaymentID}/History | Retrieves history records of a specific payment |
| [**getPaymentServices**](AccountingApi.md#getPaymentServices) | **GET** /PaymentServices | Retrieves payment services |
| [**getPayments**](AccountingApi.md#getPayments) | **GET** /Payments | Retrieves payments for invoices and credit notes |
| [**getPrepayment**](AccountingApi.md#getPrepayment) | **GET** /Prepayments/{PrepaymentID} | Allows you to retrieve a specified prepayments |
| [**getPrepaymentHistory**](AccountingApi.md#getPrepaymentHistory) | **GET** /Prepayments/{PrepaymentID}/History | Retrieves history record for a specific prepayment |
| [**getPrepayments**](AccountingApi.md#getPrepayments) | **GET** /Prepayments | Retrieves prepayments |
| [**getPurchaseOrder**](AccountingApi.md#getPurchaseOrder) | **GET** /PurchaseOrders/{PurchaseOrderID} | Retrieves a specific purchase order using a unique purchase order Id |
| [**getPurchaseOrderAsPdf**](AccountingApi.md#getPurchaseOrderAsPdf) | **GET** /PurchaseOrders/{PurchaseOrderID}/pdf | Retrieves specific purchase order as PDF files using a unique purchase order Id |
| [**getPurchaseOrderAttachmentByFileName**](AccountingApi.md#getPurchaseOrderAttachmentByFileName) | **GET** /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName} | Retrieves a specific attachment for a specific purchase order by filename |
| [**getPurchaseOrderAttachmentById**](AccountingApi.md#getPurchaseOrderAttachmentById) | **GET** /PurchaseOrders/{PurchaseOrderID}/Attachments/{AttachmentID} | Retrieves specific attachment for a specific purchase order using a unique attachment Id |
| [**getPurchaseOrderAttachments**](AccountingApi.md#getPurchaseOrderAttachments) | **GET** /PurchaseOrders/{PurchaseOrderID}/Attachments | Retrieves attachments for a specific purchase order |
| [**getPurchaseOrderByNumber**](AccountingApi.md#getPurchaseOrderByNumber) | **GET** /PurchaseOrders/{PurchaseOrderNumber} | Retrieves a specific purchase order using purchase order number |
| [**getPurchaseOrderHistory**](AccountingApi.md#getPurchaseOrderHistory) | **GET** /PurchaseOrders/{PurchaseOrderID}/History | Retrieves history for a specific purchase order |
| [**getPurchaseOrders**](AccountingApi.md#getPurchaseOrders) | **GET** /PurchaseOrders | Retrieves purchase orders |
| [**getQuote**](AccountingApi.md#getQuote) | **GET** /Quotes/{QuoteID} | Retrieves a specific quote using a unique quote Id |
| [**getQuoteAsPdf**](AccountingApi.md#getQuoteAsPdf) | **GET** /Quotes/{QuoteID}/pdf | Retrieves a specific quote as a PDF file using a unique quote Id |
| [**getQuoteAttachmentByFileName**](AccountingApi.md#getQuoteAttachmentByFileName) | **GET** /Quotes/{QuoteID}/Attachments/{FileName} | Retrieves a specific attachment from a specific quote by filename |
| [**getQuoteAttachmentById**](AccountingApi.md#getQuoteAttachmentById) | **GET** /Quotes/{QuoteID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific quote using a unique attachment Id |
| [**getQuoteAttachments**](AccountingApi.md#getQuoteAttachments) | **GET** /Quotes/{QuoteID}/Attachments | Retrieves attachments for a specific quote |
| [**getQuoteHistory**](AccountingApi.md#getQuoteHistory) | **GET** /Quotes/{QuoteID}/History | Retrieves history records of a specific quote |
| [**getQuotes**](AccountingApi.md#getQuotes) | **GET** /Quotes | Retrieves sales quotes |
| [**getReceipt**](AccountingApi.md#getReceipt) | **GET** /Receipts/{ReceiptID} | Retrieves a specific draft expense claim receipt by using a unique receipt Id |
| [**getReceiptAttachmentByFileName**](AccountingApi.md#getReceiptAttachmentByFileName) | **GET** /Receipts/{ReceiptID}/Attachments/{FileName} | Retrieves a specific attachment from a specific expense claim receipts by file name |
| [**getReceiptAttachmentById**](AccountingApi.md#getReceiptAttachmentById) | **GET** /Receipts/{ReceiptID}/Attachments/{AttachmentID} | Retrieves a specific attachments from a specific expense claim receipts by using a unique attachment Id |
| [**getReceiptAttachments**](AccountingApi.md#getReceiptAttachments) | **GET** /Receipts/{ReceiptID}/Attachments | Retrieves attachments for a specific expense claim receipt |
| [**getReceiptHistory**](AccountingApi.md#getReceiptHistory) | **GET** /Receipts/{ReceiptID}/History | Retrieves a history record for a specific receipt |
| [**getReceipts**](AccountingApi.md#getReceipts) | **GET** /Receipts | Retrieves draft expense claim receipts for any user |
| [**getRepeatingInvoice**](AccountingApi.md#getRepeatingInvoice) | **GET** /RepeatingInvoices/{RepeatingInvoiceID} | Retrieves a specific repeating invoice by using a unique repeating invoice Id |
| [**getRepeatingInvoiceAttachmentByFileName**](AccountingApi.md#getRepeatingInvoiceAttachmentByFileName) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Retrieves a specific attachment from a specific repeating invoices by file name |
| [**getRepeatingInvoiceAttachmentById**](AccountingApi.md#getRepeatingInvoiceAttachmentById) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{AttachmentID} | Retrieves a specific attachment from a specific repeating invoice |
| [**getRepeatingInvoiceAttachments**](AccountingApi.md#getRepeatingInvoiceAttachments) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments | Retrieves attachments from a specific repeating invoice |
| [**getRepeatingInvoiceHistory**](AccountingApi.md#getRepeatingInvoiceHistory) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/History | Retrieves history record for a specific repeating invoice |
| [**getRepeatingInvoices**](AccountingApi.md#getRepeatingInvoices) | **GET** /RepeatingInvoices | Retrieves repeating invoices |
| [**getReportAgedPayablesByContact**](AccountingApi.md#getReportAgedPayablesByContact) | **GET** /Reports/AgedPayablesByContact | Retrieves report for aged payables by contact |
| [**getReportAgedReceivablesByContact**](AccountingApi.md#getReportAgedReceivablesByContact) | **GET** /Reports/AgedReceivablesByContact | Retrieves report for aged receivables by contact |
| [**getReportBASorGST**](AccountingApi.md#getReportBASorGST) | **GET** /Reports/{ReportID} | Retrieves a specific report for BAS using a unique report Id (only valid for AU orgs) |
| [**getReportBASorGSTList**](AccountingApi.md#getReportBASorGSTList) | **GET** /Reports | Retrieves report for BAS (only valid for AU orgs) |
| [**getReportBalanceSheet**](AccountingApi.md#getReportBalanceSheet) | **GET** /Reports/BalanceSheet | Retrieves report for balancesheet |
| [**getReportBankSummary**](AccountingApi.md#getReportBankSummary) | **GET** /Reports/BankSummary | Retrieves report for bank summary |
| [**getReportBudgetSummary**](AccountingApi.md#getReportBudgetSummary) | **GET** /Reports/BudgetSummary | Retrieves report for budget summary |
| [**getReportExecutiveSummary**](AccountingApi.md#getReportExecutiveSummary) | **GET** /Reports/ExecutiveSummary | Retrieves report for executive summary |
| [**getReportProfitAndLoss**](AccountingApi.md#getReportProfitAndLoss) | **GET** /Reports/ProfitAndLoss | Retrieves report for profit and loss |
| [**getReportTenNinetyNine**](AccountingApi.md#getReportTenNinetyNine) | **GET** /Reports/TenNinetyNine | Retrieve reports for 1099 |
| [**getReportTrialBalance**](AccountingApi.md#getReportTrialBalance) | **GET** /Reports/TrialBalance | Retrieves report for trial balance |
| [**getTaxRates**](AccountingApi.md#getTaxRates) | **GET** /TaxRates | Retrieves tax rates |
| [**getTrackingCategories**](AccountingApi.md#getTrackingCategories) | **GET** /TrackingCategories | Retrieves tracking categories and options |
| [**getTrackingCategory**](AccountingApi.md#getTrackingCategory) | **GET** /TrackingCategories/{TrackingCategoryID} | Retrieves specific tracking categories and options using a unique tracking category Id |
| [**getUser**](AccountingApi.md#getUser) | **GET** /Users/{UserID} | Retrieves a specific user |
| [**getUsers**](AccountingApi.md#getUsers) | **GET** /Users | Retrieves users |
| [**postSetup**](AccountingApi.md#postSetup) | **POST** /Setup | Sets the chart of accounts, the conversion date and conversion balances |
| [**updateAccount**](AccountingApi.md#updateAccount) | **POST** /Accounts/{AccountID} | Updates a chart of accounts |
| [**updateAccountAttachmentByFileName**](AccountingApi.md#updateAccountAttachmentByFileName) | **POST** /Accounts/{AccountID}/Attachments/{FileName} | Updates attachment on a specific account by filename |
| [**updateBankTransaction**](AccountingApi.md#updateBankTransaction) | **POST** /BankTransactions/{BankTransactionID} | Updates a single spent or received money transaction |
| [**updateBankTransactionAttachmentByFileName**](AccountingApi.md#updateBankTransactionAttachmentByFileName) | **POST** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Updates a specific attachment from a specific bank transaction by filename |
| [**updateBankTransferAttachmentByFileName**](AccountingApi.md#updateBankTransferAttachmentByFileName) | **POST** /BankTransfers/{BankTransferID}/Attachments/{FileName} |  |
| [**updateContact**](AccountingApi.md#updateContact) | **POST** /Contacts/{ContactID} | Updates a specific contact in a Xero organisation |
| [**updateContactAttachmentByFileName**](AccountingApi.md#updateContactAttachmentByFileName) | **POST** /Contacts/{ContactID}/Attachments/{FileName} |  |
| [**updateContactGroup**](AccountingApi.md#updateContactGroup) | **POST** /ContactGroups/{ContactGroupID} | Updates a specific contact group |
| [**updateCreditNote**](AccountingApi.md#updateCreditNote) | **POST** /CreditNotes/{CreditNoteID} | Updates a specific credit note |
| [**updateCreditNoteAttachmentByFileName**](AccountingApi.md#updateCreditNoteAttachmentByFileName) | **POST** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Updates attachments on a specific credit note by file name |
| [**updateExpenseClaim**](AccountingApi.md#updateExpenseClaim) | **POST** /ExpenseClaims/{ExpenseClaimID} | Updates a specific expense claims |
| [**updateInvoice**](AccountingApi.md#updateInvoice) | **POST** /Invoices/{InvoiceID} | Updates a specific sales invoices or purchase bills |
| [**updateInvoiceAttachmentByFileName**](AccountingApi.md#updateInvoiceAttachmentByFileName) | **POST** /Invoices/{InvoiceID}/Attachments/{FileName} | Updates an attachment from a specific invoices or purchase bill by filename |
| [**updateItem**](AccountingApi.md#updateItem) | **POST** /Items/{ItemID} | Updates a specific item |
| [**updateLinkedTransaction**](AccountingApi.md#updateLinkedTransaction) | **POST** /LinkedTransactions/{LinkedTransactionID} | Updates a specific linked transactions (billable expenses) |
| [**updateManualJournal**](AccountingApi.md#updateManualJournal) | **POST** /ManualJournals/{ManualJournalID} | Updates a specific manual journal |
| [**updateManualJournalAttachmentByFileName**](AccountingApi.md#updateManualJournalAttachmentByFileName) | **POST** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Updates a specific attachment from a specific manual journal by file name |
| [**updateOrCreateBankTransactions**](AccountingApi.md#updateOrCreateBankTransactions) | **POST** /BankTransactions | Updates or creates one or more spent or received money transaction |
| [**updateOrCreateContacts**](AccountingApi.md#updateOrCreateContacts) | **POST** /Contacts | Updates or creates one or more contacts in a Xero organisation |
| [**updateOrCreateCreditNotes**](AccountingApi.md#updateOrCreateCreditNotes) | **POST** /CreditNotes | Updates or creates one or more credit notes |
| [**updateOrCreateEmployees**](AccountingApi.md#updateOrCreateEmployees) | **POST** /Employees | Creates a single new employees used in Xero payrun |
| [**updateOrCreateInvoices**](AccountingApi.md#updateOrCreateInvoices) | **POST** /Invoices | Updates or creates one or more sales invoices or purchase bills |
| [**updateOrCreateItems**](AccountingApi.md#updateOrCreateItems) | **POST** /Items | Updates or creates one or more items |
| [**updateOrCreateManualJournals**](AccountingApi.md#updateOrCreateManualJournals) | **POST** /ManualJournals | Updates or creates a single manual journal |
| [**updateOrCreatePurchaseOrders**](AccountingApi.md#updateOrCreatePurchaseOrders) | **POST** /PurchaseOrders | Updates or creates one or more purchase orders |
| [**updateOrCreateQuotes**](AccountingApi.md#updateOrCreateQuotes) | **POST** /Quotes | Updates or creates one or more quotes |
| [**updatePurchaseOrder**](AccountingApi.md#updatePurchaseOrder) | **POST** /PurchaseOrders/{PurchaseOrderID} | Updates a specific purchase order |
| [**updatePurchaseOrderAttachmentByFileName**](AccountingApi.md#updatePurchaseOrderAttachmentByFileName) | **POST** /PurchaseOrders/{PurchaseOrderID}/Attachments/{FileName} | Updates a specific attachment for a specific purchase order by filename |
| [**updateQuote**](AccountingApi.md#updateQuote) | **POST** /Quotes/{QuoteID} | Updates a specific quote |
| [**updateQuoteAttachmentByFileName**](AccountingApi.md#updateQuoteAttachmentByFileName) | **POST** /Quotes/{QuoteID}/Attachments/{FileName} | Updates a specific attachment from a specific quote by filename |
| [**updateReceipt**](AccountingApi.md#updateReceipt) | **POST** /Receipts/{ReceiptID} | Updates a specific draft expense claim receipts |
| [**updateReceiptAttachmentByFileName**](AccountingApi.md#updateReceiptAttachmentByFileName) | **POST** /Receipts/{ReceiptID}/Attachments/{FileName} | Updates a specific attachment on a specific expense claim receipts by file name |
| [**updateRepeatingInvoiceAttachmentByFileName**](AccountingApi.md#updateRepeatingInvoiceAttachmentByFileName) | **POST** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Updates a specific attachment from a specific repeating invoices by file name |
| [**updateTaxRate**](AccountingApi.md#updateTaxRate) | **POST** /TaxRates | Updates tax rates |
| [**updateTrackingCategory**](AccountingApi.md#updateTrackingCategory) | **POST** /TrackingCategories/{TrackingCategoryID} | Updates a specific tracking category |
| [**updateTrackingOptions**](AccountingApi.md#updateTrackingOptions) | **POST** /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} | Updates a specific option for a specific tracking category |


<a id="createAccount"></a>
# **createAccount**
> Accounts createAccount(xeroTenantId, account)

Creates a new chart of accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Account account = new Account(); // Account | Account object in body of request
    try {
      Accounts result = apiInstance.createAccount(xeroTenantId, account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **account** | [**Account**](Account.md)| Account object in body of request | |

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - created new Account and return response of type Accounts array with new Account |  -  |
| **400** | Validation Error - some data was incorrect returns response of type Error |  -  |

<a id="createAccountAttachmentByFileName"></a>
# **createAccountAttachmentByFileName**
> Attachments createAccountAttachmentByFileName(xeroTenantId, accountID, fileName, body)

Creates an attachment on a specific account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID accountID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Account object
    String fileName = "xero-dev.jpg"; // String | Name of the attachment
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.createAccountAttachmentByFileName(xeroTenantId, accountID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createAccountAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **accountID** | **UUID**| Unique identifier for Account object | |
| **fileName** | **String**| Name of the attachment | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Attachment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createBankTransactionAttachmentByFileName"></a>
# **createBankTransactionAttachmentByFileName**
> Attachments createBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, body)

Creates an attachment for a specific bank transaction by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transaction
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.createBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createBankTransactionAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactionID** | **UUID**| Xero generated unique identifier for a bank transaction | |
| **fileName** | **String**| The name of the file being attached | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of Attachments array of Attachment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createBankTransactionHistoryRecord"></a>
# **createBankTransactionHistoryRecord**
> HistoryRecords createBankTransactionHistoryRecord(xeroTenantId, bankTransactionID, historyRecords)

Creates a history record for a specific bank transactions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transaction
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createBankTransactionHistoryRecord(xeroTenantId, bankTransactionID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createBankTransactionHistoryRecord");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactionID** | **UUID**| Xero generated unique identifier for a bank transaction | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createBankTransactions"></a>
# **createBankTransactions**
> BankTransactions createBankTransactions(xeroTenantId, bankTransactions, summarizeErrors, unitdp)

Creates one or more spent or received money transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    BankTransactions bankTransactions = new BankTransactions(); // BankTransactions | BankTransactions with an array of BankTransaction objects in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      BankTransactions result = apiInstance.createBankTransactions(xeroTenantId, bankTransactions, summarizeErrors, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createBankTransactions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactions** | [**BankTransactions**](BankTransactions.md)| BankTransactions with an array of BankTransaction objects in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type BankTransactions array with new BankTransaction |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createBankTransfer"></a>
# **createBankTransfer**
> BankTransfers createBankTransfer(xeroTenantId, bankTransfers)

Creates a bank transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    BankTransfers bankTransfers = new BankTransfers(); // BankTransfers | BankTransfers with array of BankTransfer objects in request body
    try {
      BankTransfers result = apiInstance.createBankTransfer(xeroTenantId, bankTransfers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createBankTransfer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransfers** | [**BankTransfers**](BankTransfers.md)| BankTransfers with array of BankTransfer objects in request body | |

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of BankTransfers array of one BankTransfer |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createBankTransferAttachmentByFileName"></a>
# **createBankTransferAttachmentByFileName**
> Attachments createBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransferID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transfer
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Bank Transfer
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.createBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createBankTransferAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransferID** | **UUID**| Xero generated unique identifier for a bank transfer | |
| **fileName** | **String**| The name of the file being attached to a Bank Transfer | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of Attachments array of 0 to N Attachment for a Bank Transfer |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createBankTransferHistoryRecord"></a>
# **createBankTransferHistoryRecord**
> HistoryRecords createBankTransferHistoryRecord(xeroTenantId, bankTransferID, historyRecords)

Creates a history record for a specific bank transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransferID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transfer
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createBankTransferHistoryRecord(xeroTenantId, bankTransferID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createBankTransferHistoryRecord");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransferID** | **UUID**| Xero generated unique identifier for a bank transfer | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createBatchPayment"></a>
# **createBatchPayment**
> BatchPayments createBatchPayment(xeroTenantId, batchPayments, summarizeErrors)

Creates one or many batch payments for invoices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    BatchPayments batchPayments = new BatchPayments(); // BatchPayments | BatchPayments with an array of Payments in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      BatchPayments result = apiInstance.createBatchPayment(xeroTenantId, batchPayments, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createBatchPayment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **batchPayments** | [**BatchPayments**](BatchPayments.md)| BatchPayments with an array of Payments in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**BatchPayments**](BatchPayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type BatchPayments array of BatchPayment objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createBatchPaymentHistoryRecord"></a>
# **createBatchPaymentHistoryRecord**
> HistoryRecords createBatchPaymentHistoryRecord(xeroTenantId, batchPaymentID, historyRecords)

Creates a history record for a specific batch payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID batchPaymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for BatchPayment
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createBatchPaymentHistoryRecord(xeroTenantId, batchPaymentID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createBatchPaymentHistoryRecord");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **batchPaymentID** | **UUID**| Unique identifier for BatchPayment | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createBrandingThemePaymentServices"></a>
# **createBrandingThemePaymentServices**
> PaymentServices createBrandingThemePaymentServices(xeroTenantId, brandingThemeID, paymentService)

Creates a new custom payment service for a specific branding theme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID brandingThemeID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Branding Theme
    PaymentService paymentService = new PaymentService(); // PaymentService | PaymentService object in body of request
    try {
      PaymentServices result = apiInstance.createBrandingThemePaymentServices(xeroTenantId, brandingThemeID, paymentService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createBrandingThemePaymentServices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **brandingThemeID** | **UUID**| Unique identifier for a Branding Theme | |
| **paymentService** | [**PaymentService**](PaymentService.md)| PaymentService object in body of request | |

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type PaymentServices array with newly created PaymentService |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createContactAttachmentByFileName"></a>
# **createContactAttachmentByFileName**
> Attachments createContactAttachmentByFileName(xeroTenantId, contactID, fileName, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    String fileName = "xero-dev.jpg"; // String | Name for the file you are attaching
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.createContactAttachmentByFileName(xeroTenantId, contactID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createContactAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactID** | **UUID**| Unique identifier for a Contact | |
| **fileName** | **String**| Name for the file you are attaching | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with an newly created Attachment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createContactGroup"></a>
# **createContactGroup**
> ContactGroups createContactGroup(xeroTenantId, contactGroups)

Creates a contact group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    ContactGroups contactGroups = new ContactGroups(); // ContactGroups | ContactGroups with an array of names in request body
    try {
      ContactGroups result = apiInstance.createContactGroup(xeroTenantId, contactGroups);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createContactGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactGroups** | [**ContactGroups**](ContactGroups.md)| ContactGroups with an array of names in request body | |

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contact Groups array of newly created Contact Group |  -  |
| **400** | Validation Error - some data was incorrect returns response of type Error |  -  |

<a id="createContactGroupContacts"></a>
# **createContactGroupContacts**
> Contacts createContactGroupContacts(xeroTenantId, contactGroupID, contacts)

Creates contacts to a specific contact group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactGroupID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact Group
    Contacts contacts = new Contacts(); // Contacts | Contacts with array of contacts specifying the ContactID to be added to ContactGroup in body of request
    try {
      Contacts result = apiInstance.createContactGroupContacts(xeroTenantId, contactGroupID, contacts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createContactGroupContacts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactGroupID** | **UUID**| Unique identifier for a Contact Group | |
| **contacts** | [**Contacts**](Contacts.md)| Contacts with array of contacts specifying the ContactID to be added to ContactGroup in body of request | |

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contacts array of added Contacts |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createContactHistory"></a>
# **createContactHistory**
> HistoryRecords createContactHistory(xeroTenantId, contactID, historyRecords)

Creates a new history record for a specific contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createContactHistory(xeroTenantId, contactID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createContactHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactID** | **UUID**| Unique identifier for a Contact | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createContacts"></a>
# **createContacts**
> Contacts createContacts(xeroTenantId, contacts, summarizeErrors)

Creates multiple contacts (bulk) in a Xero organisation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Contacts contacts = new Contacts(); // Contacts | Contacts with an array of Contact objects to create in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      Contacts result = apiInstance.createContacts(xeroTenantId, contacts, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createContacts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contacts** | [**Contacts**](Contacts.md)| Contacts with an array of Contact objects to create in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contacts array with newly created Contact |  -  |
| **400** | Validation Error - some data was incorrect returns response of type Error |  -  |

<a id="createCreditNoteAllocation"></a>
# **createCreditNoteAllocation**
> Allocations createCreditNoteAllocation(xeroTenantId, creditNoteID, allocations, summarizeErrors)

Creates allocation for a specific credit note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    Allocations allocations = new Allocations(); // Allocations | Allocations with array of Allocation object in body of request.
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      Allocations result = apiInstance.createCreditNoteAllocation(xeroTenantId, creditNoteID, allocations, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createCreditNoteAllocation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |
| **allocations** | [**Allocations**](Allocations.md)| Allocations with array of Allocation object in body of request. | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**Allocations**](Allocations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Allocations array with newly created Allocation for specific Credit Note |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createCreditNoteAttachmentByFileName"></a>
# **createCreditNoteAttachmentByFileName**
> Attachments createCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, body, includeOnline)

Creates an attachment for a specific credit note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    String fileName = "xero-dev.jpg"; // String | Name of the file you are attaching to Credit Note
    byte[] body = null; // byte[] | Byte array of file in body of request
    Boolean includeOnline = false; // Boolean | Allows an attachment to be seen by the end customer within their online invoice
    try {
      Attachments result = apiInstance.createCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, body, includeOnline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createCreditNoteAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |
| **fileName** | **String**| Name of the file you are attaching to Credit Note | |
| **body** | **byte[]**| Byte array of file in body of request | |
| **includeOnline** | **Boolean**| Allows an attachment to be seen by the end customer within their online invoice | [optional] [default to false] |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with newly created Attachment for specific Credit Note |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createCreditNoteHistory"></a>
# **createCreditNoteHistory**
> HistoryRecords createCreditNoteHistory(xeroTenantId, creditNoteID, historyRecords)

Retrieves history records of a specific credit note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createCreditNoteHistory(xeroTenantId, creditNoteID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createCreditNoteHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createCreditNotes"></a>
# **createCreditNotes**
> CreditNotes createCreditNotes(xeroTenantId, creditNotes, summarizeErrors, unitdp)

Creates a new credit note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    CreditNotes creditNotes = new CreditNotes(); // CreditNotes | Credit Notes with array of CreditNote object in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      CreditNotes result = apiInstance.createCreditNotes(xeroTenantId, creditNotes, summarizeErrors, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createCreditNotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNotes** | [**CreditNotes**](CreditNotes.md)| Credit Notes with array of CreditNote object in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Credit Notes array of newly created CreditNote |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createCurrency"></a>
# **createCurrency**
> Currencies createCurrency(xeroTenantId, currency)

Create a new currency for a Xero organisation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Currency currency = new Currency(); // Currency | Currency object in the body of request
    try {
      Currencies result = apiInstance.createCurrency(xeroTenantId, currency);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createCurrency");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **currency** | [**Currency**](Currency.md)| Currency object in the body of request | |

### Return type

[**Currencies**](Currencies.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unsupported - return response incorrect exception, API is not able to create new Currency |  -  |

<a id="createEmployees"></a>
# **createEmployees**
> Employees createEmployees(xeroTenantId, employees, summarizeErrors)

Creates new employees used in Xero payrun

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Employees employees = new Employees(); // Employees | Employees with array of Employee object in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      Employees result = apiInstance.createEmployees(xeroTenantId, employees, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createEmployees");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **employees** | [**Employees**](Employees.md)| Employees with array of Employee object in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Employees array with new Employee |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createExpenseClaimHistory"></a>
# **createExpenseClaimHistory**
> HistoryRecords createExpenseClaimHistory(xeroTenantId, expenseClaimID, historyRecords)

Creates a history record for a specific expense claim

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID expenseClaimID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ExpenseClaim
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createExpenseClaimHistory(xeroTenantId, expenseClaimID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createExpenseClaimHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **expenseClaimID** | **UUID**| Unique identifier for a ExpenseClaim | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |

<a id="createExpenseClaims"></a>
# **createExpenseClaims**
> ExpenseClaims createExpenseClaims(xeroTenantId, expenseClaims)

Creates expense claims

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    ExpenseClaims expenseClaims = new ExpenseClaims(); // ExpenseClaims | ExpenseClaims with array of ExpenseClaim object in body of request
    try {
      ExpenseClaims result = apiInstance.createExpenseClaims(xeroTenantId, expenseClaims);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createExpenseClaims");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **expenseClaims** | [**ExpenseClaims**](ExpenseClaims.md)| ExpenseClaims with array of ExpenseClaim object in body of request | |

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ExpenseClaims array with newly created ExpenseClaim |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createInvoiceAttachmentByFileName"></a>
# **createInvoiceAttachmentByFileName**
> Attachments createInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, body, includeOnline)

Creates an attachment for a specific invoice or purchase bill by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    String fileName = "xero-dev.jpg"; // String | Name of the file you are attaching
    byte[] body = null; // byte[] | Byte array of file in body of request
    Boolean includeOnline = false; // Boolean | Allows an attachment to be seen by the end customer within their online invoice
    try {
      Attachments result = apiInstance.createInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, body, includeOnline);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createInvoiceAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |
| **fileName** | **String**| Name of the file you are attaching | |
| **body** | **byte[]**| Byte array of file in body of request | |
| **includeOnline** | **Boolean**| Allows an attachment to be seen by the end customer within their online invoice | [optional] [default to false] |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with newly created Attachment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createInvoiceHistory"></a>
# **createInvoiceHistory**
> HistoryRecords createInvoiceHistory(xeroTenantId, invoiceID, historyRecords)

Creates a history record for a specific invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createInvoiceHistory(xeroTenantId, invoiceID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createInvoiceHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createInvoices"></a>
# **createInvoices**
> Invoices createInvoices(xeroTenantId, invoices, summarizeErrors, unitdp)

Creates one or more sales invoices or purchase bills

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Invoices invoices = new Invoices(); // Invoices | Invoices with an array of invoice objects in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Invoices result = apiInstance.createInvoices(xeroTenantId, invoices, summarizeErrors, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createInvoices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoices** | [**Invoices**](Invoices.md)| Invoices with an array of invoice objects in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Invoices array with newly created Invoice |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createItemHistory"></a>
# **createItemHistory**
> HistoryRecords createItemHistory(xeroTenantId, itemID, historyRecords)

Creates a history record for a specific item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID itemID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Item
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createItemHistory(xeroTenantId, itemID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createItemHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **itemID** | **UUID**| Unique identifier for an Item | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |

<a id="createItems"></a>
# **createItems**
> Items createItems(xeroTenantId, items, summarizeErrors, unitdp)

Creates one or more items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Items items = new Items(); // Items | Items with an array of Item objects in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Items result = apiInstance.createItems(xeroTenantId, items, summarizeErrors, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createItems");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **items** | [**Items**](Items.md)| Items with an array of Item objects in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Items array with newly created Item |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createLinkedTransaction"></a>
# **createLinkedTransaction**
> LinkedTransactions createLinkedTransaction(xeroTenantId, linkedTransaction)

Creates linked transactions (billable expenses)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    LinkedTransaction linkedTransaction = new LinkedTransaction(); // LinkedTransaction | LinkedTransaction object in body of request
    try {
      LinkedTransactions result = apiInstance.createLinkedTransaction(xeroTenantId, linkedTransaction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createLinkedTransaction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **linkedTransaction** | [**LinkedTransaction**](LinkedTransaction.md)| LinkedTransaction object in body of request | |

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type LinkedTransactions array with newly created LinkedTransaction |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createManualJournalAttachmentByFileName"></a>
# **createManualJournalAttachmentByFileName**
> Attachments createManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, body)

Creates a specific attachment for a specific manual journal by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID manualJournalID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ManualJournal
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to a ManualJournal
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.createManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createManualJournalAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournalID** | **UUID**| Unique identifier for a ManualJournal | |
| **fileName** | **String**| The name of the file being attached to a ManualJournal | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with a newly created Attachment for a ManualJournals |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createManualJournalHistoryRecord"></a>
# **createManualJournalHistoryRecord**
> HistoryRecords createManualJournalHistoryRecord(xeroTenantId, manualJournalID, historyRecords)

Creates a history record for a specific manual journal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID manualJournalID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a manual journal
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createManualJournalHistoryRecord(xeroTenantId, manualJournalID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createManualJournalHistoryRecord");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournalID** | **UUID**| Xero generated unique identifier for a manual journal | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createManualJournals"></a>
# **createManualJournals**
> ManualJournals createManualJournals(xeroTenantId, manualJournals, summarizeErrors)

Creates one or more manual journals

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    ManualJournals manualJournals = new ManualJournals(); // ManualJournals | ManualJournals array with ManualJournal object in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      ManualJournals result = apiInstance.createManualJournals(xeroTenantId, manualJournals, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createManualJournals");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournals** | [**ManualJournals**](ManualJournals.md)| ManualJournals array with ManualJournal object in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ManualJournals array with newly created ManualJournal |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createOverpaymentAllocations"></a>
# **createOverpaymentAllocations**
> Allocations createOverpaymentAllocations(xeroTenantId, overpaymentID, allocations, summarizeErrors)

Creates a single allocation for a specific overpayment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID overpaymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Overpayment
    Allocations allocations = new Allocations(); // Allocations | Allocations array with Allocation object in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      Allocations result = apiInstance.createOverpaymentAllocations(xeroTenantId, overpaymentID, allocations, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createOverpaymentAllocations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **overpaymentID** | **UUID**| Unique identifier for a Overpayment | |
| **allocations** | [**Allocations**](Allocations.md)| Allocations array with Allocation object in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**Allocations**](Allocations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Allocations array with all Allocation for Overpayments |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createOverpaymentHistory"></a>
# **createOverpaymentHistory**
> HistoryRecords createOverpaymentHistory(xeroTenantId, overpaymentID, historyRecords)

Creates a history record for a specific overpayment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID overpaymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Overpayment
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createOverpaymentHistory(xeroTenantId, overpaymentID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createOverpaymentHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **overpaymentID** | **UUID**| Unique identifier for a Overpayment | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error - API is not able to create HistoryRecord for Overpayments |  -  |

<a id="createPayment"></a>
# **createPayment**
> Payments createPayment(xeroTenantId, payment)

Creates a single payment for invoice or credit notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Payment payment = new Payment(); // Payment | Request body with a single Payment object
    try {
      Payments result = apiInstance.createPayment(xeroTenantId, payment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createPayment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **payment** | [**Payment**](Payment.md)| Request body with a single Payment object | |

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Payments array for newly created Payment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createPaymentHistory"></a>
# **createPaymentHistory**
> HistoryRecords createPaymentHistory(xeroTenantId, paymentID, historyRecords)

Creates a history record for a specific payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID paymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Payment
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createPaymentHistory(xeroTenantId, paymentID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createPaymentHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **paymentID** | **UUID**| Unique identifier for a Payment | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error - API is not able to create HistoryRecord for Payments |  -  |

<a id="createPaymentService"></a>
# **createPaymentService**
> PaymentServices createPaymentService(xeroTenantId, paymentServices)

Creates a payment service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    PaymentServices paymentServices = new PaymentServices(); // PaymentServices | PaymentServices array with PaymentService object in body of request
    try {
      PaymentServices result = apiInstance.createPaymentService(xeroTenantId, paymentServices);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createPaymentService");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **paymentServices** | [**PaymentServices**](PaymentServices.md)| PaymentServices array with PaymentService object in body of request | |

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type PaymentServices array for newly created PaymentService |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createPayments"></a>
# **createPayments**
> Payments createPayments(xeroTenantId, payments, summarizeErrors)

Creates multiple payments for invoices or credit notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Payments payments = new Payments(); // Payments | Payments array with Payment object in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      Payments result = apiInstance.createPayments(xeroTenantId, payments, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createPayments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **payments** | [**Payments**](Payments.md)| Payments array with Payment object in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Payments array for newly created Payment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createPrepaymentAllocations"></a>
# **createPrepaymentAllocations**
> Allocations createPrepaymentAllocations(xeroTenantId, prepaymentID, allocations, summarizeErrors)

Allows you to create an Allocation for prepayments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID prepaymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Prepayment
    Allocations allocations = new Allocations(); // Allocations | Allocations with an array of Allocation object in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      Allocations result = apiInstance.createPrepaymentAllocations(xeroTenantId, prepaymentID, allocations, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createPrepaymentAllocations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **prepaymentID** | **UUID**| Unique identifier for Prepayment | |
| **allocations** | [**Allocations**](Allocations.md)| Allocations with an array of Allocation object in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**Allocations**](Allocations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Allocations array of Allocation for all Prepayment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createPrepaymentHistory"></a>
# **createPrepaymentHistory**
> HistoryRecords createPrepaymentHistory(xeroTenantId, prepaymentID, historyRecords)

Creates a history record for a specific prepayment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID prepaymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a PrePayment
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createPrepaymentHistory(xeroTenantId, prepaymentID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createPrepaymentHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **prepaymentID** | **UUID**| Unique identifier for a PrePayment | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | Unsupported - return response incorrect exception, API is not able to create HistoryRecord for Expense Claims |  -  |

<a id="createPurchaseOrderAttachmentByFileName"></a>
# **createPurchaseOrderAttachmentByFileName**
> Attachments createPurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, body)

Creates attachment for a specific purchase order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID purchaseOrderID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Purchase Order object
    String fileName = "xero-dev.png"; // String | Name of the attachment
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.createPurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createPurchaseOrderAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderID** | **UUID**| Unique identifier for Purchase Order object | |
| **fileName** | **String**| Name of the attachment | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Attachment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createPurchaseOrderHistory"></a>
# **createPurchaseOrderHistory**
> HistoryRecords createPurchaseOrderHistory(xeroTenantId, purchaseOrderID, historyRecords)

Creates a history record for a specific purchase orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID purchaseOrderID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a PurchaseOrder
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createPurchaseOrderHistory(xeroTenantId, purchaseOrderID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createPurchaseOrderHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderID** | **UUID**| Unique identifier for a PurchaseOrder | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createPurchaseOrders"></a>
# **createPurchaseOrders**
> PurchaseOrders createPurchaseOrders(xeroTenantId, purchaseOrders, summarizeErrors)

Creates one or more purchase orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    PurchaseOrders purchaseOrders = new PurchaseOrders(); // PurchaseOrders | PurchaseOrders with an array of PurchaseOrder object in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      PurchaseOrders result = apiInstance.createPurchaseOrders(xeroTenantId, purchaseOrders, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createPurchaseOrders");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrders** | [**PurchaseOrders**](PurchaseOrders.md)| PurchaseOrders with an array of PurchaseOrder object in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type PurchaseOrder array for specified PurchaseOrder |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createQuoteAttachmentByFileName"></a>
# **createQuoteAttachmentByFileName**
> Attachments createQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, body)

Creates attachment for a specific quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID quoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Quote object
    String fileName = "xero-dev.jpg"; // String | Name of the attachment
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.createQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createQuoteAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quoteID** | **UUID**| Unique identifier for Quote object | |
| **fileName** | **String**| Name of the attachment | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Attachment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createQuoteHistory"></a>
# **createQuoteHistory**
> HistoryRecords createQuoteHistory(xeroTenantId, quoteID, historyRecords)

Creates a history record for a specific quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID quoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Quote
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createQuoteHistory(xeroTenantId, quoteID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createQuoteHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quoteID** | **UUID**| Unique identifier for an Quote | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createQuotes"></a>
# **createQuotes**
> Quotes createQuotes(xeroTenantId, quotes, summarizeErrors)

Create one or more quotes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Quotes quotes = new Quotes(); // Quotes | Quotes with an array of Quote object in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      Quotes result = apiInstance.createQuotes(xeroTenantId, quotes, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createQuotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quotes** | [**Quotes**](Quotes.md)| Quotes with an array of Quote object in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Quotes with array with newly created Quote |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createReceipt"></a>
# **createReceipt**
> Receipts createReceipt(xeroTenantId, receipts, unitdp)

Creates draft expense claim receipts for any user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Receipts receipts = new Receipts(); // Receipts | Receipts with an array of Receipt object in body of request
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Receipts result = apiInstance.createReceipt(xeroTenantId, receipts, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createReceipt");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **receipts** | [**Receipts**](Receipts.md)| Receipts with an array of Receipt object in body of request | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Receipts array for newly created Receipt |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createReceiptAttachmentByFileName"></a>
# **createReceiptAttachmentByFileName**
> Attachments createReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, body)

Creates an attachment on a specific expense claim receipts by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID receiptID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Receipt
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to the Receipt
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.createReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createReceiptAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **receiptID** | **UUID**| Unique identifier for a Receipt | |
| **fileName** | **String**| The name of the file being attached to the Receipt | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with newly created Attachment for a specified Receipt |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createReceiptHistory"></a>
# **createReceiptHistory**
> HistoryRecords createReceiptHistory(xeroTenantId, receiptID, historyRecords)

Creates a history record for a specific receipt

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID receiptID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Receipt
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createReceiptHistory(xeroTenantId, receiptID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createReceiptHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **receiptID** | **UUID**| Unique identifier for a Receipt | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | Unsupported - return response incorrect exception, API is not able to create HistoryRecord for Receipts |  -  |

<a id="createRepeatingInvoiceAttachmentByFileName"></a>
# **createRepeatingInvoiceAttachmentByFileName**
> Attachments createRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, body)

Creates an attachment from a specific repeating invoices by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID repeatingInvoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Repeating Invoice
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Repeating Invoice
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.createRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createRepeatingInvoiceAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **repeatingInvoiceID** | **UUID**| Unique identifier for a Repeating Invoice | |
| **fileName** | **String**| The name of the file being attached to a Repeating Invoice | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with updated Attachment for a specified Repeating Invoice |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createRepeatingInvoiceHistory"></a>
# **createRepeatingInvoiceHistory**
> HistoryRecords createRepeatingInvoiceHistory(xeroTenantId, repeatingInvoiceID, historyRecords)

Creates a  history record for a specific repeating invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID repeatingInvoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Repeating Invoice
    HistoryRecords historyRecords = new HistoryRecords(); // HistoryRecords | HistoryRecords containing an array of HistoryRecord objects in body of request
    try {
      HistoryRecords result = apiInstance.createRepeatingInvoiceHistory(xeroTenantId, repeatingInvoiceID, historyRecords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createRepeatingInvoiceHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **repeatingInvoiceID** | **UUID**| Unique identifier for a Repeating Invoice | |
| **historyRecords** | [**HistoryRecords**](HistoryRecords.md)| HistoryRecords containing an array of HistoryRecord objects in body of request | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createTaxRates"></a>
# **createTaxRates**
> TaxRates createTaxRates(xeroTenantId, taxRates)

Creates one or more tax rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    TaxRates taxRates = new TaxRates(); // TaxRates | TaxRates array with TaxRate object in body of request
    try {
      TaxRates result = apiInstance.createTaxRates(xeroTenantId, taxRates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createTaxRates");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **taxRates** | [**TaxRates**](TaxRates.md)| TaxRates array with TaxRate object in body of request | |

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TaxRates array newly created TaxRate |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createTrackingCategory"></a>
# **createTrackingCategory**
> TrackingCategories createTrackingCategory(xeroTenantId, trackingCategory)

Create tracking categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    TrackingCategory trackingCategory = new TrackingCategory(); // TrackingCategory | TrackingCategory object in body of request
    try {
      TrackingCategories result = apiInstance.createTrackingCategory(xeroTenantId, trackingCategory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createTrackingCategory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **trackingCategory** | [**TrackingCategory**](TrackingCategory.md)| TrackingCategory object in body of request | |

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TrackingCategories array of newly created TrackingCategory |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="createTrackingOptions"></a>
# **createTrackingOptions**
> TrackingOptions createTrackingOptions(xeroTenantId, trackingCategoryID, trackingOption)

Creates options for a specific tracking category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID trackingCategoryID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a TrackingCategory
    TrackingOption trackingOption = new TrackingOption(); // TrackingOption | TrackingOption object in body of request
    try {
      TrackingOptions result = apiInstance.createTrackingOptions(xeroTenantId, trackingCategoryID, trackingOption);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#createTrackingOptions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **trackingCategoryID** | **UUID**| Unique identifier for a TrackingCategory | |
| **trackingOption** | [**TrackingOption**](TrackingOption.md)| TrackingOption object in body of request | |

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TrackingOptions array of options for a specified category |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="deleteAccount"></a>
# **deleteAccount**
> Accounts deleteAccount(xeroTenantId, accountID)

Deletes a chart of accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID accountID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for retrieving single object
    try {
      Accounts result = apiInstance.deleteAccount(xeroTenantId, accountID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#deleteAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **accountID** | **UUID**| Unique identifier for retrieving single object | |

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - delete existing Account and return response of type Accounts array with deleted Account |  -  |
| **400** | Validation Error - some data was incorrect returns response of type Error |  -  |

<a id="deleteContactGroupContact"></a>
# **deleteContactGroupContact**
> deleteContactGroupContact(xeroTenantId, contactGroupID, contactID)

Deletes a specific contact from a contact group using a unique contact Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactGroupID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact Group
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    try {
      apiInstance.deleteContactGroupContact(xeroTenantId, contactGroupID, contactID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#deleteContactGroupContact");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactGroupID** | **UUID**| Unique identifier for a Contact Group | |
| **contactID** | **UUID**| Unique identifier for a Contact | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success - return response 204 no content |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="deleteContactGroupContacts"></a>
# **deleteContactGroupContacts**
> deleteContactGroupContacts(xeroTenantId, contactGroupID)

Deletes all contacts from a specific contact group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactGroupID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact Group
    try {
      apiInstance.deleteContactGroupContacts(xeroTenantId, contactGroupID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#deleteContactGroupContacts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactGroupID** | **UUID**| Unique identifier for a Contact Group | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success - return response 204 no content |  -  |

<a id="deleteItem"></a>
# **deleteItem**
> deleteItem(xeroTenantId, itemID)

Deletes a specific item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID itemID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Item
    try {
      apiInstance.deleteItem(xeroTenantId, itemID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#deleteItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **itemID** | **UUID**| Unique identifier for an Item | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success - return response 204 no content |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="deleteLinkedTransaction"></a>
# **deleteLinkedTransaction**
> deleteLinkedTransaction(xeroTenantId, linkedTransactionID)

Deletes a specific linked transactions (billable expenses)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID linkedTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a LinkedTransaction
    try {
      apiInstance.deleteLinkedTransaction(xeroTenantId, linkedTransactionID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#deleteLinkedTransaction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **linkedTransactionID** | **UUID**| Unique identifier for a LinkedTransaction | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success - return response 204 no content |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="deletePayment"></a>
# **deletePayment**
> Payments deletePayment(xeroTenantId, paymentID, paymentDelete)

Updates a specific payment for invoices and credit notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID paymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Payment
    PaymentDelete paymentDelete = new PaymentDelete(); // PaymentDelete | 
    try {
      Payments result = apiInstance.deletePayment(xeroTenantId, paymentID, paymentDelete);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#deletePayment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **paymentID** | **UUID**| Unique identifier for a Payment | |
| **paymentDelete** | [**PaymentDelete**](PaymentDelete.md)|  | |

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Payments array for updated Payment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="deleteTrackingCategory"></a>
# **deleteTrackingCategory**
> TrackingCategories deleteTrackingCategory(xeroTenantId, trackingCategoryID)

Deletes a specific tracking category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID trackingCategoryID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a TrackingCategory
    try {
      TrackingCategories result = apiInstance.deleteTrackingCategory(xeroTenantId, trackingCategoryID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#deleteTrackingCategory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **trackingCategoryID** | **UUID**| Unique identifier for a TrackingCategory | |

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TrackingCategories array of deleted TrackingCategory |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="deleteTrackingOptions"></a>
# **deleteTrackingOptions**
> TrackingOptions deleteTrackingOptions(xeroTenantId, trackingCategoryID, trackingOptionID)

Deletes a specific option for a specific tracking category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID trackingCategoryID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a TrackingCategory
    UUID trackingOptionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Tracking Option
    try {
      TrackingOptions result = apiInstance.deleteTrackingOptions(xeroTenantId, trackingCategoryID, trackingOptionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#deleteTrackingOptions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **trackingCategoryID** | **UUID**| Unique identifier for a TrackingCategory | |
| **trackingOptionID** | **UUID**| Unique identifier for a Tracking Option | |

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TrackingOptions array of remaining options for a specified category |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="emailInvoice"></a>
# **emailInvoice**
> emailInvoice(xeroTenantId, invoiceID, requestEmpty)

Sends a copy of a specific invoice to related contact via email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    RequestEmpty requestEmpty = new RequestEmpty(); // RequestEmpty | 
    try {
      apiInstance.emailInvoice(xeroTenantId, invoiceID, requestEmpty);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#emailInvoice");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |
| **requestEmpty** | [**RequestEmpty**](RequestEmpty.md)|  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success - return response 204 no content |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="getAccount"></a>
# **getAccount**
> Accounts getAccount(xeroTenantId, accountID)

Retrieves a single chart of accounts by using a unique account Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID accountID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for retrieving single object
    try {
      Accounts result = apiInstance.getAccount(xeroTenantId, accountID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **accountID** | **UUID**| Unique identifier for retrieving single object | |

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Accounts array with one Account |  -  |

<a id="getAccountAttachmentByFileName"></a>
# **getAccountAttachmentByFileName**
> File getAccountAttachmentByFileName(xeroTenantId, accountID, fileName, contentType)

Retrieves an attachment for a specific account by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID accountID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Account object
    String fileName = "xero-dev.jpg"; // String | Name of the attachment
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getAccountAttachmentByFileName(xeroTenantId, accountID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getAccountAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **accountID** | **UUID**| Unique identifier for Account object | |
| **fileName** | **String**| Name of the attachment | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Account as binary data |  -  |

<a id="getAccountAttachmentById"></a>
# **getAccountAttachmentById**
> File getAccountAttachmentById(xeroTenantId, accountID, attachmentID, contentType)

Retrieves a specific attachment from a specific account using a unique attachment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID accountID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Account object
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Attachment object
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getAccountAttachmentById(xeroTenantId, accountID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getAccountAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **accountID** | **UUID**| Unique identifier for Account object | |
| **attachmentID** | **UUID**| Unique identifier for Attachment object | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Account as binary data |  -  |

<a id="getAccountAttachments"></a>
# **getAccountAttachments**
> Attachments getAccountAttachments(xeroTenantId, accountID)

Retrieves attachments for a specific accounts by using a unique account Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID accountID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Account object
    try {
      Attachments result = apiInstance.getAccountAttachments(xeroTenantId, accountID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getAccountAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **accountID** | **UUID**| Unique identifier for Account object | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Attachment |  -  |

<a id="getAccounts"></a>
# **getAccounts**
> Accounts getAccounts(xeroTenantId, ifModifiedSince, where, order)

Retrieves the full chart of accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==&quot;ACTIVE&quot; AND Type==&quot;BANK&quot;"; // String | Filter by an any element
    String order = "Name ASC"; // String | Order by an any element
    try {
      Accounts result = apiInstance.getAccounts(xeroTenantId, ifModifiedSince, where, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getAccounts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Accounts array with 0 to n Account |  -  |

<a id="getBankTransaction"></a>
# **getBankTransaction**
> BankTransactions getBankTransaction(xeroTenantId, bankTransactionID, unitdp)

Retrieves a single spent or received money transaction by using a unique bank transaction Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transaction
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      BankTransactions result = apiInstance.getBankTransaction(xeroTenantId, bankTransactionID, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransaction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactionID** | **UUID**| Xero generated unique identifier for a bank transaction | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type BankTransactions array with a specific BankTransaction |  -  |

<a id="getBankTransactionAttachmentByFileName"></a>
# **getBankTransactionAttachmentByFileName**
> File getBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, contentType)

Retrieves a specific attachment from a specific bank transaction by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transaction
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransactionAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactionID** | **UUID**| Xero generated unique identifier for a bank transaction | |
| **fileName** | **String**| The name of the file being attached | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for BankTransaction as binary data |  -  |

<a id="getBankTransactionAttachmentById"></a>
# **getBankTransactionAttachmentById**
> File getBankTransactionAttachmentById(xeroTenantId, bankTransactionID, attachmentID, contentType)

Retrieves specific attachments from a specific BankTransaction using a unique attachment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transaction
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for an attachment
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getBankTransactionAttachmentById(xeroTenantId, bankTransactionID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransactionAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactionID** | **UUID**| Xero generated unique identifier for a bank transaction | |
| **attachmentID** | **UUID**| Xero generated unique identifier for an attachment | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for BankTransaction as binary data |  -  |

<a id="getBankTransactionAttachments"></a>
# **getBankTransactionAttachments**
> Attachments getBankTransactionAttachments(xeroTenantId, bankTransactionID)

Retrieves any attachments from a specific bank transactions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transaction
    try {
      Attachments result = apiInstance.getBankTransactionAttachments(xeroTenantId, bankTransactionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransactionAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactionID** | **UUID**| Xero generated unique identifier for a bank transaction | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with 0 to n Attachment |  -  |

<a id="getBankTransactions"></a>
# **getBankTransactions**
> BankTransactions getBankTransactions(xeroTenantId, ifModifiedSince, where, order, page, unitdp)

Retrieves any spent or received money transactions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"AUTHORISED\""; // String | Filter by an any element
    String order = "Type ASC"; // String | Order by an any element
    Integer page = 1; // Integer | Up to 100 bank transactions will be returned in a single API call with line items details
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      BankTransactions result = apiInstance.getBankTransactions(xeroTenantId, ifModifiedSince, where, order, page, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransactions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| Up to 100 bank transactions will be returned in a single API call with line items details | [optional] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type BankTransactions array with 0 to n BankTransaction |  -  |

<a id="getBankTransactionsHistory"></a>
# **getBankTransactionsHistory**
> HistoryRecords getBankTransactionsHistory(xeroTenantId, bankTransactionID)

Retrieves history from a specific bank transaction using a unique bank transaction Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transaction
    try {
      HistoryRecords result = apiInstance.getBankTransactionsHistory(xeroTenantId, bankTransactionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransactionsHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactionID** | **UUID**| Xero generated unique identifier for a bank transaction | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getBankTransfer"></a>
# **getBankTransfer**
> BankTransfers getBankTransfer(xeroTenantId, bankTransferID)

Retrieves specific bank transfers by using a unique bank transfer Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransferID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transfer
    try {
      BankTransfers result = apiInstance.getBankTransfer(xeroTenantId, bankTransferID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransfer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransferID** | **UUID**| Xero generated unique identifier for a bank transfer | |

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of BankTransfers array with one BankTransfer |  -  |

<a id="getBankTransferAttachmentByFileName"></a>
# **getBankTransferAttachmentByFileName**
> File getBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, contentType)

Retrieves a specific attachment on a specific bank transfer by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransferID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transfer
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Bank Transfer
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransferAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransferID** | **UUID**| Xero generated unique identifier for a bank transfer | |
| **fileName** | **String**| The name of the file being attached to a Bank Transfer | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of binary data from the Attachment to a Bank Transfer |  -  |

<a id="getBankTransferAttachmentById"></a>
# **getBankTransferAttachmentById**
> File getBankTransferAttachmentById(xeroTenantId, bankTransferID, attachmentID, contentType)

Retrieves a specific attachment from a specific bank transfer using a unique attachment ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransferID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transfer
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for an Attachment to a bank transfer
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getBankTransferAttachmentById(xeroTenantId, bankTransferID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransferAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransferID** | **UUID**| Xero generated unique identifier for a bank transfer | |
| **attachmentID** | **UUID**| Xero generated unique identifier for an Attachment to a bank transfer | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of binary data from the Attachment to a Bank Transfer |  -  |

<a id="getBankTransferAttachments"></a>
# **getBankTransferAttachments**
> Attachments getBankTransferAttachments(xeroTenantId, bankTransferID)

Retrieves attachments from a specific bank transfer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransferID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transfer
    try {
      Attachments result = apiInstance.getBankTransferAttachments(xeroTenantId, bankTransferID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransferAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransferID** | **UUID**| Xero generated unique identifier for a bank transfer | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of Attachments array of 0 to N Attachment for a Bank Transfer |  -  |

<a id="getBankTransferHistory"></a>
# **getBankTransferHistory**
> HistoryRecords getBankTransferHistory(xeroTenantId, bankTransferID)

Retrieves history from a specific bank transfer using a unique bank transfer Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransferID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transfer
    try {
      HistoryRecords result = apiInstance.getBankTransferHistory(xeroTenantId, bankTransferID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransferHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransferID** | **UUID**| Xero generated unique identifier for a bank transfer | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getBankTransfers"></a>
# **getBankTransfers**
> BankTransfers getBankTransfers(xeroTenantId, ifModifiedSince, where, order)

Retrieves all bank transfers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "HasAttachments==true"; // String | Filter by an any element
    String order = "Amount ASC"; // String | Order by an any element
    try {
      BankTransfers result = apiInstance.getBankTransfers(xeroTenantId, ifModifiedSince, where, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBankTransfers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of BankTransfers array of 0 to N BankTransfer |  -  |

<a id="getBatchPaymentHistory"></a>
# **getBatchPaymentHistory**
> HistoryRecords getBatchPaymentHistory(xeroTenantId, batchPaymentID)

Retrieves history from a specific batch payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID batchPaymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for BatchPayment
    try {
      HistoryRecords result = apiInstance.getBatchPaymentHistory(xeroTenantId, batchPaymentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBatchPaymentHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **batchPaymentID** | **UUID**| Unique identifier for BatchPayment | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getBatchPayments"></a>
# **getBatchPayments**
> BatchPayments getBatchPayments(xeroTenantId, ifModifiedSince, where, order)

Retrieves either one or many batch payments for invoices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"AUTHORISED\""; // String | Filter by an any element
    String order = "Date ASC"; // String | Order by an any element
    try {
      BatchPayments result = apiInstance.getBatchPayments(xeroTenantId, ifModifiedSince, where, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBatchPayments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |

### Return type

[**BatchPayments**](BatchPayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type BatchPayments array of BatchPayment objects |  -  |

<a id="getBrandingTheme"></a>
# **getBrandingTheme**
> BrandingThemes getBrandingTheme(xeroTenantId, brandingThemeID)

Retrieves a specific branding theme using a unique branding theme Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID brandingThemeID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Branding Theme
    try {
      BrandingThemes result = apiInstance.getBrandingTheme(xeroTenantId, brandingThemeID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBrandingTheme");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **brandingThemeID** | **UUID**| Unique identifier for a Branding Theme | |

### Return type

[**BrandingThemes**](BrandingThemes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type BrandingThemes with one BrandingTheme |  -  |

<a id="getBrandingThemePaymentServices"></a>
# **getBrandingThemePaymentServices**
> PaymentServices getBrandingThemePaymentServices(xeroTenantId, brandingThemeID)

Retrieves the payment services for a specific branding theme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID brandingThemeID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Branding Theme
    try {
      PaymentServices result = apiInstance.getBrandingThemePaymentServices(xeroTenantId, brandingThemeID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBrandingThemePaymentServices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **brandingThemeID** | **UUID**| Unique identifier for a Branding Theme | |

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type PaymentServices array with 0 to N PaymentService |  -  |

<a id="getBrandingThemes"></a>
# **getBrandingThemes**
> BrandingThemes getBrandingThemes(xeroTenantId)

Retrieves all the branding themes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    try {
      BrandingThemes result = apiInstance.getBrandingThemes(xeroTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getBrandingThemes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |

### Return type

[**BrandingThemes**](BrandingThemes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type BrandingThemes |  -  |

<a id="getContact"></a>
# **getContact**
> Contacts getContact(xeroTenantId, contactID)

Retrieves a specific contacts in a Xero organisation using a unique contact Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    try {
      Contacts result = apiInstance.getContact(xeroTenantId, contactID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getContact");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactID** | **UUID**| Unique identifier for a Contact | |

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contacts array with a unique Contact |  -  |

<a id="getContactAttachmentByFileName"></a>
# **getContactAttachmentByFileName**
> File getContactAttachmentByFileName(xeroTenantId, contactID, fileName, contentType)

Retrieves a specific attachment from a specific contact by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    String fileName = "xero-dev.jpg"; // String | Name for the file you are attaching
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getContactAttachmentByFileName(xeroTenantId, contactID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getContactAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactID** | **UUID**| Unique identifier for a Contact | |
| **fileName** | **String**| Name for the file you are attaching | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Contact as binary data |  -  |

<a id="getContactAttachmentById"></a>
# **getContactAttachmentById**
> File getContactAttachmentById(xeroTenantId, contactID, attachmentID, contentType)

Retrieves a specific attachment from a specific contact using a unique attachment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Attachment
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getContactAttachmentById(xeroTenantId, contactID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getContactAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactID** | **UUID**| Unique identifier for a Contact | |
| **attachmentID** | **UUID**| Unique identifier for a Attachment | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Contact as binary data |  -  |

<a id="getContactAttachments"></a>
# **getContactAttachments**
> Attachments getContactAttachments(xeroTenantId, contactID)

Retrieves attachments for a specific contact in a Xero organisation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    try {
      Attachments result = apiInstance.getContactAttachments(xeroTenantId, contactID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getContactAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactID** | **UUID**| Unique identifier for a Contact | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with 0 to N Attachment |  -  |

<a id="getContactByContactNumber"></a>
# **getContactByContactNumber**
> Contacts getContactByContactNumber(xeroTenantId, contactNumber)

Retrieves a specific contact by contact number in a Xero organisation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    String contactNumber = "SB2"; // String | This field is read only on the Xero contact screen, used to identify contacts in external systems (max length = 50).
    try {
      Contacts result = apiInstance.getContactByContactNumber(xeroTenantId, contactNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getContactByContactNumber");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactNumber** | **String**| This field is read only on the Xero contact screen, used to identify contacts in external systems (max length &#x3D; 50). | |

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contacts array with a unique Contact |  -  |

<a id="getContactCISSettings"></a>
# **getContactCISSettings**
> CISSettings getContactCISSettings(xeroTenantId, contactID)

Retrieves CIS settings for a specific contact in a Xero organisation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    try {
      CISSettings result = apiInstance.getContactCISSettings(xeroTenantId, contactID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getContactCISSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactID** | **UUID**| Unique identifier for a Contact | |

### Return type

[**CISSettings**](CISSettings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type CISSettings for a specific Contact |  -  |

<a id="getContactGroup"></a>
# **getContactGroup**
> ContactGroups getContactGroup(xeroTenantId, contactGroupID)

Retrieves a specific contact group by using a unique contact group Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactGroupID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact Group
    try {
      ContactGroups result = apiInstance.getContactGroup(xeroTenantId, contactGroupID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getContactGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactGroupID** | **UUID**| Unique identifier for a Contact Group | |

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contact Groups array with a specific Contact Group |  -  |

<a id="getContactGroups"></a>
# **getContactGroups**
> ContactGroups getContactGroups(xeroTenantId, where, order)

Retrieves the contact Id and name of all the contacts in a contact group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "Name ASC"; // String | Order by an any element
    try {
      ContactGroups result = apiInstance.getContactGroups(xeroTenantId, where, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getContactGroups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contact Groups array of Contact Group |  -  |

<a id="getContactHistory"></a>
# **getContactHistory**
> HistoryRecords getContactHistory(xeroTenantId, contactID)

Retrieves history records for a specific contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    try {
      HistoryRecords result = apiInstance.getContactHistory(xeroTenantId, contactID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getContactHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactID** | **UUID**| Unique identifier for a Contact | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getContacts"></a>
# **getContacts**
> Contacts getContacts(xeroTenantId, ifModifiedSince, where, order, ids, page, includeArchived)

Retrieves all contacts in a Xero organisation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "ContactStatus==&quot;ACTIVE&quot;"; // String | Filter by an any element
    String order = "Name ASC"; // String | Order by an any element
    List<UUID> ids = Arrays.asList(); // List<UUID> | Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call.
    Integer page = 1; // Integer | e.g. page=1 - Up to 100 contacts will be returned in a single API call.
    Boolean includeArchived = true; // Boolean | e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response
    try {
      Contacts result = apiInstance.getContacts(xeroTenantId, ifModifiedSince, where, order, ids, page, includeArchived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getContacts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **ids** | [**List&lt;UUID&gt;**](UUID.md)| Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call. | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 - Up to 100 contacts will be returned in a single API call. | [optional] |
| **includeArchived** | **Boolean**| e.g. includeArchived&#x3D;true - Contacts with a status of ARCHIVED will be included in the response | [optional] |

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contacts array with 0 to N Contact |  -  |

<a id="getCreditNote"></a>
# **getCreditNote**
> CreditNotes getCreditNote(xeroTenantId, creditNoteID, unitdp)

Retrieves a specific credit note using a unique credit note Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      CreditNotes result = apiInstance.getCreditNote(xeroTenantId, creditNoteID, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getCreditNote");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Credit Notes array with a unique CreditNote |  -  |

<a id="getCreditNoteAsPdf"></a>
# **getCreditNoteAsPdf**
> File getCreditNoteAsPdf(xeroTenantId, creditNoteID)

Retrieves credit notes as PDF files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    try {
      File result = apiInstance.getCreditNoteAsPdf(xeroTenantId, creditNoteID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getCreditNoteAsPdf");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of binary data from the Attachment to a Credit Note |  -  |

<a id="getCreditNoteAttachmentByFileName"></a>
# **getCreditNoteAttachmentByFileName**
> File getCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, contentType)

Retrieves a specific attachment on a specific credit note by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    String fileName = "xero-dev.jpg"; // String | Name of the file you are attaching to Credit Note
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getCreditNoteAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |
| **fileName** | **String**| Name of the file you are attaching to Credit Note | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Credit Note as binary data |  -  |

<a id="getCreditNoteAttachmentById"></a>
# **getCreditNoteAttachmentById**
> File getCreditNoteAttachmentById(xeroTenantId, creditNoteID, attachmentID, contentType)

Retrieves a specific attachment from a specific credit note using a unique attachment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Attachment
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getCreditNoteAttachmentById(xeroTenantId, creditNoteID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getCreditNoteAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |
| **attachmentID** | **UUID**| Unique identifier for a Attachment | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Credit Note as binary data |  -  |

<a id="getCreditNoteAttachments"></a>
# **getCreditNoteAttachments**
> Attachments getCreditNoteAttachments(xeroTenantId, creditNoteID)

Retrieves attachments for a specific credit notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    try {
      Attachments result = apiInstance.getCreditNoteAttachments(xeroTenantId, creditNoteID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getCreditNoteAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with all Attachment for specific Credit Note |  -  |

<a id="getCreditNoteHistory"></a>
# **getCreditNoteHistory**
> HistoryRecords getCreditNoteHistory(xeroTenantId, creditNoteID)

Retrieves history records of a specific credit note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    try {
      HistoryRecords result = apiInstance.getCreditNoteHistory(xeroTenantId, creditNoteID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getCreditNoteHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getCreditNotes"></a>
# **getCreditNotes**
> CreditNotes getCreditNotes(xeroTenantId, ifModifiedSince, where, order, page, unitdp)

Retrieves any credit notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"DRAFT\""; // String | Filter by an any element
    String order = "CreditNoteNumber ASC"; // String | Order by an any element
    Integer page = 1; // Integer | e.g. page=1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      CreditNotes result = apiInstance.getCreditNotes(xeroTenantId, ifModifiedSince, where, order, page, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getCreditNotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note | [optional] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Credit Notes array of CreditNote |  -  |

<a id="getCurrencies"></a>
# **getCurrencies**
> Currencies getCurrencies(xeroTenantId, where, order)

Retrieves currencies for your Xero organisation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    String where = "Code==\"USD\""; // String | Filter by an any element
    String order = "Code ASC"; // String | Order by an any element
    try {
      Currencies result = apiInstance.getCurrencies(xeroTenantId, where, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getCurrencies");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |

### Return type

[**Currencies**](Currencies.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Currencies array with all Currencies |  -  |

<a id="getEmployee"></a>
# **getEmployee**
> Employees getEmployee(xeroTenantId, employeeID)

Retrieves a specific employee used in Xero payrun using a unique employee Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID employeeID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Employee
    try {
      Employees result = apiInstance.getEmployee(xeroTenantId, employeeID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getEmployee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **employeeID** | **UUID**| Unique identifier for a Employee | |

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Employees array with specified Employee |  -  |

<a id="getEmployees"></a>
# **getEmployees**
> Employees getEmployees(xeroTenantId, ifModifiedSince, where, order)

Retrieves employees used in Xero payrun

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "LastName ASC"; // String | Order by an any element
    try {
      Employees result = apiInstance.getEmployees(xeroTenantId, ifModifiedSince, where, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getEmployees");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Employees array with all Employee |  -  |

<a id="getExpenseClaim"></a>
# **getExpenseClaim**
> ExpenseClaims getExpenseClaim(xeroTenantId, expenseClaimID)

Retrieves a specific expense claim using a unique expense claim Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID expenseClaimID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ExpenseClaim
    try {
      ExpenseClaims result = apiInstance.getExpenseClaim(xeroTenantId, expenseClaimID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getExpenseClaim");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **expenseClaimID** | **UUID**| Unique identifier for a ExpenseClaim | |

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ExpenseClaims array with specified ExpenseClaim |  -  |

<a id="getExpenseClaimHistory"></a>
# **getExpenseClaimHistory**
> HistoryRecords getExpenseClaimHistory(xeroTenantId, expenseClaimID)

Retrieves history records of a specific expense claim

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID expenseClaimID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ExpenseClaim
    try {
      HistoryRecords result = apiInstance.getExpenseClaimHistory(xeroTenantId, expenseClaimID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getExpenseClaimHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **expenseClaimID** | **UUID**| Unique identifier for a ExpenseClaim | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getExpenseClaims"></a>
# **getExpenseClaims**
> ExpenseClaims getExpenseClaims(xeroTenantId, ifModifiedSince, where, order)

Retrieves expense claims

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"SUBMITTED\""; // String | Filter by an any element
    String order = "Status ASC"; // String | Order by an any element
    try {
      ExpenseClaims result = apiInstance.getExpenseClaims(xeroTenantId, ifModifiedSince, where, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getExpenseClaims");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ExpenseClaims array with all ExpenseClaims |  -  |

<a id="getInvoice"></a>
# **getInvoice**
> Invoices getInvoice(xeroTenantId, invoiceID, unitdp)

Retrieves a specific sales invoice or purchase bill using a unique invoice Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Invoices result = apiInstance.getInvoice(xeroTenantId, invoiceID, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getInvoice");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Invoices array with specified Invoices |  -  |

<a id="getInvoiceAsPdf"></a>
# **getInvoiceAsPdf**
> File getInvoiceAsPdf(xeroTenantId, invoiceID)

Retrieves invoices or purchase bills as PDF files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    try {
      File result = apiInstance.getInvoiceAsPdf(xeroTenantId, invoiceID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getInvoiceAsPdf");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of byte array pdf version of specified Invoices |  -  |

<a id="getInvoiceAttachmentByFileName"></a>
# **getInvoiceAttachmentByFileName**
> File getInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, contentType)

Retrieves an attachment from a specific invoice or purchase bill by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    String fileName = "xero-dev.jpg"; // String | Name of the file you are attaching
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getInvoiceAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |
| **fileName** | **String**| Name of the file you are attaching | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Invoice as binary data |  -  |

<a id="getInvoiceAttachmentById"></a>
# **getInvoiceAttachmentById**
> File getInvoiceAttachmentById(xeroTenantId, invoiceID, attachmentID, contentType)

Retrieves a specific attachment from a specific invoices or purchase bills by using a unique attachment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Attachment
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getInvoiceAttachmentById(xeroTenantId, invoiceID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getInvoiceAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |
| **attachmentID** | **UUID**| Unique identifier for an Attachment | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Invoice as binary data |  -  |

<a id="getInvoiceAttachments"></a>
# **getInvoiceAttachments**
> Attachments getInvoiceAttachments(xeroTenantId, invoiceID)

Retrieves attachments for a specific invoice or purchase bill

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    try {
      Attachments result = apiInstance.getInvoiceAttachments(xeroTenantId, invoiceID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getInvoiceAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Attachments for specified Invoices |  -  |

<a id="getInvoiceHistory"></a>
# **getInvoiceHistory**
> HistoryRecords getInvoiceHistory(xeroTenantId, invoiceID)

Retrieves history records for a specific invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    try {
      HistoryRecords result = apiInstance.getInvoiceHistory(xeroTenantId, invoiceID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getInvoiceHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getInvoiceReminders"></a>
# **getInvoiceReminders**
> InvoiceReminders getInvoiceReminders(xeroTenantId)

Retrieves invoice reminder settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    try {
      InvoiceReminders result = apiInstance.getInvoiceReminders(xeroTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getInvoiceReminders");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |

### Return type

[**InvoiceReminders**](InvoiceReminders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of Invoice Reminders |  -  |

<a id="getInvoices"></a>
# **getInvoices**
> Invoices getInvoices(xeroTenantId, ifModifiedSince, where, order, ids, invoiceNumbers, contactIDs, statuses, page, includeArchived, createdByMyApp, unitdp)

Retrieves sales invoices or purchase bills

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"DRAFT\""; // String | Filter by an any element
    String order = "InvoiceNumber ASC"; // String | Order by an any element
    List<UUID> ids = Arrays.asList(); // List<UUID> | Filter by a comma-separated list of InvoicesIDs.
    List<String> invoiceNumbers = Arrays.asList(); // List<String> | Filter by a comma-separated list of InvoiceNumbers.
    List<UUID> contactIDs = Arrays.asList(); // List<UUID> | Filter by a comma-separated list of ContactIDs.
    List<String> statuses = Arrays.asList(); // List<String> | Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter.
    Integer page = 1; // Integer | e.g. page=1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice
    Boolean includeArchived = true; // Boolean | e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response
    Boolean createdByMyApp = false; // Boolean | When set to true you'll only retrieve Invoices created by your app
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Invoices result = apiInstance.getInvoices(xeroTenantId, ifModifiedSince, where, order, ids, invoiceNumbers, contactIDs, statuses, page, includeArchived, createdByMyApp, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getInvoices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **ids** | [**List&lt;UUID&gt;**](UUID.md)| Filter by a comma-separated list of InvoicesIDs. | [optional] |
| **invoiceNumbers** | [**List&lt;String&gt;**](String.md)| Filter by a comma-separated list of InvoiceNumbers. | [optional] |
| **contactIDs** | [**List&lt;UUID&gt;**](UUID.md)| Filter by a comma-separated list of ContactIDs. | [optional] |
| **statuses** | [**List&lt;String&gt;**](String.md)| Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice | [optional] |
| **includeArchived** | **Boolean**| e.g. includeArchived&#x3D;true - Contacts with a status of ARCHIVED will be included in the response | [optional] |
| **createdByMyApp** | **Boolean**| When set to true you&#39;ll only retrieve Invoices created by your app | [optional] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Invoices array with all Invoices |  -  |

<a id="getItem"></a>
# **getItem**
> Items getItem(xeroTenantId, itemID, unitdp)

Retrieves a specific item using a unique item Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID itemID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Item
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Items result = apiInstance.getItem(xeroTenantId, itemID, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **itemID** | **UUID**| Unique identifier for an Item | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Items array with specified Item |  -  |

<a id="getItemHistory"></a>
# **getItemHistory**
> HistoryRecords getItemHistory(xeroTenantId, itemID)

Retrieves history for a specific item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID itemID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Item
    try {
      HistoryRecords result = apiInstance.getItemHistory(xeroTenantId, itemID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getItemHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **itemID** | **UUID**| Unique identifier for an Item | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getItems"></a>
# **getItems**
> Items getItems(xeroTenantId, ifModifiedSince, where, order, unitdp)

Retrieves items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "IsSold==true"; // String | Filter by an any element
    String order = "Code ASC"; // String | Order by an any element
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Items result = apiInstance.getItems(xeroTenantId, ifModifiedSince, where, order, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getItems");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Items array with all Item |  -  |

<a id="getJournal"></a>
# **getJournal**
> Journals getJournal(xeroTenantId, journalID)

Retrieves a specific journal using a unique journal Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID journalID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Journal
    try {
      Journals result = apiInstance.getJournal(xeroTenantId, journalID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getJournal");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **journalID** | **UUID**| Unique identifier for a Journal | |

### Return type

[**Journals**](Journals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Journals array with specified Journal |  -  |

<a id="getJournals"></a>
# **getJournals**
> Journals getJournals(xeroTenantId, ifModifiedSince, offset, paymentsOnly)

Retrieves journals

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    Integer offset = 10; // Integer | Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned
    Boolean paymentsOnly = true; // Boolean | Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default.
    try {
      Journals result = apiInstance.getJournals(xeroTenantId, ifModifiedSince, offset, paymentsOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getJournals");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **offset** | **Integer**| Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned | [optional] |
| **paymentsOnly** | **Boolean**| Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default. | [optional] |

### Return type

[**Journals**](Journals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Journals array with all Journals |  -  |

<a id="getLinkedTransaction"></a>
# **getLinkedTransaction**
> LinkedTransactions getLinkedTransaction(xeroTenantId, linkedTransactionID)

Retrieves a specific linked transaction (billable expenses) using a unique linked transaction Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID linkedTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a LinkedTransaction
    try {
      LinkedTransactions result = apiInstance.getLinkedTransaction(xeroTenantId, linkedTransactionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getLinkedTransaction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **linkedTransactionID** | **UUID**| Unique identifier for a LinkedTransaction | |

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type LinkedTransactions array with a specified LinkedTransaction |  -  |

<a id="getLinkedTransactions"></a>
# **getLinkedTransactions**
> LinkedTransactions getLinkedTransactions(xeroTenantId, page, linkedTransactionID, sourceTransactionID, contactID, status, targetTransactionID)

Retrieves linked transactions (billable expenses)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Integer page = 1; // Integer | Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page=1.
    UUID linkedTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | The Xero identifier for an Linked Transaction
    UUID sourceTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Filter by the SourceTransactionID. Get the linked transactions created from a particular ACCPAY invoice
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer.
    String status = "APPROVED"; // String | Filter by the combination of ContactID and Status. Get  the linked transactions associated to a  customer and with a status
    UUID targetTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice
    try {
      LinkedTransactions result = apiInstance.getLinkedTransactions(xeroTenantId, page, linkedTransactionID, sourceTransactionID, contactID, status, targetTransactionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getLinkedTransactions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **page** | **Integer**| Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page&#x3D;1. | [optional] |
| **linkedTransactionID** | **UUID**| The Xero identifier for an Linked Transaction | [optional] |
| **sourceTransactionID** | **UUID**| Filter by the SourceTransactionID. Get the linked transactions created from a particular ACCPAY invoice | [optional] |
| **contactID** | **UUID**| Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer. | [optional] |
| **status** | **String**| Filter by the combination of ContactID and Status. Get  the linked transactions associated to a  customer and with a status | [optional] |
| **targetTransactionID** | **UUID**| Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice | [optional] |

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type LinkedTransactions array with all LinkedTransaction |  -  |

<a id="getManualJournal"></a>
# **getManualJournal**
> ManualJournals getManualJournal(xeroTenantId, manualJournalID)

Retrieves a specific manual journal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID manualJournalID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ManualJournal
    try {
      ManualJournals result = apiInstance.getManualJournal(xeroTenantId, manualJournalID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getManualJournal");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournalID** | **UUID**| Unique identifier for a ManualJournal | |

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ManualJournals array with a specified ManualJournals |  -  |

<a id="getManualJournalAttachmentByFileName"></a>
# **getManualJournalAttachmentByFileName**
> File getManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, contentType)

Retrieves a specific attachment from a specific manual journal by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID manualJournalID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ManualJournal
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to a ManualJournal
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getManualJournalAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournalID** | **UUID**| Unique identifier for a ManualJournal | |
| **fileName** | **String**| The name of the file being attached to a ManualJournal | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Manual Journal as binary data |  -  |

<a id="getManualJournalAttachmentById"></a>
# **getManualJournalAttachmentById**
> File getManualJournalAttachmentById(xeroTenantId, manualJournalID, attachmentID, contentType)

Allows you to retrieve a specific attachment from a specific manual journal using a unique attachment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID manualJournalID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ManualJournal
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Attachment
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getManualJournalAttachmentById(xeroTenantId, manualJournalID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getManualJournalAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournalID** | **UUID**| Unique identifier for a ManualJournal | |
| **attachmentID** | **UUID**| Unique identifier for a Attachment | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Manual Journal as binary data |  -  |

<a id="getManualJournalAttachments"></a>
# **getManualJournalAttachments**
> Attachments getManualJournalAttachments(xeroTenantId, manualJournalID)

Retrieves attachment for a specific manual journal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID manualJournalID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ManualJournal
    try {
      Attachments result = apiInstance.getManualJournalAttachments(xeroTenantId, manualJournalID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getManualJournalAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournalID** | **UUID**| Unique identifier for a ManualJournal | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with all Attachments for a ManualJournals |  -  |

<a id="getManualJournals"></a>
# **getManualJournals**
> ManualJournals getManualJournals(xeroTenantId, ifModifiedSince, where, order, page)

Retrieves manual journals

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"DRAFT\""; // String | Filter by an any element
    String order = "Date ASC"; // String | Order by an any element
    Integer page = 1; // Integer | e.g. page=1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment
    try {
      ManualJournals result = apiInstance.getManualJournals(xeroTenantId, ifModifiedSince, where, order, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getManualJournals");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment | [optional] |

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ManualJournals array with a all ManualJournals |  -  |

<a id="getManualJournalsHistory"></a>
# **getManualJournalsHistory**
> HistoryRecords getManualJournalsHistory(xeroTenantId, manualJournalID)

Retrieves history for a specific manual journal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID manualJournalID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a manual journal
    try {
      HistoryRecords result = apiInstance.getManualJournalsHistory(xeroTenantId, manualJournalID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getManualJournalsHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournalID** | **UUID**| Xero generated unique identifier for a manual journal | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getOnlineInvoice"></a>
# **getOnlineInvoice**
> OnlineInvoices getOnlineInvoice(xeroTenantId, invoiceID)

Retrieves a URL to an online invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    try {
      OnlineInvoices result = apiInstance.getOnlineInvoice(xeroTenantId, invoiceID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getOnlineInvoice");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |

### Return type

[**OnlineInvoices**](OnlineInvoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type OnlineInvoice array with one OnlineInvoice |  -  |

<a id="getOrganisationActions"></a>
# **getOrganisationActions**
> Actions getOrganisationActions(xeroTenantId)

Retrieves a list of the key actions your app has permission to perform in the connected Xero organisation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    try {
      Actions result = apiInstance.getOrganisationActions(xeroTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getOrganisationActions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |

### Return type

[**Actions**](Actions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Actions array with all key actions |  -  |

<a id="getOrganisationCISSettings"></a>
# **getOrganisationCISSettings**
> CISOrgSettings getOrganisationCISSettings(xeroTenantId, organisationID)

Retrieves the CIS settings for the Xero organistaion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID organisationID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | The unique Xero identifier for an organisation
    try {
      CISOrgSettings result = apiInstance.getOrganisationCISSettings(xeroTenantId, organisationID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getOrganisationCISSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **organisationID** | **UUID**| The unique Xero identifier for an organisation | |

### Return type

[**CISOrgSettings**](CISOrgSettings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Organisation array with specified Organisation |  -  |

<a id="getOrganisations"></a>
# **getOrganisations**
> Organisations getOrganisations(xeroTenantId)

Retrieves Xero organisation details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    try {
      Organisations result = apiInstance.getOrganisations(xeroTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getOrganisations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |

### Return type

[**Organisations**](Organisations.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Organisation array with all Organisation |  -  |

<a id="getOverpayment"></a>
# **getOverpayment**
> Overpayments getOverpayment(xeroTenantId, overpaymentID)

Retrieves a specific overpayment using a unique overpayment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID overpaymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Overpayment
    try {
      Overpayments result = apiInstance.getOverpayment(xeroTenantId, overpaymentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getOverpayment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **overpaymentID** | **UUID**| Unique identifier for a Overpayment | |

### Return type

[**Overpayments**](Overpayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Overpayments array with specified Overpayments |  -  |

<a id="getOverpaymentHistory"></a>
# **getOverpaymentHistory**
> HistoryRecords getOverpaymentHistory(xeroTenantId, overpaymentID)

Retrieves history records of a specific overpayment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID overpaymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Overpayment
    try {
      HistoryRecords result = apiInstance.getOverpaymentHistory(xeroTenantId, overpaymentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getOverpaymentHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **overpaymentID** | **UUID**| Unique identifier for a Overpayment | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getOverpayments"></a>
# **getOverpayments**
> Overpayments getOverpayments(xeroTenantId, ifModifiedSince, where, order, page, unitdp)

Retrieves overpayments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"AUTHORISED\""; // String | Filter by an any element
    String order = "Status ASC"; // String | Order by an any element
    Integer page = 1; // Integer | e.g. page=1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Overpayments result = apiInstance.getOverpayments(xeroTenantId, ifModifiedSince, where, order, page, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getOverpayments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment | [optional] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Overpayments**](Overpayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Overpayments array with all Overpayments |  -  |

<a id="getPayment"></a>
# **getPayment**
> Payments getPayment(xeroTenantId, paymentID)

Retrieves a specific payment for invoices and credit notes using a unique payment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID paymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Payment
    try {
      Payments result = apiInstance.getPayment(xeroTenantId, paymentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPayment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **paymentID** | **UUID**| Unique identifier for a Payment | |

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Payments array for specified Payment |  -  |

<a id="getPaymentHistory"></a>
# **getPaymentHistory**
> HistoryRecords getPaymentHistory(xeroTenantId, paymentID)

Retrieves history records of a specific payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID paymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Payment
    try {
      HistoryRecords result = apiInstance.getPaymentHistory(xeroTenantId, paymentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPaymentHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **paymentID** | **UUID**| Unique identifier for a Payment | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getPaymentServices"></a>
# **getPaymentServices**
> PaymentServices getPaymentServices(xeroTenantId)

Retrieves payment services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    try {
      PaymentServices result = apiInstance.getPaymentServices(xeroTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPaymentServices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type PaymentServices array for all PaymentService |  -  |

<a id="getPayments"></a>
# **getPayments**
> Payments getPayments(xeroTenantId, ifModifiedSince, where, order, page)

Retrieves payments for invoices and credit notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"AUTHORISED\""; // String | Filter by an any element
    String order = "Amount ASC"; // String | Order by an any element
    Integer page = 1; // Integer | Up to 100 payments will be returned in a single API call
    try {
      Payments result = apiInstance.getPayments(xeroTenantId, ifModifiedSince, where, order, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPayments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| Up to 100 payments will be returned in a single API call | [optional] |

### Return type

[**Payments**](Payments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Payments array for all Payments |  -  |

<a id="getPrepayment"></a>
# **getPrepayment**
> Prepayments getPrepayment(xeroTenantId, prepaymentID)

Allows you to retrieve a specified prepayments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID prepaymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a PrePayment
    try {
      Prepayments result = apiInstance.getPrepayment(xeroTenantId, prepaymentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPrepayment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **prepaymentID** | **UUID**| Unique identifier for a PrePayment | |

### Return type

[**Prepayments**](Prepayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Prepayments array for a specified Prepayment |  -  |

<a id="getPrepaymentHistory"></a>
# **getPrepaymentHistory**
> HistoryRecords getPrepaymentHistory(xeroTenantId, prepaymentID)

Retrieves history record for a specific prepayment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID prepaymentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a PrePayment
    try {
      HistoryRecords result = apiInstance.getPrepaymentHistory(xeroTenantId, prepaymentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPrepaymentHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **prepaymentID** | **UUID**| Unique identifier for a PrePayment | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getPrepayments"></a>
# **getPrepayments**
> Prepayments getPrepayments(xeroTenantId, ifModifiedSince, where, order, page, unitdp)

Retrieves prepayments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"AUTHORISED\""; // String | Filter by an any element
    String order = "Reference ASC"; // String | Order by an any element
    Integer page = 1; // Integer | e.g. page=1 – Up to 100 prepayments will be returned in a single API call with line items shown for each overpayment
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Prepayments result = apiInstance.getPrepayments(xeroTenantId, ifModifiedSince, where, order, page, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPrepayments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 prepayments will be returned in a single API call with line items shown for each overpayment | [optional] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Prepayments**](Prepayments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Prepayments array for all Prepayment |  -  |

<a id="getPurchaseOrder"></a>
# **getPurchaseOrder**
> PurchaseOrders getPurchaseOrder(xeroTenantId, purchaseOrderID)

Retrieves a specific purchase order using a unique purchase order Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID purchaseOrderID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a PurchaseOrder
    try {
      PurchaseOrders result = apiInstance.getPurchaseOrder(xeroTenantId, purchaseOrderID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPurchaseOrder");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderID** | **UUID**| Unique identifier for a PurchaseOrder | |

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type PurchaseOrder array for specified PurchaseOrder |  -  |

<a id="getPurchaseOrderAsPdf"></a>
# **getPurchaseOrderAsPdf**
> File getPurchaseOrderAsPdf(xeroTenantId, purchaseOrderID)

Retrieves specific purchase order as PDF files using a unique purchase order Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID purchaseOrderID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Purchase Order
    try {
      File result = apiInstance.getPurchaseOrderAsPdf(xeroTenantId, purchaseOrderID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPurchaseOrderAsPdf");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderID** | **UUID**| Unique identifier for an Purchase Order | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of byte array pdf version of specified Purchase Orders |  -  |

<a id="getPurchaseOrderAttachmentByFileName"></a>
# **getPurchaseOrderAttachmentByFileName**
> File getPurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, contentType)

Retrieves a specific attachment for a specific purchase order by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID purchaseOrderID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Purchase Order object
    String fileName = "xero-dev.jpg"; // String | Name of the attachment
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getPurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPurchaseOrderAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderID** | **UUID**| Unique identifier for Purchase Order object | |
| **fileName** | **String**| Name of the attachment | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Purchase Order as binary data |  -  |

<a id="getPurchaseOrderAttachmentById"></a>
# **getPurchaseOrderAttachmentById**
> File getPurchaseOrderAttachmentById(xeroTenantId, purchaseOrderID, attachmentID, contentType)

Retrieves specific attachment for a specific purchase order using a unique attachment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID purchaseOrderID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Purchase Order object
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Attachment object
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getPurchaseOrderAttachmentById(xeroTenantId, purchaseOrderID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPurchaseOrderAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderID** | **UUID**| Unique identifier for Purchase Order object | |
| **attachmentID** | **UUID**| Unique identifier for Attachment object | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Account as binary data |  -  |

<a id="getPurchaseOrderAttachments"></a>
# **getPurchaseOrderAttachments**
> Attachments getPurchaseOrderAttachments(xeroTenantId, purchaseOrderID)

Retrieves attachments for a specific purchase order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID purchaseOrderID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Purchase Orders object
    try {
      Attachments result = apiInstance.getPurchaseOrderAttachments(xeroTenantId, purchaseOrderID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPurchaseOrderAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderID** | **UUID**| Unique identifier for Purchase Orders object | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Purchase Orders |  -  |

<a id="getPurchaseOrderByNumber"></a>
# **getPurchaseOrderByNumber**
> PurchaseOrders getPurchaseOrderByNumber(xeroTenantId, purchaseOrderNumber)

Retrieves a specific purchase order using purchase order number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    String purchaseOrderNumber = "PO1234"; // String | Unique identifier for a PurchaseOrder
    try {
      PurchaseOrders result = apiInstance.getPurchaseOrderByNumber(xeroTenantId, purchaseOrderNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPurchaseOrderByNumber");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderNumber** | **String**| Unique identifier for a PurchaseOrder | |

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type PurchaseOrder array for specified PurchaseOrder |  -  |

<a id="getPurchaseOrderHistory"></a>
# **getPurchaseOrderHistory**
> HistoryRecords getPurchaseOrderHistory(xeroTenantId, purchaseOrderID)

Retrieves history for a specific purchase order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID purchaseOrderID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a PurchaseOrder
    try {
      HistoryRecords result = apiInstance.getPurchaseOrderHistory(xeroTenantId, purchaseOrderID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPurchaseOrderHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderID** | **UUID**| Unique identifier for a PurchaseOrder | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getPurchaseOrders"></a>
# **getPurchaseOrders**
> PurchaseOrders getPurchaseOrders(xeroTenantId, ifModifiedSince, status, dateFrom, dateTo, order, page)

Retrieves purchase orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String status = "DRAFT"; // String | Filter by purchase order status
    String dateFrom = "2019-12-01"; // String | Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31
    String dateTo = "2019-12-31"; // String | Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31
    String order = "PurchaseOrderNumber ASC"; // String | Order by an any element
    Integer page = 1; // Integer | To specify a page, append the page parameter to the URL e.g. ?page=1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page=2 and continuing this process until no more results are returned.
    try {
      PurchaseOrders result = apiInstance.getPurchaseOrders(xeroTenantId, ifModifiedSince, status, dateFrom, dateTo, order, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getPurchaseOrders");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **status** | **String**| Filter by purchase order status | [optional] [enum: DRAFT, SUBMITTED, AUTHORISED, BILLED, DELETED] |
| **dateFrom** | **String**| Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom&#x3D;2015-12-01&amp;DateTo&#x3D;2015-12-31 | [optional] |
| **dateTo** | **String**| Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom&#x3D;2015-12-01&amp;DateTo&#x3D;2015-12-31 | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **page** | **Integer**| To specify a page, append the page parameter to the URL e.g. ?page&#x3D;1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page&#x3D;2 and continuing this process until no more results are returned. | [optional] |

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type PurchaseOrder array of all PurchaseOrder |  -  |

<a id="getQuote"></a>
# **getQuote**
> Quotes getQuote(xeroTenantId, quoteID)

Retrieves a specific quote using a unique quote Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID quoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Quote
    try {
      Quotes result = apiInstance.getQuote(xeroTenantId, quoteID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getQuote");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quoteID** | **UUID**| Unique identifier for an Quote | |

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Quotes array with specified Quote |  -  |

<a id="getQuoteAsPdf"></a>
# **getQuoteAsPdf**
> File getQuoteAsPdf(xeroTenantId, quoteID)

Retrieves a specific quote as a PDF file using a unique quote Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID quoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Quote
    try {
      File result = apiInstance.getQuoteAsPdf(xeroTenantId, quoteID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getQuoteAsPdf");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quoteID** | **UUID**| Unique identifier for an Quote | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of byte array pdf version of specified Quotes |  -  |

<a id="getQuoteAttachmentByFileName"></a>
# **getQuoteAttachmentByFileName**
> File getQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, contentType)

Retrieves a specific attachment from a specific quote by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID quoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Quote object
    String fileName = "xero-dev.jpg"; // String | Name of the attachment
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getQuoteAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quoteID** | **UUID**| Unique identifier for Quote object | |
| **fileName** | **String**| Name of the attachment | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Quote as binary data |  -  |

<a id="getQuoteAttachmentById"></a>
# **getQuoteAttachmentById**
> File getQuoteAttachmentById(xeroTenantId, quoteID, attachmentID, contentType)

Retrieves a specific attachment from a specific quote using a unique attachment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID quoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Quote object
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Attachment object
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getQuoteAttachmentById(xeroTenantId, quoteID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getQuoteAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quoteID** | **UUID**| Unique identifier for Quote object | |
| **attachmentID** | **UUID**| Unique identifier for Attachment object | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Quote as binary data |  -  |

<a id="getQuoteAttachments"></a>
# **getQuoteAttachments**
> Attachments getQuoteAttachments(xeroTenantId, quoteID)

Retrieves attachments for a specific quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID quoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Quote object
    try {
      Attachments result = apiInstance.getQuoteAttachments(xeroTenantId, quoteID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getQuoteAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quoteID** | **UUID**| Unique identifier for Quote object | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Attachment |  -  |

<a id="getQuoteHistory"></a>
# **getQuoteHistory**
> HistoryRecords getQuoteHistory(xeroTenantId, quoteID)

Retrieves history records of a specific quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID quoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Quote
    try {
      HistoryRecords result = apiInstance.getQuoteHistory(xeroTenantId, quoteID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getQuoteHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quoteID** | **UUID**| Unique identifier for an Quote | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getQuotes"></a>
# **getQuotes**
> Quotes getQuotes(xeroTenantId, ifModifiedSince, dateFrom, dateTo, expiryDateFrom, expiryDateTo, contactID, status, page, order, quoteNumber)

Retrieves sales quotes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    LocalDate dateFrom = LocalDate.now(); // LocalDate | Filter for quotes after a particular date
    LocalDate dateTo = LocalDate.now(); // LocalDate | Filter for quotes before a particular date
    LocalDate expiryDateFrom = LocalDate.now(); // LocalDate | Filter for quotes expiring after a particular date
    LocalDate expiryDateTo = LocalDate.now(); // LocalDate | Filter for quotes before a particular date
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Filter for quotes belonging to a particular contact
    String status = "DRAFT"; // String | Filter for quotes of a particular Status
    Integer page = 1; // Integer | e.g. page=1 – Up to 100 Quotes will be returned in a single API call with line items shown for each quote
    String order = "Status ASC"; // String | Order by an any element
    String quoteNumber = "QU-0001"; // String | Filter by quote number (e.g. GET https://.../Quotes?QuoteNumber=QU-0001)
    try {
      Quotes result = apiInstance.getQuotes(xeroTenantId, ifModifiedSince, dateFrom, dateTo, expiryDateFrom, expiryDateTo, contactID, status, page, order, quoteNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getQuotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **dateFrom** | **LocalDate**| Filter for quotes after a particular date | [optional] |
| **dateTo** | **LocalDate**| Filter for quotes before a particular date | [optional] |
| **expiryDateFrom** | **LocalDate**| Filter for quotes expiring after a particular date | [optional] |
| **expiryDateTo** | **LocalDate**| Filter for quotes before a particular date | [optional] |
| **contactID** | **UUID**| Filter for quotes belonging to a particular contact | [optional] |
| **status** | **String**| Filter for quotes of a particular Status | [optional] |
| **page** | **Integer**| e.g. page&#x3D;1 – Up to 100 Quotes will be returned in a single API call with line items shown for each quote | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **quoteNumber** | **String**| Filter by quote number (e.g. GET https://.../Quotes?QuoteNumber&#x3D;QU-0001) | [optional] |

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type quotes array with all quotes |  -  |

<a id="getReceipt"></a>
# **getReceipt**
> Receipts getReceipt(xeroTenantId, receiptID, unitdp)

Retrieves a specific draft expense claim receipt by using a unique receipt Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID receiptID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Receipt
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Receipts result = apiInstance.getReceipt(xeroTenantId, receiptID, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReceipt");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **receiptID** | **UUID**| Unique identifier for a Receipt | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Receipts array for a specified Receipt |  -  |

<a id="getReceiptAttachmentByFileName"></a>
# **getReceiptAttachmentByFileName**
> File getReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, contentType)

Retrieves a specific attachment from a specific expense claim receipts by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID receiptID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Receipt
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to the Receipt
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReceiptAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **receiptID** | **UUID**| Unique identifier for a Receipt | |
| **fileName** | **String**| The name of the file being attached to the Receipt | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Receipt as binary data |  -  |

<a id="getReceiptAttachmentById"></a>
# **getReceiptAttachmentById**
> File getReceiptAttachmentById(xeroTenantId, receiptID, attachmentID, contentType)

Retrieves a specific attachments from a specific expense claim receipts by using a unique attachment Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID receiptID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Receipt
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Attachment
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getReceiptAttachmentById(xeroTenantId, receiptID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReceiptAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **receiptID** | **UUID**| Unique identifier for a Receipt | |
| **attachmentID** | **UUID**| Unique identifier for a Attachment | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Receipt as binary data |  -  |

<a id="getReceiptAttachments"></a>
# **getReceiptAttachments**
> Attachments getReceiptAttachments(xeroTenantId, receiptID)

Retrieves attachments for a specific expense claim receipt

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID receiptID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Receipt
    try {
      Attachments result = apiInstance.getReceiptAttachments(xeroTenantId, receiptID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReceiptAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **receiptID** | **UUID**| Unique identifier for a Receipt | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Attachments for a specified Receipt |  -  |

<a id="getReceiptHistory"></a>
# **getReceiptHistory**
> HistoryRecords getReceiptHistory(xeroTenantId, receiptID)

Retrieves a history record for a specific receipt

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID receiptID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Receipt
    try {
      HistoryRecords result = apiInstance.getReceiptHistory(xeroTenantId, receiptID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReceiptHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **receiptID** | **UUID**| Unique identifier for a Receipt | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getReceipts"></a>
# **getReceipts**
> Receipts getReceipts(xeroTenantId, ifModifiedSince, where, order, unitdp)

Retrieves draft expense claim receipts for any user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "Status==\"DRAFT\""; // String | Filter by an any element
    String order = "ReceiptNumber ASC"; // String | Order by an any element
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Receipts result = apiInstance.getReceipts(xeroTenantId, ifModifiedSince, where, order, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReceipts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Receipts array for all Receipt |  -  |

<a id="getRepeatingInvoice"></a>
# **getRepeatingInvoice**
> RepeatingInvoices getRepeatingInvoice(xeroTenantId, repeatingInvoiceID)

Retrieves a specific repeating invoice by using a unique repeating invoice Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID repeatingInvoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Repeating Invoice
    try {
      RepeatingInvoices result = apiInstance.getRepeatingInvoice(xeroTenantId, repeatingInvoiceID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getRepeatingInvoice");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **repeatingInvoiceID** | **UUID**| Unique identifier for a Repeating Invoice | |

### Return type

[**RepeatingInvoices**](RepeatingInvoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Repeating Invoices array with a specified Repeating Invoice |  -  |

<a id="getRepeatingInvoiceAttachmentByFileName"></a>
# **getRepeatingInvoiceAttachmentByFileName**
> File getRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, contentType)

Retrieves a specific attachment from a specific repeating invoices by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID repeatingInvoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Repeating Invoice
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Repeating Invoice
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getRepeatingInvoiceAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **repeatingInvoiceID** | **UUID**| Unique identifier for a Repeating Invoice | |
| **fileName** | **String**| The name of the file being attached to a Repeating Invoice | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Repeating Invoice as binary data |  -  |

<a id="getRepeatingInvoiceAttachmentById"></a>
# **getRepeatingInvoiceAttachmentById**
> File getRepeatingInvoiceAttachmentById(xeroTenantId, repeatingInvoiceID, attachmentID, contentType)

Retrieves a specific attachment from a specific repeating invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID repeatingInvoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Repeating Invoice
    UUID attachmentID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Attachment
    String contentType = "image/jpg"; // String | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    try {
      File result = apiInstance.getRepeatingInvoiceAttachmentById(xeroTenantId, repeatingInvoiceID, attachmentID, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getRepeatingInvoiceAttachmentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **repeatingInvoiceID** | **UUID**| Unique identifier for a Repeating Invoice | |
| **attachmentID** | **UUID**| Unique identifier for a Attachment | |
| **contentType** | **String**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of attachment for Repeating Invoice as binary data |  -  |

<a id="getRepeatingInvoiceAttachments"></a>
# **getRepeatingInvoiceAttachments**
> Attachments getRepeatingInvoiceAttachments(xeroTenantId, repeatingInvoiceID)

Retrieves attachments from a specific repeating invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID repeatingInvoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Repeating Invoice
    try {
      Attachments result = apiInstance.getRepeatingInvoiceAttachments(xeroTenantId, repeatingInvoiceID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getRepeatingInvoiceAttachments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **repeatingInvoiceID** | **UUID**| Unique identifier for a Repeating Invoice | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with all Attachments for a specified Repeating Invoice |  -  |

<a id="getRepeatingInvoiceHistory"></a>
# **getRepeatingInvoiceHistory**
> HistoryRecords getRepeatingInvoiceHistory(xeroTenantId, repeatingInvoiceID)

Retrieves history record for a specific repeating invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID repeatingInvoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Repeating Invoice
    try {
      HistoryRecords result = apiInstance.getRepeatingInvoiceHistory(xeroTenantId, repeatingInvoiceID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getRepeatingInvoiceHistory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **repeatingInvoiceID** | **UUID**| Unique identifier for a Repeating Invoice | |

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

<a id="getRepeatingInvoices"></a>
# **getRepeatingInvoices**
> RepeatingInvoices getRepeatingInvoices(xeroTenantId, where, order)

Retrieves repeating invoices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    String where = "Status==\"DRAFT\""; // String | Filter by an any element
    String order = "Total ASC"; // String | Order by an any element
    try {
      RepeatingInvoices result = apiInstance.getRepeatingInvoices(xeroTenantId, where, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getRepeatingInvoices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |

### Return type

[**RepeatingInvoices**](RepeatingInvoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Repeating Invoices array for all Repeating Invoice |  -  |

<a id="getReportAgedPayablesByContact"></a>
# **getReportAgedPayablesByContact**
> ReportWithRows getReportAgedPayablesByContact(xeroTenantId, contactId, date, fromDate, toDate)

Retrieves report for aged payables by contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactId = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    LocalDate date = LocalDate.now(); // LocalDate | The date of the Aged Payables By Contact report
    LocalDate fromDate = LocalDate.now(); // LocalDate | The from date of the Aged Payables By Contact report
    LocalDate toDate = LocalDate.now(); // LocalDate | The to date of the Aged Payables By Contact report
    try {
      ReportWithRows result = apiInstance.getReportAgedPayablesByContact(xeroTenantId, contactId, date, fromDate, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportAgedPayablesByContact");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactId** | **UUID**| Unique identifier for a Contact | |
| **date** | **LocalDate**| The date of the Aged Payables By Contact report | [optional] |
| **fromDate** | **LocalDate**| The from date of the Aged Payables By Contact report | [optional] |
| **toDate** | **LocalDate**| The to date of the Aged Payables By Contact report | [optional] |

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ReportWithRows |  -  |

<a id="getReportAgedReceivablesByContact"></a>
# **getReportAgedReceivablesByContact**
> ReportWithRows getReportAgedReceivablesByContact(xeroTenantId, contactId, date, fromDate, toDate)

Retrieves report for aged receivables by contact

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactId = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    LocalDate date = LocalDate.now(); // LocalDate | The date of the Aged Receivables By Contact report
    LocalDate fromDate = LocalDate.now(); // LocalDate | The from date of the Aged Receivables By Contact report
    LocalDate toDate = LocalDate.now(); // LocalDate | The to date of the Aged Receivables By Contact report
    try {
      ReportWithRows result = apiInstance.getReportAgedReceivablesByContact(xeroTenantId, contactId, date, fromDate, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportAgedReceivablesByContact");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactId** | **UUID**| Unique identifier for a Contact | |
| **date** | **LocalDate**| The date of the Aged Receivables By Contact report | [optional] |
| **fromDate** | **LocalDate**| The from date of the Aged Receivables By Contact report | [optional] |
| **toDate** | **LocalDate**| The to date of the Aged Receivables By Contact report | [optional] |

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ReportWithRows |  -  |

<a id="getReportBASorGST"></a>
# **getReportBASorGST**
> ReportWithRows getReportBASorGST(xeroTenantId, reportID)

Retrieves a specific report for BAS using a unique report Id (only valid for AU orgs)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    String reportID = "00000000-0000-0000-0000-000000000000"; // String | Unique identifier for a Report
    try {
      ReportWithRows result = apiInstance.getReportBASorGST(xeroTenantId, reportID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportBASorGST");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **reportID** | **String**| Unique identifier for a Report | |

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ReportWithRows |  -  |

<a id="getReportBASorGSTList"></a>
# **getReportBASorGSTList**
> ReportWithRows getReportBASorGSTList(xeroTenantId)

Retrieves report for BAS (only valid for AU orgs)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    try {
      ReportWithRows result = apiInstance.getReportBASorGSTList(xeroTenantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportBASorGSTList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ReportWithRows |  -  |

<a id="getReportBalanceSheet"></a>
# **getReportBalanceSheet**
> ReportWithRows getReportBalanceSheet(xeroTenantId, date, periods, timeframe, trackingOptionID1, trackingOptionID2, standardLayout, paymentsOnly)

Retrieves report for balancesheet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    LocalDate date = LocalDate.parse("2019-11-01"); // LocalDate | The date of the Balance Sheet report
    Integer periods = 3; // Integer | The number of periods for the Balance Sheet report
    String timeframe = "MONTH"; // String | The period size to compare to (MONTH, QUARTER, YEAR)
    String trackingOptionID1 = "00000000-0000-0000-0000-000000000000"; // String | The tracking option 1 for the Balance Sheet report
    String trackingOptionID2 = "00000000-0000-0000-0000-000000000000"; // String | The tracking option 2 for the Balance Sheet report
    Boolean standardLayout = true; // Boolean | The standard layout boolean for the Balance Sheet report
    Boolean paymentsOnly = false; // Boolean | return a cash basis for the Balance Sheet report
    try {
      ReportWithRows result = apiInstance.getReportBalanceSheet(xeroTenantId, date, periods, timeframe, trackingOptionID1, trackingOptionID2, standardLayout, paymentsOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportBalanceSheet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **date** | **LocalDate**| The date of the Balance Sheet report | [optional] |
| **periods** | **Integer**| The number of periods for the Balance Sheet report | [optional] |
| **timeframe** | **String**| The period size to compare to (MONTH, QUARTER, YEAR) | [optional] [enum: MONTH, QUARTER, YEAR] |
| **trackingOptionID1** | **String**| The tracking option 1 for the Balance Sheet report | [optional] |
| **trackingOptionID2** | **String**| The tracking option 2 for the Balance Sheet report | [optional] |
| **standardLayout** | **Boolean**| The standard layout boolean for the Balance Sheet report | [optional] |
| **paymentsOnly** | **Boolean**| return a cash basis for the Balance Sheet report | [optional] |

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ReportWithRows |  -  |

<a id="getReportBankSummary"></a>
# **getReportBankSummary**
> ReportWithRows getReportBankSummary(xeroTenantId, fromDate, toDate)

Retrieves report for bank summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    LocalDate fromDate = LocalDate.parse("2019-11-01"); // LocalDate | The from date for the Bank Summary report e.g. 2018-03-31
    LocalDate toDate = LocalDate.parse("2019-11-30"); // LocalDate | The to date for the Bank Summary report e.g. 2018-03-31
    try {
      ReportWithRows result = apiInstance.getReportBankSummary(xeroTenantId, fromDate, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportBankSummary");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **fromDate** | **LocalDate**| The from date for the Bank Summary report e.g. 2018-03-31 | [optional] |
| **toDate** | **LocalDate**| The to date for the Bank Summary report e.g. 2018-03-31 | [optional] |

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ReportWithRows |  -  |

<a id="getReportBudgetSummary"></a>
# **getReportBudgetSummary**
> ReportWithRows getReportBudgetSummary(xeroTenantId, date, period, timeframe)

Retrieves report for budget summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    LocalDate date = LocalDate.parse("2019-03-31"); // LocalDate | The date for the Bank Summary report e.g. 2018-03-31
    Integer period = 2; // Integer | The number of periods to compare (integer between 1 and 12)
    Integer timeframe = 3; // Integer | The period size to compare to (1=month, 3=quarter, 12=year)
    try {
      ReportWithRows result = apiInstance.getReportBudgetSummary(xeroTenantId, date, period, timeframe);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportBudgetSummary");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **date** | **LocalDate**| The date for the Bank Summary report e.g. 2018-03-31 | [optional] |
| **period** | **Integer**| The number of periods to compare (integer between 1 and 12) | [optional] |
| **timeframe** | **Integer**| The period size to compare to (1&#x3D;month, 3&#x3D;quarter, 12&#x3D;year) | [optional] |

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success- return a Report with Rows object |  -  |

<a id="getReportExecutiveSummary"></a>
# **getReportExecutiveSummary**
> ReportWithRows getReportExecutiveSummary(xeroTenantId, date)

Retrieves report for executive summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    LocalDate date = LocalDate.parse("2019-03-31"); // LocalDate | The date for the Bank Summary report e.g. 2018-03-31
    try {
      ReportWithRows result = apiInstance.getReportExecutiveSummary(xeroTenantId, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportExecutiveSummary");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **date** | **LocalDate**| The date for the Bank Summary report e.g. 2018-03-31 | [optional] |

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ReportWithRows |  -  |

<a id="getReportProfitAndLoss"></a>
# **getReportProfitAndLoss**
> ReportWithRows getReportProfitAndLoss(xeroTenantId, fromDate, toDate, periods, timeframe, trackingCategoryID, trackingCategoryID2, trackingOptionID, trackingOptionID2, standardLayout, paymentsOnly)

Retrieves report for profit and loss

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    LocalDate fromDate = LocalDate.parse("2019-03-01"); // LocalDate | The from date for the ProfitAndLoss report e.g. 2018-03-31
    LocalDate toDate = LocalDate.parse("2019-03-31"); // LocalDate | The to date for the ProfitAndLoss report e.g. 2018-03-31
    Integer periods = 3; // Integer | The number of periods to compare (integer between 1 and 12)
    String timeframe = "MONTH"; // String | The period size to compare to (MONTH, QUARTER, YEAR)
    String trackingCategoryID = "00000000-0000-0000-0000-000000000000"; // String | The trackingCategory 1 for the ProfitAndLoss report
    String trackingCategoryID2 = "00000000-0000-0000-0000-000000000000"; // String | The trackingCategory 2 for the ProfitAndLoss report
    String trackingOptionID = "00000000-0000-0000-0000-000000000000"; // String | The tracking option 1 for the ProfitAndLoss report
    String trackingOptionID2 = "00000000-0000-0000-0000-000000000000"; // String | The tracking option 2 for the ProfitAndLoss report
    Boolean standardLayout = true; // Boolean | Return the standard layout for the ProfitAndLoss report
    Boolean paymentsOnly = false; // Boolean | Return cash only basis for the ProfitAndLoss report
    try {
      ReportWithRows result = apiInstance.getReportProfitAndLoss(xeroTenantId, fromDate, toDate, periods, timeframe, trackingCategoryID, trackingCategoryID2, trackingOptionID, trackingOptionID2, standardLayout, paymentsOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportProfitAndLoss");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **fromDate** | **LocalDate**| The from date for the ProfitAndLoss report e.g. 2018-03-31 | [optional] |
| **toDate** | **LocalDate**| The to date for the ProfitAndLoss report e.g. 2018-03-31 | [optional] |
| **periods** | **Integer**| The number of periods to compare (integer between 1 and 12) | [optional] |
| **timeframe** | **String**| The period size to compare to (MONTH, QUARTER, YEAR) | [optional] [enum: MONTH, QUARTER, YEAR] |
| **trackingCategoryID** | **String**| The trackingCategory 1 for the ProfitAndLoss report | [optional] |
| **trackingCategoryID2** | **String**| The trackingCategory 2 for the ProfitAndLoss report | [optional] |
| **trackingOptionID** | **String**| The tracking option 1 for the ProfitAndLoss report | [optional] |
| **trackingOptionID2** | **String**| The tracking option 2 for the ProfitAndLoss report | [optional] |
| **standardLayout** | **Boolean**| Return the standard layout for the ProfitAndLoss report | [optional] |
| **paymentsOnly** | **Boolean**| Return cash only basis for the ProfitAndLoss report | [optional] |

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ReportWithRows |  -  |

<a id="getReportTenNinetyNine"></a>
# **getReportTenNinetyNine**
> Reports getReportTenNinetyNine(xeroTenantId, reportYear)

Retrieve reports for 1099

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    String reportYear = "2019"; // String | The year of the 1099 report
    try {
      Reports result = apiInstance.getReportTenNinetyNine(xeroTenantId, reportYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportTenNinetyNine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **reportYear** | **String**| The year of the 1099 report | [optional] |

### Return type

[**Reports**](Reports.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Reports |  -  |

<a id="getReportTrialBalance"></a>
# **getReportTrialBalance**
> ReportWithRows getReportTrialBalance(xeroTenantId, date, paymentsOnly)

Retrieves report for trial balance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    LocalDate date = LocalDate.parse("2019-10-31"); // LocalDate | The date for the Trial Balance report e.g. 2018-03-31
    Boolean paymentsOnly = true; // Boolean | Return cash only basis for the Trial Balance report
    try {
      ReportWithRows result = apiInstance.getReportTrialBalance(xeroTenantId, date, paymentsOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getReportTrialBalance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **date** | **LocalDate**| The date for the Trial Balance report e.g. 2018-03-31 | [optional] |
| **paymentsOnly** | **Boolean**| Return cash only basis for the Trial Balance report | [optional] |

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ReportWithRows |  -  |

<a id="getTaxRates"></a>
# **getTaxRates**
> TaxRates getTaxRates(xeroTenantId, where, order, taxType)

Retrieves tax rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "Name ASC"; // String | Order by an any element
    String taxType = "INPUT"; // String | Filter by tax type
    try {
      TaxRates result = apiInstance.getTaxRates(xeroTenantId, where, order, taxType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getTaxRates");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **taxType** | **String**| Filter by tax type | [optional] |

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TaxRates array with TaxRates |  -  |

<a id="getTrackingCategories"></a>
# **getTrackingCategories**
> TrackingCategories getTrackingCategories(xeroTenantId, where, order, includeArchived)

Retrieves tracking categories and options

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    String where = "Status==\"ACTIVE\""; // String | Filter by an any element
    String order = "Name ASC"; // String | Order by an any element
    Boolean includeArchived = true; // Boolean | e.g. includeArchived=true - Categories and options with a status of ARCHIVED will be included in the response
    try {
      TrackingCategories result = apiInstance.getTrackingCategories(xeroTenantId, where, order, includeArchived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getTrackingCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |
| **includeArchived** | **Boolean**| e.g. includeArchived&#x3D;true - Categories and options with a status of ARCHIVED will be included in the response | [optional] |

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TrackingCategories array of TrackingCategory |  -  |

<a id="getTrackingCategory"></a>
# **getTrackingCategory**
> TrackingCategories getTrackingCategory(xeroTenantId, trackingCategoryID)

Retrieves specific tracking categories and options using a unique tracking category Id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID trackingCategoryID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a TrackingCategory
    try {
      TrackingCategories result = apiInstance.getTrackingCategory(xeroTenantId, trackingCategoryID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getTrackingCategory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **trackingCategoryID** | **UUID**| Unique identifier for a TrackingCategory | |

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TrackingCategories array of specified TrackingCategory |  -  |

<a id="getUser"></a>
# **getUser**
> Users getUser(xeroTenantId, userID)

Retrieves a specific user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID userID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a User
    try {
      Users result = apiInstance.getUser(xeroTenantId, userID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **userID** | **UUID**| Unique identifier for a User | |

### Return type

[**Users**](Users.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Users array of specified User |  -  |

<a id="getUsers"></a>
# **getUsers**
> Users getUsers(xeroTenantId, ifModifiedSince, where, order)

Retrieves users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    OffsetDateTime ifModifiedSince = OffsetDateTime.parse("2020-02-06T12:17:43.202-08:00"); // OffsetDateTime | Only records created or modified since this timestamp will be returned
    String where = "IsSubscriber==true"; // String | Filter by an any element
    String order = "LastName ASC"; // String | Order by an any element
    try {
      Users result = apiInstance.getUsers(xeroTenantId, ifModifiedSince, where, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#getUsers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **ifModifiedSince** | **OffsetDateTime**| Only records created or modified since this timestamp will be returned | [optional] |
| **where** | **String**| Filter by an any element | [optional] |
| **order** | **String**| Order by an any element | [optional] |

### Return type

[**Users**](Users.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Users array of all User |  -  |

<a id="postSetup"></a>
# **postSetup**
> ImportSummaryObject postSetup(xeroTenantId, setup)

Sets the chart of accounts, the conversion date and conversion balances

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Setup setup = new Setup(); // Setup | Object including an accounts array, a conversion balances array and a conversion date object in body of request
    try {
      ImportSummaryObject result = apiInstance.postSetup(xeroTenantId, setup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#postSetup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **setup** | [**Setup**](Setup.md)| Object including an accounts array, a conversion balances array and a conversion date object in body of request | |

### Return type

[**ImportSummaryObject**](ImportSummaryObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - returns a summary of the chart of accounts updates |  -  |

<a id="updateAccount"></a>
# **updateAccount**
> Accounts updateAccount(xeroTenantId, accountID, accounts)

Updates a chart of accounts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID accountID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for retrieving single object
    Accounts accounts = new Accounts(); // Accounts | Request of type Accounts array with one Account
    try {
      Accounts result = apiInstance.updateAccount(xeroTenantId, accountID, accounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **accountID** | **UUID**| Unique identifier for retrieving single object | |
| **accounts** | [**Accounts**](Accounts.md)| Request of type Accounts array with one Account | |

### Return type

[**Accounts**](Accounts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - update existing Account and return response of type Accounts array with updated Account |  -  |
| **400** | Validation Error - some data was incorrect returns response of type Error |  -  |

<a id="updateAccountAttachmentByFileName"></a>
# **updateAccountAttachmentByFileName**
> Attachments updateAccountAttachmentByFileName(xeroTenantId, accountID, fileName, body)

Updates attachment on a specific account by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID accountID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Account object
    String fileName = "xero-dev.jpg"; // String | Name of the attachment
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updateAccountAttachmentByFileName(xeroTenantId, accountID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateAccountAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **accountID** | **UUID**| Unique identifier for Account object | |
| **fileName** | **String**| Name of the attachment | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Attachment |  -  |
| **400** | Validation Error - some data was incorrect returns response of type Error |  -  |

<a id="updateBankTransaction"></a>
# **updateBankTransaction**
> BankTransactions updateBankTransaction(xeroTenantId, bankTransactionID, bankTransactions, unitdp)

Updates a single spent or received money transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transaction
    BankTransactions bankTransactions = new BankTransactions(); // BankTransactions | 
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      BankTransactions result = apiInstance.updateBankTransaction(xeroTenantId, bankTransactionID, bankTransactions, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateBankTransaction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactionID** | **UUID**| Xero generated unique identifier for a bank transaction | |
| **bankTransactions** | [**BankTransactions**](BankTransactions.md)|  | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type BankTransactions array with updated BankTransaction |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateBankTransactionAttachmentByFileName"></a>
# **updateBankTransactionAttachmentByFileName**
> Attachments updateBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, body)

Updates a specific attachment from a specific bank transaction by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transaction
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updateBankTransactionAttachmentByFileName(xeroTenantId, bankTransactionID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateBankTransactionAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactionID** | **UUID**| Xero generated unique identifier for a bank transaction | |
| **fileName** | **String**| The name of the file being attached | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of Attachments array of Attachment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateBankTransferAttachmentByFileName"></a>
# **updateBankTransferAttachmentByFileName**
> Attachments updateBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID bankTransferID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Xero generated unique identifier for a bank transfer
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Bank Transfer
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updateBankTransferAttachmentByFileName(xeroTenantId, bankTransferID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateBankTransferAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransferID** | **UUID**| Xero generated unique identifier for a bank transfer | |
| **fileName** | **String**| The name of the file being attached to a Bank Transfer | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of Attachments array of 0 to N Attachment for a Bank Transfer |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateContact"></a>
# **updateContact**
> Contacts updateContact(xeroTenantId, contactID, contacts)

Updates a specific contact in a Xero organisation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    Contacts contacts = new Contacts(); // Contacts | an array of Contacts containing single Contact object with properties to update
    try {
      Contacts result = apiInstance.updateContact(xeroTenantId, contactID, contacts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateContact");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactID** | **UUID**| Unique identifier for a Contact | |
| **contacts** | [**Contacts**](Contacts.md)| an array of Contacts containing single Contact object with properties to update | |

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contacts array with an updated Contact |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateContactAttachmentByFileName"></a>
# **updateContactAttachmentByFileName**
> Attachments updateContactAttachmentByFileName(xeroTenantId, contactID, fileName, body)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact
    String fileName = "xero-dev.jpg"; // String | Name for the file you are attaching
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updateContactAttachmentByFileName(xeroTenantId, contactID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateContactAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactID** | **UUID**| Unique identifier for a Contact | |
| **fileName** | **String**| Name for the file you are attaching | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with an updated Attachment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateContactGroup"></a>
# **updateContactGroup**
> ContactGroups updateContactGroup(xeroTenantId, contactGroupID, contactGroups)

Updates a specific contact group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID contactGroupID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Contact Group
    ContactGroups contactGroups = new ContactGroups(); // ContactGroups | an array of Contact groups with Name of specific group to update
    try {
      ContactGroups result = apiInstance.updateContactGroup(xeroTenantId, contactGroupID, contactGroups);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateContactGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contactGroupID** | **UUID**| Unique identifier for a Contact Group | |
| **contactGroups** | [**ContactGroups**](ContactGroups.md)| an array of Contact groups with Name of specific group to update | |

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contact Groups array of updated Contact Group |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateCreditNote"></a>
# **updateCreditNote**
> CreditNotes updateCreditNote(xeroTenantId, creditNoteID, creditNotes, unitdp)

Updates a specific credit note

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    CreditNotes creditNotes = new CreditNotes(); // CreditNotes | an array of Credit Notes containing credit note details to update
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      CreditNotes result = apiInstance.updateCreditNote(xeroTenantId, creditNoteID, creditNotes, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateCreditNote");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |
| **creditNotes** | [**CreditNotes**](CreditNotes.md)| an array of Credit Notes containing credit note details to update | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Credit Notes array with updated CreditNote |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateCreditNoteAttachmentByFileName"></a>
# **updateCreditNoteAttachmentByFileName**
> Attachments updateCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, body)

Updates attachments on a specific credit note by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID creditNoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Credit Note
    String fileName = "xero-dev.jpg"; // String | Name of the file you are attaching to Credit Note
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updateCreditNoteAttachmentByFileName(xeroTenantId, creditNoteID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateCreditNoteAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNoteID** | **UUID**| Unique identifier for a Credit Note | |
| **fileName** | **String**| Name of the file you are attaching to Credit Note | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with updated Attachment for specific Credit Note |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateExpenseClaim"></a>
# **updateExpenseClaim**
> ExpenseClaims updateExpenseClaim(xeroTenantId, expenseClaimID, expenseClaims)

Updates a specific expense claims

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID expenseClaimID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ExpenseClaim
    ExpenseClaims expenseClaims = new ExpenseClaims(); // ExpenseClaims | 
    try {
      ExpenseClaims result = apiInstance.updateExpenseClaim(xeroTenantId, expenseClaimID, expenseClaims);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateExpenseClaim");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **expenseClaimID** | **UUID**| Unique identifier for a ExpenseClaim | |
| **expenseClaims** | [**ExpenseClaims**](ExpenseClaims.md)|  | |

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ExpenseClaims array with updated ExpenseClaim |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateInvoice"></a>
# **updateInvoice**
> Invoices updateInvoice(xeroTenantId, invoiceID, invoices, unitdp)

Updates a specific sales invoices or purchase bills

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    Invoices invoices = new Invoices(); // Invoices | 
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Invoices result = apiInstance.updateInvoice(xeroTenantId, invoiceID, invoices, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateInvoice");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |
| **invoices** | [**Invoices**](Invoices.md)|  | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Invoices array with updated Invoice |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateInvoiceAttachmentByFileName"></a>
# **updateInvoiceAttachmentByFileName**
> Attachments updateInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, body)

Updates an attachment from a specific invoices or purchase bill by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID invoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Invoice
    String fileName = "xero-dev.jpg"; // String | Name of the file you are attaching
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updateInvoiceAttachmentByFileName(xeroTenantId, invoiceID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateInvoiceAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoiceID** | **UUID**| Unique identifier for an Invoice | |
| **fileName** | **String**| Name of the file you are attaching | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with updated Attachment |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateItem"></a>
# **updateItem**
> Items updateItem(xeroTenantId, itemID, items, unitdp)

Updates a specific item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID itemID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Item
    Items items = new Items(); // Items | 
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Items result = apiInstance.updateItem(xeroTenantId, itemID, items, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **itemID** | **UUID**| Unique identifier for an Item | |
| **items** | [**Items**](Items.md)|  | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Items array with updated Item |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateLinkedTransaction"></a>
# **updateLinkedTransaction**
> LinkedTransactions updateLinkedTransaction(xeroTenantId, linkedTransactionID, linkedTransactions)

Updates a specific linked transactions (billable expenses)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID linkedTransactionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a LinkedTransaction
    LinkedTransactions linkedTransactions = new LinkedTransactions(); // LinkedTransactions | 
    try {
      LinkedTransactions result = apiInstance.updateLinkedTransaction(xeroTenantId, linkedTransactionID, linkedTransactions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateLinkedTransaction");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **linkedTransactionID** | **UUID**| Unique identifier for a LinkedTransaction | |
| **linkedTransactions** | [**LinkedTransactions**](LinkedTransactions.md)|  | |

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type LinkedTransactions array with updated LinkedTransaction |  -  |
| **400** | Success - return response of type LinkedTransactions array with updated LinkedTransaction |  -  |

<a id="updateManualJournal"></a>
# **updateManualJournal**
> ManualJournals updateManualJournal(xeroTenantId, manualJournalID, manualJournals)

Updates a specific manual journal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID manualJournalID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ManualJournal
    ManualJournals manualJournals = new ManualJournals(); // ManualJournals | 
    try {
      ManualJournals result = apiInstance.updateManualJournal(xeroTenantId, manualJournalID, manualJournals);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateManualJournal");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournalID** | **UUID**| Unique identifier for a ManualJournal | |
| **manualJournals** | [**ManualJournals**](ManualJournals.md)|  | |

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ManualJournals array with an updated ManualJournal |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateManualJournalAttachmentByFileName"></a>
# **updateManualJournalAttachmentByFileName**
> Attachments updateManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, body)

Updates a specific attachment from a specific manual journal by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID manualJournalID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a ManualJournal
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to a ManualJournal
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updateManualJournalAttachmentByFileName(xeroTenantId, manualJournalID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateManualJournalAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournalID** | **UUID**| Unique identifier for a ManualJournal | |
| **fileName** | **String**| The name of the file being attached to a ManualJournal | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with an update Attachment for a ManualJournals |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateOrCreateBankTransactions"></a>
# **updateOrCreateBankTransactions**
> BankTransactions updateOrCreateBankTransactions(xeroTenantId, bankTransactions, summarizeErrors, unitdp)

Updates or creates one or more spent or received money transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    BankTransactions bankTransactions = new BankTransactions(); // BankTransactions | 
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      BankTransactions result = apiInstance.updateOrCreateBankTransactions(xeroTenantId, bankTransactions, summarizeErrors, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateOrCreateBankTransactions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **bankTransactions** | [**BankTransactions**](BankTransactions.md)|  | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type BankTransactions array with new BankTransaction |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateOrCreateContacts"></a>
# **updateOrCreateContacts**
> Contacts updateOrCreateContacts(xeroTenantId, contacts, summarizeErrors)

Updates or creates one or more contacts in a Xero organisation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Contacts contacts = new Contacts(); // Contacts | 
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      Contacts result = apiInstance.updateOrCreateContacts(xeroTenantId, contacts, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateOrCreateContacts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **contacts** | [**Contacts**](Contacts.md)|  | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**Contacts**](Contacts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Contacts array with newly created Contact |  -  |
| **400** | Validation Error - some data was incorrect returns response of type Error |  -  |

<a id="updateOrCreateCreditNotes"></a>
# **updateOrCreateCreditNotes**
> CreditNotes updateOrCreateCreditNotes(xeroTenantId, creditNotes, summarizeErrors, unitdp)

Updates or creates one or more credit notes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    CreditNotes creditNotes = new CreditNotes(); // CreditNotes | an array of Credit Notes with a single CreditNote object.
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      CreditNotes result = apiInstance.updateOrCreateCreditNotes(xeroTenantId, creditNotes, summarizeErrors, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateOrCreateCreditNotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **creditNotes** | [**CreditNotes**](CreditNotes.md)| an array of Credit Notes with a single CreditNote object. | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Credit Notes array of newly created CreditNote |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateOrCreateEmployees"></a>
# **updateOrCreateEmployees**
> Employees updateOrCreateEmployees(xeroTenantId, employees, summarizeErrors)

Creates a single new employees used in Xero payrun

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Employees employees = new Employees(); // Employees | Employees with array of Employee object in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      Employees result = apiInstance.updateOrCreateEmployees(xeroTenantId, employees, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateOrCreateEmployees");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **employees** | [**Employees**](Employees.md)| Employees with array of Employee object in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Employees array with new Employee |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateOrCreateInvoices"></a>
# **updateOrCreateInvoices**
> Invoices updateOrCreateInvoices(xeroTenantId, invoices, summarizeErrors, unitdp)

Updates or creates one or more sales invoices or purchase bills

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Invoices invoices = new Invoices(); // Invoices | 
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Invoices result = apiInstance.updateOrCreateInvoices(xeroTenantId, invoices, summarizeErrors, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateOrCreateInvoices");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **invoices** | [**Invoices**](Invoices.md)|  | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Invoices**](Invoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Invoices array with newly created Invoice |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateOrCreateItems"></a>
# **updateOrCreateItems**
> Items updateOrCreateItems(xeroTenantId, items, summarizeErrors, unitdp)

Updates or creates one or more items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Items items = new Items(); // Items | 
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Items result = apiInstance.updateOrCreateItems(xeroTenantId, items, summarizeErrors, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateOrCreateItems");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **items** | [**Items**](Items.md)|  | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Items**](Items.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Items array with newly created Item |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateOrCreateManualJournals"></a>
# **updateOrCreateManualJournals**
> ManualJournals updateOrCreateManualJournals(xeroTenantId, manualJournals, summarizeErrors)

Updates or creates a single manual journal

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    ManualJournals manualJournals = new ManualJournals(); // ManualJournals | ManualJournals array with ManualJournal object in body of request
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      ManualJournals result = apiInstance.updateOrCreateManualJournals(xeroTenantId, manualJournals, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateOrCreateManualJournals");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **manualJournals** | [**ManualJournals**](ManualJournals.md)| ManualJournals array with ManualJournal object in body of request | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type ManualJournals array with newly created ManualJournal |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateOrCreatePurchaseOrders"></a>
# **updateOrCreatePurchaseOrders**
> PurchaseOrders updateOrCreatePurchaseOrders(xeroTenantId, purchaseOrders, summarizeErrors)

Updates or creates one or more purchase orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    PurchaseOrders purchaseOrders = new PurchaseOrders(); // PurchaseOrders | 
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      PurchaseOrders result = apiInstance.updateOrCreatePurchaseOrders(xeroTenantId, purchaseOrders, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateOrCreatePurchaseOrders");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrders** | [**PurchaseOrders**](PurchaseOrders.md)|  | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type PurchaseOrder array for specified PurchaseOrder |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateOrCreateQuotes"></a>
# **updateOrCreateQuotes**
> Quotes updateOrCreateQuotes(xeroTenantId, quotes, summarizeErrors)

Updates or creates one or more quotes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    Quotes quotes = new Quotes(); // Quotes | 
    Boolean summarizeErrors = false; // Boolean | If false return 200 OK and mix of successfully created objects and any with validation errors
    try {
      Quotes result = apiInstance.updateOrCreateQuotes(xeroTenantId, quotes, summarizeErrors);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateOrCreateQuotes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quotes** | [**Quotes**](Quotes.md)|  | |
| **summarizeErrors** | **Boolean**| If false return 200 OK and mix of successfully created objects and any with validation errors | [optional] [default to false] |

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Quotes array with updated or created Quote |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updatePurchaseOrder"></a>
# **updatePurchaseOrder**
> PurchaseOrders updatePurchaseOrder(xeroTenantId, purchaseOrderID, purchaseOrders)

Updates a specific purchase order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID purchaseOrderID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a PurchaseOrder
    PurchaseOrders purchaseOrders = new PurchaseOrders(); // PurchaseOrders | 
    try {
      PurchaseOrders result = apiInstance.updatePurchaseOrder(xeroTenantId, purchaseOrderID, purchaseOrders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updatePurchaseOrder");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderID** | **UUID**| Unique identifier for a PurchaseOrder | |
| **purchaseOrders** | [**PurchaseOrders**](PurchaseOrders.md)|  | |

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type PurchaseOrder array for updated PurchaseOrder |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updatePurchaseOrderAttachmentByFileName"></a>
# **updatePurchaseOrderAttachmentByFileName**
> Attachments updatePurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, body)

Updates a specific attachment for a specific purchase order by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID purchaseOrderID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Purchase Order object
    String fileName = "xero-dev.png"; // String | Name of the attachment
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updatePurchaseOrderAttachmentByFileName(xeroTenantId, purchaseOrderID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updatePurchaseOrderAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **purchaseOrderID** | **UUID**| Unique identifier for Purchase Order object | |
| **fileName** | **String**| Name of the attachment | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Attachment |  -  |
| **400** | Validation Error - some data was incorrect returns response of type Error |  -  |

<a id="updateQuote"></a>
# **updateQuote**
> Quotes updateQuote(xeroTenantId, quoteID, quotes)

Updates a specific quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID quoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for an Quote
    Quotes quotes = new Quotes(); // Quotes | 
    try {
      Quotes result = apiInstance.updateQuote(xeroTenantId, quoteID, quotes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateQuote");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quoteID** | **UUID**| Unique identifier for an Quote | |
| **quotes** | [**Quotes**](Quotes.md)|  | |

### Return type

[**Quotes**](Quotes.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Quotes array with updated Quote |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateQuoteAttachmentByFileName"></a>
# **updateQuoteAttachmentByFileName**
> Attachments updateQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, body)

Updates a specific attachment from a specific quote by filename

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID quoteID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for Quote object
    String fileName = "xero-dev.jpg"; // String | Name of the attachment
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updateQuoteAttachmentByFileName(xeroTenantId, quoteID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateQuoteAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **quoteID** | **UUID**| Unique identifier for Quote object | |
| **fileName** | **String**| Name of the attachment | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array of Attachment |  -  |
| **400** | Validation Error - some data was incorrect returns response of type Error |  -  |

<a id="updateReceipt"></a>
# **updateReceipt**
> Receipts updateReceipt(xeroTenantId, receiptID, receipts, unitdp)

Updates a specific draft expense claim receipts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID receiptID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Receipt
    Receipts receipts = new Receipts(); // Receipts | 
    Integer unitdp = 4; // Integer | e.g. unitdp=4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    try {
      Receipts result = apiInstance.updateReceipt(xeroTenantId, receiptID, receipts, unitdp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateReceipt");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **receiptID** | **UUID**| Unique identifier for a Receipt | |
| **receipts** | [**Receipts**](Receipts.md)|  | |
| **unitdp** | **Integer**| e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts | [optional] |

### Return type

[**Receipts**](Receipts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Receipts array for updated Receipt |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateReceiptAttachmentByFileName"></a>
# **updateReceiptAttachmentByFileName**
> Attachments updateReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, body)

Updates a specific attachment on a specific expense claim receipts by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID receiptID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Receipt
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to the Receipt
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updateReceiptAttachmentByFileName(xeroTenantId, receiptID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateReceiptAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **receiptID** | **UUID**| Unique identifier for a Receipt | |
| **fileName** | **String**| The name of the file being attached to the Receipt | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with updated Attachment for a specified Receipt |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateRepeatingInvoiceAttachmentByFileName"></a>
# **updateRepeatingInvoiceAttachmentByFileName**
> Attachments updateRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, body)

Updates a specific attachment from a specific repeating invoices by file name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID repeatingInvoiceID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Repeating Invoice
    String fileName = "xero-dev.jpg"; // String | The name of the file being attached to a Repeating Invoice
    byte[] body = null; // byte[] | Byte array of file in body of request
    try {
      Attachments result = apiInstance.updateRepeatingInvoiceAttachmentByFileName(xeroTenantId, repeatingInvoiceID, fileName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateRepeatingInvoiceAttachmentByFileName");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **repeatingInvoiceID** | **UUID**| Unique identifier for a Repeating Invoice | |
| **fileName** | **String**| The name of the file being attached to a Repeating Invoice | |
| **body** | **byte[]**| Byte array of file in body of request | |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type Attachments array with specified Attachment for a specified Repeating Invoice |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateTaxRate"></a>
# **updateTaxRate**
> TaxRates updateTaxRate(xeroTenantId, taxRates)

Updates tax rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    TaxRates taxRates = new TaxRates(); // TaxRates | 
    try {
      TaxRates result = apiInstance.updateTaxRate(xeroTenantId, taxRates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateTaxRate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **taxRates** | [**TaxRates**](TaxRates.md)|  | |

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TaxRates array updated TaxRate |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateTrackingCategory"></a>
# **updateTrackingCategory**
> TrackingCategories updateTrackingCategory(xeroTenantId, trackingCategoryID, trackingCategory)

Updates a specific tracking category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID trackingCategoryID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a TrackingCategory
    TrackingCategory trackingCategory = new TrackingCategory(); // TrackingCategory | 
    try {
      TrackingCategories result = apiInstance.updateTrackingCategory(xeroTenantId, trackingCategoryID, trackingCategory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateTrackingCategory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **trackingCategoryID** | **UUID**| Unique identifier for a TrackingCategory | |
| **trackingCategory** | [**TrackingCategory**](TrackingCategory.md)|  | |

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TrackingCategories array of updated TrackingCategory |  -  |
| **400** | A failed request due to validation error |  -  |

<a id="updateTrackingOptions"></a>
# **updateTrackingOptions**
> TrackingOptions updateTrackingOptions(xeroTenantId, trackingCategoryID, trackingOptionID, trackingOption)

Updates a specific option for a specific tracking category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.xero.com/api.xro/2.0");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    AccountingApi apiInstance = new AccountingApi(defaultClient);
    String xeroTenantId = "YOUR_XERO_TENANT_ID"; // String | Xero identifier for Tenant
    UUID trackingCategoryID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a TrackingCategory
    UUID trackingOptionID = UUID.fromString("00000000-0000-0000-0000-000000000000"); // UUID | Unique identifier for a Tracking Option
    TrackingOption trackingOption = new TrackingOption(); // TrackingOption | 
    try {
      TrackingOptions result = apiInstance.updateTrackingOptions(xeroTenantId, trackingCategoryID, trackingOptionID, trackingOption);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountingApi#updateTrackingOptions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xeroTenantId** | **String**| Xero identifier for Tenant | |
| **trackingCategoryID** | **UUID**| Unique identifier for a TrackingCategory | |
| **trackingOptionID** | **UUID**| Unique identifier for a Tracking Option | |
| **trackingOption** | [**TrackingOption**](TrackingOption.md)|  | |

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - return response of type TrackingOptions array of options for a specified category |  -  |
| **400** | A failed request due to validation error |  -  |

