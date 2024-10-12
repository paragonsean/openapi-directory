/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserAuthDataUpdateRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserAuthDataUpdateRequest::OAIUserAuthDataUpdateRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserAuthDataUpdateRequest::OAIUserAuthDataUpdateRequest() {
    this->initializeModel();
}

OAIUserAuthDataUpdateRequest::~OAIUserAuthDataUpdateRequest() {}

void OAIUserAuthDataUpdateRequest::initializeModel() {

    m_ad_config_id_isSet = false;
    m_ad_config_id_isValid = false;

    m_login_isSet = false;
    m_login_isValid = false;

    m_method_isSet = false;
    m_method_isValid = false;

    m_oid_config_id_isSet = false;
    m_oid_config_id_isValid = false;
}

void OAIUserAuthDataUpdateRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserAuthDataUpdateRequest::fromJsonObject(QJsonObject json) {

    m_ad_config_id_isValid = ::OpenAPI::fromJsonValue(m_ad_config_id, json[QString("adConfigId")]);
    m_ad_config_id_isSet = !json[QString("adConfigId")].isNull() && m_ad_config_id_isValid;

    m_login_isValid = ::OpenAPI::fromJsonValue(m_login, json[QString("login")]);
    m_login_isSet = !json[QString("login")].isNull() && m_login_isValid;

    m_method_isValid = ::OpenAPI::fromJsonValue(m_method, json[QString("method")]);
    m_method_isSet = !json[QString("method")].isNull() && m_method_isValid;

    m_oid_config_id_isValid = ::OpenAPI::fromJsonValue(m_oid_config_id, json[QString("oidConfigId")]);
    m_oid_config_id_isSet = !json[QString("oidConfigId")].isNull() && m_oid_config_id_isValid;
}

QString OAIUserAuthDataUpdateRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserAuthDataUpdateRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_ad_config_id_isSet) {
        obj.insert(QString("adConfigId"), ::OpenAPI::toJsonValue(m_ad_config_id));
    }
    if (m_login_isSet) {
        obj.insert(QString("login"), ::OpenAPI::toJsonValue(m_login));
    }
    if (m_method_isSet) {
        obj.insert(QString("method"), ::OpenAPI::toJsonValue(m_method));
    }
    if (m_oid_config_id_isSet) {
        obj.insert(QString("oidConfigId"), ::OpenAPI::toJsonValue(m_oid_config_id));
    }
    return obj;
}

qint32 OAIUserAuthDataUpdateRequest::getAdConfigId() const {
    return m_ad_config_id;
}
void OAIUserAuthDataUpdateRequest::setAdConfigId(const qint32 &ad_config_id) {
    m_ad_config_id = ad_config_id;
    m_ad_config_id_isSet = true;
}

bool OAIUserAuthDataUpdateRequest::is_ad_config_id_Set() const{
    return m_ad_config_id_isSet;
}

bool OAIUserAuthDataUpdateRequest::is_ad_config_id_Valid() const{
    return m_ad_config_id_isValid;
}

QString OAIUserAuthDataUpdateRequest::getLogin() const {
    return m_login;
}
void OAIUserAuthDataUpdateRequest::setLogin(const QString &login) {
    m_login = login;
    m_login_isSet = true;
}

bool OAIUserAuthDataUpdateRequest::is_login_Set() const{
    return m_login_isSet;
}

bool OAIUserAuthDataUpdateRequest::is_login_Valid() const{
    return m_login_isValid;
}

QString OAIUserAuthDataUpdateRequest::getMethod() const {
    return m_method;
}
void OAIUserAuthDataUpdateRequest::setMethod(const QString &method) {
    m_method = method;
    m_method_isSet = true;
}

bool OAIUserAuthDataUpdateRequest::is_method_Set() const{
    return m_method_isSet;
}

bool OAIUserAuthDataUpdateRequest::is_method_Valid() const{
    return m_method_isValid;
}

qint32 OAIUserAuthDataUpdateRequest::getOidConfigId() const {
    return m_oid_config_id;
}
void OAIUserAuthDataUpdateRequest::setOidConfigId(const qint32 &oid_config_id) {
    m_oid_config_id = oid_config_id;
    m_oid_config_id_isSet = true;
}

bool OAIUserAuthDataUpdateRequest::is_oid_config_id_Set() const{
    return m_oid_config_id_isSet;
}

bool OAIUserAuthDataUpdateRequest::is_oid_config_id_Valid() const{
    return m_oid_config_id_isValid;
}

bool OAIUserAuthDataUpdateRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ad_config_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_login_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_oid_config_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserAuthDataUpdateRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
