/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPrice.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPrice::OAIPrice(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPrice::OAIPrice() {
    this->initializeModel();
}

OAIPrice::~OAIPrice() {}

void OAIPrice::initializeModel() {

    m_base_isSet = false;
    m_base_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_fees_isSet = false;
    m_fees_isValid = false;

    m_refundable_taxes_isSet = false;
    m_refundable_taxes_isValid = false;

    m_taxes_isSet = false;
    m_taxes_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;
}

void OAIPrice::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPrice::fromJsonObject(QJsonObject json) {

    m_base_isValid = ::OpenAPI::fromJsonValue(m_base, json[QString("base")]);
    m_base_isSet = !json[QString("base")].isNull() && m_base_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_fees_isValid = ::OpenAPI::fromJsonValue(m_fees, json[QString("fees")]);
    m_fees_isSet = !json[QString("fees")].isNull() && m_fees_isValid;

    m_refundable_taxes_isValid = ::OpenAPI::fromJsonValue(m_refundable_taxes, json[QString("refundableTaxes")]);
    m_refundable_taxes_isSet = !json[QString("refundableTaxes")].isNull() && m_refundable_taxes_isValid;

    m_taxes_isValid = ::OpenAPI::fromJsonValue(m_taxes, json[QString("taxes")]);
    m_taxes_isSet = !json[QString("taxes")].isNull() && m_taxes_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;
}

QString OAIPrice::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPrice::asJsonObject() const {
    QJsonObject obj;
    if (m_base_isSet) {
        obj.insert(QString("base"), ::OpenAPI::toJsonValue(m_base));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_fees.size() > 0) {
        obj.insert(QString("fees"), ::OpenAPI::toJsonValue(m_fees));
    }
    if (m_refundable_taxes_isSet) {
        obj.insert(QString("refundableTaxes"), ::OpenAPI::toJsonValue(m_refundable_taxes));
    }
    if (m_taxes.size() > 0) {
        obj.insert(QString("taxes"), ::OpenAPI::toJsonValue(m_taxes));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    return obj;
}

QString OAIPrice::getBase() const {
    return m_base;
}
void OAIPrice::setBase(const QString &base) {
    m_base = base;
    m_base_isSet = true;
}

bool OAIPrice::is_base_Set() const{
    return m_base_isSet;
}

bool OAIPrice::is_base_Valid() const{
    return m_base_isValid;
}

QString OAIPrice::getCurrency() const {
    return m_currency;
}
void OAIPrice::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIPrice::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIPrice::is_currency_Valid() const{
    return m_currency_isValid;
}

QList<OAIFee> OAIPrice::getFees() const {
    return m_fees;
}
void OAIPrice::setFees(const QList<OAIFee> &fees) {
    m_fees = fees;
    m_fees_isSet = true;
}

bool OAIPrice::is_fees_Set() const{
    return m_fees_isSet;
}

bool OAIPrice::is_fees_Valid() const{
    return m_fees_isValid;
}

QString OAIPrice::getRefundableTaxes() const {
    return m_refundable_taxes;
}
void OAIPrice::setRefundableTaxes(const QString &refundable_taxes) {
    m_refundable_taxes = refundable_taxes;
    m_refundable_taxes_isSet = true;
}

bool OAIPrice::is_refundable_taxes_Set() const{
    return m_refundable_taxes_isSet;
}

bool OAIPrice::is_refundable_taxes_Valid() const{
    return m_refundable_taxes_isValid;
}

QList<OAITax> OAIPrice::getTaxes() const {
    return m_taxes;
}
void OAIPrice::setTaxes(const QList<OAITax> &taxes) {
    m_taxes = taxes;
    m_taxes_isSet = true;
}

bool OAIPrice::is_taxes_Set() const{
    return m_taxes_isSet;
}

bool OAIPrice::is_taxes_Valid() const{
    return m_taxes_isValid;
}

QString OAIPrice::getTotal() const {
    return m_total;
}
void OAIPrice::setTotal(const QString &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIPrice::is_total_Set() const{
    return m_total_isSet;
}

bool OAIPrice::is_total_Valid() const{
    return m_total_isValid;
}

bool OAIPrice::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_base_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fees.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_refundable_taxes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_taxes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPrice::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
