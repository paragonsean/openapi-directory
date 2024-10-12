/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIReferenceVmFragment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIReferenceVmFragment::OAIReferenceVmFragment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIReferenceVmFragment::OAIReferenceVmFragment() {
    this->initializeModel();
}

OAIReferenceVmFragment::~OAIReferenceVmFragment() {}

void OAIReferenceVmFragment::initializeModel() {

    m_password_isSet = false;
    m_password_isValid = false;

    m_user_name_isSet = false;
    m_user_name_isValid = false;
}

void OAIReferenceVmFragment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIReferenceVmFragment::fromJsonObject(QJsonObject json) {

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_user_name_isValid = ::OpenAPI::fromJsonValue(m_user_name, json[QString("userName")]);
    m_user_name_isSet = !json[QString("userName")].isNull() && m_user_name_isValid;
}

QString OAIReferenceVmFragment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIReferenceVmFragment::asJsonObject() const {
    QJsonObject obj;
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_user_name_isSet) {
        obj.insert(QString("userName"), ::OpenAPI::toJsonValue(m_user_name));
    }
    return obj;
}

QString OAIReferenceVmFragment::getPassword() const {
    return m_password;
}
void OAIReferenceVmFragment::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIReferenceVmFragment::is_password_Set() const{
    return m_password_isSet;
}

bool OAIReferenceVmFragment::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIReferenceVmFragment::getUserName() const {
    return m_user_name;
}
void OAIReferenceVmFragment::setUserName(const QString &user_name) {
    m_user_name = user_name;
    m_user_name_isSet = true;
}

bool OAIReferenceVmFragment::is_user_name_Set() const{
    return m_user_name_isSet;
}

bool OAIReferenceVmFragment::is_user_name_Valid() const{
    return m_user_name_isValid;
}

bool OAIReferenceVmFragment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIReferenceVmFragment::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
