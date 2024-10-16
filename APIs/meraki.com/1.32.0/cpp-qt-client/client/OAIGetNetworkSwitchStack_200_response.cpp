/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetNetworkSwitchStack_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkSwitchStack_200_response::OAIGetNetworkSwitchStack_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkSwitchStack_200_response::OAIGetNetworkSwitchStack_200_response() {
    this->initializeModel();
}

OAIGetNetworkSwitchStack_200_response::~OAIGetNetworkSwitchStack_200_response() {}

void OAIGetNetworkSwitchStack_200_response::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_serials_isSet = false;
    m_serials_isValid = false;
}

void OAIGetNetworkSwitchStack_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkSwitchStack_200_response::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_serials_isValid = ::OpenAPI::fromJsonValue(m_serials, json[QString("serials")]);
    m_serials_isSet = !json[QString("serials")].isNull() && m_serials_isValid;
}

QString OAIGetNetworkSwitchStack_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkSwitchStack_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_serials.size() > 0) {
        obj.insert(QString("serials"), ::OpenAPI::toJsonValue(m_serials));
    }
    return obj;
}

QString OAIGetNetworkSwitchStack_200_response::getId() const {
    return m_id;
}
void OAIGetNetworkSwitchStack_200_response::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetNetworkSwitchStack_200_response::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetNetworkSwitchStack_200_response::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIGetNetworkSwitchStack_200_response::getName() const {
    return m_name;
}
void OAIGetNetworkSwitchStack_200_response::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGetNetworkSwitchStack_200_response::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGetNetworkSwitchStack_200_response::is_name_Valid() const{
    return m_name_isValid;
}

QList<QString> OAIGetNetworkSwitchStack_200_response::getSerials() const {
    return m_serials;
}
void OAIGetNetworkSwitchStack_200_response::setSerials(const QList<QString> &serials) {
    m_serials = serials;
    m_serials_isSet = true;
}

bool OAIGetNetworkSwitchStack_200_response::is_serials_Set() const{
    return m_serials_isSet;
}

bool OAIGetNetworkSwitchStack_200_response::is_serials_Valid() const{
    return m_serials_isValid;
}

bool OAIGetNetworkSwitchStack_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_serials.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkSwitchStack_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
