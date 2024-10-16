/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIListTransactionsIn.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListTransactionsIn::OAIListTransactionsIn(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListTransactionsIn::OAIListTransactionsIn() {
    this->initializeModel();
}

OAIListTransactionsIn::~OAIListTransactionsIn() {}

void OAIListTransactionsIn::initializeModel() {

    m_currency_code_isSet = false;
    m_currency_code_isValid = false;

    m_filter_text_isSet = false;
    m_filter_text_isValid = false;

    m_format_isSet = false;
    m_format_isValid = false;

    m_has_note_isSet = false;
    m_has_note_isValid = false;

    m_invoice_number_isSet = false;
    m_invoice_number_isValid = false;

    m_key_or_custom_id_isSet = false;
    m_key_or_custom_id_isValid = false;

    m_limit_isSet = false;
    m_limit_isValid = false;

    m_offset_isSet = false;
    m_offset_isValid = false;

    m_order_date_from_isSet = false;
    m_order_date_from_isValid = false;

    m_order_date_to_isSet = false;
    m_order_date_to_isValid = false;

    m_original_transaction_key_isSet = false;
    m_original_transaction_key_isValid = false;

    m_sort_reverse_isSet = false;
    m_sort_reverse_isValid = false;

    m_statuses_isSet = false;
    m_statuses_isValid = false;

    m_tax_country_code_isSet = false;
    m_tax_country_code_isValid = false;

    m_tax_country_codes_isSet = false;
    m_tax_country_codes_isValid = false;

    m_total_amount_greater_than_isSet = false;
    m_total_amount_greater_than_isValid = false;

    m_total_amount_less_than_isSet = false;
    m_total_amount_less_than_isValid = false;
}

void OAIListTransactionsIn::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListTransactionsIn::fromJsonObject(QJsonObject json) {

    m_currency_code_isValid = ::OpenAPI::fromJsonValue(m_currency_code, json[QString("currency_code")]);
    m_currency_code_isSet = !json[QString("currency_code")].isNull() && m_currency_code_isValid;

    m_filter_text_isValid = ::OpenAPI::fromJsonValue(m_filter_text, json[QString("filter_text")]);
    m_filter_text_isSet = !json[QString("filter_text")].isNull() && m_filter_text_isValid;

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("format")]);
    m_format_isSet = !json[QString("format")].isNull() && m_format_isValid;

    m_has_note_isValid = ::OpenAPI::fromJsonValue(m_has_note, json[QString("has_note")]);
    m_has_note_isSet = !json[QString("has_note")].isNull() && m_has_note_isValid;

    m_invoice_number_isValid = ::OpenAPI::fromJsonValue(m_invoice_number, json[QString("invoice_number")]);
    m_invoice_number_isSet = !json[QString("invoice_number")].isNull() && m_invoice_number_isValid;

    m_key_or_custom_id_isValid = ::OpenAPI::fromJsonValue(m_key_or_custom_id, json[QString("key_or_custom_id")]);
    m_key_or_custom_id_isSet = !json[QString("key_or_custom_id")].isNull() && m_key_or_custom_id_isValid;

    m_limit_isValid = ::OpenAPI::fromJsonValue(m_limit, json[QString("limit")]);
    m_limit_isSet = !json[QString("limit")].isNull() && m_limit_isValid;

    m_offset_isValid = ::OpenAPI::fromJsonValue(m_offset, json[QString("offset")]);
    m_offset_isSet = !json[QString("offset")].isNull() && m_offset_isValid;

    m_order_date_from_isValid = ::OpenAPI::fromJsonValue(m_order_date_from, json[QString("order_date_from")]);
    m_order_date_from_isSet = !json[QString("order_date_from")].isNull() && m_order_date_from_isValid;

    m_order_date_to_isValid = ::OpenAPI::fromJsonValue(m_order_date_to, json[QString("order_date_to")]);
    m_order_date_to_isSet = !json[QString("order_date_to")].isNull() && m_order_date_to_isValid;

    m_original_transaction_key_isValid = ::OpenAPI::fromJsonValue(m_original_transaction_key, json[QString("original_transaction_key")]);
    m_original_transaction_key_isSet = !json[QString("original_transaction_key")].isNull() && m_original_transaction_key_isValid;

    m_sort_reverse_isValid = ::OpenAPI::fromJsonValue(m_sort_reverse, json[QString("sort_reverse")]);
    m_sort_reverse_isSet = !json[QString("sort_reverse")].isNull() && m_sort_reverse_isValid;

    m_statuses_isValid = ::OpenAPI::fromJsonValue(m_statuses, json[QString("statuses")]);
    m_statuses_isSet = !json[QString("statuses")].isNull() && m_statuses_isValid;

    m_tax_country_code_isValid = ::OpenAPI::fromJsonValue(m_tax_country_code, json[QString("tax_country_code")]);
    m_tax_country_code_isSet = !json[QString("tax_country_code")].isNull() && m_tax_country_code_isValid;

    m_tax_country_codes_isValid = ::OpenAPI::fromJsonValue(m_tax_country_codes, json[QString("tax_country_codes")]);
    m_tax_country_codes_isSet = !json[QString("tax_country_codes")].isNull() && m_tax_country_codes_isValid;

    m_total_amount_greater_than_isValid = ::OpenAPI::fromJsonValue(m_total_amount_greater_than, json[QString("total_amount_greater_than")]);
    m_total_amount_greater_than_isSet = !json[QString("total_amount_greater_than")].isNull() && m_total_amount_greater_than_isValid;

    m_total_amount_less_than_isValid = ::OpenAPI::fromJsonValue(m_total_amount_less_than, json[QString("total_amount_less_than")]);
    m_total_amount_less_than_isSet = !json[QString("total_amount_less_than")].isNull() && m_total_amount_less_than_isValid;
}

