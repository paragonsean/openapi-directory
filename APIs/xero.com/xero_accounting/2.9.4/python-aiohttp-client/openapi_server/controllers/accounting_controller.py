from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts import Accounts
from openapi_server.models.actions import Actions
from openapi_server.models.allocations import Allocations
from openapi_server.models.attachments import Attachments
from openapi_server.models.bank_transactions import BankTransactions
from openapi_server.models.bank_transfers import BankTransfers
from openapi_server.models.batch_payments import BatchPayments
from openapi_server.models.branding_themes import BrandingThemes
from openapi_server.models.cis_org_settings import CISOrgSettings
from openapi_server.models.cis_settings import CISSettings
from openapi_server.models.contact_groups import ContactGroups
from openapi_server.models.contacts import Contacts
from openapi_server.models.credit_notes import CreditNotes
from openapi_server.models.currencies import Currencies
from openapi_server.models.currency import Currency
from openapi_server.models.employees import Employees
from openapi_server.models.error import Error
from openapi_server.models.expense_claims import ExpenseClaims
from openapi_server.models.history_records import HistoryRecords
from openapi_server.models.import_summary_object import ImportSummaryObject
from openapi_server.models.invoice_reminders import InvoiceReminders
from openapi_server.models.invoices import Invoices
from openapi_server.models.items import Items
from openapi_server.models.journals import Journals
from openapi_server.models.linked_transaction import LinkedTransaction
from openapi_server.models.linked_transactions import LinkedTransactions
from openapi_server.models.manual_journals import ManualJournals
from openapi_server.models.online_invoices import OnlineInvoices
from openapi_server.models.organisations import Organisations
from openapi_server.models.overpayments import Overpayments
from openapi_server.models.payment import Payment
from openapi_server.models.payment_delete import PaymentDelete
from openapi_server.models.payment_service import PaymentService
from openapi_server.models.payment_services import PaymentServices
from openapi_server.models.payments import Payments
from openapi_server.models.prepayments import Prepayments
from openapi_server.models.purchase_orders import PurchaseOrders
from openapi_server.models.quotes import Quotes
from openapi_server.models.receipts import Receipts
from openapi_server.models.repeating_invoices import RepeatingInvoices
from openapi_server.models.report_with_rows import ReportWithRows
from openapi_server.models.reports import Reports
from openapi_server.models.request_empty import RequestEmpty
from openapi_server.models.setup import Setup
from openapi_server.models.tax_rates import TaxRates
from openapi_server.models.tracking_categories import TrackingCategories
from openapi_server.models.tracking_category import TrackingCategory
from openapi_server.models.tracking_option import TrackingOption
from openapi_server.models.tracking_options import TrackingOptions
from openapi_server.models.users import Users
from openapi_server import util


