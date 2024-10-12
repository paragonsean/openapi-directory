/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExtended_Price.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExtended_Price::OAIExtended_Price(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExtended_Price::OAIExtended_Price() {
    this->initializeModel();
}

OAIExtended_Price::~OAIExtended_Price() {}

void OAIExtended_Price::initializeModel() {

    m_base_isSet = false;
    m_base_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_fees_isSet = false;
    m_fees_isValid = false;

    m_taxes_isSet = false;
    m_taxes_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;

    m_additional_services_isSet = false;
    m_additional_services_isValid = false;

    m_billing_currency_isSet = false;
    m_billing_currency_isValid = false;

    m_grand_total_isSet = false;
    m_grand_total_isValid = false;

    m_margin_isSet = false;
    m_margin_isValid = false;
}

void OAIExtended_Price::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExtended_Price::fromJsonObject(QJsonObject json) {

    m_base_isValid = ::OpenAPI::fromJsonValue(m_base, json[QString("base")]);
    m_base_isSet = !json[QString("base")].isNull() && m_base_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_fees_isValid = ::OpenAPI::fromJsonValue(m_fees, json[QString("fees")]);
    m_fees_isSet = !json[QString("fees")].isNull() && m_fees_isValid;

    m_taxes_isValid = ::OpenAPI::fromJsonValue(m_taxes, json[QString("taxes")]);
    m_taxes_isSet = !json[QString("taxes")].isNull() && m_taxes_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;

    m_additional_services_isValid = ::OpenAPI::fromJsonValue(m_additional_services, json[QString("additionalServices")]);
    m_additional_services_isSet = !json[QString("additionalServices")].isNull() && m_additional_services_isValid;

    m_billing_currency_isValid = ::OpenAPI::fromJsonValue(m_billing_currency, json[QString("billingCurrency")]);
    m_billing_currency_isSet = !json[QString("billingCurrency")].isNull() && m_billing_currency_isValid;

    m_grand_total_isValid = ::OpenAPI::fromJsonValue(m_grand_total, json[QString("grandTotal")]);
    m_grand_total_isSet = !json[QString("grandTotal")].isNull() && m_grand_total_isValid;

    m_margin_isValid = ::OpenAPI::fromJsonValue(m_margin, json[QString("margin")]);
    m_margin_isSet = !json[QString("margin")].isNull() && m_margin_isValid;
}

QString OAIExtended_Price::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExtended_Price::asJsonObject() const {
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
    if (m_taxes.size() > 0) {
        obj.insert(QString("taxes"), ::OpenAPI::toJsonValue(m_taxes));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    if (m_additional_services.size() > 0) {
        obj.insert(QString("additionalServices"), ::OpenAPI::toJsonValue(m_additional_services));
    }
    if (m_billing_currency_isSet) {
        obj.insert(QString("billingCurrency"), ::OpenAPI::toJsonValue(m_billing_currency));
    }
    if (m_grand_total_isSet) {
        obj.insert(QString("grandTotal"), ::OpenAPI::toJsonValue(m_grand_total));
    }
    if (m_margin_isSet) {
        obj.insert(QString("margin"), ::OpenAPI::toJsonValue(m_margin));
    }
    return obj;
}

QString OAIExtended_Price::getBase() const {
    return m_base;
}
void OAIExtended_Price::setBase(const QString &base) {
    m_base = base;
    m_base_isSet = true;
}

bool OAIExtended_Price::is_base_Set() const{
    return m_base_isSet;
}

bool OAIExtended_Price::is_base_Valid() const{
    return m_base_isValid;
}

QString OAIExtended_Price::getCurrency() const {
    return m_currency;
}
void OAIExtended_Price::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIExtended_Price::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIExtended_Price::is_currency_Valid() const{
    return m_currency_isValid;
}

QList<OAIFee> OAIExtended_Price::getFees() const {
    return m_fees;
}
void OAIExtended_Price::setFees(const QList<OAIFee> &fees) {
    m_fees = fees;
    m_fees_isSet = true;
}

bool OAIExtended_Price::is_fees_Set() const{
    return m_fees_isSet;
}

bool OAIExtended_Price::is_fees_Valid() const{
    return m_fees_isValid;
}

QList<OAITax> OAIExtended_Price::getTaxes() const {
    return m_taxes;
}
void OAIExtended_Price::setTaxes(const QList<OAITax> &taxes) {
    m_taxes = taxes;
    m_taxes_isSet = true;
}

bool OAIExtended_Price::is_taxes_Set() const{
    return m_taxes_isSet;
}

bool OAIExtended_Price::is_taxes_Valid() const{
    return m_taxes_isValid;
}

QString OAIExtended_Price::getTotal() const {
    return m_total;
}
void OAIExtended_Price::setTotal(const QString &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIExtended_Price::is_total_Set() const{
    return m_total_isSet;
}

bool OAIExtended_Price::is_total_Valid() const{
    return m_total_isValid;
}

QList<OAIAdditionalService> OAIExtended_Price::getAdditionalServices() const {
    return m_additional_services;
}
void OAIExtended_Price::setAdditionalServices(const QList<OAIAdditionalService> &additional_services) {
    m_additional_services = additional_services;
    m_additional_services_isSet = true;
}

bool OAIExtended_Price::is_additional_services_Set() const{
    return m_additional_services_isSet;
}

bool OAIExtended_Price::is_additional_services_Valid() const{
    return m_additional_services_isValid;
}

QString OAIExtended_Price::getBillingCurrency() const {
    return m_billing_currency;
}
void OAIExtended_Price::setBillingCurrency(const QString &billing_currency) {
    m_billing_currency = billing_currency;
    m_billing_currency_isSet = true;
}

bool OAIExtended_Price::is_billing_currency_Set() const{
    return m_billing_currency_isSet;
}

bool OAIExtended_Price::is_billing_currency_Valid() const{
    return m_billing_currency_isValid;
}

QString OAIExtended_Price::getGrandTotal() const {
    return m_grand_total;
}
void OAIExtended_Price::setGrandTotal(const QString &grand_total) {
    m_grand_total = grand_total;
    m_grand_total_isSet = true;
}

bool OAIExtended_Price::is_grand_total_Set() const{
    return m_grand_total_isSet;
}

bool OAIExtended_Price::is_grand_total_Valid() const{
    return m_grand_total_isValid;
}

QString OAIExtended_Price::getMargin() const {
    return m_margin;
}
void OAIExtended_Price::setMargin(const QString &margin) {
    m_margin = margin;
    m_margin_isSet = true;
}

bool OAIExtended_Price::is_margin_Set() const{
    return m_margin_isSet;
}

bool OAIExtended_Price::is_margin_Valid() const{
    return m_margin_isValid;
}

bool OAIExtended_Price::isSet() const {
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

        if (m_taxes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_additional_services.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_grand_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_margin_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExtended_Price::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
