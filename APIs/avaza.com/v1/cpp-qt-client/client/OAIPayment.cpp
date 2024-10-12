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

#include "OAIPayment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPayment::OAIPayment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPayment::OAIPayment() {
    this->initializeModel();
}

OAIPayment::~OAIPayment() {}

void OAIPayment::initializeModel() {

    m_account_idfk_isSet = false;
    m_account_idfk_isValid = false;

    m_balance_isSet = false;
    m_balance_isValid = false;

    m_currency_code_isSet = false;
    m_currency_code_isValid = false;

    m_customer_idfk_isSet = false;
    m_customer_idfk_isValid = false;

    m_date_created_isSet = false;
    m_date_created_isValid = false;

    m_date_issued_isSet = false;
    m_date_issued_isValid = false;

    m_date_updated_isSet = false;
    m_date_updated_isValid = false;

    m_exchange_rate_isSet = false;
    m_exchange_rate_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_payment_allocations_isSet = false;
    m_payment_allocations_isValid = false;

    m_payment_number_isSet = false;
    m_payment_number_isValid = false;

    m_payment_provider_code_isSet = false;
    m_payment_provider_code_isValid = false;

    m_total_amount_isSet = false;
    m_total_amount_isValid = false;

    m_transaction_id_isSet = false;
    m_transaction_id_isValid = false;

    m_transaction_prefix_isSet = false;
    m_transaction_prefix_isValid = false;

    m_transaction_reference_isSet = false;
    m_transaction_reference_isValid = false;

    m_transaction_status_code_isSet = false;
    m_transaction_status_code_isValid = false;
}

void OAIPayment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPayment::fromJsonObject(QJsonObject json) {

    m_account_idfk_isValid = ::OpenAPI::fromJsonValue(m_account_idfk, json[QString("AccountIDFK")]);
    m_account_idfk_isSet = !json[QString("AccountIDFK")].isNull() && m_account_idfk_isValid;

    m_balance_isValid = ::OpenAPI::fromJsonValue(m_balance, json[QString("Balance")]);
    m_balance_isSet = !json[QString("Balance")].isNull() && m_balance_isValid;

    m_currency_code_isValid = ::OpenAPI::fromJsonValue(m_currency_code, json[QString("CurrencyCode")]);
    m_currency_code_isSet = !json[QString("CurrencyCode")].isNull() && m_currency_code_isValid;

    m_customer_idfk_isValid = ::OpenAPI::fromJsonValue(m_customer_idfk, json[QString("CustomerIDFK")]);
    m_customer_idfk_isSet = !json[QString("CustomerIDFK")].isNull() && m_customer_idfk_isValid;

    m_date_created_isValid = ::OpenAPI::fromJsonValue(m_date_created, json[QString("DateCreated")]);
    m_date_created_isSet = !json[QString("DateCreated")].isNull() && m_date_created_isValid;

    m_date_issued_isValid = ::OpenAPI::fromJsonValue(m_date_issued, json[QString("DateIssued")]);
    m_date_issued_isSet = !json[QString("DateIssued")].isNull() && m_date_issued_isValid;

    m_date_updated_isValid = ::OpenAPI::fromJsonValue(m_date_updated, json[QString("DateUpdated")]);
    m_date_updated_isSet = !json[QString("DateUpdated")].isNull() && m_date_updated_isValid;

    m_exchange_rate_isValid = ::OpenAPI::fromJsonValue(m_exchange_rate, json[QString("ExchangeRate")]);
    m_exchange_rate_isSet = !json[QString("ExchangeRate")].isNull() && m_exchange_rate_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("Notes")]);
    m_notes_isSet = !json[QString("Notes")].isNull() && m_notes_isValid;

    m_payment_allocations_isValid = ::OpenAPI::fromJsonValue(m_payment_allocations, json[QString("PaymentAllocations")]);
    m_payment_allocations_isSet = !json[QString("PaymentAllocations")].isNull() && m_payment_allocations_isValid;

    m_payment_number_isValid = ::OpenAPI::fromJsonValue(m_payment_number, json[QString("PaymentNumber")]);
    m_payment_number_isSet = !json[QString("PaymentNumber")].isNull() && m_payment_number_isValid;

    m_payment_provider_code_isValid = ::OpenAPI::fromJsonValue(m_payment_provider_code, json[QString("PaymentProviderCode")]);
    m_payment_provider_code_isSet = !json[QString("PaymentProviderCode")].isNull() && m_payment_provider_code_isValid;

    m_total_amount_isValid = ::OpenAPI::fromJsonValue(m_total_amount, json[QString("TotalAmount")]);
    m_total_amount_isSet = !json[QString("TotalAmount")].isNull() && m_total_amount_isValid;

    m_transaction_id_isValid = ::OpenAPI::fromJsonValue(m_transaction_id, json[QString("TransactionID")]);
    m_transaction_id_isSet = !json[QString("TransactionID")].isNull() && m_transaction_id_isValid;

    m_transaction_prefix_isValid = ::OpenAPI::fromJsonValue(m_transaction_prefix, json[QString("TransactionPrefix")]);
    m_transaction_prefix_isSet = !json[QString("TransactionPrefix")].isNull() && m_transaction_prefix_isValid;

    m_transaction_reference_isValid = ::OpenAPI::fromJsonValue(m_transaction_reference, json[QString("TransactionReference")]);
    m_transaction_reference_isSet = !json[QString("TransactionReference")].isNull() && m_transaction_reference_isValid;

    m_transaction_status_code_isValid = ::OpenAPI::fromJsonValue(m_transaction_status_code, json[QString("TransactionStatusCode")]);
    m_transaction_status_code_isSet = !json[QString("TransactionStatusCode")].isNull() && m_transaction_status_code_isValid;
}

