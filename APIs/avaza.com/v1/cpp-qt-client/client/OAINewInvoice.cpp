/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINewInvoice.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINewInvoice::OAINewInvoice(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINewInvoice::OAINewInvoice() {
    this->initializeModel();
}

OAINewInvoice::~OAINewInvoice() {}

void OAINewInvoice::initializeModel() {

    m_company_idfk_isSet = false;
    m_company_idfk_isValid = false;

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_currency_code_isSet = false;
    m_currency_code_isValid = false;

    m_customer_po_number_isSet = false;
    m_customer_po_number_isValid = false;

    m_date_issued_isSet = false;
    m_date_issued_isValid = false;

    m_due_date_isSet = false;
    m_due_date_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_exchange_rate_isSet = false;
    m_exchange_rate_isValid = false;

    m_firstname_isSet = false;
    m_firstname_isValid = false;

    m_invoice_number_isSet = false;
    m_invoice_number_isValid = false;

    m_invoice_template_idfk_isSet = false;
    m_invoice_template_idfk_isValid = false;

    m_lastname_isSet = false;
    m_lastname_isValid = false;

    m_line_items_isSet = false;
    m_line_items_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_payment_terms_isSet = false;
    m_payment_terms_isValid = false;

    m_subject_isSet = false;
    m_subject_isValid = false;

    m_transaction_prefix_isSet = false;
    m_transaction_prefix_isValid = false;

    m_transaction_tax_config_code_isSet = false;
    m_transaction_tax_config_code_isValid = false;
}

void OAINewInvoice::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINewInvoice::fromJsonObject(QJsonObject json) {

    m_company_idfk_isValid = ::OpenAPI::fromJsonValue(m_company_idfk, json[QString("CompanyIDFK")]);
    m_company_idfk_isSet = !json[QString("CompanyIDFK")].isNull() && m_company_idfk_isValid;

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("CompanyName")]);
    m_company_name_isSet = !json[QString("CompanyName")].isNull() && m_company_name_isValid;

    m_currency_code_isValid = ::OpenAPI::fromJsonValue(m_currency_code, json[QString("CurrencyCode")]);
    m_currency_code_isSet = !json[QString("CurrencyCode")].isNull() && m_currency_code_isValid;

    m_customer_po_number_isValid = ::OpenAPI::fromJsonValue(m_customer_po_number, json[QString("CustomerPONumber")]);
    m_customer_po_number_isSet = !json[QString("CustomerPONumber")].isNull() && m_customer_po_number_isValid;

    m_date_issued_isValid = ::OpenAPI::fromJsonValue(m_date_issued, json[QString("DateIssued")]);
    m_date_issued_isSet = !json[QString("DateIssued")].isNull() && m_date_issued_isValid;

    m_due_date_isValid = ::OpenAPI::fromJsonValue(m_due_date, json[QString("DueDate")]);
    m_due_date_isSet = !json[QString("DueDate")].isNull() && m_due_date_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("Email")]);
    m_email_isSet = !json[QString("Email")].isNull() && m_email_isValid;

    m_exchange_rate_isValid = ::OpenAPI::fromJsonValue(m_exchange_rate, json[QString("ExchangeRate")]);
    m_exchange_rate_isSet = !json[QString("ExchangeRate")].isNull() && m_exchange_rate_isValid;

    m_firstname_isValid = ::OpenAPI::fromJsonValue(m_firstname, json[QString("Firstname")]);
    m_firstname_isSet = !json[QString("Firstname")].isNull() && m_firstname_isValid;

    m_invoice_number_isValid = ::OpenAPI::fromJsonValue(m_invoice_number, json[QString("InvoiceNumber")]);
    m_invoice_number_isSet = !json[QString("InvoiceNumber")].isNull() && m_invoice_number_isValid;

    m_invoice_template_idfk_isValid = ::OpenAPI::fromJsonValue(m_invoice_template_idfk, json[QString("InvoiceTemplateIDFK")]);
    m_invoice_template_idfk_isSet = !json[QString("InvoiceTemplateIDFK")].isNull() && m_invoice_template_idfk_isValid;

    m_lastname_isValid = ::OpenAPI::fromJsonValue(m_lastname, json[QString("Lastname")]);
    m_lastname_isSet = !json[QString("Lastname")].isNull() && m_lastname_isValid;

    m_line_items_isValid = ::OpenAPI::fromJsonValue(m_line_items, json[QString("LineItems")]);
    m_line_items_isSet = !json[QString("LineItems")].isNull() && m_line_items_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("Notes")]);
    m_notes_isSet = !json[QString("Notes")].isNull() && m_notes_isValid;

    m_payment_terms_isValid = ::OpenAPI::fromJsonValue(m_payment_terms, json[QString("PaymentTerms")]);
    m_payment_terms_isSet = !json[QString("PaymentTerms")].isNull() && m_payment_terms_isValid;

    m_subject_isValid = ::OpenAPI::fromJsonValue(m_subject, json[QString("Subject")]);
    m_subject_isSet = !json[QString("Subject")].isNull() && m_subject_isValid;

    m_transaction_prefix_isValid = ::OpenAPI::fromJsonValue(m_transaction_prefix, json[QString("TransactionPrefix")]);
    m_transaction_prefix_isSet = !json[QString("TransactionPrefix")].isNull() && m_transaction_prefix_isValid;

    m_transaction_tax_config_code_isValid = ::OpenAPI::fromJsonValue(m_transaction_tax_config_code, json[QString("TransactionTaxConfigCode")]);
    m_transaction_tax_config_code_isSet = !json[QString("TransactionTaxConfigCode")].isNull() && m_transaction_tax_config_code_isValid;
}

