/**
 * Airport & City Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, in test this API only contains data from the United States, Spain, United Kingdom, Germany and India. 
 *
 * The version of the OpenAPI document: 1.2.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAnalytics.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAnalytics::OAIAnalytics(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAnalytics::OAIAnalytics() {
    this->initializeModel();
}

OAIAnalytics::~OAIAnalytics() {}

void OAIAnalytics::initializeModel() {

    m_travelers_isSet = false;
    m_travelers_isValid = false;
}

void OAIAnalytics::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAnalytics::fromJsonObject(QJsonObject json) {

    m_travelers_isValid = ::OpenAPI::fromJsonValue(m_travelers, json[QString("travelers")]);
    m_travelers_isSet = !json[QString("travelers")].isNull() && m_travelers_isValid;
}

QString OAIAnalytics::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAnalytics::asJsonObject() const {
    QJsonObject obj;
    if (m_travelers.isSet()) {
        obj.insert(QString("travelers"), ::OpenAPI::toJsonValue(m_travelers));
    }
    return obj;
}

OAITravelers OAIAnalytics::getTravelers() const {
    return m_travelers;
}
void OAIAnalytics::setTravelers(const OAITravelers &travelers) {
    m_travelers = travelers;
    m_travelers_isSet = true;
}

bool OAIAnalytics::is_travelers_Set() const{
    return m_travelers_isSet;
}

bool OAIAnalytics::is_travelers_Valid() const{
    return m_travelers_isValid;
}

bool OAIAnalytics::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_travelers.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAnalytics::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
