/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties() {
    this->initializeModel();
}

OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::~OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties() {}

void OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::initializeModel() {

    m_send_key_name_isSet = false;
    m_send_key_name_isValid = false;

    m_send_key_value_isSet = false;
    m_send_key_value_isValid = false;
}

void OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::fromJsonObject(QJsonObject json) {

    m_send_key_name_isValid = ::OpenAPI::fromJsonValue(m_send_key_name, json[QString("sendKeyName")]);
    m_send_key_name_isSet = !json[QString("sendKeyName")].isNull() && m_send_key_name_isValid;

    m_send_key_value_isValid = ::OpenAPI::fromJsonValue(m_send_key_value, json[QString("sendKeyValue")]);
    m_send_key_value_isSet = !json[QString("sendKeyValue")].isNull() && m_send_key_value_isValid;
}

QString OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::asJsonObject() const {
    QJsonObject obj;
    if (m_send_key_name_isSet) {
        obj.insert(QString("sendKeyName"), ::OpenAPI::toJsonValue(m_send_key_name));
    }
    if (m_send_key_value_isSet) {
        obj.insert(QString("sendKeyValue"), ::OpenAPI::toJsonValue(m_send_key_value));
    }
    return obj;
}

QString OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::getSendKeyName() const {
    return m_send_key_name;
}
void OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::setSendKeyName(const QString &send_key_name) {
    m_send_key_name = send_key_name;
    m_send_key_name_isSet = true;
}

bool OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::is_send_key_name_Set() const{
    return m_send_key_name_isSet;
}

bool OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::is_send_key_name_Valid() const{
    return m_send_key_name_isValid;
}

QString OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::getSendKeyValue() const {
    return m_send_key_value;
}
void OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::setSendKeyValue(const QString &send_key_value) {
    m_send_key_value = send_key_value;
    m_send_key_value_isSet = true;
}

bool OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::is_send_key_value_Set() const{
    return m_send_key_value_isSet;
}

bool OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::is_send_key_value_Valid() const{
    return m_send_key_value_isValid;
}

bool OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_send_key_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_send_key_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListHybridConnectionKeys_200_response_properties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
