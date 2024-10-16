/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQuoteDetailVO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQuoteDetailVO::OAIQuoteDetailVO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQuoteDetailVO::OAIQuoteDetailVO() {
    this->initializeModel();
}

OAIQuoteDetailVO::~OAIQuoteDetailVO() {}

void OAIQuoteDetailVO::initializeModel() {

    m_client_isSet = false;
    m_client_isValid = false;

    m_client_user_id_isSet = false;
    m_client_user_id_isValid = false;

    m_comments_isSet = false;
    m_comments_isValid = false;

    m_creator_user_id_isSet = false;
    m_creator_user_id_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_grand_total_isSet = false;
    m_grand_total_isValid = false;

    m_is_show_supplier_information_isSet = false;
    m_is_show_supplier_information_isValid = false;

    m_last_update_by_user_id_isSet = false;
    m_last_update_by_user_id_isValid = false;

    m_proposed_order_completion_date_isSet = false;
    m_proposed_order_completion_date_isValid = false;

    m_quote_expiration_date_isSet = false;
    m_quote_expiration_date_isValid = false;

    m_quote_id_isSet = false;
    m_quote_id_isValid = false;

    m_quote_items_isSet = false;
    m_quote_items_isValid = false;

    m_quote_items_total_isSet = false;
    m_quote_items_total_isValid = false;

    m_quote_title_isSet = false;
    m_quote_title_isValid = false;

    m_shipping_isSet = false;
    m_shipping_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_submit_date_isSet = false;
    m_submit_date_isValid = false;

    m_tax_isSet = false;
    m_tax_isValid = false;

    m_transactional_currency_isSet = false;
    m_transactional_currency_isValid = false;

    m_transactional_grand_total_isSet = false;
    m_transactional_grand_total_isValid = false;

    m_transactional_quote_items_total_isSet = false;
    m_transactional_quote_items_total_isValid = false;

    m_transactional_shipping_isSet = false;
    m_transactional_shipping_isValid = false;

    m_transactional_tax_isSet = false;
    m_transactional_tax_isValid = false;

    m_vat_code_isSet = false;
    m_vat_code_isValid = false;

    m_vat_rate_isSet = false;
    m_vat_rate_isValid = false;
}

