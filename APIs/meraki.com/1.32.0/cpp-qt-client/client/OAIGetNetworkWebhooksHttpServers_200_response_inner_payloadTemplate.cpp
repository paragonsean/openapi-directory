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

#include "OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate() {
    this->initializeModel();
}

OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::~OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate() {}

void OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_payload_template_id_isSet = false;
    m_payload_template_id_isValid = false;
}

void OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_payload_template_id_isValid = ::OpenAPI::fromJsonValue(m_payload_template_id, json[QString("payloadTemplateId")]);
    m_payload_template_id_isSet = !json[QString("payloadTemplateId")].isNull() && m_payload_template_id_isValid;
}

QString OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_payload_template_id_isSet) {
        obj.insert(QString("payloadTemplateId"), ::OpenAPI::toJsonValue(m_payload_template_id));
    }
    return obj;
}

QString OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::getName() const {
    return m_name;
}
void OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::getPayloadTemplateId() const {
    return m_payload_template_id;
}
void OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::setPayloadTemplateId(const QString &payload_template_id) {
    m_payload_template_id = payload_template_id;
    m_payload_template_id_isSet = true;
}

bool OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::is_payload_template_id_Set() const{
    return m_payload_template_id_isSet;
}

bool OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::is_payload_template_id_Valid() const{
    return m_payload_template_id_isValid;
}

bool OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payload_template_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkWebhooksHttpServers_200_response_inner_payloadTemplate::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