QString OAIListTransactionsIn::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListTransactionsIn::asJsonObject() const {
    QJsonObject obj;
    if (m_currency_code_isSet) {
        obj.insert(QString("currency_code"), ::OpenAPI::toJsonValue(m_currency_code));
    }
    if (m_filter_text_isSet) {
        obj.insert(QString("filter_text"), ::OpenAPI::toJsonValue(m_filter_text));
    }
    if (m_format_isSet) {
        obj.insert(QString("format"), ::OpenAPI::toJsonValue(m_format));
    }
    if (m_has_note_isSet) {
        obj.insert(QString("has_note"), ::OpenAPI::toJsonValue(m_has_note));
    }
    if (m_invoice_number_isSet) {
        obj.insert(QString("invoice_number"), ::OpenAPI::toJsonValue(m_invoice_number));
    }
    if (m_key_or_custom_id_isSet) {
        obj.insert(QString("key_or_custom_id"), ::OpenAPI::toJsonValue(m_key_or_custom_id));
    }
    if (m_limit_isSet) {
        obj.insert(QString("limit"), ::OpenAPI::toJsonValue(m_limit));
    }
    if (m_offset_isSet) {
        obj.insert(QString("offset"), ::OpenAPI::toJsonValue(m_offset));
    }
    if (m_order_date_from_isSet) {
        obj.insert(QString("order_date_from"), ::OpenAPI::toJsonValue(m_order_date_from));
    }
    if (m_order_date_to_isSet) {
        obj.insert(QString("order_date_to"), ::OpenAPI::toJsonValue(m_order_date_to));
    }
    if (m_original_transaction_key_isSet) {
        obj.insert(QString("original_transaction_key"), ::OpenAPI::toJsonValue(m_original_transaction_key));
    }
    if (m_sort_reverse_isSet) {
        obj.insert(QString("sort_reverse"), ::OpenAPI::toJsonValue(m_sort_reverse));
    }
    if (m_statuses_isSet) {
        obj.insert(QString("statuses"), ::OpenAPI::toJsonValue(m_statuses));
    }
    if (m_tax_country_code_isSet) {
        obj.insert(QString("tax_country_code"), ::OpenAPI::toJsonValue(m_tax_country_code));
    }
    if (m_tax_country_codes_isSet) {
        obj.insert(QString("tax_country_codes"), ::OpenAPI::toJsonValue(m_tax_country_codes));
    }
    if (m_total_amount_greater_than_isSet) {
        obj.insert(QString("total_amount_greater_than"), ::OpenAPI::toJsonValue(m_total_amount_greater_than));
    }
    if (m_total_amount_less_than_isSet) {
        obj.insert(QString("total_amount_less_than"), ::OpenAPI::toJsonValue(m_total_amount_less_than));
    }
    return obj;
}