void OAIQuoteDetailVO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQuoteDetailVO::fromJsonObject(QJsonObject json) {

    m_client_isValid = ::OpenAPI::fromJsonValue(m_client, json[QString("client")]);
    m_client_isSet = !json[QString("client")].isNull() && m_client_isValid;

    m_client_user_id_isValid = ::OpenAPI::fromJsonValue(m_client_user_id, json[QString("client_user_id")]);
    m_client_user_id_isSet = !json[QString("client_user_id")].isNull() && m_client_user_id_isValid;

    m_comments_isValid = ::OpenAPI::fromJsonValue(m_comments, json[QString("comments")]);
    m_comments_isSet = !json[QString("comments")].isNull() && m_comments_isValid;

    m_creator_user_id_isValid = ::OpenAPI::fromJsonValue(m_creator_user_id, json[QString("creator_user_id")]);
    m_creator_user_id_isSet = !json[QString("creator_user_id")].isNull() && m_creator_user_id_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_grand_total_isValid = ::OpenAPI::fromJsonValue(m_grand_total, json[QString("grand_total")]);
    m_grand_total_isSet = !json[QString("grand_total")].isNull() && m_grand_total_isValid;

    m_is_show_supplier_information_isValid = ::OpenAPI::fromJsonValue(m_is_show_supplier_information, json[QString("is_show_supplier_information")]);
    m_is_show_supplier_information_isSet = !json[QString("is_show_supplier_information")].isNull() && m_is_show_supplier_information_isValid;

    m_last_update_by_user_id_isValid = ::OpenAPI::fromJsonValue(m_last_update_by_user_id, json[QString("last_update_by_user_id")]);
    m_last_update_by_user_id_isSet = !json[QString("last_update_by_user_id")].isNull() && m_last_update_by_user_id_isValid;

    m_proposed_order_completion_date_isValid = ::OpenAPI::fromJsonValue(m_proposed_order_completion_date, json[QString("proposed_order_completion_date")]);
    m_proposed_order_completion_date_isSet = !json[QString("proposed_order_completion_date")].isNull() && m_proposed_order_completion_date_isValid;

    m_quote_expiration_date_isValid = ::OpenAPI::fromJsonValue(m_quote_expiration_date, json[QString("quote_expiration_date")]);
    m_quote_expiration_date_isSet = !json[QString("quote_expiration_date")].isNull() && m_quote_expiration_date_isValid;

    m_quote_id_isValid = ::OpenAPI::fromJsonValue(m_quote_id, json[QString("quote_id")]);
    m_quote_id_isSet = !json[QString("quote_id")].isNull() && m_quote_id_isValid;

    m_quote_items_isValid = ::OpenAPI::fromJsonValue(m_quote_items, json[QString("quote_items")]);
    m_quote_items_isSet = !json[QString("quote_items")].isNull() && m_quote_items_isValid;

    m_quote_items_total_isValid = ::OpenAPI::fromJsonValue(m_quote_items_total, json[QString("quote_items_total")]);
    m_quote_items_total_isSet = !json[QString("quote_items_total")].isNull() && m_quote_items_total_isValid;

    m_quote_title_isValid = ::OpenAPI::fromJsonValue(m_quote_title, json[QString("quote_title")]);
    m_quote_title_isSet = !json[QString("quote_title")].isNull() && m_quote_title_isValid;

    m_shipping_isValid = ::OpenAPI::fromJsonValue(m_shipping, json[QString("shipping")]);
    m_shipping_isSet = !json[QString("shipping")].isNull() && m_shipping_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_submit_date_isValid = ::OpenAPI::fromJsonValue(m_submit_date, json[QString("submit_date")]);
    m_submit_date_isSet = !json[QString("submit_date")].isNull() && m_submit_date_isValid;

    m_tax_isValid = ::OpenAPI::fromJsonValue(m_tax, json[QString("tax")]);
    m_tax_isSet = !json[QString("tax")].isNull() && m_tax_isValid;

    m_transactional_currency_isValid = ::OpenAPI::fromJsonValue(m_transactional_currency, json[QString("transactional_currency")]);
    m_transactional_currency_isSet = !json[QString("transactional_currency")].isNull() && m_transactional_currency_isValid;

    m_transactional_grand_total_isValid = ::OpenAPI::fromJsonValue(m_transactional_grand_total, json[QString("transactional_grand_total")]);
    m_transactional_grand_total_isSet = !json[QString("transactional_grand_total")].isNull() && m_transactional_grand_total_isValid;

    m_transactional_quote_items_total_isValid = ::OpenAPI::fromJsonValue(m_transactional_quote_items_total, json[QString("transactional_quote_items_total")]);
    m_transactional_quote_items_total_isSet = !json[QString("transactional_quote_items_total")].isNull() && m_transactional_quote_items_total_isValid;

    m_transactional_shipping_isValid = ::OpenAPI::fromJsonValue(m_transactional_shipping, json[QString("transactional_shipping")]);
    m_transactional_shipping_isSet = !json[QString("transactional_shipping")].isNull() && m_transactional_shipping_isValid;

    m_transactional_tax_isValid = ::OpenAPI::fromJsonValue(m_transactional_tax, json[QString("transactional_tax")]);
    m_transactional_tax_isSet = !json[QString("transactional_tax")].isNull() && m_transactional_tax_isValid;

    m_vat_code_isValid = ::OpenAPI::fromJsonValue(m_vat_code, json[QString("vat_code")]);
    m_vat_code_isSet = !json[QString("vat_code")].isNull() && m_vat_code_isValid;

    m_vat_rate_isValid = ::OpenAPI::fromJsonValue(m_vat_rate, json[QString("vat_rate")]);
    m_vat_rate_isSet = !json[QString("vat_rate")].isNull() && m_vat_rate_isValid;
}

