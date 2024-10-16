/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMasterUser.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMasterUser::OAIMasterUser(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMasterUser::OAIMasterUser() {
    this->initializeModel();
}

OAIMasterUser::~OAIMasterUser() {}

void OAIMasterUser::initializeModel() {

    m_master_user_isSet = false;
    m_master_user_isValid = false;
}

void OAIMasterUser::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMasterUser::fromJsonObject(QJsonObject json) {

    m_master_user_isValid = ::OpenAPI::fromJsonValue(m_master_user, json[QString("masterUser")]);
    m_master_user_isSet = !json[QString("masterUser")].isNull() && m_master_user_isValid;
}

QString OAIMasterUser::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMasterUser::asJsonObject() const {
    QJsonObject obj;
    if (m_master_user.isSet()) {
        obj.insert(QString("masterUser"), ::OpenAPI::toJsonValue(m_master_user));
    }
    return obj;
}

OAIMasterUser_masterUser OAIMasterUser::getMasterUser() const {
    return m_master_user;
}
void OAIMasterUser::setMasterUser(const OAIMasterUser_masterUser &master_user) {
    m_master_user = master_user;
    m_master_user_isSet = true;
}

bool OAIMasterUser::is_master_user_Set() const{
    return m_master_user_isSet;
}

bool OAIMasterUser::is_master_user_Valid() const{
    return m_master_user_isValid;
}

bool OAIMasterUser::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_master_user.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMasterUser::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