QString OAIListTransactionsIn::getCurrencyCode() const {
    return m_currency_code;
}
void OAIListTransactionsIn::setCurrencyCode(const QString &currency_code) {
    m_currency_code = currency_code;
    m_currency_code_isSet = true;
}

bool OAIListTransactionsIn::is_currency_code_Set() const{
    return m_currency_code_isSet;
}

bool OAIListTransactionsIn::is_currency_code_Valid() const{
    return m_currency_code_isValid;
}

QString OAIListTransactionsIn::getFilterText() const {
    return m_filter_text;
}
void OAIListTransactionsIn::setFilterText(const QString &filter_text) {
    m_filter_text = filter_text;
    m_filter_text_isSet = true;
}

bool OAIListTransactionsIn::is_filter_text_Set() const{
    return m_filter_text_isSet;
}

bool OAIListTransactionsIn::is_filter_text_Valid() const{
    return m_filter_text_isValid;
}

QString OAIListTransactionsIn::getFormat() const {
    return m_format;
}
void OAIListTransactionsIn::setFormat(const QString &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAIListTransactionsIn::is_format_Set() const{
    return m_format_isSet;
}

bool OAIListTransactionsIn::is_format_Valid() const{
    return m_format_isValid;
}

bool OAIListTransactionsIn::isHasNote() const {
    return m_has_note;
}
void OAIListTransactionsIn::setHasNote(const bool &has_note) {
    m_has_note = has_note;
    m_has_note_isSet = true;
}

bool OAIListTransactionsIn::is_has_note_Set() const{
    return m_has_note_isSet;
}

bool OAIListTransactionsIn::is_has_note_Valid() const{
    return m_has_note_isValid;
}

QString OAIListTransactionsIn::getInvoiceNumber() const {
    return m_invoice_number;
}
void OAIListTransactionsIn::setInvoiceNumber(const QString &invoice_number) {
    m_invoice_number = invoice_number;
    m_invoice_number_isSet = true;
}

bool OAIListTransactionsIn::is_invoice_number_Set() const{
    return m_invoice_number_isSet;
}

bool OAIListTransactionsIn::is_invoice_number_Valid() const{
    return m_invoice_number_isValid;
}

QString OAIListTransactionsIn::getKeyOrCustomId() const {
    return m_key_or_custom_id;
}
void OAIListTransactionsIn::setKeyOrCustomId(const QString &key_or_custom_id) {
    m_key_or_custom_id = key_or_custom_id;
    m_key_or_custom_id_isSet = true;
}

bool OAIListTransactionsIn::is_key_or_custom_id_Set() const{
    return m_key_or_custom_id_isSet;
}

bool OAIListTransactionsIn::is_key_or_custom_id_Valid() const{
    return m_key_or_custom_id_isValid;
}

qint32 OAIListTransactionsIn::getLimit() const {
    return m_limit;
}
void OAIListTransactionsIn::setLimit(const qint32 &limit) {
    m_limit = limit;
    m_limit_isSet = true;
}

bool OAIListTransactionsIn::is_limit_Set() const{
    return m_limit_isSet;
}

bool OAIListTransactionsIn::is_limit_Valid() const{
    return m_limit_isValid;
}

qint32 OAIListTransactionsIn::getOffset() const {
    return m_offset;
}
void OAIListTransactionsIn::setOffset(const qint32 &offset) {
    m_offset = offset;
    m_offset_isSet = true;
}

bool OAIListTransactionsIn::is_offset_Set() const{
    return m_offset_isSet;
}

bool OAIListTransactionsIn::is_offset_Valid() const{
    return m_offset_isValid;
}

QString OAIListTransactionsIn::getOrderDateFrom() const {
    return m_order_date_from;
}
void OAIListTransactionsIn::setOrderDateFrom(const QString &order_date_from) {
    m_order_date_from = order_date_from;
    m_order_date_from_isSet = true;
}

bool OAIListTransactionsIn::is_order_date_from_Set() const{
    return m_order_date_from_isSet;
}

bool OAIListTransactionsIn::is_order_date_from_Valid() const{
    return m_order_date_from_isValid;
}

QString OAIListTransactionsIn::getOrderDateTo() const {
    return m_order_date_to;
}
void OAIListTransactionsIn::setOrderDateTo(const QString &order_date_to) {
    m_order_date_to = order_date_to;
    m_order_date_to_isSet = true;
}

bool OAIListTransactionsIn::is_order_date_to_Set() const{
    return m_order_date_to_isSet;
}

bool OAIListTransactionsIn::is_order_date_to_Valid() const{
    return m_order_date_to_isValid;
}

QString OAIListTransactionsIn::getOriginalTransactionKey() const {
    return m_original_transaction_key;
}
void OAIListTransactionsIn::setOriginalTransactionKey(const QString &original_transaction_key) {
    m_original_transaction_key = original_transaction_key;
    m_original_transaction_key_isSet = true;
}

bool OAIListTransactionsIn::is_original_transaction_key_Set() const{
    return m_original_transaction_key_isSet;
}

bool OAIListTransactionsIn::is_original_transaction_key_Valid() const{
    return m_original_transaction_key_isValid;
}

bool OAIListTransactionsIn::isSortReverse() const {
    return m_sort_reverse;
}
void OAIListTransactionsIn::setSortReverse(const bool &sort_reverse) {
    m_sort_reverse = sort_reverse;
    m_sort_reverse_isSet = true;
}

bool OAIListTransactionsIn::is_sort_reverse_Set() const{
    return m_sort_reverse_isSet;
}

bool OAIListTransactionsIn::is_sort_reverse_Valid() const{
    return m_sort_reverse_isValid;
}

QString OAIListTransactionsIn::getStatuses() const {
    return m_statuses;
}
void OAIListTransactionsIn::setStatuses(const QString &statuses) {
    m_statuses = statuses;
    m_statuses_isSet = true;
}

bool OAIListTransactionsIn::is_statuses_Set() const{
    return m_statuses_isSet;
}

bool OAIListTransactionsIn::is_statuses_Valid() const{
    return m_statuses_isValid;
}

QString OAIListTransactionsIn::getTaxCountryCode() const {
    return m_tax_country_code;
}
void OAIListTransactionsIn::setTaxCountryCode(const QString &tax_country_code) {
    m_tax_country_code = tax_country_code;
    m_tax_country_code_isSet = true;
}

bool OAIListTransactionsIn::is_tax_country_code_Set() const{
    return m_tax_country_code_isSet;
}

bool OAIListTransactionsIn::is_tax_country_code_Valid() const{
    return m_tax_country_code_isValid;
}

QString OAIListTransactionsIn::getTaxCountryCodes() const {
    return m_tax_country_codes;
}
void OAIListTransactionsIn::setTaxCountryCodes(const QString &tax_country_codes) {
    m_tax_country_codes = tax_country_codes;
    m_tax_country_codes_isSet = true;
}

bool OAIListTransactionsIn::is_tax_country_codes_Set() const{
    return m_tax_country_codes_isSet;
}

bool OAIListTransactionsIn::is_tax_country_codes_Valid() const{
    return m_tax_country_codes_isValid;
}

QString OAIListTransactionsIn::getTotalAmountGreaterThan() const {
    return m_total_amount_greater_than;
}
void OAIListTransactionsIn::setTotalAmountGreaterThan(const QString &total_amount_greater_than) {
    m_total_amount_greater_than = total_amount_greater_than;
    m_total_amount_greater_than_isSet = true;
}

bool OAIListTransactionsIn::is_total_amount_greater_than_Set() const{
    return m_total_amount_greater_than_isSet;
}

bool OAIListTransactionsIn::is_total_amount_greater_than_Valid() const{
    return m_total_amount_greater_than_isValid;
}

QString OAIListTransactionsIn::getTotalAmountLessThan() const {
    return m_total_amount_less_than;
}
void OAIListTransactionsIn::setTotalAmountLessThan(const QString &total_amount_less_than) {
    m_total_amount_less_than = total_amount_less_than;
    m_total_amount_less_than_isSet = true;
}

bool OAIListTransactionsIn::is_total_amount_less_than_Set() const{
    return m_total_amount_less_than_isSet;
}

bool OAIListTransactionsIn::is_total_amount_less_than_Valid() const{
    return m_total_amount_less_than_isValid;
}

bool OAIListTransactionsIn::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_currency_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_filter_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_key_or_custom_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offset_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_date_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_date_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_original_transaction_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sort_reverse_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_statuses_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_country_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_country_codes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_amount_greater_than_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_amount_less_than_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListTransactionsIn::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
