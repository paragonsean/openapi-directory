/**
 * Cenit IO - REST API Specification
 * Cenit IO is an Open Platform for Data and Business Integration (iPaaS) 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@cenit.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFlow.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFlow::OAIFlow(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFlow::OAIFlow() {
    this->initializeModel();
}

OAIFlow::~OAIFlow() {}

void OAIFlow::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_connection_role_isSet = false;
    m_connection_role_isValid = false;

    m_custom_data_type_isSet = false;
    m_custom_data_type_isValid = false;

    m_event_isSet = false;
    m_event_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_r_namespace_isSet = false;
    m_r_namespace_isValid = false;

    m_notify_request_isSet = false;
    m_notify_request_isValid = false;

    m_notify_response_isSet = false;
    m_notify_response_isValid = false;

    m_response_translator_isSet = false;
    m_response_translator_isValid = false;

    m_translator_isSet = false;
    m_translator_isValid = false;

    m_webhook_isSet = false;
    m_webhook_isValid = false;
}

void OAIFlow::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFlow::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("active")]);
    m_active_isSet = !json[QString("active")].isNull() && m_active_isValid;

    m_connection_role_isValid = ::OpenAPI::fromJsonValue(m_connection_role, json[QString("connection_role")]);
    m_connection_role_isSet = !json[QString("connection_role")].isNull() && m_connection_role_isValid;

    m_custom_data_type_isValid = ::OpenAPI::fromJsonValue(m_custom_data_type, json[QString("custom_data_type")]);
    m_custom_data_type_isSet = !json[QString("custom_data_type")].isNull() && m_custom_data_type_isValid;

    m_event_isValid = ::OpenAPI::fromJsonValue(m_event, json[QString("event")]);
    m_event_isSet = !json[QString("event")].isNull() && m_event_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_r_namespace_isValid = ::OpenAPI::fromJsonValue(m_r_namespace, json[QString("namespace")]);
    m_r_namespace_isSet = !json[QString("namespace")].isNull() && m_r_namespace_isValid;

    m_notify_request_isValid = ::OpenAPI::fromJsonValue(m_notify_request, json[QString("notify_request")]);
    m_notify_request_isSet = !json[QString("notify_request")].isNull() && m_notify_request_isValid;

    m_notify_response_isValid = ::OpenAPI::fromJsonValue(m_notify_response, json[QString("notify_response")]);
    m_notify_response_isSet = !json[QString("notify_response")].isNull() && m_notify_response_isValid;

    m_response_translator_isValid = ::OpenAPI::fromJsonValue(m_response_translator, json[QString("response_translator")]);
    m_response_translator_isSet = !json[QString("response_translator")].isNull() && m_response_translator_isValid;

    m_translator_isValid = ::OpenAPI::fromJsonValue(m_translator, json[QString("translator")]);
    m_translator_isSet = !json[QString("translator")].isNull() && m_translator_isValid;

    m_webhook_isValid = ::OpenAPI::fromJsonValue(m_webhook, json[QString("webhook")]);
    m_webhook_isSet = !json[QString("webhook")].isNull() && m_webhook_isValid;
}

QString OAIFlow::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFlow::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_connection_role.isSet()) {
        obj.insert(QString("connection_role"), ::OpenAPI::toJsonValue(m_connection_role));
    }
    if (m_custom_data_type.isSet()) {
        obj.insert(QString("custom_data_type"), ::OpenAPI::toJsonValue(m_custom_data_type));
    }
    if (m_event_isSet) {
        obj.insert(QString("event"), ::OpenAPI::toJsonValue(m_event));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_r_namespace.isSet()) {
        obj.insert(QString("namespace"), ::OpenAPI::toJsonValue(m_r_namespace));
    }
    if (m_notify_request_isSet) {
        obj.insert(QString("notify_request"), ::OpenAPI::toJsonValue(m_notify_request));
    }
    if (m_notify_response_isSet) {
        obj.insert(QString("notify_response"), ::OpenAPI::toJsonValue(m_notify_response));
    }
    if (m_response_translator.isSet()) {
        obj.insert(QString("response_translator"), ::OpenAPI::toJsonValue(m_response_translator));
    }
    if (m_translator.isSet()) {
        obj.insert(QString("translator"), ::OpenAPI::toJsonValue(m_translator));
    }
    if (m_webhook.isSet()) {
        obj.insert(QString("webhook"), ::OpenAPI::toJsonValue(m_webhook));
    }
    return obj;
}

bool OAIFlow::isActive() const {
    return m_active;
}
void OAIFlow::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAIFlow::is_active_Set() const{
    return m_active_isSet;
}

bool OAIFlow::is_active_Valid() const{
    return m_active_isValid;
}

OAIConnection_role OAIFlow::getConnectionRole() const {
    return m_connection_role;
}
void OAIFlow::setConnectionRole(const OAIConnection_role &connection_role) {
    m_connection_role = connection_role;
    m_connection_role_isSet = true;
}

bool OAIFlow::is_connection_role_Set() const{
    return m_connection_role_isSet;
}

bool OAIFlow::is_connection_role_Valid() const{
    return m_connection_role_isValid;
}

OAIData_type OAIFlow::getCustomDataType() const {
    return m_custom_data_type;
}
void OAIFlow::setCustomDataType(const OAIData_type &custom_data_type) {
    m_custom_data_type = custom_data_type;
    m_custom_data_type_isSet = true;
}

bool OAIFlow::is_custom_data_type_Set() const{
    return m_custom_data_type_isSet;
}

bool OAIFlow::is_custom_data_type_Valid() const{
    return m_custom_data_type_isValid;
}

OAIObject OAIFlow::getEvent() const {
    return m_event;
}
void OAIFlow::setEvent(const OAIObject &event) {
    m_event = event;
    m_event_isSet = true;
}

bool OAIFlow::is_event_Set() const{
    return m_event_isSet;
}

bool OAIFlow::is_event_Valid() const{
    return m_event_isValid;
}

QString OAIFlow::getId() const {
    return m_id;
}
void OAIFlow::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIFlow::is_id_Set() const{
    return m_id_isSet;
}

bool OAIFlow::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIFlow::getName() const {
    return m_name;
}
void OAIFlow::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIFlow::is_name_Set() const{
    return m_name_isSet;
}

bool OAIFlow::is_name_Valid() const{
    return m_name_isValid;
}

OAINamespace OAIFlow::getRNamespace() const {
    return m_r_namespace;
}
void OAIFlow::setRNamespace(const OAINamespace &r_namespace) {
    m_r_namespace = r_namespace;
    m_r_namespace_isSet = true;
}

bool OAIFlow::is_r_namespace_Set() const{
    return m_r_namespace_isSet;
}

bool OAIFlow::is_r_namespace_Valid() const{
    return m_r_namespace_isValid;
}

bool OAIFlow::isNotifyRequest() const {
    return m_notify_request;
}
void OAIFlow::setNotifyRequest(const bool &notify_request) {
    m_notify_request = notify_request;
    m_notify_request_isSet = true;
}

bool OAIFlow::is_notify_request_Set() const{
    return m_notify_request_isSet;
}

bool OAIFlow::is_notify_request_Valid() const{
    return m_notify_request_isValid;
}

bool OAIFlow::isNotifyResponse() const {
    return m_notify_response;
}
void OAIFlow::setNotifyResponse(const bool &notify_response) {
    m_notify_response = notify_response;
    m_notify_response_isSet = true;
}

bool OAIFlow::is_notify_response_Set() const{
    return m_notify_response_isSet;
}

bool OAIFlow::is_notify_response_Valid() const{
    return m_notify_response_isValid;
}

OAITranslator OAIFlow::getResponseTranslator() const {
    return m_response_translator;
}
void OAIFlow::setResponseTranslator(const OAITranslator &response_translator) {
    m_response_translator = response_translator;
    m_response_translator_isSet = true;
}

bool OAIFlow::is_response_translator_Set() const{
    return m_response_translator_isSet;
}

bool OAIFlow::is_response_translator_Valid() const{
    return m_response_translator_isValid;
}

OAITranslator OAIFlow::getTranslator() const {
    return m_translator;
}
void OAIFlow::setTranslator(const OAITranslator &translator) {
    m_translator = translator;
    m_translator_isSet = true;
}

bool OAIFlow::is_translator_Set() const{
    return m_translator_isSet;
}

bool OAIFlow::is_translator_Valid() const{
    return m_translator_isValid;
}

OAIWebhook OAIFlow::getWebhook() const {
    return m_webhook;
}
void OAIFlow::setWebhook(const OAIWebhook &webhook) {
    m_webhook = webhook;
    m_webhook_isSet = true;
}

bool OAIFlow::is_webhook_Set() const{
    return m_webhook_isSet;
}

bool OAIFlow::is_webhook_Valid() const{
    return m_webhook_isValid;
}

bool OAIFlow::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_connection_role.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_data_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_event_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_namespace.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_notify_request_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notify_response_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_response_translator.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_translator.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_webhook.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFlow::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
