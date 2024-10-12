/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHotelProduct_PriceVariation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHotelProduct_PriceVariation::OAIHotelProduct_PriceVariation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHotelProduct_PriceVariation::OAIHotelProduct_PriceVariation() {
    this->initializeModel();
}

OAIHotelProduct_PriceVariation::~OAIHotelProduct_PriceVariation() {}

void OAIHotelProduct_PriceVariation::initializeModel() {

    m_base_isSet = false;
    m_base_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_markups_isSet = false;
    m_markups_isValid = false;

    m_selling_total_isSet = false;
    m_selling_total_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;
}

void OAIHotelProduct_PriceVariation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHotelProduct_PriceVariation::fromJsonObject(QJsonObject json) {

    m_base_isValid = ::OpenAPI::fromJsonValue(m_base, json[QString("base")]);
    m_base_isSet = !json[QString("base")].isNull() && m_base_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("endDate")]);
    m_end_date_isSet = !json[QString("endDate")].isNull() && m_end_date_isValid;

    m_markups_isValid = ::OpenAPI::fromJsonValue(m_markups, json[QString("markups")]);
    m_markups_isSet = !json[QString("markups")].isNull() && m_markups_isValid;

    m_selling_total_isValid = ::OpenAPI::fromJsonValue(m_selling_total, json[QString("sellingTotal")]);
    m_selling_total_isSet = !json[QString("sellingTotal")].isNull() && m_selling_total_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("startDate")]);
    m_start_date_isSet = !json[QString("startDate")].isNull() && m_start_date_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;
}

QString OAIHotelProduct_PriceVariation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHotelProduct_PriceVariation::asJsonObject() const {
    QJsonObject obj;
    if (m_base_isSet) {
        obj.insert(QString("base"), ::OpenAPI::toJsonValue(m_base));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("endDate"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_markups.size() > 0) {
        obj.insert(QString("markups"), ::OpenAPI::toJsonValue(m_markups));
    }
    if (m_selling_total_isSet) {
        obj.insert(QString("sellingTotal"), ::OpenAPI::toJsonValue(m_selling_total));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("startDate"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    return obj;
}

QString OAIHotelProduct_PriceVariation::getBase() const {
    return m_base;
}
void OAIHotelProduct_PriceVariation::setBase(const QString &base) {
    m_base = base;
    m_base_isSet = true;
}

bool OAIHotelProduct_PriceVariation::is_base_Set() const{
    return m_base_isSet;
}

bool OAIHotelProduct_PriceVariation::is_base_Valid() const{
    return m_base_isValid;
}

QString OAIHotelProduct_PriceVariation::getCurrency() const {
    return m_currency;
}
void OAIHotelProduct_PriceVariation::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIHotelProduct_PriceVariation::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIHotelProduct_PriceVariation::is_currency_Valid() const{
    return m_currency_isValid;
}

QDate OAIHotelProduct_PriceVariation::getEndDate() const {
    return m_end_date;
}
void OAIHotelProduct_PriceVariation::setEndDate(const QDate &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIHotelProduct_PriceVariation::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIHotelProduct_PriceVariation::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QList<OAIMarkup> OAIHotelProduct_PriceVariation::getMarkups() const {
    return m_markups;
}
void OAIHotelProduct_PriceVariation::setMarkups(const QList<OAIMarkup> &markups) {
    m_markups = markups;
    m_markups_isSet = true;
}

bool OAIHotelProduct_PriceVariation::is_markups_Set() const{
    return m_markups_isSet;
}

bool OAIHotelProduct_PriceVariation::is_markups_Valid() const{
    return m_markups_isValid;
}

QString OAIHotelProduct_PriceVariation::getSellingTotal() const {
    return m_selling_total;
}
void OAIHotelProduct_PriceVariation::setSellingTotal(const QString &selling_total) {
    m_selling_total = selling_total;
    m_selling_total_isSet = true;
}

bool OAIHotelProduct_PriceVariation::is_selling_total_Set() const{
    return m_selling_total_isSet;
}

bool OAIHotelProduct_PriceVariation::is_selling_total_Valid() const{
    return m_selling_total_isValid;
}

QDate OAIHotelProduct_PriceVariation::getStartDate() const {
    return m_start_date;
}
void OAIHotelProduct_PriceVariation::setStartDate(const QDate &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIHotelProduct_PriceVariation::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIHotelProduct_PriceVariation::is_start_date_Valid() const{
    return m_start_date_isValid;
}

QString OAIHotelProduct_PriceVariation::getTotal() const {
    return m_total;
}
void OAIHotelProduct_PriceVariation::setTotal(const QString &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIHotelProduct_PriceVariation::is_total_Set() const{
    return m_total_isSet;
}

bool OAIHotelProduct_PriceVariation::is_total_Valid() const{
    return m_total_isValid;
}

bool OAIHotelProduct_PriceVariation::isSet() const {
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

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_markups.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_selling_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
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

bool OAIHotelProduct_PriceVariation::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_end_date_isValid && m_start_date_isValid && true;
}

} // namespace OpenAPI
