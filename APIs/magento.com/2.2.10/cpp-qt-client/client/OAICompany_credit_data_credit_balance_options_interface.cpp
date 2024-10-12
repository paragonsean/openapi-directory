/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICompany_credit_data_credit_balance_options_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICompany_credit_data_credit_balance_options_interface::OAICompany_credit_data_credit_balance_options_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICompany_credit_data_credit_balance_options_interface::OAICompany_credit_data_credit_balance_options_interface() {
    this->initializeModel();
}

OAICompany_credit_data_credit_balance_options_interface::~OAICompany_credit_data_credit_balance_options_interface() {}

void OAICompany_credit_data_credit_balance_options_interface::initializeModel() {

    m_currency_base_isSet = false;
    m_currency_base_isValid = false;

    m_currency_display_isSet = false;
    m_currency_display_isValid = false;

    m_order_increment_isSet = false;
    m_order_increment_isValid = false;

    m_purchase_order_isSet = false;
    m_purchase_order_isValid = false;
}

void OAICompany_credit_data_credit_balance_options_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICompany_credit_data_credit_balance_options_interface::fromJsonObject(QJsonObject json) {

    m_currency_base_isValid = ::OpenAPI::fromJsonValue(m_currency_base, json[QString("currency_base")]);
    m_currency_base_isSet = !json[QString("currency_base")].isNull() && m_currency_base_isValid;

    m_currency_display_isValid = ::OpenAPI::fromJsonValue(m_currency_display, json[QString("currency_display")]);
    m_currency_display_isSet = !json[QString("currency_display")].isNull() && m_currency_display_isValid;

    m_order_increment_isValid = ::OpenAPI::fromJsonValue(m_order_increment, json[QString("order_increment")]);
    m_order_increment_isSet = !json[QString("order_increment")].isNull() && m_order_increment_isValid;

    m_purchase_order_isValid = ::OpenAPI::fromJsonValue(m_purchase_order, json[QString("purchase_order")]);
    m_purchase_order_isSet = !json[QString("purchase_order")].isNull() && m_purchase_order_isValid;
}

QString OAICompany_credit_data_credit_balance_options_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICompany_credit_data_credit_balance_options_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_currency_base_isSet) {
        obj.insert(QString("currency_base"), ::OpenAPI::toJsonValue(m_currency_base));
    }
    if (m_currency_display_isSet) {
        obj.insert(QString("currency_display"), ::OpenAPI::toJsonValue(m_currency_display));
    }
    if (m_order_increment_isSet) {
        obj.insert(QString("order_increment"), ::OpenAPI::toJsonValue(m_order_increment));
    }
    if (m_purchase_order_isSet) {
        obj.insert(QString("purchase_order"), ::OpenAPI::toJsonValue(m_purchase_order));
    }
    return obj;
}

QString OAICompany_credit_data_credit_balance_options_interface::getCurrencyBase() const {
    return m_currency_base;
}
void OAICompany_credit_data_credit_balance_options_interface::setCurrencyBase(const QString &currency_base) {
    m_currency_base = currency_base;
    m_currency_base_isSet = true;
}

bool OAICompany_credit_data_credit_balance_options_interface::is_currency_base_Set() const{
    return m_currency_base_isSet;
}

bool OAICompany_credit_data_credit_balance_options_interface::is_currency_base_Valid() const{
    return m_currency_base_isValid;
}

QString OAICompany_credit_data_credit_balance_options_interface::getCurrencyDisplay() const {
    return m_currency_display;
}
void OAICompany_credit_data_credit_balance_options_interface::setCurrencyDisplay(const QString &currency_display) {
    m_currency_display = currency_display;
    m_currency_display_isSet = true;
}

bool OAICompany_credit_data_credit_balance_options_interface::is_currency_display_Set() const{
    return m_currency_display_isSet;
}

bool OAICompany_credit_data_credit_balance_options_interface::is_currency_display_Valid() const{
    return m_currency_display_isValid;
}

QString OAICompany_credit_data_credit_balance_options_interface::getOrderIncrement() const {
    return m_order_increment;
}
void OAICompany_credit_data_credit_balance_options_interface::setOrderIncrement(const QString &order_increment) {
    m_order_increment = order_increment;
    m_order_increment_isSet = true;
}

bool OAICompany_credit_data_credit_balance_options_interface::is_order_increment_Set() const{
    return m_order_increment_isSet;
}

bool OAICompany_credit_data_credit_balance_options_interface::is_order_increment_Valid() const{
    return m_order_increment_isValid;
}

QString OAICompany_credit_data_credit_balance_options_interface::getPurchaseOrder() const {
    return m_purchase_order;
}
void OAICompany_credit_data_credit_balance_options_interface::setPurchaseOrder(const QString &purchase_order) {
    m_purchase_order = purchase_order;
    m_purchase_order_isSet = true;
}

bool OAICompany_credit_data_credit_balance_options_interface::is_purchase_order_Set() const{
    return m_purchase_order_isSet;
}

bool OAICompany_credit_data_credit_balance_options_interface::is_purchase_order_Valid() const{
    return m_purchase_order_isValid;
}

bool OAICompany_credit_data_credit_balance_options_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_currency_base_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_display_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_increment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_purchase_order_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICompany_credit_data_credit_balance_options_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_currency_base_isValid && m_currency_display_isValid && m_order_increment_isValid && m_purchase_order_isValid && true;
}

} // namespace OpenAPI
