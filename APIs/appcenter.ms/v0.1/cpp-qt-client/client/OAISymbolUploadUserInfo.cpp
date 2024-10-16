/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISymbolUploadUserInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISymbolUploadUserInfo::OAISymbolUploadUserInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISymbolUploadUserInfo::OAISymbolUploadUserInfo() {
    this->initializeModel();
}

OAISymbolUploadUserInfo::~OAISymbolUploadUserInfo() {}

void OAISymbolUploadUserInfo::initializeModel() {

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;
}

void OAISymbolUploadUserInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISymbolUploadUserInfo::fromJsonObject(QJsonObject json) {

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("display_name")]);
    m_display_name_isSet = !json[QString("display_name")].isNull() && m_display_name_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;
}

QString OAISymbolUploadUserInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISymbolUploadUserInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_display_name_isSet) {
        obj.insert(QString("display_name"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    return obj;
}

QString OAISymbolUploadUserInfo::getDisplayName() const {
    return m_display_name;
}
void OAISymbolUploadUserInfo::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAISymbolUploadUserInfo::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAISymbolUploadUserInfo::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAISymbolUploadUserInfo::getEmail() const {
    return m_email;
}
void OAISymbolUploadUserInfo::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAISymbolUploadUserInfo::is_email_Set() const{
    return m_email_isSet;
}

bool OAISymbolUploadUserInfo::is_email_Valid() const{
    return m_email_isValid;
}

bool OAISymbolUploadUserInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISymbolUploadUserInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
