/**
 * KumpeApps API
 * KKid API. Due to security concerns all calls to this API requires authentication. If you have access then you may use your KumpeApps username/password to authenticate. To gain access please use the contact developer link below.
 *
 * The version of the OpenAPI document: 5.0.0
 * Contact: helpdesk@kumpeapps.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI201_share.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI201_share::OAI201_share(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI201_share::OAI201_share() {
    this->initializeModel();
}

OAI201_share::~OAI201_share() {}

void OAI201_share::initializeModel() {

    m_auth_link_isSet = false;
    m_auth_link_isValid = false;

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAI201_share::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI201_share::fromJsonObject(QJsonObject json) {

    m_auth_link_isValid = ::OpenAPI::fromJsonValue(m_auth_link, json[QString("auth_link")]);
    m_auth_link_isSet = !json[QString("auth_link")].isNull() && m_auth_link_isValid;

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAI201_share::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI201_share::asJsonObject() const {
    QJsonObject obj;
    if (m_auth_link_isSet) {
        obj.insert(QString("auth_link"), ::OpenAPI::toJsonValue(m_auth_link));
    }
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

QString OAI201_share::getAuthLink() const {
    return m_auth_link;
}
void OAI201_share::setAuthLink(const QString &auth_link) {
    m_auth_link = auth_link;
    m_auth_link_isSet = true;
}

bool OAI201_share::is_auth_link_Set() const{
    return m_auth_link_isSet;
}

bool OAI201_share::is_auth_link_Valid() const{
    return m_auth_link_isValid;
}

bool OAI201_share::isSuccess() const {
    return m_success;
}
void OAI201_share::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAI201_share::is_success_Set() const{
    return m_success_isSet;
}

bool OAI201_share::is_success_Valid() const{
    return m_success_isValid;
}

bool OAI201_share::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auth_link_isSet) {
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

bool OAI201_share::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