QString OAINewInvoice::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINewInvoice::asJsonObject() const {
    QJsonObject obj;
    if (m_company_idfk_isSet) {
        obj.insert(QString("CompanyIDFK"), ::OpenAPI::toJsonValue(m_company_idfk));
    }
    if (m_company_name_isSet) {
        obj.insert(QString("CompanyName"), ::OpenAPI::toJsonValue(m_company_name));
    }
    if (m_currency_code_isSet) {
        obj.insert(QString("CurrencyCode"), ::OpenAPI::toJsonValue(m_currency_code));
    }
    if (m_customer_po_number_isSet) {
        obj.insert(QString("CustomerPONumber"), ::OpenAPI::toJsonValue(m_customer_po_number));
    }
    if (m_date_issued_isSet) {
        obj.insert(QString("DateIssued"), ::OpenAPI::toJsonValue(m_date_issued));
    }
    if (m_due_date_isSet) {
        obj.insert(QString("DueDate"), ::OpenAPI::toJsonValue(m_due_date));
    }
    if (m_email_isSet) {
        obj.insert(QString("Email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_exchange_rate_isSet) {
        obj.insert(QString("ExchangeRate"), ::OpenAPI::toJsonValue(m_exchange_rate));
    }
    if (m_firstname_isSet) {
        obj.insert(QString("Firstname"), ::OpenAPI::toJsonValue(m_firstname));
    }
    if (m_invoice_number_isSet) {
        obj.insert(QString("InvoiceNumber"), ::OpenAPI::toJsonValue(m_invoice_number));
    }
    if (m_invoice_template_idfk_isSet) {
        obj.insert(QString("InvoiceTemplateIDFK"), ::OpenAPI::toJsonValue(m_invoice_template_idfk));
    }
    if (m_lastname_isSet) {
        obj.insert(QString("Lastname"), ::OpenAPI::toJsonValue(m_lastname));
    }
    if (m_line_items.size() > 0) {
        obj.insert(QString("LineItems"), ::OpenAPI::toJsonValue(m_line_items));
    }
    if (m_notes_isSet) {
        obj.insert(QString("Notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_payment_terms_isSet) {
        obj.insert(QString("PaymentTerms"), ::OpenAPI::toJsonValue(m_payment_terms));
    }
    if (m_subject_isSet) {
        obj.insert(QString("Subject"), ::OpenAPI::toJsonValue(m_subject));
    }
    if (m_transaction_prefix_isSet) {
        obj.insert(QString("TransactionPrefix"), ::OpenAPI::toJsonValue(m_transaction_prefix));
    }
    if (m_transaction_tax_config_code_isSet) {
        obj.insert(QString("TransactionTaxConfigCode"), ::OpenAPI::toJsonValue(m_transaction_tax_config_code));
    }
    return obj;
}

qint32 OAINewInvoice::getCompanyIdfk() const {
    return m_company_idfk;
}
void OAINewInvoice::setCompanyIdfk(const qint32 &company_idfk) {
    m_company_idfk = company_idfk;
    m_company_idfk_isSet = true;
}

bool OAINewInvoice::is_company_idfk_Set() const{
    return m_company_idfk_isSet;
}

bool OAINewInvoice::is_company_idfk_Valid() const{
    return m_company_idfk_isValid;
}

QString OAINewInvoice::getCompanyName() const {
    return m_company_name;
}
void OAINewInvoice::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAINewInvoice::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAINewInvoice::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QString OAINewInvoice::getCurrencyCode() const {
    return m_currency_code;
}
void OAINewInvoice::setCurrencyCode(const QString &currency_code) {
    m_currency_code = currency_code;
    m_currency_code_isSet = true;
}

bool OAINewInvoice::is_currency_code_Set() const{
    return m_currency_code_isSet;
}

bool OAINewInvoice::is_currency_code_Valid() const{
    return m_currency_code_isValid;
}

QString OAINewInvoice::getCustomerPoNumber() const {
    return m_customer_po_number;
}
void OAINewInvoice::setCustomerPoNumber(const QString &customer_po_number) {
    m_customer_po_number = customer_po_number;
    m_customer_po_number_isSet = true;
}

bool OAINewInvoice::is_customer_po_number_Set() const{
    return m_customer_po_number_isSet;
}

bool OAINewInvoice::is_customer_po_number_Valid() const{
    return m_customer_po_number_isValid;
}

QDateTime OAINewInvoice::getDateIssued() const {
    return m_date_issued;
}
void OAINewInvoice::setDateIssued(const QDateTime &date_issued) {
    m_date_issued = date_issued;
    m_date_issued_isSet = true;
}

bool OAINewInvoice::is_date_issued_Set() const{
    return m_date_issued_isSet;
}

bool OAINewInvoice::is_date_issued_Valid() const{
    return m_date_issued_isValid;
}

QDateTime OAINewInvoice::getDueDate() const {
    return m_due_date;
}
void OAINewInvoice::setDueDate(const QDateTime &due_date) {
    m_due_date = due_date;
    m_due_date_isSet = true;
}

bool OAINewInvoice::is_due_date_Set() const{
    return m_due_date_isSet;
}

bool OAINewInvoice::is_due_date_Valid() const{
    return m_due_date_isValid;
}

QString OAINewInvoice::getEmail() const {
    return m_email;
}
void OAINewInvoice::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAINewInvoice::is_email_Set() const{
    return m_email_isSet;
}

bool OAINewInvoice::is_email_Valid() const{
    return m_email_isValid;
}

double OAINewInvoice::getExchangeRate() const {
    return m_exchange_rate;
}
void OAINewInvoice::setExchangeRate(const double &exchange_rate) {
    m_exchange_rate = exchange_rate;
    m_exchange_rate_isSet = true;
}

bool OAINewInvoice::is_exchange_rate_Set() const{
    return m_exchange_rate_isSet;
}

bool OAINewInvoice::is_exchange_rate_Valid() const{
    return m_exchange_rate_isValid;
}

QString OAINewInvoice::getFirstname() const {
    return m_firstname;
}
void OAINewInvoice::setFirstname(const QString &firstname) {
    m_firstname = firstname;
    m_firstname_isSet = true;
}

bool OAINewInvoice::is_firstname_Set() const{
    return m_firstname_isSet;
}

bool OAINewInvoice::is_firstname_Valid() const{
    return m_firstname_isValid;
}

QString OAINewInvoice::getInvoiceNumber() const {
    return m_invoice_number;
}
void OAINewInvoice::setInvoiceNumber(const QString &invoice_number) {
    m_invoice_number = invoice_number;
    m_invoice_number_isSet = true;
}

bool OAINewInvoice::is_invoice_number_Set() const{
    return m_invoice_number_isSet;
}

bool OAINewInvoice::is_invoice_number_Valid() const{
    return m_invoice_number_isValid;
}

qint32 OAINewInvoice::getInvoiceTemplateIdfk() const {
    return m_invoice_template_idfk;
}
void OAINewInvoice::setInvoiceTemplateIdfk(const qint32 &invoice_template_idfk) {
    m_invoice_template_idfk = invoice_template_idfk;
    m_invoice_template_idfk_isSet = true;
}

bool OAINewInvoice::is_invoice_template_idfk_Set() const{
    return m_invoice_template_idfk_isSet;
}

bool OAINewInvoice::is_invoice_template_idfk_Valid() const{
    return m_invoice_template_idfk_isValid;
}

QString OAINewInvoice::getLastname() const {
    return m_lastname;
}
void OAINewInvoice::setLastname(const QString &lastname) {
    m_lastname = lastname;
    m_lastname_isSet = true;
}

bool OAINewInvoice::is_lastname_Set() const{
    return m_lastname_isSet;
}

bool OAINewInvoice::is_lastname_Valid() const{
    return m_lastname_isValid;
}

QList<OAINewInvoiceLineItem> OAINewInvoice::getLineItems() const {
    return m_line_items;
}
void OAINewInvoice::setLineItems(const QList<OAINewInvoiceLineItem> &line_items) {
    m_line_items = line_items;
    m_line_items_isSet = true;
}

bool OAINewInvoice::is_line_items_Set() const{
    return m_line_items_isSet;
}

bool OAINewInvoice::is_line_items_Valid() const{
    return m_line_items_isValid;
}

QString OAINewInvoice::getNotes() const {
    return m_notes;
}
void OAINewInvoice::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAINewInvoice::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAINewInvoice::is_notes_Valid() const{
    return m_notes_isValid;
}

qint32 OAINewInvoice::getPaymentTerms() const {
    return m_payment_terms;
}
void OAINewInvoice::setPaymentTerms(const qint32 &payment_terms) {
    m_payment_terms = payment_terms;
    m_payment_terms_isSet = true;
}

bool OAINewInvoice::is_payment_terms_Set() const{
    return m_payment_terms_isSet;
}

bool OAINewInvoice::is_payment_terms_Valid() const{
    return m_payment_terms_isValid;
}

QString OAINewInvoice::getSubject() const {
    return m_subject;
}
void OAINewInvoice::setSubject(const QString &subject) {
    m_subject = subject;
    m_subject_isSet = true;
}

bool OAINewInvoice::is_subject_Set() const{
    return m_subject_isSet;
}

bool OAINewInvoice::is_subject_Valid() const{
    return m_subject_isValid;
}

QString OAINewInvoice::getTransactionPrefix() const {
    return m_transaction_prefix;
}
void OAINewInvoice::setTransactionPrefix(const QString &transaction_prefix) {
    m_transaction_prefix = transaction_prefix;
    m_transaction_prefix_isSet = true;
}

bool OAINewInvoice::is_transaction_prefix_Set() const{
    return m_transaction_prefix_isSet;
}

bool OAINewInvoice::is_transaction_prefix_Valid() const{
    return m_transaction_prefix_isValid;
}

QString OAINewInvoice::getTransactionTaxConfigCode() const {
    return m_transaction_tax_config_code;
}
void OAINewInvoice::setTransactionTaxConfigCode(const QString &transaction_tax_config_code) {
    m_transaction_tax_config_code = transaction_tax_config_code;
    m_transaction_tax_config_code_isSet = true;
}

bool OAINewInvoice::is_transaction_tax_config_code_Set() const{
    return m_transaction_tax_config_code_isSet;
}

bool OAINewInvoice::is_transaction_tax_config_code_Valid() const{
    return m_transaction_tax_config_code_isValid;
}

bool OAINewInvoice::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_company_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_po_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_issued_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_due_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exchange_rate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_firstname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_template_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lastname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_terms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subject_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_prefix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_tax_config_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINewInvoice::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
