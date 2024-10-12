/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICarrierEntry.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICarrierEntry::OAICarrierEntry(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICarrierEntry::OAICarrierEntry() {
    this->initializeModel();
}

OAICarrierEntry::~OAICarrierEntry() {}

void OAICarrierEntry::initializeModel() {

    m_key_isSet = false;
    m_key_isValid = false;
}

void OAICarrierEntry::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICarrierEntry::fromJsonObject(QJsonObject json) {

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("key")]);
    m_key_isSet = !json[QString("key")].isNull() && m_key_isValid;
}

QString OAICarrierEntry::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICarrierEntry::asJsonObject() const {
    QJsonObject obj;
    if (m_key_isSet) {
        obj.insert(QString("key"), ::OpenAPI::toJsonValue(m_key));
    }
    return obj;
}

QString OAICarrierEntry::getKey() const {
    return m_key;
}
void OAICarrierEntry::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAICarrierEntry::is_key_Set() const{
    return m_key_isSet;
}

bool OAICarrierEntry::is_key_Valid() const{
    return m_key_isValid;
}

bool OAICarrierEntry::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_key_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICarrierEntry::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
