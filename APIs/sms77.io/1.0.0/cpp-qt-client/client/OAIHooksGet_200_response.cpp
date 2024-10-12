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

#include "OAIHooksGet_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHooksGet_200_response::OAIHooksGet_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHooksGet_200_response::OAIHooksGet_200_response() {
    this->initializeModel();
}

OAIHooksGet_200_response::~OAIHooksGet_200_response() {}

void OAIHooksGet_200_response::initializeModel() {

    m_hooks_isSet = false;
    m_hooks_isValid = false;

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAIHooksGet_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHooksGet_200_response::fromJsonObject(QJsonObject json) {

    m_hooks_isValid = ::OpenAPI::fromJsonValue(m_hooks, json[QString("hooks")]);
    m_hooks_isSet = !json[QString("hooks")].isNull() && m_hooks_isValid;

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAIHooksGet_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHooksGet_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_hooks.size() > 0) {
        obj.insert(QString("hooks"), ::OpenAPI::toJsonValue(m_hooks));
    }
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

QList<OAIHooksGet_200_response_hooks_inner> OAIHooksGet_200_response::getHooks() const {
    return m_hooks;
}
void OAIHooksGet_200_response::setHooks(const QList<OAIHooksGet_200_response_hooks_inner> &hooks) {
    m_hooks = hooks;
    m_hooks_isSet = true;
}

bool OAIHooksGet_200_response::is_hooks_Set() const{
    return m_hooks_isSet;
}

bool OAIHooksGet_200_response::is_hooks_Valid() const{
    return m_hooks_isValid;
}

bool OAIHooksGet_200_response::isSuccess() const {
    return m_success;
}
void OAIHooksGet_200_response::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAIHooksGet_200_response::is_success_Set() const{
    return m_success_isSet;
}

bool OAIHooksGet_200_response::is_success_Valid() const{
    return m_success_isValid;
}

bool OAIHooksGet_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_hooks.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHooksGet_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