QString OAIQuoteDetailVO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQuoteDetailVO::asJsonObject() const {
    QJsonObject obj;
    if (m_client_isSet) {
        obj.insert(QString("client"), ::OpenAPI::toJsonValue(m_client));
    }
    if (m_client_user_id_isSet) {
        obj.insert(QString("client_user_id"), ::OpenAPI::toJsonValue(m_client_user_id));
    }
    if (m_comments_isSet) {
        obj.insert(QString("comments"), ::OpenAPI::toJsonValue(m_comments));
    }
    if (m_creator_user_id_isSet) {
        obj.insert(QString("creator_user_id"), ::OpenAPI::toJsonValue(m_creator_user_id));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_custom_fields.size() > 0) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_grand_total_isSet) {
        obj.insert(QString("grand_total"), ::OpenAPI::toJsonValue(m_grand_total));
    }
    if (m_is_show_supplier_information_isSet) {
        obj.insert(QString("is_show_supplier_information"), ::OpenAPI::toJsonValue(m_is_show_supplier_information));
    }
    if (m_last_update_by_user_id_isSet) {
        obj.insert(QString("last_update_by_user_id"), ::OpenAPI::toJsonValue(m_last_update_by_user_id));
    }
    if (m_proposed_order_completion_date_isSet) {
        obj.insert(QString("proposed_order_completion_date"), ::OpenAPI::toJsonValue(m_proposed_order_completion_date));
    }
    if (m_quote_expiration_date_isSet) {
        obj.insert(QString("quote_expiration_date"), ::OpenAPI::toJsonValue(m_quote_expiration_date));
    }
    if (m_quote_id_isSet) {
        obj.insert(QString("quote_id"), ::OpenAPI::toJsonValue(m_quote_id));
    }
    if (m_quote_items.size() > 0) {
        obj.insert(QString("quote_items"), ::OpenAPI::toJsonValue(m_quote_items));
    }
    if (m_quote_items_total_isSet) {
        obj.insert(QString("quote_items_total"), ::OpenAPI::toJsonValue(m_quote_items_total));
    }
    if (m_quote_title_isSet) {
        obj.insert(QString("quote_title"), ::OpenAPI::toJsonValue(m_quote_title));
    }
    if (m_shipping_isSet) {
        obj.insert(QString("shipping"), ::OpenAPI::toJsonValue(m_shipping));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_submit_date_isSet) {
        obj.insert(QString("submit_date"), ::OpenAPI::toJsonValue(m_submit_date));
    }
    if (m_tax_isSet) {
        obj.insert(QString("tax"), ::OpenAPI::toJsonValue(m_tax));
    }
    if (m_transactional_currency_isSet) {
        obj.insert(QString("transactional_currency"), ::OpenAPI::toJsonValue(m_transactional_currency));
    }
    if (m_transactional_grand_total_isSet) {
        obj.insert(QString("transactional_grand_total"), ::OpenAPI::toJsonValue(m_transactional_grand_total));
    }
    if (m_transactional_quote_items_total_isSet) {
        obj.insert(QString("transactional_quote_items_total"), ::OpenAPI::toJsonValue(m_transactional_quote_items_total));
    }
    if (m_transactional_shipping_isSet) {
        obj.insert(QString("transactional_shipping"), ::OpenAPI::toJsonValue(m_transactional_shipping));
    }
    if (m_transactional_tax_isSet) {
        obj.insert(QString("transactional_tax"), ::OpenAPI::toJsonValue(m_transactional_tax));
    }
    if (m_vat_code_isSet) {
        obj.insert(QString("vat_code"), ::OpenAPI::toJsonValue(m_vat_code));
    }
    if (m_vat_rate_isSet) {
        obj.insert(QString("vat_rate"), ::OpenAPI::toJsonValue(m_vat_rate));
    }
    return obj;
}

QString OAIQuoteDetailVO::getClient() const {
    return m_client;
}
void OAIQuoteDetailVO::setClient(const QString &client) {
    m_client = client;
    m_client_isSet = true;
}

bool OAIQuoteDetailVO::is_client_Set() const{
    return m_client_isSet;
}

bool OAIQuoteDetailVO::is_client_Valid() const{
    return m_client_isValid;
}

qint64 OAIQuoteDetailVO::getClientUserId() const {
    return m_client_user_id;
}
void OAIQuoteDetailVO::setClientUserId(const qint64 &client_user_id) {
    m_client_user_id = client_user_id;
    m_client_user_id_isSet = true;
}

bool OAIQuoteDetailVO::is_client_user_id_Set() const{
    return m_client_user_id_isSet;
}

bool OAIQuoteDetailVO::is_client_user_id_Valid() const{
    return m_client_user_id_isValid;
}