QString OAIPayment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPayment::asJsonObject() const {
    QJsonObject obj;
    if (m_account_idfk_isSet) {
        obj.insert(QString("AccountIDFK"), ::OpenAPI::toJsonValue(m_account_idfk));
    }
    if (m_balance_isSet) {
        obj.insert(QString("Balance"), ::OpenAPI::toJsonValue(m_balance));
    }
    if (m_currency_code_isSet) {
        obj.insert(QString("CurrencyCode"), ::OpenAPI::toJsonValue(m_currency_code));
    }
    if (m_customer_idfk_isSet) {
        obj.insert(QString("CustomerIDFK"), ::OpenAPI::toJsonValue(m_customer_idfk));
    }
    if (m_date_created_isSet) {
        obj.insert(QString("DateCreated"), ::OpenAPI::toJsonValue(m_date_created));
    }
    if (m_date_issued_isSet) {
        obj.insert(QString("DateIssued"), ::OpenAPI::toJsonValue(m_date_issued));
    }
    if (m_date_updated_isSet) {
        obj.insert(QString("DateUpdated"), ::OpenAPI::toJsonValue(m_date_updated));
    }
    if (m_exchange_rate_isSet) {
        obj.insert(QString("ExchangeRate"), ::OpenAPI::toJsonValue(m_exchange_rate));
    }
    if (m_notes_isSet) {
        obj.insert(QString("Notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_payment_allocations.size() > 0) {
        obj.insert(QString("PaymentAllocations"), ::OpenAPI::toJsonValue(m_payment_allocations));
    }
    if (m_payment_number_isSet) {
        obj.insert(QString("PaymentNumber"), ::OpenAPI::toJsonValue(m_payment_number));
    }
    if (m_payment_provider_code_isSet) {
        obj.insert(QString("PaymentProviderCode"), ::OpenAPI::toJsonValue(m_payment_provider_code));
    }
    if (m_total_amount_isSet) {
        obj.insert(QString("TotalAmount"), ::OpenAPI::toJsonValue(m_total_amount));
    }
    if (m_transaction_id_isSet) {
        obj.insert(QString("TransactionID"), ::OpenAPI::toJsonValue(m_transaction_id));
    }
    if (m_transaction_prefix_isSet) {
        obj.insert(QString("TransactionPrefix"), ::OpenAPI::toJsonValue(m_transaction_prefix));
    }
    if (m_transaction_reference_isSet) {
        obj.insert(QString("TransactionReference"), ::OpenAPI::toJsonValue(m_transaction_reference));
    }
    if (m_transaction_status_code_isSet) {
        obj.insert(QString("TransactionStatusCode"), ::OpenAPI::toJsonValue(m_transaction_status_code));
    }
    return obj;
}

qint32 OAIPayment::getAccountIdfk() const {
    return m_account_idfk;
}
void OAIPayment::setAccountIdfk(const qint32 &account_idfk) {
    m_account_idfk = account_idfk;
    m_account_idfk_isSet = true;
}

bool OAIPayment::is_account_idfk_Set() const{
    return m_account_idfk_isSet;
}

bool OAIPayment::is_account_idfk_Valid() const{
    return m_account_idfk_isValid;
}

double OAIPayment::getBalance() const {
    return m_balance;
}
void OAIPayment::setBalance(const double &balance) {
    m_balance = balance;
    m_balance_isSet = true;
}

bool OAIPayment::is_balance_Set() const{
    return m_balance_isSet;
}

bool OAIPayment::is_balance_Valid() const{
    return m_balance_isValid;
}

QString OAIPayment::getCurrencyCode() const {
    return m_currency_code;
}
void OAIPayment::setCurrencyCode(const QString &currency_code) {
    m_currency_code = currency_code;
    m_currency_code_isSet = true;
}

bool OAIPayment::is_currency_code_Set() const{
    return m_currency_code_isSet;
}

bool OAIPayment::is_currency_code_Valid() const{
    return m_currency_code_isValid;
}

qint32 OAIPayment::getCustomerIdfk() const {
    return m_customer_idfk;
}
void OAIPayment::setCustomerIdfk(const qint32 &customer_idfk) {
    m_customer_idfk = customer_idfk;
    m_customer_idfk_isSet = true;
}

bool OAIPayment::is_customer_idfk_Set() const{
    return m_customer_idfk_isSet;
}

bool OAIPayment::is_customer_idfk_Valid() const{
    return m_customer_idfk_isValid;
}

QDateTime OAIPayment::getDateCreated() const {
    return m_date_created;
}
void OAIPayment::setDateCreated(const QDateTime &date_created) {
    m_date_created = date_created;
    m_date_created_isSet = true;
}

bool OAIPayment::is_date_created_Set() const{
    return m_date_created_isSet;
}

bool OAIPayment::is_date_created_Valid() const{
    return m_date_created_isValid;
}

QDateTime OAIPayment::getDateIssued() const {
    return m_date_issued;
}
void OAIPayment::setDateIssued(const QDateTime &date_issued) {
    m_date_issued = date_issued;
    m_date_issued_isSet = true;
}

bool OAIPayment::is_date_issued_Set() const{
    return m_date_issued_isSet;
}

bool OAIPayment::is_date_issued_Valid() const{
    return m_date_issued_isValid;
}

QDateTime OAIPayment::getDateUpdated() const {
    return m_date_updated;
}
void OAIPayment::setDateUpdated(const QDateTime &date_updated) {
    m_date_updated = date_updated;
    m_date_updated_isSet = true;
}

bool OAIPayment::is_date_updated_Set() const{
    return m_date_updated_isSet;
}

bool OAIPayment::is_date_updated_Valid() const{
    return m_date_updated_isValid;
}

double OAIPayment::getExchangeRate() const {
    return m_exchange_rate;
}
void OAIPayment::setExchangeRate(const double &exchange_rate) {
    m_exchange_rate = exchange_rate;
    m_exchange_rate_isSet = true;
}

bool OAIPayment::is_exchange_rate_Set() const{
    return m_exchange_rate_isSet;
}

bool OAIPayment::is_exchange_rate_Valid() const{
    return m_exchange_rate_isValid;
}

QString OAIPayment::getNotes() const {
    return m_notes;
}
void OAIPayment::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIPayment::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIPayment::is_notes_Valid() const{
    return m_notes_isValid;
}

QList<OAIPaymentAllocation> OAIPayment::getPaymentAllocations() const {
    return m_payment_allocations;
}
void OAIPayment::setPaymentAllocations(const QList<OAIPaymentAllocation> &payment_allocations) {
    m_payment_allocations = payment_allocations;
    m_payment_allocations_isSet = true;
}

bool OAIPayment::is_payment_allocations_Set() const{
    return m_payment_allocations_isSet;
}

bool OAIPayment::is_payment_allocations_Valid() const{
    return m_payment_allocations_isValid;
}

QString OAIPayment::getPaymentNumber() const {
    return m_payment_number;
}
void OAIPayment::setPaymentNumber(const QString &payment_number) {
    m_payment_number = payment_number;
    m_payment_number_isSet = true;
}

bool OAIPayment::is_payment_number_Set() const{
    return m_payment_number_isSet;
}

bool OAIPayment::is_payment_number_Valid() const{
    return m_payment_number_isValid;
}

QString OAIPayment::getPaymentProviderCode() const {
    return m_payment_provider_code;
}
void OAIPayment::setPaymentProviderCode(const QString &payment_provider_code) {
    m_payment_provider_code = payment_provider_code;
    m_payment_provider_code_isSet = true;
}

bool OAIPayment::is_payment_provider_code_Set() const{
    return m_payment_provider_code_isSet;
}

bool OAIPayment::is_payment_provider_code_Valid() const{
    return m_payment_provider_code_isValid;
}

double OAIPayment::getTotalAmount() const {
    return m_total_amount;
}
void OAIPayment::setTotalAmount(const double &total_amount) {
    m_total_amount = total_amount;
    m_total_amount_isSet = true;
}

bool OAIPayment::is_total_amount_Set() const{
    return m_total_amount_isSet;
}

bool OAIPayment::is_total_amount_Valid() const{
    return m_total_amount_isValid;
}

qint64 OAIPayment::getTransactionId() const {
    return m_transaction_id;
}
void OAIPayment::setTransactionId(const qint64 &transaction_id) {
    m_transaction_id = transaction_id;
    m_transaction_id_isSet = true;
}

bool OAIPayment::is_transaction_id_Set() const{
    return m_transaction_id_isSet;
}

bool OAIPayment::is_transaction_id_Valid() const{
    return m_transaction_id_isValid;
}

QString OAIPayment::getTransactionPrefix() const {
    return m_transaction_prefix;
}
void OAIPayment::setTransactionPrefix(const QString &transaction_prefix) {
    m_transaction_prefix = transaction_prefix;
    m_transaction_prefix_isSet = true;
}

bool OAIPayment::is_transaction_prefix_Set() const{
    return m_transaction_prefix_isSet;
}

bool OAIPayment::is_transaction_prefix_Valid() const{
    return m_transaction_prefix_isValid;
}

QString OAIPayment::getTransactionReference() const {
    return m_transaction_reference;
}
void OAIPayment::setTransactionReference(const QString &transaction_reference) {
    m_transaction_reference = transaction_reference;
    m_transaction_reference_isSet = true;
}

bool OAIPayment::is_transaction_reference_Set() const{
    return m_transaction_reference_isSet;
}

bool OAIPayment::is_transaction_reference_Valid() const{
    return m_transaction_reference_isValid;
}

QString OAIPayment::getTransactionStatusCode() const {
    return m_transaction_status_code;
}
void OAIPayment::setTransactionStatusCode(const QString &transaction_status_code) {
    m_transaction_status_code = transaction_status_code;
    m_transaction_status_code_isSet = true;
}

bool OAIPayment::is_transaction_status_code_Set() const{
    return m_transaction_status_code_isSet;
}

bool OAIPayment::is_transaction_status_code_Valid() const{
    return m_transaction_status_code_isValid;
}

bool OAIPayment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_balance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_idfk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_issued_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_updated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exchange_rate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_allocations.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_provider_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_prefix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_status_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPayment::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
