/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArticle_Price.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArticle_Price::OAIArticle_Price(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArticle_Price::OAIArticle_Price() {
    this->initializeModel();
}

OAIArticle_Price::~OAIArticle_Price() {}

void OAIArticle_Price::initializeModel() {

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_formatted_isSet = false;
    m_formatted_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIArticle_Price::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArticle_Price::fromJsonObject(QJsonObject json) {

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_formatted_isValid = ::OpenAPI::fromJsonValue(m_formatted, json[QString("formatted")]);
    m_formatted_isSet = !json[QString("formatted")].isNull() && m_formatted_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIArticle_Price::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArticle_Price::asJsonObject() const {
    QJsonObject obj;
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_formatted_isSet) {
        obj.insert(QString("formatted"), ::OpenAPI::toJsonValue(m_formatted));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIArticle_Price::getCurrency() const {
    return m_currency;
}
void OAIArticle_Price::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIArticle_Price::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIArticle_Price::is_currency_Valid() const{
    return m_currency_isValid;
}

QString OAIArticle_Price::getFormatted() const {
    return m_formatted;
}
void OAIArticle_Price::setFormatted(const QString &formatted) {
    m_formatted = formatted;
    m_formatted_isSet = true;
}

bool OAIArticle_Price::is_formatted_Set() const{
    return m_formatted_isSet;
}

bool OAIArticle_Price::is_formatted_Valid() const{
    return m_formatted_isValid;
}

double OAIArticle_Price::getValue() const {
    return m_value;
}
void OAIArticle_Price::setValue(const double &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIArticle_Price::is_value_Set() const{
    return m_value_isSet;
}

bool OAIArticle_Price::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIArticle_Price::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_formatted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArticle_Price::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_currency_isValid && m_formatted_isValid && m_value_isValid && true;
}

} // namespace OpenAPI
