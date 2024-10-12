/**
 * seven.io API
 * seven.io Swagger API. Get your API-Key now at seven.io.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@seven.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHooksGet_200_response_hooks_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHooksGet_200_response_hooks_inner::OAIHooksGet_200_response_hooks_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHooksGet_200_response_hooks_inner::OAIHooksGet_200_response_hooks_inner() {
    this->initializeModel();
}

OAIHooksGet_200_response_hooks_inner::~OAIHooksGet_200_response_hooks_inner() {}

void OAIHooksGet_200_response_hooks_inner::initializeModel() {

    m_created_isSet = false;
    m_created_isValid = false;

    m_event_type_isSet = false;
    m_event_type_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_request_method_isSet = false;
    m_request_method_isValid = false;

    m_target_url_isSet = false;
    m_target_url_isValid = false;
}

void OAIHooksGet_200_response_hooks_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHooksGet_200_response_hooks_inner::fromJsonObject(QJsonObject json) {

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_event_type_isValid = ::OpenAPI::fromJsonValue(m_event_type, json[QString("event_type")]);
    m_event_type_isSet = !json[QString("event_type")].isNull() && m_event_type_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_request_method_isValid = ::OpenAPI::fromJsonValue(m_request_method, json[QString("request_method")]);
    m_request_method_isSet = !json[QString("request_method")].isNull() && m_request_method_isValid;

    m_target_url_isValid = ::OpenAPI::fromJsonValue(m_target_url, json[QString("target_url")]);
    m_target_url_isSet = !json[QString("target_url")].isNull() && m_target_url_isValid;
}

QString OAIHooksGet_200_response_hooks_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHooksGet_200_response_hooks_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_event_type_isSet) {
        obj.insert(QString("event_type"), ::OpenAPI::toJsonValue(m_event_type));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_request_method_isSet) {
        obj.insert(QString("request_method"), ::OpenAPI::toJsonValue(m_request_method));
    }
    if (m_target_url_isSet) {
        obj.insert(QString("target_url"), ::OpenAPI::toJsonValue(m_target_url));
    }
    return obj;
}

QString OAIHooksGet_200_response_hooks_inner::getCreated() const {
    return m_created;
}
void OAIHooksGet_200_response_hooks_inner::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIHooksGet_200_response_hooks_inner::is_created_Set() const{
    return m_created_isSet;
}

bool OAIHooksGet_200_response_hooks_inner::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIHooksGet_200_response_hooks_inner::getEventType() const {
    return m_event_type;
}
void OAIHooksGet_200_response_hooks_inner::setEventType(const QString &event_type) {
    m_event_type = event_type;
    m_event_type_isSet = true;
}

bool OAIHooksGet_200_response_hooks_inner::is_event_type_Set() const{
    return m_event_type_isSet;
}

bool OAIHooksGet_200_response_hooks_inner::is_event_type_Valid() const{
    return m_event_type_isValid;
}

QString OAIHooksGet_200_response_hooks_inner::getId() const {
    return m_id;
}
void OAIHooksGet_200_response_hooks_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIHooksGet_200_response_hooks_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIHooksGet_200_response_hooks_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIHooksGet_200_response_hooks_inner::getRequestMethod() const {
    return m_request_method;
}
void OAIHooksGet_200_response_hooks_inner::setRequestMethod(const QString &request_method) {
    m_request_method = request_method;
    m_request_method_isSet = true;
}

bool OAIHooksGet_200_response_hooks_inner::is_request_method_Set() const{
    return m_request_method_isSet;
}

bool OAIHooksGet_200_response_hooks_inner::is_request_method_Valid() const{
    return m_request_method_isValid;
}

QString OAIHooksGet_200_response_hooks_inner::getTargetUrl() const {
    return m_target_url;
}
void OAIHooksGet_200_response_hooks_inner::setTargetUrl(const QString &target_url) {
    m_target_url = target_url;
    m_target_url_isSet = true;
}

bool OAIHooksGet_200_response_hooks_inner::is_target_url_Set() const{
    return m_target_url_isSet;
}

bool OAIHooksGet_200_response_hooks_inner::is_target_url_Valid() const{
    return m_target_url_isValid;
}

bool OAIHooksGet_200_response_hooks_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_event_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHooksGet_200_response_hooks_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
