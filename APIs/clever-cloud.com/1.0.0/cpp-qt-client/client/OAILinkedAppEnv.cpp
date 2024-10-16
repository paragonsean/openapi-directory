/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILinkedAppEnv.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILinkedAppEnv::OAILinkedAppEnv(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILinkedAppEnv::OAILinkedAppEnv() {
    this->initializeModel();
}

OAILinkedAppEnv::~OAILinkedAppEnv() {}

void OAILinkedAppEnv::initializeModel() {

    m_app_id_isSet = false;
    m_app_id_isValid = false;

    m_app_name_isSet = false;
    m_app_name_isValid = false;

    m_env_isSet = false;
    m_env_isValid = false;
}

void OAILinkedAppEnv::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILinkedAppEnv::fromJsonObject(QJsonObject json) {

    m_app_id_isValid = ::OpenAPI::fromJsonValue(m_app_id, json[QString("app_id")]);
    m_app_id_isSet = !json[QString("app_id")].isNull() && m_app_id_isValid;

    m_app_name_isValid = ::OpenAPI::fromJsonValue(m_app_name, json[QString("app_name")]);
    m_app_name_isSet = !json[QString("app_name")].isNull() && m_app_name_isValid;

    m_env_isValid = ::OpenAPI::fromJsonValue(m_env, json[QString("env")]);
    m_env_isSet = !json[QString("env")].isNull() && m_env_isValid;
}

QString OAILinkedAppEnv::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILinkedAppEnv::asJsonObject() const {
    QJsonObject obj;
    if (m_app_id_isSet) {
        obj.insert(QString("app_id"), ::OpenAPI::toJsonValue(m_app_id));
    }
    if (m_app_name_isSet) {
        obj.insert(QString("app_name"), ::OpenAPI::toJsonValue(m_app_name));
    }
    if (m_env.size() > 0) {
        obj.insert(QString("env"), ::OpenAPI::toJsonValue(m_env));
    }
    return obj;
}

QString OAILinkedAppEnv::getAppId() const {
    return m_app_id;
}
void OAILinkedAppEnv::setAppId(const QString &app_id) {
    m_app_id = app_id;
    m_app_id_isSet = true;
}

bool OAILinkedAppEnv::is_app_id_Set() const{
    return m_app_id_isSet;
}

bool OAILinkedAppEnv::is_app_id_Valid() const{
    return m_app_id_isValid;
}

QString OAILinkedAppEnv::getAppName() const {
    return m_app_name;
}
void OAILinkedAppEnv::setAppName(const QString &app_name) {
    m_app_name = app_name;
    m_app_name_isSet = true;
}

bool OAILinkedAppEnv::is_app_name_Set() const{
    return m_app_name_isSet;
}

bool OAILinkedAppEnv::is_app_name_Valid() const{
    return m_app_name_isValid;
}

QList<OAIWannabeEnv> OAILinkedAppEnv::getEnv() const {
    return m_env;
}
void OAILinkedAppEnv::setEnv(const QList<OAIWannabeEnv> &env) {
    m_env = env;
    m_env_isSet = true;
}

bool OAILinkedAppEnv::is_env_Set() const{
    return m_env_isSet;
}

bool OAILinkedAppEnv::is_env_Valid() const{
    return m_env_isValid;
}

bool OAILinkedAppEnv::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_app_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_env.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILinkedAppEnv::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_app_id_isValid && m_app_name_isValid && m_env_isValid && true;
}

} // namespace OpenAPI
