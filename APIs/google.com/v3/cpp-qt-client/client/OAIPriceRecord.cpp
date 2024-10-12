/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPriceRecord.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPriceRecord::OAIPriceRecord(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPriceRecord::OAIPriceRecord() {
    this->initializeModel();
}

OAIPriceRecord::~OAIPriceRecord() {}

void OAIPriceRecord::initializeModel() {

    m_base_price_isSet = false;
    m_base_price_isValid = false;

    m_currency_code_isSet = false;
    m_currency_code_isValid = false;

    m_taxes_and_fees_isSet = false;
    m_taxes_and_fees_isValid = false;

    m_time_isSet = false;
    m_time_isValid = false;
}

void OAIPriceRecord::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPriceRecord::fromJsonObject(QJsonObject json) {

    m_base_price_isValid = ::OpenAPI::fromJsonValue(m_base_price, json[QString("basePrice")]);
    m_base_price_isSet = !json[QString("basePrice")].isNull() && m_base_price_isValid;

    m_currency_code_isValid = ::OpenAPI::fromJsonValue(m_currency_code, json[QString("currencyCode")]);
    m_currency_code_isSet = !json[QString("currencyCode")].isNull() && m_currency_code_isValid;

    m_taxes_and_fees_isValid = ::OpenAPI::fromJsonValue(m_taxes_and_fees, json[QString("taxesAndFees")]);
    m_taxes_and_fees_isSet = !json[QString("taxesAndFees")].isNull() && m_taxes_and_fees_isValid;

    m_time_isValid = ::OpenAPI::fromJsonValue(m_time, json[QString("time")]);
    m_time_isSet = !json[QString("time")].isNull() && m_time_isValid;
}

QString OAIPriceRecord::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPriceRecord::asJsonObject() const {
    QJsonObject obj;
    if (m_base_price_isSet) {
        obj.insert(QString("basePrice"), ::OpenAPI::toJsonValue(m_base_price));
    }
    if (m_currency_code_isSet) {
        obj.insert(QString("currencyCode"), ::OpenAPI::toJsonValue(m_currency_code));
    }
    if (m_taxes_and_fees_isSet) {
        obj.insert(QString("taxesAndFees"), ::OpenAPI::toJsonValue(m_taxes_and_fees));
    }
    if (m_time_isSet) {
        obj.insert(QString("time"), ::OpenAPI::toJsonValue(m_time));
    }
    return obj;
}

float OAIPriceRecord::getBasePrice() const {
    return m_base_price;
}
void OAIPriceRecord::setBasePrice(const float &base_price) {
    m_base_price = base_price;
    m_base_price_isSet = true;
}

bool OAIPriceRecord::is_base_price_Set() const{
    return m_base_price_isSet;
}

bool OAIPriceRecord::is_base_price_Valid() const{
    return m_base_price_isValid;
}

QString OAIPriceRecord::getCurrencyCode() const {
    return m_currency_code;
}
void OAIPriceRecord::setCurrencyCode(const QString &currency_code) {
    m_currency_code = currency_code;
    m_currency_code_isSet = true;
}

bool OAIPriceRecord::is_currency_code_Set() const{
    return m_currency_code_isSet;
}

bool OAIPriceRecord::is_currency_code_Valid() const{
    return m_currency_code_isValid;
}

float OAIPriceRecord::getTaxesAndFees() const {
    return m_taxes_and_fees;
}
void OAIPriceRecord::setTaxesAndFees(const float &taxes_and_fees) {
    m_taxes_and_fees = taxes_and_fees;
    m_taxes_and_fees_isSet = true;
}

bool OAIPriceRecord::is_taxes_and_fees_Set() const{
    return m_taxes_and_fees_isSet;
}

bool OAIPriceRecord::is_taxes_and_fees_Valid() const{
    return m_taxes_and_fees_isValid;
}

QString OAIPriceRecord::getTime() const {
    return m_time;
}
void OAIPriceRecord::setTime(const QString &time) {
    m_time = time;
    m_time_isSet = true;
}

bool OAIPriceRecord::is_time_Set() const{
    return m_time_isSet;
}

bool OAIPriceRecord::is_time_Valid() const{
    return m_time_isValid;
}

bool OAIPriceRecord::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_base_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_taxes_and_fees_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPriceRecord::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