async def create_account(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a new chart of accounts

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Account object in body of request
    :type body: dict | bytes

    """
    body = Account.from_dict(body)
    return web.Response(status=200)


async def create_account_attachment_by_file_name(request: web.Request, xero_tenant_id, account_id, file_name, body) -> web.Response:
    """Creates an attachment on a specific account

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param account_id: Unique identifier for Account object
    :type account_id: str
    :type account_id: str
    :param file_name: Name of the attachment
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def create_bank_transaction_attachment_by_file_name(request: web.Request, xero_tenant_id, bank_transaction_id, file_name, body) -> web.Response:
    """Creates an attachment for a specific bank transaction by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transaction_id: Xero generated unique identifier for a bank transaction
    :type bank_transaction_id: str
    :type bank_transaction_id: str
    :param file_name: The name of the file being attached
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def create_bank_transaction_history_record(request: web.Request, xero_tenant_id, bank_transaction_id, body) -> web.Response:
    """Creates a history record for a specific bank transactions

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transaction_id: Xero generated unique identifier for a bank transaction
    :type bank_transaction_id: str
    :type bank_transaction_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_bank_transactions(request: web.Request, xero_tenant_id, body, summarize_errors=None, unitdp=None) -> web.Response:
    """Creates one or more spent or received money transaction

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: BankTransactions with an array of BankTransaction objects in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = BankTransactions.from_dict(body)
    return web.Response(status=200)


async def create_bank_transfer(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a bank transfer

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: BankTransfers with array of BankTransfer objects in request body
    :type body: dict | bytes

    """
    body = BankTransfers.from_dict(body)
    return web.Response(status=200)


async def create_bank_transfer_attachment_by_file_name(request: web.Request, xero_tenant_id, bank_transfer_id, file_name, body) -> web.Response:
    """create_bank_transfer_attachment_by_file_name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transfer_id: Xero generated unique identifier for a bank transfer
    :type bank_transfer_id: str
    :type bank_transfer_id: str
    :param file_name: The name of the file being attached to a Bank Transfer
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def create_bank_transfer_history_record(request: web.Request, xero_tenant_id, bank_transfer_id, body) -> web.Response:
    """Creates a history record for a specific bank transfer

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transfer_id: Xero generated unique identifier for a bank transfer
    :type bank_transfer_id: str
    :type bank_transfer_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_batch_payment(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Creates one or many batch payments for invoices

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: BatchPayments with an array of Payments in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = BatchPayments.from_dict(body)
    return web.Response(status=200)


async def create_batch_payment_history_record(request: web.Request, xero_tenant_id, batch_payment_id, body) -> web.Response:
    """Creates a history record for a specific batch payment

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param batch_payment_id: Unique identifier for BatchPayment
    :type batch_payment_id: str
    :type batch_payment_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_branding_theme_payment_services(request: web.Request, xero_tenant_id, branding_theme_id, body) -> web.Response:
    """Creates a new custom payment service for a specific branding theme

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param branding_theme_id: Unique identifier for a Branding Theme
    :type branding_theme_id: str
    :type branding_theme_id: str
    :param body: PaymentService object in body of request
    :type body: dict | bytes

    """
    body = PaymentService.from_dict(body)
    return web.Response(status=200)


async def create_contact_attachment_by_file_name(request: web.Request, xero_tenant_id, contact_id, file_name, body) -> web.Response:
    """create_contact_attachment_by_file_name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str
    :param file_name: Name for the file you are attaching
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def create_contact_group(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a contact group

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: ContactGroups with an array of names in request body
    :type body: dict | bytes

    """
    body = ContactGroups.from_dict(body)
    return web.Response(status=200)


async def create_contact_group_contacts(request: web.Request, xero_tenant_id, contact_group_id, body) -> web.Response:
    """Creates contacts to a specific contact group

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_group_id: Unique identifier for a Contact Group
    :type contact_group_id: str
    :type contact_group_id: str
    :param body: Contacts with array of contacts specifying the ContactID to be added to ContactGroup in body of request
    :type body: dict | bytes

    """
    body = Contacts.from_dict(body)
    return web.Response(status=200)


async def create_contact_history(request: web.Request, xero_tenant_id, contact_id, body) -> web.Response:
    """Creates a new history record for a specific contact

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_contacts(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Creates multiple contacts (bulk) in a Xero organisation

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Contacts with an array of Contact objects to create in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = Contacts.from_dict(body)
    return web.Response(status=200)


async def create_credit_note_allocation(request: web.Request, xero_tenant_id, credit_note_id, body, summarize_errors=None) -> web.Response:
    """Creates allocation for a specific credit note

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str
    :param body: Allocations with array of Allocation object in body of request.
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = Allocations.from_dict(body)
    return web.Response(status=200)


async def create_credit_note_attachment_by_file_name(request: web.Request, xero_tenant_id, credit_note_id, file_name, body, include_online=None) -> web.Response:
    """Creates an attachment for a specific credit note

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str
    :param file_name: Name of the file you are attaching to Credit Note
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str
    :param include_online: Allows an attachment to be seen by the end customer within their online invoice
    :type include_online: bool

    """
    return web.Response(status=200)


async def create_credit_note_history(request: web.Request, xero_tenant_id, credit_note_id, body) -> web.Response:
    """Retrieves history records of a specific credit note

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_credit_notes(request: web.Request, xero_tenant_id, body, summarize_errors=None, unitdp=None) -> web.Response:
    """Creates a new credit note

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Credit Notes with array of CreditNote object in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = CreditNotes.from_dict(body)
    return web.Response(status=200)


async def create_currency(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Create a new currency for a Xero organisation

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Currency object in the body of request
    :type body: dict | bytes

    """
    body = Currency.from_dict(body)
    return web.Response(status=200)


async def create_employees(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Creates new employees used in Xero payrun

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Employees with array of Employee object in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = Employees.from_dict(body)
    return web.Response(status=200)


async def create_expense_claim_history(request: web.Request, xero_tenant_id, expense_claim_id, body) -> web.Response:
    """Creates a history record for a specific expense claim

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param expense_claim_id: Unique identifier for a ExpenseClaim
    :type expense_claim_id: str
    :type expense_claim_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_expense_claims(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates expense claims

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: ExpenseClaims with array of ExpenseClaim object in body of request
    :type body: dict | bytes

    """
    body = ExpenseClaims.from_dict(body)
    return web.Response(status=200)


async def create_invoice_attachment_by_file_name(request: web.Request, xero_tenant_id, invoice_id, file_name, body, include_online=None) -> web.Response:
    """Creates an attachment for a specific invoice or purchase bill by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str
    :param file_name: Name of the file you are attaching
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str
    :param include_online: Allows an attachment to be seen by the end customer within their online invoice
    :type include_online: bool

    """
    return web.Response(status=200)


async def create_invoice_history(request: web.Request, xero_tenant_id, invoice_id, body) -> web.Response:
    """Creates a history record for a specific invoice

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_invoices(request: web.Request, xero_tenant_id, body, summarize_errors=None, unitdp=None) -> web.Response:
    """Creates one or more sales invoices or purchase bills

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Invoices with an array of invoice objects in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = Invoices.from_dict(body)
    return web.Response(status=200)


async def create_item_history(request: web.Request, xero_tenant_id, item_id, body) -> web.Response:
    """Creates a history record for a specific item

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param item_id: Unique identifier for an Item
    :type item_id: str
    :type item_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_items(request: web.Request, xero_tenant_id, body, summarize_errors=None, unitdp=None) -> web.Response:
    """Creates one or more items

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Items with an array of Item objects in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = Items.from_dict(body)
    return web.Response(status=200)


async def create_linked_transaction(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates linked transactions (billable expenses)

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: LinkedTransaction object in body of request
    :type body: dict | bytes

    """
    body = LinkedTransaction.from_dict(body)
    return web.Response(status=200)


async def create_manual_journal_attachment_by_file_name(request: web.Request, xero_tenant_id, manual_journal_id, file_name, body) -> web.Response:
    """Creates a specific attachment for a specific manual journal by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param manual_journal_id: Unique identifier for a ManualJournal
    :type manual_journal_id: str
    :type manual_journal_id: str
    :param file_name: The name of the file being attached to a ManualJournal
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def create_manual_journal_history_record(request: web.Request, xero_tenant_id, manual_journal_id, body) -> web.Response:
    """Creates a history record for a specific manual journal

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param manual_journal_id: Xero generated unique identifier for a manual journal
    :type manual_journal_id: str
    :type manual_journal_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_manual_journals(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Creates one or more manual journals

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: ManualJournals array with ManualJournal object in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = ManualJournals.from_dict(body)
    return web.Response(status=200)


async def create_overpayment_allocations(request: web.Request, xero_tenant_id, overpayment_id, body, summarize_errors=None) -> web.Response:
    """Creates a single allocation for a specific overpayment

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param overpayment_id: Unique identifier for a Overpayment
    :type overpayment_id: str
    :type overpayment_id: str
    :param body: Allocations array with Allocation object in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = Allocations.from_dict(body)
    return web.Response(status=200)


async def create_overpayment_history(request: web.Request, xero_tenant_id, overpayment_id, body) -> web.Response:
    """Creates a history record for a specific overpayment

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param overpayment_id: Unique identifier for a Overpayment
    :type overpayment_id: str
    :type overpayment_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_payment(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a single payment for invoice or credit notes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Request body with a single Payment object
    :type body: dict | bytes

    """
    body = Payment.from_dict(body)
    return web.Response(status=200)


async def create_payment_history(request: web.Request, xero_tenant_id, payment_id, body) -> web.Response:
    """Creates a history record for a specific payment

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param payment_id: Unique identifier for a Payment
    :type payment_id: str
    :type payment_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_payment_service(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a payment service

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: PaymentServices array with PaymentService object in body of request
    :type body: dict | bytes

    """
    body = PaymentServices.from_dict(body)
    return web.Response(status=200)


async def create_payments(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Creates multiple payments for invoices or credit notes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Payments array with Payment object in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = Payments.from_dict(body)
    return web.Response(status=200)


async def create_prepayment_allocations(request: web.Request, xero_tenant_id, prepayment_id, body, summarize_errors=None) -> web.Response:
    """Allows you to create an Allocation for prepayments

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param prepayment_id: Unique identifier for Prepayment
    :type prepayment_id: str
    :type prepayment_id: str
    :param body: Allocations with an array of Allocation object in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = Allocations.from_dict(body)
    return web.Response(status=200)


async def create_prepayment_history(request: web.Request, xero_tenant_id, prepayment_id, body) -> web.Response:
    """Creates a history record for a specific prepayment

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param prepayment_id: Unique identifier for a PrePayment
    :type prepayment_id: str
    :type prepayment_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_purchase_order_attachment_by_file_name(request: web.Request, xero_tenant_id, purchase_order_id, file_name, body) -> web.Response:
    """Creates attachment for a specific purchase order

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_id: Unique identifier for Purchase Order object
    :type purchase_order_id: str
    :type purchase_order_id: str
    :param file_name: Name of the attachment
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def create_purchase_order_history(request: web.Request, xero_tenant_id, purchase_order_id, body) -> web.Response:
    """Creates a history record for a specific purchase orders

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_id: Unique identifier for a PurchaseOrder
    :type purchase_order_id: str
    :type purchase_order_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_purchase_orders(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Creates one or more purchase orders

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: PurchaseOrders with an array of PurchaseOrder object in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = PurchaseOrders.from_dict(body)
    return web.Response(status=200)


async def create_quote_attachment_by_file_name(request: web.Request, xero_tenant_id, quote_id, file_name, body) -> web.Response:
    """Creates attachment for a specific quote

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param quote_id: Unique identifier for Quote object
    :type quote_id: str
    :type quote_id: str
    :param file_name: Name of the attachment
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def create_quote_history(request: web.Request, xero_tenant_id, quote_id, body) -> web.Response:
    """Creates a history record for a specific quote

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param quote_id: Unique identifier for an Quote
    :type quote_id: str
    :type quote_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_quotes(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Create one or more quotes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Quotes with an array of Quote object in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = Quotes.from_dict(body)
    return web.Response(status=200)


async def create_receipt(request: web.Request, xero_tenant_id, body, unitdp=None) -> web.Response:
    """Creates draft expense claim receipts for any user

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Receipts with an array of Receipt object in body of request
    :type body: dict | bytes
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = Receipts.from_dict(body)
    return web.Response(status=200)


async def create_receipt_attachment_by_file_name(request: web.Request, xero_tenant_id, receipt_id, file_name, body) -> web.Response:
    """Creates an attachment on a specific expense claim receipts by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param receipt_id: Unique identifier for a Receipt
    :type receipt_id: str
    :type receipt_id: str
    :param file_name: The name of the file being attached to the Receipt
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def create_receipt_history(request: web.Request, xero_tenant_id, receipt_id, body) -> web.Response:
    """Creates a history record for a specific receipt

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param receipt_id: Unique identifier for a Receipt
    :type receipt_id: str
    :type receipt_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_repeating_invoice_attachment_by_file_name(request: web.Request, xero_tenant_id, repeating_invoice_id, file_name, body) -> web.Response:
    """Creates an attachment from a specific repeating invoices by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param repeating_invoice_id: Unique identifier for a Repeating Invoice
    :type repeating_invoice_id: str
    :type repeating_invoice_id: str
    :param file_name: The name of the file being attached to a Repeating Invoice
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def create_repeating_invoice_history(request: web.Request, xero_tenant_id, repeating_invoice_id, body) -> web.Response:
    """Creates a  history record for a specific repeating invoice

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param repeating_invoice_id: Unique identifier for a Repeating Invoice
    :type repeating_invoice_id: str
    :type repeating_invoice_id: str
    :param body: HistoryRecords containing an array of HistoryRecord objects in body of request
    :type body: dict | bytes

    """
    body = HistoryRecords.from_dict(body)
    return web.Response(status=200)


async def create_tax_rates(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates one or more tax rates

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: TaxRates array with TaxRate object in body of request
    :type body: dict | bytes

    """
    body = TaxRates.from_dict(body)
    return web.Response(status=200)


async def create_tracking_category(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Create tracking categories

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: TrackingCategory object in body of request
    :type body: dict | bytes

    """
    body = TrackingCategory.from_dict(body)
    return web.Response(status=200)


async def create_tracking_options(request: web.Request, xero_tenant_id, tracking_category_id, body) -> web.Response:
    """Creates options for a specific tracking category

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param tracking_category_id: Unique identifier for a TrackingCategory
    :type tracking_category_id: str
    :type tracking_category_id: str
    :param body: TrackingOption object in body of request
    :type body: dict | bytes

    """
    body = TrackingOption.from_dict(body)
    return web.Response(status=200)


async def delete_account(request: web.Request, xero_tenant_id, account_id) -> web.Response:
    """Deletes a chart of accounts

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param account_id: Unique identifier for retrieving single object
    :type account_id: str
    :type account_id: str

    """
    return web.Response(status=200)


async def delete_contact_group_contact(request: web.Request, xero_tenant_id, contact_group_id, contact_id) -> web.Response:
    """Deletes a specific contact from a contact group using a unique contact Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_group_id: Unique identifier for a Contact Group
    :type contact_group_id: str
    :type contact_group_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str

    """
    return web.Response(status=200)


async def delete_contact_group_contacts(request: web.Request, xero_tenant_id, contact_group_id) -> web.Response:
    """Deletes all contacts from a specific contact group

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_group_id: Unique identifier for a Contact Group
    :type contact_group_id: str
    :type contact_group_id: str

    """
    return web.Response(status=200)


async def delete_item(request: web.Request, xero_tenant_id, item_id) -> web.Response:
    """Deletes a specific item

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param item_id: Unique identifier for an Item
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def delete_linked_transaction(request: web.Request, xero_tenant_id, linked_transaction_id) -> web.Response:
    """Deletes a specific linked transactions (billable expenses)

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param linked_transaction_id: Unique identifier for a LinkedTransaction
    :type linked_transaction_id: str
    :type linked_transaction_id: str

    """
    return web.Response(status=200)


async def delete_payment(request: web.Request, xero_tenant_id, payment_id, body) -> web.Response:
    """Updates a specific payment for invoices and credit notes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param payment_id: Unique identifier for a Payment
    :type payment_id: str
    :type payment_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentDelete.from_dict(body)
    return web.Response(status=200)


async def delete_tracking_category(request: web.Request, xero_tenant_id, tracking_category_id) -> web.Response:
    """Deletes a specific tracking category

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param tracking_category_id: Unique identifier for a TrackingCategory
    :type tracking_category_id: str
    :type tracking_category_id: str

    """
    return web.Response(status=200)


async def delete_tracking_options(request: web.Request, xero_tenant_id, tracking_category_id, tracking_option_id) -> web.Response:
    """Deletes a specific option for a specific tracking category

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param tracking_category_id: Unique identifier for a TrackingCategory
    :type tracking_category_id: str
    :type tracking_category_id: str
    :param tracking_option_id: Unique identifier for a Tracking Option
    :type tracking_option_id: str
    :type tracking_option_id: str

    """
    return web.Response(status=200)


async def email_invoice(request: web.Request, xero_tenant_id, invoice_id, body) -> web.Response:
    """Sends a copy of a specific invoice to related contact via email

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestEmpty.from_dict(body)
    return web.Response(status=200)


async def get_account(request: web.Request, xero_tenant_id, account_id) -> web.Response:
    """Retrieves a single chart of accounts by using a unique account Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param account_id: Unique identifier for retrieving single object
    :type account_id: str
    :type account_id: str

    """
    return web.Response(status=200)


async def get_account_attachment_by_file_name(request: web.Request, xero_tenant_id, account_id, file_name, content_type) -> web.Response:
    """Retrieves an attachment for a specific account by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param account_id: Unique identifier for Account object
    :type account_id: str
    :type account_id: str
    :param file_name: Name of the attachment
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_account_attachment_by_id(request: web.Request, xero_tenant_id, account_id, attachment_id, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific account using a unique attachment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param account_id: Unique identifier for Account object
    :type account_id: str
    :type account_id: str
    :param attachment_id: Unique identifier for Attachment object
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_account_attachments(request: web.Request, xero_tenant_id, account_id) -> web.Response:
    """Retrieves attachments for a specific accounts by using a unique account Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param account_id: Unique identifier for Account object
    :type account_id: str
    :type account_id: str

    """
    return web.Response(status=200)


async def get_accounts(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None) -> web.Response:
    """Retrieves the full chart of accounts

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_bank_transaction(request: web.Request, xero_tenant_id, bank_transaction_id, unitdp=None) -> web.Response:
    """Retrieves a single spent or received money transaction by using a unique bank transaction Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transaction_id: Xero generated unique identifier for a bank transaction
    :type bank_transaction_id: str
    :type bank_transaction_id: str
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    return web.Response(status=200)


async def get_bank_transaction_attachment_by_file_name(request: web.Request, xero_tenant_id, bank_transaction_id, file_name, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific bank transaction by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transaction_id: Xero generated unique identifier for a bank transaction
    :type bank_transaction_id: str
    :type bank_transaction_id: str
    :param file_name: The name of the file being attached
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_bank_transaction_attachment_by_id(request: web.Request, xero_tenant_id, bank_transaction_id, attachment_id, content_type) -> web.Response:
    """Retrieves specific attachments from a specific BankTransaction using a unique attachment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transaction_id: Xero generated unique identifier for a bank transaction
    :type bank_transaction_id: str
    :type bank_transaction_id: str
    :param attachment_id: Xero generated unique identifier for an attachment
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_bank_transaction_attachments(request: web.Request, xero_tenant_id, bank_transaction_id) -> web.Response:
    """Retrieves any attachments from a specific bank transactions

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transaction_id: Xero generated unique identifier for a bank transaction
    :type bank_transaction_id: str
    :type bank_transaction_id: str

    """
    return web.Response(status=200)


async def get_bank_transactions(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None, unitdp=None) -> web.Response:
    """Retrieves any spent or received money transactions

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: Up to 100 bank transactions will be returned in a single API call with line items details
    :type page: int
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_bank_transactions_history(request: web.Request, xero_tenant_id, bank_transaction_id) -> web.Response:
    """Retrieves history from a specific bank transaction using a unique bank transaction Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transaction_id: Xero generated unique identifier for a bank transaction
    :type bank_transaction_id: str
    :type bank_transaction_id: str

    """
    return web.Response(status=200)


async def get_bank_transfer(request: web.Request, xero_tenant_id, bank_transfer_id) -> web.Response:
    """Retrieves specific bank transfers by using a unique bank transfer Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transfer_id: Xero generated unique identifier for a bank transfer
    :type bank_transfer_id: str
    :type bank_transfer_id: str

    """
    return web.Response(status=200)


async def get_bank_transfer_attachment_by_file_name(request: web.Request, xero_tenant_id, bank_transfer_id, file_name, content_type) -> web.Response:
    """Retrieves a specific attachment on a specific bank transfer by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transfer_id: Xero generated unique identifier for a bank transfer
    :type bank_transfer_id: str
    :type bank_transfer_id: str
    :param file_name: The name of the file being attached to a Bank Transfer
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_bank_transfer_attachment_by_id(request: web.Request, xero_tenant_id, bank_transfer_id, attachment_id, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific bank transfer using a unique attachment ID

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transfer_id: Xero generated unique identifier for a bank transfer
    :type bank_transfer_id: str
    :type bank_transfer_id: str
    :param attachment_id: Xero generated unique identifier for an Attachment to a bank transfer
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_bank_transfer_attachments(request: web.Request, xero_tenant_id, bank_transfer_id) -> web.Response:
    """Retrieves attachments from a specific bank transfer

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transfer_id: Xero generated unique identifier for a bank transfer
    :type bank_transfer_id: str
    :type bank_transfer_id: str

    """
    return web.Response(status=200)


async def get_bank_transfer_history(request: web.Request, xero_tenant_id, bank_transfer_id) -> web.Response:
    """Retrieves history from a specific bank transfer using a unique bank transfer Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transfer_id: Xero generated unique identifier for a bank transfer
    :type bank_transfer_id: str
    :type bank_transfer_id: str

    """
    return web.Response(status=200)


async def get_bank_transfers(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None) -> web.Response:
    """Retrieves all bank transfers

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_batch_payment_history(request: web.Request, xero_tenant_id, batch_payment_id) -> web.Response:
    """Retrieves history from a specific batch payment

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param batch_payment_id: Unique identifier for BatchPayment
    :type batch_payment_id: str
    :type batch_payment_id: str

    """
    return web.Response(status=200)


async def get_batch_payments(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None) -> web.Response:
    """Retrieves either one or many batch payments for invoices

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_branding_theme(request: web.Request, xero_tenant_id, branding_theme_id) -> web.Response:
    """Retrieves a specific branding theme using a unique branding theme Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param branding_theme_id: Unique identifier for a Branding Theme
    :type branding_theme_id: str
    :type branding_theme_id: str

    """
    return web.Response(status=200)


async def get_branding_theme_payment_services(request: web.Request, xero_tenant_id, branding_theme_id) -> web.Response:
    """Retrieves the payment services for a specific branding theme

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param branding_theme_id: Unique identifier for a Branding Theme
    :type branding_theme_id: str
    :type branding_theme_id: str

    """
    return web.Response(status=200)


async def get_branding_themes(request: web.Request, xero_tenant_id) -> web.Response:
    """Retrieves all the branding themes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str

    """
    return web.Response(status=200)


async def get_contact(request: web.Request, xero_tenant_id, contact_id) -> web.Response:
    """Retrieves a specific contacts in a Xero organisation using a unique contact Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str

    """
    return web.Response(status=200)


async def get_contact_attachment_by_file_name(request: web.Request, xero_tenant_id, contact_id, file_name, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific contact by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str
    :param file_name: Name for the file you are attaching
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_contact_attachment_by_id(request: web.Request, xero_tenant_id, contact_id, attachment_id, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific contact using a unique attachment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str
    :param attachment_id: Unique identifier for a Attachment
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_contact_attachments(request: web.Request, xero_tenant_id, contact_id) -> web.Response:
    """Retrieves attachments for a specific contact in a Xero organisation

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str

    """
    return web.Response(status=200)


async def get_contact_by_contact_number(request: web.Request, xero_tenant_id, contact_number) -> web.Response:
    """Retrieves a specific contact by contact number in a Xero organisation

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_number: This field is read only on the Xero contact screen, used to identify contacts in external systems (max length &#x3D; 50).
    :type contact_number: str

    """
    return web.Response(status=200)


async def get_contact_cis_settings(request: web.Request, xero_tenant_id, contact_id) -> web.Response:
    """Retrieves CIS settings for a specific contact in a Xero organisation

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str

    """
    return web.Response(status=200)


async def get_contact_group(request: web.Request, xero_tenant_id, contact_group_id) -> web.Response:
    """Retrieves a specific contact group by using a unique contact group Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_group_id: Unique identifier for a Contact Group
    :type contact_group_id: str
    :type contact_group_id: str

    """
    return web.Response(status=200)


async def get_contact_groups(request: web.Request, xero_tenant_id, where=None, order=None) -> web.Response:
    """Retrieves the contact Id and name of all the contacts in a contact group

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str

    """
    return web.Response(status=200)


async def get_contact_history(request: web.Request, xero_tenant_id, contact_id) -> web.Response:
    """Retrieves history records for a specific contact

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str

    """
    return web.Response(status=200)


async def get_contacts(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, ids=None, page=None, include_archived=None) -> web.Response:
    """Retrieves all contacts in a Xero organisation

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param ids: Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call.
    :type ids: List[str]
    :param page: e.g. page&#x3D;1 - Up to 100 contacts will be returned in a single API call.
    :type page: int
    :param include_archived: e.g. includeArchived&#x3D;true - Contacts with a status of ARCHIVED will be included in the response
    :type include_archived: bool

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_credit_note(request: web.Request, xero_tenant_id, credit_note_id, unitdp=None) -> web.Response:
    """Retrieves a specific credit note using a unique credit note Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    return web.Response(status=200)


async def get_credit_note_as_pdf(request: web.Request, xero_tenant_id, credit_note_id) -> web.Response:
    """Retrieves credit notes as PDF files

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str

    """
    return web.Response(status=200)


async def get_credit_note_attachment_by_file_name(request: web.Request, xero_tenant_id, credit_note_id, file_name, content_type) -> web.Response:
    """Retrieves a specific attachment on a specific credit note by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str
    :param file_name: Name of the file you are attaching to Credit Note
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_credit_note_attachment_by_id(request: web.Request, xero_tenant_id, credit_note_id, attachment_id, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific credit note using a unique attachment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str
    :param attachment_id: Unique identifier for a Attachment
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_credit_note_attachments(request: web.Request, xero_tenant_id, credit_note_id) -> web.Response:
    """Retrieves attachments for a specific credit notes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str

    """
    return web.Response(status=200)


async def get_credit_note_history(request: web.Request, xero_tenant_id, credit_note_id) -> web.Response:
    """Retrieves history records of a specific credit note

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str

    """
    return web.Response(status=200)


async def get_credit_notes(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None, unitdp=None) -> web.Response:
    """Retrieves any credit notes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note
    :type page: int
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_currencies(request: web.Request, xero_tenant_id, where=None, order=None) -> web.Response:
    """Retrieves currencies for your Xero organisation

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str

    """
    return web.Response(status=200)


async def get_employee(request: web.Request, xero_tenant_id, employee_id) -> web.Response:
    """Retrieves a specific employee used in Xero payrun using a unique employee Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param employee_id: Unique identifier for a Employee
    :type employee_id: str
    :type employee_id: str

    """
    return web.Response(status=200)


async def get_employees(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None) -> web.Response:
    """Retrieves employees used in Xero payrun

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_expense_claim(request: web.Request, xero_tenant_id, expense_claim_id) -> web.Response:
    """Retrieves a specific expense claim using a unique expense claim Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param expense_claim_id: Unique identifier for a ExpenseClaim
    :type expense_claim_id: str
    :type expense_claim_id: str

    """
    return web.Response(status=200)


async def get_expense_claim_history(request: web.Request, xero_tenant_id, expense_claim_id) -> web.Response:
    """Retrieves history records of a specific expense claim

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param expense_claim_id: Unique identifier for a ExpenseClaim
    :type expense_claim_id: str
    :type expense_claim_id: str

    """
    return web.Response(status=200)


async def get_expense_claims(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None) -> web.Response:
    """Retrieves expense claims

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_invoice(request: web.Request, xero_tenant_id, invoice_id, unitdp=None) -> web.Response:
    """Retrieves a specific sales invoice or purchase bill using a unique invoice Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    return web.Response(status=200)


async def get_invoice_as_pdf(request: web.Request, xero_tenant_id, invoice_id) -> web.Response:
    """Retrieves invoices or purchase bills as PDF files

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str

    """
    return web.Response(status=200)


async def get_invoice_attachment_by_file_name(request: web.Request, xero_tenant_id, invoice_id, file_name, content_type) -> web.Response:
    """Retrieves an attachment from a specific invoice or purchase bill by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str
    :param file_name: Name of the file you are attaching
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_invoice_attachment_by_id(request: web.Request, xero_tenant_id, invoice_id, attachment_id, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific invoices or purchase bills by using a unique attachment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str
    :param attachment_id: Unique identifier for an Attachment
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_invoice_attachments(request: web.Request, xero_tenant_id, invoice_id) -> web.Response:
    """Retrieves attachments for a specific invoice or purchase bill

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str

    """
    return web.Response(status=200)


async def get_invoice_history(request: web.Request, xero_tenant_id, invoice_id) -> web.Response:
    """Retrieves history records for a specific invoice

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str

    """
    return web.Response(status=200)


async def get_invoice_reminders(request: web.Request, xero_tenant_id) -> web.Response:
    """Retrieves invoice reminder settings

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str

    """
    return web.Response(status=200)


async def get_invoices(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, ids=None, invoice_numbers=None, contact_ids=None, statuses=None, page=None, include_archived=None, created_by_my_app=None, unitdp=None) -> web.Response:
    """Retrieves sales invoices or purchase bills

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param ids: Filter by a comma-separated list of InvoicesIDs.
    :type ids: List[str]
    :param invoice_numbers: Filter by a comma-separated list of InvoiceNumbers.
    :type invoice_numbers: List[str]
    :param contact_ids: Filter by a comma-separated list of ContactIDs.
    :type contact_ids: List[str]
    :param statuses: Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter.
    :type statuses: List[str]
    :param page: e.g. page&#x3D;1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice
    :type page: int
    :param include_archived: e.g. includeArchived&#x3D;true - Contacts with a status of ARCHIVED will be included in the response
    :type include_archived: bool
    :param created_by_my_app: When set to true you&#39;ll only retrieve Invoices created by your app
    :type created_by_my_app: bool
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_item(request: web.Request, xero_tenant_id, item_id, unitdp=None) -> web.Response:
    """Retrieves a specific item using a unique item Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param item_id: Unique identifier for an Item
    :type item_id: str
    :type item_id: str
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    return web.Response(status=200)


async def get_item_history(request: web.Request, xero_tenant_id, item_id) -> web.Response:
    """Retrieves history for a specific item

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param item_id: Unique identifier for an Item
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def get_items(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, unitdp=None) -> web.Response:
    """Retrieves items

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_journal(request: web.Request, xero_tenant_id, journal_id) -> web.Response:
    """Retrieves a specific journal using a unique journal Id.

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param journal_id: Unique identifier for a Journal
    :type journal_id: str
    :type journal_id: str

    """
    return web.Response(status=200)


async def get_journals(request: web.Request, xero_tenant_id, if_modified_since=None, offset=None, payments_only=None) -> web.Response:
    """Retrieves journals

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param offset: Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned
    :type offset: int
    :param payments_only: Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default.
    :type payments_only: bool

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_linked_transaction(request: web.Request, xero_tenant_id, linked_transaction_id) -> web.Response:
    """Retrieves a specific linked transaction (billable expenses) using a unique linked transaction Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param linked_transaction_id: Unique identifier for a LinkedTransaction
    :type linked_transaction_id: str
    :type linked_transaction_id: str

    """
    return web.Response(status=200)


async def get_linked_transactions(request: web.Request, xero_tenant_id, page=None, linked_transaction_id=None, source_transaction_id=None, contact_id=None, status=None, target_transaction_id=None) -> web.Response:
    """Retrieves linked transactions (billable expenses)

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param page: Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page&#x3D;1.
    :type page: int
    :param linked_transaction_id: The Xero identifier for an Linked Transaction
    :type linked_transaction_id: str
    :type linked_transaction_id: str
    :param source_transaction_id: Filter by the SourceTransactionID. Get the linked transactions created from a particular ACCPAY invoice
    :type source_transaction_id: str
    :type source_transaction_id: str
    :param contact_id: Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer.
    :type contact_id: str
    :type contact_id: str
    :param status: Filter by the combination of ContactID and Status. Get  the linked transactions associated to a  customer and with a status
    :type status: str
    :param target_transaction_id: Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice
    :type target_transaction_id: str
    :type target_transaction_id: str

    """
    return web.Response(status=200)


async def get_manual_journal(request: web.Request, xero_tenant_id, manual_journal_id) -> web.Response:
    """Retrieves a specific manual journal

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param manual_journal_id: Unique identifier for a ManualJournal
    :type manual_journal_id: str
    :type manual_journal_id: str

    """
    return web.Response(status=200)


async def get_manual_journal_attachment_by_file_name(request: web.Request, xero_tenant_id, manual_journal_id, file_name, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific manual journal by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param manual_journal_id: Unique identifier for a ManualJournal
    :type manual_journal_id: str
    :type manual_journal_id: str
    :param file_name: The name of the file being attached to a ManualJournal
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_manual_journal_attachment_by_id(request: web.Request, xero_tenant_id, manual_journal_id, attachment_id, content_type) -> web.Response:
    """Allows you to retrieve a specific attachment from a specific manual journal using a unique attachment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param manual_journal_id: Unique identifier for a ManualJournal
    :type manual_journal_id: str
    :type manual_journal_id: str
    :param attachment_id: Unique identifier for a Attachment
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_manual_journal_attachments(request: web.Request, xero_tenant_id, manual_journal_id) -> web.Response:
    """Retrieves attachment for a specific manual journal

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param manual_journal_id: Unique identifier for a ManualJournal
    :type manual_journal_id: str
    :type manual_journal_id: str

    """
    return web.Response(status=200)


async def get_manual_journals(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None) -> web.Response:
    """Retrieves manual journals

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment
    :type page: int

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_manual_journals_history(request: web.Request, xero_tenant_id, manual_journal_id) -> web.Response:
    """Retrieves history for a specific manual journal

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param manual_journal_id: Xero generated unique identifier for a manual journal
    :type manual_journal_id: str
    :type manual_journal_id: str

    """
    return web.Response(status=200)


async def get_online_invoice(request: web.Request, xero_tenant_id, invoice_id) -> web.Response:
    """Retrieves a URL to an online invoice

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str

    """
    return web.Response(status=200)


async def get_organisation_actions(request: web.Request, xero_tenant_id) -> web.Response:
    """Retrieves a list of the key actions your app has permission to perform in the connected Xero organisation.

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str

    """
    return web.Response(status=200)


async def get_organisation_cis_settings(request: web.Request, xero_tenant_id, organisation_id) -> web.Response:
    """Retrieves the CIS settings for the Xero organistaion.

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param organisation_id: The unique Xero identifier for an organisation
    :type organisation_id: str
    :type organisation_id: str

    """
    return web.Response(status=200)


async def get_organisations(request: web.Request, xero_tenant_id) -> web.Response:
    """Retrieves Xero organisation details

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str

    """
    return web.Response(status=200)


async def get_overpayment(request: web.Request, xero_tenant_id, overpayment_id) -> web.Response:
    """Retrieves a specific overpayment using a unique overpayment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param overpayment_id: Unique identifier for a Overpayment
    :type overpayment_id: str
    :type overpayment_id: str

    """
    return web.Response(status=200)


async def get_overpayment_history(request: web.Request, xero_tenant_id, overpayment_id) -> web.Response:
    """Retrieves history records of a specific overpayment

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param overpayment_id: Unique identifier for a Overpayment
    :type overpayment_id: str
    :type overpayment_id: str

    """
    return web.Response(status=200)


async def get_overpayments(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None, unitdp=None) -> web.Response:
    """Retrieves overpayments

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment
    :type page: int
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_payment(request: web.Request, xero_tenant_id, payment_id) -> web.Response:
    """Retrieves a specific payment for invoices and credit notes using a unique payment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param payment_id: Unique identifier for a Payment
    :type payment_id: str
    :type payment_id: str

    """
    return web.Response(status=200)


async def get_payment_history(request: web.Request, xero_tenant_id, payment_id) -> web.Response:
    """Retrieves history records of a specific payment

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param payment_id: Unique identifier for a Payment
    :type payment_id: str
    :type payment_id: str

    """
    return web.Response(status=200)


async def get_payment_services(request: web.Request, xero_tenant_id) -> web.Response:
    """Retrieves payment services

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str

    """
    return web.Response(status=200)


async def get_payments(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None) -> web.Response:
    """Retrieves payments for invoices and credit notes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: Up to 100 payments will be returned in a single API call
    :type page: int

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_prepayment(request: web.Request, xero_tenant_id, prepayment_id) -> web.Response:
    """Allows you to retrieve a specified prepayments

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param prepayment_id: Unique identifier for a PrePayment
    :type prepayment_id: str
    :type prepayment_id: str

    """
    return web.Response(status=200)


async def get_prepayment_history(request: web.Request, xero_tenant_id, prepayment_id) -> web.Response:
    """Retrieves history record for a specific prepayment

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param prepayment_id: Unique identifier for a PrePayment
    :type prepayment_id: str
    :type prepayment_id: str

    """
    return web.Response(status=200)


async def get_prepayments(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None, unitdp=None) -> web.Response:
    """Retrieves prepayments

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 prepayments will be returned in a single API call with line items shown for each overpayment
    :type page: int
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_purchase_order(request: web.Request, xero_tenant_id, purchase_order_id) -> web.Response:
    """Retrieves a specific purchase order using a unique purchase order Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_id: Unique identifier for a PurchaseOrder
    :type purchase_order_id: str
    :type purchase_order_id: str

    """
    return web.Response(status=200)


async def get_purchase_order_as_pdf(request: web.Request, xero_tenant_id, purchase_order_id) -> web.Response:
    """Retrieves specific purchase order as PDF files using a unique purchase order Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_id: Unique identifier for an Purchase Order
    :type purchase_order_id: str
    :type purchase_order_id: str

    """
    return web.Response(status=200)


async def get_purchase_order_attachment_by_file_name(request: web.Request, xero_tenant_id, purchase_order_id, file_name, content_type) -> web.Response:
    """Retrieves a specific attachment for a specific purchase order by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_id: Unique identifier for Purchase Order object
    :type purchase_order_id: str
    :type purchase_order_id: str
    :param file_name: Name of the attachment
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_purchase_order_attachment_by_id(request: web.Request, xero_tenant_id, purchase_order_id, attachment_id, content_type) -> web.Response:
    """Retrieves specific attachment for a specific purchase order using a unique attachment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_id: Unique identifier for Purchase Order object
    :type purchase_order_id: str
    :type purchase_order_id: str
    :param attachment_id: Unique identifier for Attachment object
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_purchase_order_attachments(request: web.Request, xero_tenant_id, purchase_order_id) -> web.Response:
    """Retrieves attachments for a specific purchase order

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_id: Unique identifier for Purchase Orders object
    :type purchase_order_id: str
    :type purchase_order_id: str

    """
    return web.Response(status=200)


async def get_purchase_order_by_number(request: web.Request, xero_tenant_id, purchase_order_number) -> web.Response:
    """Retrieves a specific purchase order using purchase order number

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_number: Unique identifier for a PurchaseOrder
    :type purchase_order_number: str

    """
    return web.Response(status=200)


async def get_purchase_order_history(request: web.Request, xero_tenant_id, purchase_order_id) -> web.Response:
    """Retrieves history for a specific purchase order

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_id: Unique identifier for a PurchaseOrder
    :type purchase_order_id: str
    :type purchase_order_id: str

    """
    return web.Response(status=200)


async def get_purchase_orders(request: web.Request, xero_tenant_id, if_modified_since=None, status=None, date_from=None, date_to=None, order=None, page=None) -> web.Response:
    """Retrieves purchase orders

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param status: Filter by purchase order status
    :type status: str
    :param date_from: Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom&#x3D;2015-12-01&amp;DateTo&#x3D;2015-12-31
    :type date_from: str
    :param date_to: Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom&#x3D;2015-12-01&amp;DateTo&#x3D;2015-12-31
    :type date_to: str
    :param order: Order by an any element
    :type order: str
    :param page: To specify a page, append the page parameter to the URL e.g. ?page&#x3D;1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page&#x3D;2 and continuing this process until no more results are returned.
    :type page: int

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_quote(request: web.Request, xero_tenant_id, quote_id) -> web.Response:
    """Retrieves a specific quote using a unique quote Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param quote_id: Unique identifier for an Quote
    :type quote_id: str
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_quote_as_pdf(request: web.Request, xero_tenant_id, quote_id) -> web.Response:
    """Retrieves a specific quote as a PDF file using a unique quote Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param quote_id: Unique identifier for an Quote
    :type quote_id: str
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_quote_attachment_by_file_name(request: web.Request, xero_tenant_id, quote_id, file_name, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific quote by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param quote_id: Unique identifier for Quote object
    :type quote_id: str
    :type quote_id: str
    :param file_name: Name of the attachment
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_quote_attachment_by_id(request: web.Request, xero_tenant_id, quote_id, attachment_id, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific quote using a unique attachment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param quote_id: Unique identifier for Quote object
    :type quote_id: str
    :type quote_id: str
    :param attachment_id: Unique identifier for Attachment object
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_quote_attachments(request: web.Request, xero_tenant_id, quote_id) -> web.Response:
    """Retrieves attachments for a specific quote

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param quote_id: Unique identifier for Quote object
    :type quote_id: str
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_quote_history(request: web.Request, xero_tenant_id, quote_id) -> web.Response:
    """Retrieves history records of a specific quote

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param quote_id: Unique identifier for an Quote
    :type quote_id: str
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_quotes(request: web.Request, xero_tenant_id, if_modified_since=None, date_from=None, date_to=None, expiry_date_from=None, expiry_date_to=None, contact_id=None, status=None, page=None, order=None, quote_number=None) -> web.Response:
    """Retrieves sales quotes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param date_from: Filter for quotes after a particular date
    :type date_from: str
    :param date_to: Filter for quotes before a particular date
    :type date_to: str
    :param expiry_date_from: Filter for quotes expiring after a particular date
    :type expiry_date_from: str
    :param expiry_date_to: Filter for quotes before a particular date
    :type expiry_date_to: str
    :param contact_id: Filter for quotes belonging to a particular contact
    :type contact_id: str
    :type contact_id: str
    :param status: Filter for quotes of a particular Status
    :type status: str
    :param page: e.g. page&#x3D;1 – Up to 100 Quotes will be returned in a single API call with line items shown for each quote
    :type page: int
    :param order: Order by an any element
    :type order: str
    :param quote_number: Filter by quote number (e.g. GET https://.../Quotes?QuoteNumber&#x3D;QU-0001)
    :type quote_number: str

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    expiry_date_from = util.deserialize_date(expiry_date_from)
    expiry_date_to = util.deserialize_date(expiry_date_to)
    return web.Response(status=200)


async def get_receipt(request: web.Request, xero_tenant_id, receipt_id, unitdp=None) -> web.Response:
    """Retrieves a specific draft expense claim receipt by using a unique receipt Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param receipt_id: Unique identifier for a Receipt
    :type receipt_id: str
    :type receipt_id: str
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    return web.Response(status=200)


async def get_receipt_attachment_by_file_name(request: web.Request, xero_tenant_id, receipt_id, file_name, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific expense claim receipts by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param receipt_id: Unique identifier for a Receipt
    :type receipt_id: str
    :type receipt_id: str
    :param file_name: The name of the file being attached to the Receipt
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_receipt_attachment_by_id(request: web.Request, xero_tenant_id, receipt_id, attachment_id, content_type) -> web.Response:
    """Retrieves a specific attachments from a specific expense claim receipts by using a unique attachment Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param receipt_id: Unique identifier for a Receipt
    :type receipt_id: str
    :type receipt_id: str
    :param attachment_id: Unique identifier for a Attachment
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_receipt_attachments(request: web.Request, xero_tenant_id, receipt_id) -> web.Response:
    """Retrieves attachments for a specific expense claim receipt

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param receipt_id: Unique identifier for a Receipt
    :type receipt_id: str
    :type receipt_id: str

    """
    return web.Response(status=200)


async def get_receipt_history(request: web.Request, xero_tenant_id, receipt_id) -> web.Response:
    """Retrieves a history record for a specific receipt

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param receipt_id: Unique identifier for a Receipt
    :type receipt_id: str
    :type receipt_id: str

    """
    return web.Response(status=200)


async def get_receipts(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, unitdp=None) -> web.Response:
    """Retrieves draft expense claim receipts for any user

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def get_repeating_invoice(request: web.Request, xero_tenant_id, repeating_invoice_id) -> web.Response:
    """Retrieves a specific repeating invoice by using a unique repeating invoice Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param repeating_invoice_id: Unique identifier for a Repeating Invoice
    :type repeating_invoice_id: str
    :type repeating_invoice_id: str

    """
    return web.Response(status=200)


async def get_repeating_invoice_attachment_by_file_name(request: web.Request, xero_tenant_id, repeating_invoice_id, file_name, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific repeating invoices by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param repeating_invoice_id: Unique identifier for a Repeating Invoice
    :type repeating_invoice_id: str
    :type repeating_invoice_id: str
    :param file_name: The name of the file being attached to a Repeating Invoice
    :type file_name: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_repeating_invoice_attachment_by_id(request: web.Request, xero_tenant_id, repeating_invoice_id, attachment_id, content_type) -> web.Response:
    """Retrieves a specific attachment from a specific repeating invoice

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param repeating_invoice_id: Unique identifier for a Repeating Invoice
    :type repeating_invoice_id: str
    :type repeating_invoice_id: str
    :param attachment_id: Unique identifier for a Attachment
    :type attachment_id: str
    :type attachment_id: str
    :param content_type: The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf
    :type content_type: str

    """
    return web.Response(status=200)


async def get_repeating_invoice_attachments(request: web.Request, xero_tenant_id, repeating_invoice_id) -> web.Response:
    """Retrieves attachments from a specific repeating invoice

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param repeating_invoice_id: Unique identifier for a Repeating Invoice
    :type repeating_invoice_id: str
    :type repeating_invoice_id: str

    """
    return web.Response(status=200)


async def get_repeating_invoice_history(request: web.Request, xero_tenant_id, repeating_invoice_id) -> web.Response:
    """Retrieves history record for a specific repeating invoice

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param repeating_invoice_id: Unique identifier for a Repeating Invoice
    :type repeating_invoice_id: str
    :type repeating_invoice_id: str

    """
    return web.Response(status=200)


async def get_repeating_invoices(request: web.Request, xero_tenant_id, where=None, order=None) -> web.Response:
    """Retrieves repeating invoices

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str

    """
    return web.Response(status=200)


async def get_report_aged_payables_by_contact(request: web.Request, xero_tenant_id, contact_id, _date=None, from_date=None, to_date=None) -> web.Response:
    """Retrieves report for aged payables by contact

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str
    :param _date: The date of the Aged Payables By Contact report
    :type _date: str
    :param from_date: The from date of the Aged Payables By Contact report
    :type from_date: str
    :param to_date: The to date of the Aged Payables By Contact report
    :type to_date: str

    """
    _date = util.deserialize_date(_date)
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def get_report_aged_receivables_by_contact(request: web.Request, xero_tenant_id, contact_id, _date=None, from_date=None, to_date=None) -> web.Response:
    """Retrieves report for aged receivables by contact

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str
    :param _date: The date of the Aged Receivables By Contact report
    :type _date: str
    :param from_date: The from date of the Aged Receivables By Contact report
    :type from_date: str
    :param to_date: The to date of the Aged Receivables By Contact report
    :type to_date: str

    """
    _date = util.deserialize_date(_date)
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def get_report_ba_sor_gst(request: web.Request, xero_tenant_id, report_id) -> web.Response:
    """Retrieves a specific report for BAS using a unique report Id (only valid for AU orgs)

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param report_id: Unique identifier for a Report
    :type report_id: str

    """
    return web.Response(status=200)


async def get_report_ba_sor_gst_list(request: web.Request, xero_tenant_id) -> web.Response:
    """Retrieves report for BAS (only valid for AU orgs)

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str

    """
    return web.Response(status=200)


async def get_report_balance_sheet(request: web.Request, xero_tenant_id, _date=None, periods=None, timeframe=None, tracking_option_id1=None, tracking_option_id2=None, standard_layout=None, payments_only=None) -> web.Response:
    """Retrieves report for balancesheet

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param _date: The date of the Balance Sheet report
    :type _date: str
    :param periods: The number of periods for the Balance Sheet report
    :type periods: int
    :param timeframe: The period size to compare to (MONTH, QUARTER, YEAR)
    :type timeframe: str
    :param tracking_option_id1: The tracking option 1 for the Balance Sheet report
    :type tracking_option_id1: str
    :param tracking_option_id2: The tracking option 2 for the Balance Sheet report
    :type tracking_option_id2: str
    :param standard_layout: The standard layout boolean for the Balance Sheet report
    :type standard_layout: bool
    :param payments_only: return a cash basis for the Balance Sheet report
    :type payments_only: bool

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def get_report_bank_summary(request: web.Request, xero_tenant_id, from_date=None, to_date=None) -> web.Response:
    """Retrieves report for bank summary

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param from_date: The from date for the Bank Summary report e.g. 2018-03-31
    :type from_date: str
    :param to_date: The to date for the Bank Summary report e.g. 2018-03-31
    :type to_date: str

    """
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def get_report_budget_summary(request: web.Request, xero_tenant_id, _date=None, period=None, timeframe=None) -> web.Response:
    """Retrieves report for budget summary

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param _date: The date for the Bank Summary report e.g. 2018-03-31
    :type _date: str
    :param period: The number of periods to compare (integer between 1 and 12)
    :type period: int
    :param timeframe: The period size to compare to (1&#x3D;month, 3&#x3D;quarter, 12&#x3D;year)
    :type timeframe: int

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def get_report_executive_summary(request: web.Request, xero_tenant_id, _date=None) -> web.Response:
    """Retrieves report for executive summary

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param _date: The date for the Bank Summary report e.g. 2018-03-31
    :type _date: str

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def get_report_profit_and_loss(request: web.Request, xero_tenant_id, from_date=None, to_date=None, periods=None, timeframe=None, tracking_category_id=None, tracking_category_id2=None, tracking_option_id=None, tracking_option_id2=None, standard_layout=None, payments_only=None) -> web.Response:
    """Retrieves report for profit and loss

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param from_date: The from date for the ProfitAndLoss report e.g. 2018-03-31
    :type from_date: str
    :param to_date: The to date for the ProfitAndLoss report e.g. 2018-03-31
    :type to_date: str
    :param periods: The number of periods to compare (integer between 1 and 12)
    :type periods: int
    :param timeframe: The period size to compare to (MONTH, QUARTER, YEAR)
    :type timeframe: str
    :param tracking_category_id: The trackingCategory 1 for the ProfitAndLoss report
    :type tracking_category_id: str
    :param tracking_category_id2: The trackingCategory 2 for the ProfitAndLoss report
    :type tracking_category_id2: str
    :param tracking_option_id: The tracking option 1 for the ProfitAndLoss report
    :type tracking_option_id: str
    :param tracking_option_id2: The tracking option 2 for the ProfitAndLoss report
    :type tracking_option_id2: str
    :param standard_layout: Return the standard layout for the ProfitAndLoss report
    :type standard_layout: bool
    :param payments_only: Return cash only basis for the ProfitAndLoss report
    :type payments_only: bool

    """
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def get_report_ten_ninety_nine(request: web.Request, xero_tenant_id, report_year=None) -> web.Response:
    """Retrieve reports for 1099

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param report_year: The year of the 1099 report
    :type report_year: str

    """
    return web.Response(status=200)


async def get_report_trial_balance(request: web.Request, xero_tenant_id, _date=None, payments_only=None) -> web.Response:
    """Retrieves report for trial balance

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param _date: The date for the Trial Balance report e.g. 2018-03-31
    :type _date: str
    :param payments_only: Return cash only basis for the Trial Balance report
    :type payments_only: bool

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def get_tax_rates(request: web.Request, xero_tenant_id, where=None, order=None, tax_type=None) -> web.Response:
    """Retrieves tax rates

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param tax_type: Filter by tax type
    :type tax_type: str

    """
    return web.Response(status=200)


async def get_tracking_categories(request: web.Request, xero_tenant_id, where=None, order=None, include_archived=None) -> web.Response:
    """Retrieves tracking categories and options

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param include_archived: e.g. includeArchived&#x3D;true - Categories and options with a status of ARCHIVED will be included in the response
    :type include_archived: bool

    """
    return web.Response(status=200)


async def get_tracking_category(request: web.Request, xero_tenant_id, tracking_category_id) -> web.Response:
    """Retrieves specific tracking categories and options using a unique tracking category Id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param tracking_category_id: Unique identifier for a TrackingCategory
    :type tracking_category_id: str
    :type tracking_category_id: str

    """
    return web.Response(status=200)


async def get_user(request: web.Request, xero_tenant_id, user_id) -> web.Response:
    """Retrieves a specific user

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param user_id: Unique identifier for a User
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_users(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None) -> web.Response:
    """Retrieves users

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str

    """
    if_modified_since = util.deserialize_datetime(if_modified_since)
    return web.Response(status=200)


async def post_setup(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Sets the chart of accounts, the conversion date and conversion balances

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Object including an accounts array, a conversion balances array and a conversion date object in body of request
    :type body: dict | bytes

    """
    body = Setup.from_dict(body)
    return web.Response(status=200)


async def update_account(request: web.Request, xero_tenant_id, account_id, body) -> web.Response:
    """Updates a chart of accounts

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param account_id: Unique identifier for retrieving single object
    :type account_id: str
    :type account_id: str
    :param body: Request of type Accounts array with one Account
    :type body: dict | bytes

    """
    body = Accounts.from_dict(body)
    return web.Response(status=200)


async def update_account_attachment_by_file_name(request: web.Request, xero_tenant_id, account_id, file_name, body) -> web.Response:
    """Updates attachment on a specific account by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param account_id: Unique identifier for Account object
    :type account_id: str
    :type account_id: str
    :param file_name: Name of the attachment
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_bank_transaction(request: web.Request, xero_tenant_id, bank_transaction_id, body, unitdp=None) -> web.Response:
    """Updates a single spent or received money transaction

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transaction_id: Xero generated unique identifier for a bank transaction
    :type bank_transaction_id: str
    :type bank_transaction_id: str
    :param body: 
    :type body: dict | bytes
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = BankTransactions.from_dict(body)
    return web.Response(status=200)


async def update_bank_transaction_attachment_by_file_name(request: web.Request, xero_tenant_id, bank_transaction_id, file_name, body) -> web.Response:
    """Updates a specific attachment from a specific bank transaction by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transaction_id: Xero generated unique identifier for a bank transaction
    :type bank_transaction_id: str
    :type bank_transaction_id: str
    :param file_name: The name of the file being attached
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_bank_transfer_attachment_by_file_name(request: web.Request, xero_tenant_id, bank_transfer_id, file_name, body) -> web.Response:
    """update_bank_transfer_attachment_by_file_name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param bank_transfer_id: Xero generated unique identifier for a bank transfer
    :type bank_transfer_id: str
    :type bank_transfer_id: str
    :param file_name: The name of the file being attached to a Bank Transfer
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_contact(request: web.Request, xero_tenant_id, contact_id, body) -> web.Response:
    """Updates a specific contact in a Xero organisation

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str
    :param body: an array of Contacts containing single Contact object with properties to update
    :type body: dict | bytes

    """
    body = Contacts.from_dict(body)
    return web.Response(status=200)


async def update_contact_attachment_by_file_name(request: web.Request, xero_tenant_id, contact_id, file_name, body) -> web.Response:
    """update_contact_attachment_by_file_name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_id: Unique identifier for a Contact
    :type contact_id: str
    :type contact_id: str
    :param file_name: Name for the file you are attaching
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_contact_group(request: web.Request, xero_tenant_id, contact_group_id, body) -> web.Response:
    """Updates a specific contact group

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param contact_group_id: Unique identifier for a Contact Group
    :type contact_group_id: str
    :type contact_group_id: str
    :param body: an array of Contact groups with Name of specific group to update
    :type body: dict | bytes

    """
    body = ContactGroups.from_dict(body)
    return web.Response(status=200)


async def update_credit_note(request: web.Request, xero_tenant_id, credit_note_id, body, unitdp=None) -> web.Response:
    """Updates a specific credit note

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str
    :param body: an array of Credit Notes containing credit note details to update
    :type body: dict | bytes
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = CreditNotes.from_dict(body)
    return web.Response(status=200)


async def update_credit_note_attachment_by_file_name(request: web.Request, xero_tenant_id, credit_note_id, file_name, body) -> web.Response:
    """Updates attachments on a specific credit note by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param credit_note_id: Unique identifier for a Credit Note
    :type credit_note_id: str
    :type credit_note_id: str
    :param file_name: Name of the file you are attaching to Credit Note
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_expense_claim(request: web.Request, xero_tenant_id, expense_claim_id, body) -> web.Response:
    """Updates a specific expense claims

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param expense_claim_id: Unique identifier for a ExpenseClaim
    :type expense_claim_id: str
    :type expense_claim_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ExpenseClaims.from_dict(body)
    return web.Response(status=200)


async def update_invoice(request: web.Request, xero_tenant_id, invoice_id, body, unitdp=None) -> web.Response:
    """Updates a specific sales invoices or purchase bills

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str
    :param body: 
    :type body: dict | bytes
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = Invoices.from_dict(body)
    return web.Response(status=200)


async def update_invoice_attachment_by_file_name(request: web.Request, xero_tenant_id, invoice_id, file_name, body) -> web.Response:
    """Updates an attachment from a specific invoices or purchase bill by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param invoice_id: Unique identifier for an Invoice
    :type invoice_id: str
    :type invoice_id: str
    :param file_name: Name of the file you are attaching
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_item(request: web.Request, xero_tenant_id, item_id, body, unitdp=None) -> web.Response:
    """Updates a specific item

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param item_id: Unique identifier for an Item
    :type item_id: str
    :type item_id: str
    :param body: 
    :type body: dict | bytes
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = Items.from_dict(body)
    return web.Response(status=200)


async def update_linked_transaction(request: web.Request, xero_tenant_id, linked_transaction_id, body) -> web.Response:
    """Updates a specific linked transactions (billable expenses)

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param linked_transaction_id: Unique identifier for a LinkedTransaction
    :type linked_transaction_id: str
    :type linked_transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = LinkedTransactions.from_dict(body)
    return web.Response(status=200)


async def update_manual_journal(request: web.Request, xero_tenant_id, manual_journal_id, body) -> web.Response:
    """Updates a specific manual journal

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param manual_journal_id: Unique identifier for a ManualJournal
    :type manual_journal_id: str
    :type manual_journal_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ManualJournals.from_dict(body)
    return web.Response(status=200)


async def update_manual_journal_attachment_by_file_name(request: web.Request, xero_tenant_id, manual_journal_id, file_name, body) -> web.Response:
    """Updates a specific attachment from a specific manual journal by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param manual_journal_id: Unique identifier for a ManualJournal
    :type manual_journal_id: str
    :type manual_journal_id: str
    :param file_name: The name of the file being attached to a ManualJournal
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_or_create_bank_transactions(request: web.Request, xero_tenant_id, body, summarize_errors=None, unitdp=None) -> web.Response:
    """Updates or creates one or more spent or received money transaction

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = BankTransactions.from_dict(body)
    return web.Response(status=200)


async def update_or_create_contacts(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Updates or creates one or more contacts in a Xero organisation

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = Contacts.from_dict(body)
    return web.Response(status=200)


async def update_or_create_credit_notes(request: web.Request, xero_tenant_id, body, summarize_errors=None, unitdp=None) -> web.Response:
    """Updates or creates one or more credit notes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: an array of Credit Notes with a single CreditNote object.
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = CreditNotes.from_dict(body)
    return web.Response(status=200)


async def update_or_create_employees(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Creates a single new employees used in Xero payrun

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Employees with array of Employee object in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = Employees.from_dict(body)
    return web.Response(status=200)


async def update_or_create_invoices(request: web.Request, xero_tenant_id, body, summarize_errors=None, unitdp=None) -> web.Response:
    """Updates or creates one or more sales invoices or purchase bills

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = Invoices.from_dict(body)
    return web.Response(status=200)


async def update_or_create_items(request: web.Request, xero_tenant_id, body, summarize_errors=None, unitdp=None) -> web.Response:
    """Updates or creates one or more items

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = Items.from_dict(body)
    return web.Response(status=200)


async def update_or_create_manual_journals(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Updates or creates a single manual journal

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: ManualJournals array with ManualJournal object in body of request
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = ManualJournals.from_dict(body)
    return web.Response(status=200)


async def update_or_create_purchase_orders(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Updates or creates one or more purchase orders

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = PurchaseOrders.from_dict(body)
    return web.Response(status=200)


async def update_or_create_quotes(request: web.Request, xero_tenant_id, body, summarize_errors=None) -> web.Response:
    """Updates or creates one or more quotes

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: dict | bytes
    :param summarize_errors: If false return 200 OK and mix of successfully created objects and any with validation errors
    :type summarize_errors: bool

    """
    body = Quotes.from_dict(body)
    return web.Response(status=200)


async def update_purchase_order(request: web.Request, xero_tenant_id, purchase_order_id, body) -> web.Response:
    """Updates a specific purchase order

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_id: Unique identifier for a PurchaseOrder
    :type purchase_order_id: str
    :type purchase_order_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PurchaseOrders.from_dict(body)
    return web.Response(status=200)


async def update_purchase_order_attachment_by_file_name(request: web.Request, xero_tenant_id, purchase_order_id, file_name, body) -> web.Response:
    """Updates a specific attachment for a specific purchase order by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param purchase_order_id: Unique identifier for Purchase Order object
    :type purchase_order_id: str
    :type purchase_order_id: str
    :param file_name: Name of the attachment
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_quote(request: web.Request, xero_tenant_id, quote_id, body) -> web.Response:
    """Updates a specific quote

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param quote_id: Unique identifier for an Quote
    :type quote_id: str
    :type quote_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Quotes.from_dict(body)
    return web.Response(status=200)


async def update_quote_attachment_by_file_name(request: web.Request, xero_tenant_id, quote_id, file_name, body) -> web.Response:
    """Updates a specific attachment from a specific quote by filename

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param quote_id: Unique identifier for Quote object
    :type quote_id: str
    :type quote_id: str
    :param file_name: Name of the attachment
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_receipt(request: web.Request, xero_tenant_id, receipt_id, body, unitdp=None) -> web.Response:
    """Updates a specific draft expense claim receipts

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param receipt_id: Unique identifier for a Receipt
    :type receipt_id: str
    :type receipt_id: str
    :param body: 
    :type body: dict | bytes
    :param unitdp: e.g. unitdp&#x3D;4 – (Unit Decimal Places) You can opt in to use four decimal places for unit amounts
    :type unitdp: int

    """
    body = Receipts.from_dict(body)
    return web.Response(status=200)


async def update_receipt_attachment_by_file_name(request: web.Request, xero_tenant_id, receipt_id, file_name, body) -> web.Response:
    """Updates a specific attachment on a specific expense claim receipts by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param receipt_id: Unique identifier for a Receipt
    :type receipt_id: str
    :type receipt_id: str
    :param file_name: The name of the file being attached to the Receipt
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_repeating_invoice_attachment_by_file_name(request: web.Request, xero_tenant_id, repeating_invoice_id, file_name, body) -> web.Response:
    """Updates a specific attachment from a specific repeating invoices by file name

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param repeating_invoice_id: Unique identifier for a Repeating Invoice
    :type repeating_invoice_id: str
    :type repeating_invoice_id: str
    :param file_name: The name of the file being attached to a Repeating Invoice
    :type file_name: str
    :param body: Byte array of file in body of request
    :type body: str

    """
    return web.Response(status=200)


async def update_tax_rate(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Updates tax rates

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TaxRates.from_dict(body)
    return web.Response(status=200)


async def update_tracking_category(request: web.Request, xero_tenant_id, tracking_category_id, body) -> web.Response:
    """Updates a specific tracking category

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param tracking_category_id: Unique identifier for a TrackingCategory
    :type tracking_category_id: str
    :type tracking_category_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TrackingCategory.from_dict(body)
    return web.Response(status=200)


async def update_tracking_options(request: web.Request, xero_tenant_id, tracking_category_id, tracking_option_id, body) -> web.Response:
    """Updates a specific option for a specific tracking category

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param tracking_category_id: Unique identifier for a TrackingCategory
    :type tracking_category_id: str
    :type tracking_category_id: str
    :param tracking_option_id: Unique identifier for a Tracking Option
    :type tracking_option_id: str
    :type tracking_option_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TrackingOption.from_dict(body)
    return web.Response(status=200)
