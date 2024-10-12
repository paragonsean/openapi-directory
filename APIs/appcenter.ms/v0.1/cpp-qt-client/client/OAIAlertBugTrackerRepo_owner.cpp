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

#include "OAIAlertBugTrackerRepo_owner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAlertBugTrackerRepo_owner::OAIAlertBugTrackerRepo_owner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAlertBugTrackerRepo_owner::OAIAlertBugTrackerRepo_owner() {
    this->initializeModel();
}

OAIAlertBugTrackerRepo_owner::~OAIAlertBugTrackerRepo_owner() {}

void OAIAlertBugTrackerRepo_owner::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_login_isSet = false;
    m_login_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIAlertBugTrackerRepo_owner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAlertBugTrackerRepo_owner::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_login_isValid = ::OpenAPI::fromJsonValue(m_login, json[QString("login")]);
    m_login_isSet = !json[QString("login")].isNull() && m_login_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIAlertBugTrackerRepo_owner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAlertBugTrackerRepo_owner::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_login_isSet) {
        obj.insert(QString("login"), ::OpenAPI::toJsonValue(m_login));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIAlertBugTrackerRepo_owner::getId() const {
    return m_id;
}
void OAIAlertBugTrackerRepo_owner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAlertBugTrackerRepo_owner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAlertBugTrackerRepo_owner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAlertBugTrackerRepo_owner::getLogin() const {
    return m_login;
}
void OAIAlertBugTrackerRepo_owner::setLogin(const QString &login) {
    m_login = login;
    m_login_isSet = true;
}

bool OAIAlertBugTrackerRepo_owner::is_login_Set() const{
    return m_login_isSet;
}

bool OAIAlertBugTrackerRepo_owner::is_login_Valid() const{
    return m_login_isValid;
}

QString OAIAlertBugTrackerRepo_owner::getName() const {
    return m_name;
}
void OAIAlertBugTrackerRepo_owner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAlertBugTrackerRepo_owner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAlertBugTrackerRepo_owner::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIAlertBugTrackerRepo_owner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_login_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAlertBugTrackerRepo_owner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