QString OAIQuoteDetailVO::getComments() const {
    return m_comments;
}
void OAIQuoteDetailVO::setComments(const QString &comments) {
    m_comments = comments;
    m_comments_isSet = true;
}

bool OAIQuoteDetailVO::is_comments_Set() const{
    return m_comments_isSet;
}

bool OAIQuoteDetailVO::is_comments_Valid() const{
    return m_comments_isValid;
}

qint64 OAIQuoteDetailVO::getCreatorUserId() const {
    return m_creator_user_id;
}
void OAIQuoteDetailVO::setCreatorUserId(const qint64 &creator_user_id) {
    m_creator_user_id = creator_user_id;
    m_creator_user_id_isSet = true;
}

bool OAIQuoteDetailVO::is_creator_user_id_Set() const{
    return m_creator_user_id_isSet;
}

bool OAIQuoteDetailVO::is_creator_user_id_Valid() const{
    return m_creator_user_id_isValid;
}

QString OAIQuoteDetailVO::getCurrency() const {
    return m_currency;
}
void OAIQuoteDetailVO::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIQuoteDetailVO::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIQuoteDetailVO::is_currency_Valid() const{
    return m_currency_isValid;
}

QList<OAIPropertyPaAndAttVO> OAIQuoteDetailVO::getCustomFields() const {
    return m_custom_fields;
}
void OAIQuoteDetailVO::setCustomFields(const QList<OAIPropertyPaAndAttVO> &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIQuoteDetailVO::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIQuoteDetailVO::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAIQuoteDetailVO::getDescription() const {
    return m_description;
}
void OAIQuoteDetailVO::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIQuoteDetailVO::is_description_Set() const{
    return m_description_isSet;
}

bool OAIQuoteDetailVO::is_description_Valid() const{
    return m_description_isValid;
}

QJsonValue OAIQuoteDetailVO::getGrandTotal() const {
    return m_grand_total;
}
void OAIQuoteDetailVO::setGrandTotal(const QJsonValue &grand_total) {
    m_grand_total = grand_total;
    m_grand_total_isSet = true;
}

bool OAIQuoteDetailVO::is_grand_total_Set() const{
    return m_grand_total_isSet;
}

bool OAIQuoteDetailVO::is_grand_total_Valid() const{
    return m_grand_total_isValid;
}

bool OAIQuoteDetailVO::isIsShowSupplierInformation() const {
    return m_is_show_supplier_information;
}
void OAIQuoteDetailVO::setIsShowSupplierInformation(const bool &is_show_supplier_information) {
    m_is_show_supplier_information = is_show_supplier_information;
    m_is_show_supplier_information_isSet = true;
}

bool OAIQuoteDetailVO::is_is_show_supplier_information_Set() const{
    return m_is_show_supplier_information_isSet;
}

bool OAIQuoteDetailVO::is_is_show_supplier_information_Valid() const{
    return m_is_show_supplier_information_isValid;
}

qint64 OAIQuoteDetailVO::getLastUpdateByUserId() const {
    return m_last_update_by_user_id;
}
void OAIQuoteDetailVO::setLastUpdateByUserId(const qint64 &last_update_by_user_id) {
    m_last_update_by_user_id = last_update_by_user_id;
    m_last_update_by_user_id_isSet = true;
}

bool OAIQuoteDetailVO::is_last_update_by_user_id_Set() const{
    return m_last_update_by_user_id_isSet;
}

bool OAIQuoteDetailVO::is_last_update_by_user_id_Valid() const{
    return m_last_update_by_user_id_isValid;
}

QDate OAIQuoteDetailVO::getProposedOrderCompletionDate() const {
    return m_proposed_order_completion_date;
}
void OAIQuoteDetailVO::setProposedOrderCompletionDate(const QDate &proposed_order_completion_date) {
    m_proposed_order_completion_date = proposed_order_completion_date;
    m_proposed_order_completion_date_isSet = true;
}

bool OAIQuoteDetailVO::is_proposed_order_completion_date_Set() const{
    return m_proposed_order_completion_date_isSet;
}

bool OAIQuoteDetailVO::is_proposed_order_completion_date_Valid() const{
    return m_proposed_order_completion_date_isValid;
}

QDate OAIQuoteDetailVO::getQuoteExpirationDate() const {
    return m_quote_expiration_date;
}
void OAIQuoteDetailVO::setQuoteExpirationDate(const QDate &quote_expiration_date) {
    m_quote_expiration_date = quote_expiration_date;
    m_quote_expiration_date_isSet = true;
}

bool OAIQuoteDetailVO::is_quote_expiration_date_Set() const{
    return m_quote_expiration_date_isSet;
}

bool OAIQuoteDetailVO::is_quote_expiration_date_Valid() const{
    return m_quote_expiration_date_isValid;
}

qint64 OAIQuoteDetailVO::getQuoteId() const {
    return m_quote_id;
}
void OAIQuoteDetailVO::setQuoteId(const qint64 &quote_id) {
    m_quote_id = quote_id;
    m_quote_id_isSet = true;
}

bool OAIQuoteDetailVO::is_quote_id_Set() const{
    return m_quote_id_isSet;
}

bool OAIQuoteDetailVO::is_quote_id_Valid() const{
    return m_quote_id_isValid;
}

QList<OAIQuoteItemDetailVO> OAIQuoteDetailVO::getQuoteItems() const {
    return m_quote_items;
}
void OAIQuoteDetailVO::setQuoteItems(const QList<OAIQuoteItemDetailVO> &quote_items) {
    m_quote_items = quote_items;
    m_quote_items_isSet = true;
}

bool OAIQuoteDetailVO::is_quote_items_Set() const{
    return m_quote_items_isSet;
}

bool OAIQuoteDetailVO::is_quote_items_Valid() const{
    return m_quote_items_isValid;
}

QJsonValue OAIQuoteDetailVO::getQuoteItemsTotal() const {
    return m_quote_items_total;
}
void OAIQuoteDetailVO::setQuoteItemsTotal(const QJsonValue &quote_items_total) {
    m_quote_items_total = quote_items_total;
    m_quote_items_total_isSet = true;
}

bool OAIQuoteDetailVO::is_quote_items_total_Set() const{
    return m_quote_items_total_isSet;
}

bool OAIQuoteDetailVO::is_quote_items_total_Valid() const{
    return m_quote_items_total_isValid;
}

QString OAIQuoteDetailVO::getQuoteTitle() const {
    return m_quote_title;
}
void OAIQuoteDetailVO::setQuoteTitle(const QString &quote_title) {
    m_quote_title = quote_title;
    m_quote_title_isSet = true;
}

bool OAIQuoteDetailVO::is_quote_title_Set() const{
    return m_quote_title_isSet;
}

bool OAIQuoteDetailVO::is_quote_title_Valid() const{
    return m_quote_title_isValid;
}

QJsonValue OAIQuoteDetailVO::getShipping() const {
    return m_shipping;
}
void OAIQuoteDetailVO::setShipping(const QJsonValue &shipping) {
    m_shipping = shipping;
    m_shipping_isSet = true;
}

bool OAIQuoteDetailVO::is_shipping_Set() const{
    return m_shipping_isSet;
}

bool OAIQuoteDetailVO::is_shipping_Valid() const{
    return m_shipping_isValid;
}

QString OAIQuoteDetailVO::getStatus() const {
    return m_status;
}
void OAIQuoteDetailVO::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIQuoteDetailVO::is_status_Set() const{
    return m_status_isSet;
}

bool OAIQuoteDetailVO::is_status_Valid() const{
    return m_status_isValid;
}

QDate OAIQuoteDetailVO::getSubmitDate() const {
    return m_submit_date;
}
void OAIQuoteDetailVO::setSubmitDate(const QDate &submit_date) {
    m_submit_date = submit_date;
    m_submit_date_isSet = true;
}

bool OAIQuoteDetailVO::is_submit_date_Set() const{
    return m_submit_date_isSet;
}

bool OAIQuoteDetailVO::is_submit_date_Valid() const{
    return m_submit_date_isValid;
}

QJsonValue OAIQuoteDetailVO::getTax() const {
    return m_tax;
}
void OAIQuoteDetailVO::setTax(const QJsonValue &tax) {
    m_tax = tax;
    m_tax_isSet = true;
}

bool OAIQuoteDetailVO::is_tax_Set() const{
    return m_tax_isSet;
}

bool OAIQuoteDetailVO::is_tax_Valid() const{
    return m_tax_isValid;
}

QString OAIQuoteDetailVO::getTransactionalCurrency() const {
    return m_transactional_currency;
}
void OAIQuoteDetailVO::setTransactionalCurrency(const QString &transactional_currency) {
    m_transactional_currency = transactional_currency;
    m_transactional_currency_isSet = true;
}

bool OAIQuoteDetailVO::is_transactional_currency_Set() const{
    return m_transactional_currency_isSet;
}

bool OAIQuoteDetailVO::is_transactional_currency_Valid() const{
    return m_transactional_currency_isValid;
}

QJsonValue OAIQuoteDetailVO::getTransactionalGrandTotal() const {
    return m_transactional_grand_total;
}
void OAIQuoteDetailVO::setTransactionalGrandTotal(const QJsonValue &transactional_grand_total) {
    m_transactional_grand_total = transactional_grand_total;
    m_transactional_grand_total_isSet = true;
}

bool OAIQuoteDetailVO::is_transactional_grand_total_Set() const{
    return m_transactional_grand_total_isSet;
}

bool OAIQuoteDetailVO::is_transactional_grand_total_Valid() const{
    return m_transactional_grand_total_isValid;
}

QJsonValue OAIQuoteDetailVO::getTransactionalQuoteItemsTotal() const {
    return m_transactional_quote_items_total;
}
void OAIQuoteDetailVO::setTransactionalQuoteItemsTotal(const QJsonValue &transactional_quote_items_total) {
    m_transactional_quote_items_total = transactional_quote_items_total;
    m_transactional_quote_items_total_isSet = true;
}

bool OAIQuoteDetailVO::is_transactional_quote_items_total_Set() const{
    return m_transactional_quote_items_total_isSet;
}

bool OAIQuoteDetailVO::is_transactional_quote_items_total_Valid() const{
    return m_transactional_quote_items_total_isValid;
}

QJsonValue OAIQuoteDetailVO::getTransactionalShipping() const {
    return m_transactional_shipping;
}
void OAIQuoteDetailVO::setTransactionalShipping(const QJsonValue &transactional_shipping) {
    m_transactional_shipping = transactional_shipping;
    m_transactional_shipping_isSet = true;
}

bool OAIQuoteDetailVO::is_transactional_shipping_Set() const{
    return m_transactional_shipping_isSet;
}

bool OAIQuoteDetailVO::is_transactional_shipping_Valid() const{
    return m_transactional_shipping_isValid;
}

QJsonValue OAIQuoteDetailVO::getTransactionalTax() const {
    return m_transactional_tax;
}
void OAIQuoteDetailVO::setTransactionalTax(const QJsonValue &transactional_tax) {
    m_transactional_tax = transactional_tax;
    m_transactional_tax_isSet = true;
}

bool OAIQuoteDetailVO::is_transactional_tax_Set() const{
    return m_transactional_tax_isSet;
}

bool OAIQuoteDetailVO::is_transactional_tax_Valid() const{
    return m_transactional_tax_isValid;
}

QString OAIQuoteDetailVO::getVatCode() const {
    return m_vat_code;
}
void OAIQuoteDetailVO::setVatCode(const QString &vat_code) {
    m_vat_code = vat_code;
    m_vat_code_isSet = true;
}

bool OAIQuoteDetailVO::is_vat_code_Set() const{
    return m_vat_code_isSet;
}

bool OAIQuoteDetailVO::is_vat_code_Valid() const{
    return m_vat_code_isValid;
}

QJsonValue OAIQuoteDetailVO::getVatRate() const {
    return m_vat_rate;
}
void OAIQuoteDetailVO::setVatRate(const QJsonValue &vat_rate) {
    m_vat_rate = vat_rate;
    m_vat_rate_isSet = true;
}

bool OAIQuoteDetailVO::is_vat_rate_Set() const{
    return m_vat_rate_isSet;
}

bool OAIQuoteDetailVO::is_vat_rate_Valid() const{
    return m_vat_rate_isValid;
}

bool OAIQuoteDetailVO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_creator_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_grand_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_show_supplier_information_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_update_by_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_proposed_order_completion_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quote_expiration_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quote_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quote_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_quote_items_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quote_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_submit_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transactional_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transactional_grand_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transactional_quote_items_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transactional_shipping_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transactional_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_rate_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQuoteDetailVO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
