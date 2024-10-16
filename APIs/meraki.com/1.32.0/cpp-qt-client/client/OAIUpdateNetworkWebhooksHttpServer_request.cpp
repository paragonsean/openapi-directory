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

#include "OAIUpdateNetworkWebhooksHttpServer_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkWebhooksHttpServer_request::OAIUpdateNetworkWebhooksHttpServer_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkWebhooksHttpServer_request::OAIUpdateNetworkWebhooksHttpServer_request() {
    this->initializeModel();
}

OAIUpdateNetworkWebhooksHttpServer_request::~OAIUpdateNetworkWebhooksHttpServer_request() {}

void OAIUpdateNetworkWebhooksHttpServer_request::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_payload_template_isSet = false;
    m_payload_template_isValid = false;

    m_shared_secret_isSet = false;
    m_shared_secret_isValid = false;
}

void OAIUpdateNetworkWebhooksHttpServer_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkWebhooksHttpServer_request::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_payload_template_isValid = ::OpenAPI::fromJsonValue(m_payload_template, json[QString("payloadTemplate")]);
    m_payload_template_isSet = !json[QString("payloadTemplate")].isNull() && m_payload_template_isValid;

    m_shared_secret_isValid = ::OpenAPI::fromJsonValue(m_shared_secret, json[QString("sharedSecret")]);
    m_shared_secret_isSet = !json[QString("sharedSecret")].isNull() && m_shared_secret_isValid;
}

QString OAIUpdateNetworkWebhooksHttpServer_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkWebhooksHttpServer_request::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_payload_template.isSet()) {
        obj.insert(QString("payloadTemplate"), ::OpenAPI::toJsonValue(m_payload_template));
    }
    if (m_shared_secret_isSet) {
        obj.insert(QString("sharedSecret"), ::OpenAPI::toJsonValue(m_shared_secret));
    }
    return obj;
}

QString OAIUpdateNetworkWebhooksHttpServer_request::getName() const {
    return m_name;
}
void OAIUpdateNetworkWebhooksHttpServer_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateNetworkWebhooksHttpServer_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateNetworkWebhooksHttpServer_request::is_name_Valid() const{
    return m_name_isValid;
}

OAIUpdateNetworkWebhooksHttpServer_request_payloadTemplate OAIUpdateNetworkWebhooksHttpServer_request::getPayloadTemplate() const {
    return m_payload_template;
}
void OAIUpdateNetworkWebhooksHttpServer_request::setPayloadTemplate(const OAIUpdateNetworkWebhooksHttpServer_request_payloadTemplate &payload_template) {
    m_payload_template = payload_template;
    m_payload_template_isSet = true;
}

bool OAIUpdateNetworkWebhooksHttpServer_request::is_payload_template_Set() const{
    return m_payload_template_isSet;
}

bool OAIUpdateNetworkWebhooksHttpServer_request::is_payload_template_Valid() const{
    return m_payload_template_isValid;
}

QString OAIUpdateNetworkWebhooksHttpServer_request::getSharedSecret() const {
    return m_shared_secret;
}
void OAIUpdateNetworkWebhooksHttpServer_request::setSharedSecret(const QString &shared_secret) {
    m_shared_secret = shared_secret;
    m_shared_secret_isSet = true;
}

bool OAIUpdateNetworkWebhooksHttpServer_request::is_shared_secret_Set() const{
    return m_shared_secret_isSet;
}

bool OAIUpdateNetworkWebhooksHttpServer_request::is_shared_secret_Valid() const{
    return m_shared_secret_isValid;
}

bool OAIUpdateNetworkWebhooksHttpServer_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payload_template.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_shared_secret_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkWebhooksHttpServer_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
