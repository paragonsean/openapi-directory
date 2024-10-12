/**
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDateTimeType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDateTimeType::OAIDateTimeType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDateTimeType::OAIDateTimeType() {
    this->initializeModel();
}

OAIDateTimeType::~OAIDateTimeType() {}

void OAIDateTimeType::initializeModel() {

    m_date_isSet = false;
    m_date_isValid = false;

    m_time_isSet = false;
    m_time_isValid = false;
}

void OAIDateTimeType::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDateTimeType::fromJsonObject(QJsonObject json) {

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("date")]);
    m_date_isSet = !json[QString("date")].isNull() && m_date_isValid;

    m_time_isValid = ::OpenAPI::fromJsonValue(m_time, json[QString("time")]);
    m_time_isSet = !json[QString("time")].isNull() && m_time_isValid;
}

QString OAIDateTimeType::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDateTimeType::asJsonObject() const {
    QJsonObject obj;
    if (m_date_isSet) {
        obj.insert(QString("date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_time_isSet) {
        obj.insert(QString("time"), ::OpenAPI::toJsonValue(m_time));
    }
    return obj;
}

QDate OAIDateTimeType::getDate() const {
    return m_date;
}
void OAIDateTimeType::setDate(const QDate &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAIDateTimeType::is_date_Set() const{
    return m_date_isSet;
}

bool OAIDateTimeType::is_date_Valid() const{
    return m_date_isValid;
}

QString OAIDateTimeType::getTime() const {
    return m_time;
}
void OAIDateTimeType::setTime(const QString &time) {
    m_time = time;
    m_time_isSet = true;
}

bool OAIDateTimeType::is_time_Set() const{
    return m_time_isSet;
}

bool OAIDateTimeType::is_time_Valid() const{
    return m_time_isValid;
}

bool OAIDateTimeType::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_date_isSet) {
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

bool OAIDateTimeType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_date_isValid && true;
}

} // namespace OpenAPI
