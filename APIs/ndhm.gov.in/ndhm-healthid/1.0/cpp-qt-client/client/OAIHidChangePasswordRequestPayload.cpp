/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIHidChangePasswordRequestPayload.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHidChangePasswordRequestPayload::OAIHidChangePasswordRequestPayload(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHidChangePasswordRequestPayload::OAIHidChangePasswordRequestPayload() {
    this->initializeModel();
}

OAIHidChangePasswordRequestPayload::~OAIHidChangePasswordRequestPayload() {}

void OAIHidChangePasswordRequestPayload::initializeModel() {

    m_new_password_isSet = false;
    m_new_password_isValid = false;

    m_old_password_isSet = false;
    m_old_password_isValid = false;
}

void OAIHidChangePasswordRequestPayload::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHidChangePasswordRequestPayload::fromJsonObject(QJsonObject json) {

    m_new_password_isValid = ::OpenAPI::fromJsonValue(m_new_password, json[QString("newPassword")]);
    m_new_password_isSet = !json[QString("newPassword")].isNull() && m_new_password_isValid;

    m_old_password_isValid = ::OpenAPI::fromJsonValue(m_old_password, json[QString("oldPassword")]);
    m_old_password_isSet = !json[QString("oldPassword")].isNull() && m_old_password_isValid;
}

QString OAIHidChangePasswordRequestPayload::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHidChangePasswordRequestPayload::asJsonObject() const {
    QJsonObject obj;
    if (m_new_password_isSet) {
        obj.insert(QString("newPassword"), ::OpenAPI::toJsonValue(m_new_password));
    }
    if (m_old_password_isSet) {
        obj.insert(QString("oldPassword"), ::OpenAPI::toJsonValue(m_old_password));
    }
    return obj;
}

QString OAIHidChangePasswordRequestPayload::getNewPassword() const {
    return m_new_password;
}
void OAIHidChangePasswordRequestPayload::setNewPassword(const QString &new_password) {
    m_new_password = new_password;
    m_new_password_isSet = true;
}

bool OAIHidChangePasswordRequestPayload::is_new_password_Set() const{
    return m_new_password_isSet;
}

bool OAIHidChangePasswordRequestPayload::is_new_password_Valid() const{
    return m_new_password_isValid;
}

QString OAIHidChangePasswordRequestPayload::getOldPassword() const {
    return m_old_password;
}
void OAIHidChangePasswordRequestPayload::setOldPassword(const QString &old_password) {
    m_old_password = old_password;
    m_old_password_isSet = true;
}

bool OAIHidChangePasswordRequestPayload::is_old_password_Set() const{
    return m_old_password_isSet;
}

bool OAIHidChangePasswordRequestPayload::is_old_password_Valid() const{
    return m_old_password_isValid;
}

bool OAIHidChangePasswordRequestPayload::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_new_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_old_password_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHidChangePasswordRequestPayload::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
