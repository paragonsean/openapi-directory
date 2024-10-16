/**
 * API for the COVID-19 Tracking QR Code Signin Server.
 * This is the API for the COVID-19 Contact Tracing QRCode Signin Server
 *
 * The version of the OpenAPI document: 1.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILoginResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILoginResponse::OAILoginResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILoginResponse::OAILoginResponse() {
    this->initializeModel();
}

OAILoginResponse::~OAILoginResponse() {}

void OAILoginResponse::initializeModel() {

    m_admin_isSet = false;
    m_admin_isValid = false;

    m_login_id_isSet = false;
    m_login_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_read_only_isSet = false;
    m_read_only_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;
}

void OAILoginResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILoginResponse::fromJsonObject(QJsonObject json) {

    m_admin_isValid = ::OpenAPI::fromJsonValue(m_admin, json[QString("admin")]);
    m_admin_isSet = !json[QString("admin")].isNull() && m_admin_isValid;

    m_login_id_isValid = ::OpenAPI::fromJsonValue(m_login_id, json[QString("login_id")]);
    m_login_id_isSet = !json[QString("login_id")].isNull() && m_login_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_read_only_isValid = ::OpenAPI::fromJsonValue(m_read_only, json[QString("read_only")]);
    m_read_only_isSet = !json[QString("read_only")].isNull() && m_read_only_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;
}

QString OAILoginResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILoginResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_admin_isSet) {
        obj.insert(QString("admin"), ::OpenAPI::toJsonValue(m_admin));
    }
    if (m_login_id_isSet) {
        obj.insert(QString("login_id"), ::OpenAPI::toJsonValue(m_login_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_read_only_isSet) {
        obj.insert(QString("read_only"), ::OpenAPI::toJsonValue(m_read_only));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    return obj;
}

bool OAILoginResponse::isAdmin() const {
    return m_admin;
}
void OAILoginResponse::setAdmin(const bool &admin) {
    m_admin = admin;
    m_admin_isSet = true;
}

bool OAILoginResponse::is_admin_Set() const{
    return m_admin_isSet;
}

bool OAILoginResponse::is_admin_Valid() const{
    return m_admin_isValid;
}

qint32 OAILoginResponse::getLoginId() const {
    return m_login_id;
}
void OAILoginResponse::setLoginId(const qint32 &login_id) {
    m_login_id = login_id;
    m_login_id_isSet = true;
}

bool OAILoginResponse::is_login_id_Set() const{
    return m_login_id_isSet;
}

bool OAILoginResponse::is_login_id_Valid() const{
    return m_login_id_isValid;
}

QString OAILoginResponse::getName() const {
    return m_name;
}
void OAILoginResponse::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAILoginResponse::is_name_Set() const{
    return m_name_isSet;
}

bool OAILoginResponse::is_name_Valid() const{
    return m_name_isValid;
}

bool OAILoginResponse::isReadOnly() const {
    return m_read_only;
}
void OAILoginResponse::setReadOnly(const bool &read_only) {
    m_read_only = read_only;
    m_read_only_isSet = true;
}

bool OAILoginResponse::is_read_only_Set() const{
    return m_read_only_isSet;
}

bool OAILoginResponse::is_read_only_Valid() const{
    return m_read_only_isValid;
}

QString OAILoginResponse::getToken() const {
    return m_token;
}
void OAILoginResponse::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAILoginResponse::is_token_Set() const{
    return m_token_isSet;
}

bool OAILoginResponse::is_token_Valid() const{
    return m_token_isValid;
}

bool OAILoginResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_admin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_login_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_read_only_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILoginResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
