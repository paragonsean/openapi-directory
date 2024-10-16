/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBusinessUserUpdateModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBusinessUserUpdateModel::OAIBusinessUserUpdateModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBusinessUserUpdateModel::OAIBusinessUserUpdateModel() {
    this->initializeModel();
}

OAIBusinessUserUpdateModel::~OAIBusinessUserUpdateModel() {}

void OAIBusinessUserUpdateModel::initializeModel() {

    m_email_isSet = false;
    m_email_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_resource_id_isSet = false;
    m_resource_id_isValid = false;

    m_role_isSet = false;
    m_role_isValid = false;

    m_send_registration_invite_isSet = false;
    m_send_registration_invite_isValid = false;
}

void OAIBusinessUserUpdateModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBusinessUserUpdateModel::fromJsonObject(QJsonObject json) {

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_resource_id_isValid = ::OpenAPI::fromJsonValue(m_resource_id, json[QString("resourceId")]);
    m_resource_id_isSet = !json[QString("resourceId")].isNull() && m_resource_id_isValid;

    m_role_isValid = ::OpenAPI::fromJsonValue(m_role, json[QString("role")]);
    m_role_isSet = !json[QString("role")].isNull() && m_role_isValid;

    m_send_registration_invite_isValid = ::OpenAPI::fromJsonValue(m_send_registration_invite, json[QString("sendRegistrationInvite")]);
    m_send_registration_invite_isSet = !json[QString("sendRegistrationInvite")].isNull() && m_send_registration_invite_isValid;
}

QString OAIBusinessUserUpdateModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBusinessUserUpdateModel::asJsonObject() const {
    QJsonObject obj;
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_resource_id_isSet) {
        obj.insert(QString("resourceId"), ::OpenAPI::toJsonValue(m_resource_id));
    }
    if (m_role_isSet) {
        obj.insert(QString("role"), ::OpenAPI::toJsonValue(m_role));
    }
    if (m_send_registration_invite_isSet) {
        obj.insert(QString("sendRegistrationInvite"), ::OpenAPI::toJsonValue(m_send_registration_invite));
    }
    return obj;
}

QString OAIBusinessUserUpdateModel::getEmail() const {
    return m_email;
}
void OAIBusinessUserUpdateModel::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIBusinessUserUpdateModel::is_email_Set() const{
    return m_email_isSet;
}

bool OAIBusinessUserUpdateModel::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIBusinessUserUpdateModel::getName() const {
    return m_name;
}
void OAIBusinessUserUpdateModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBusinessUserUpdateModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBusinessUserUpdateModel::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIBusinessUserUpdateModel::getResourceId() const {
    return m_resource_id;
}
void OAIBusinessUserUpdateModel::setResourceId(const QString &resource_id) {
    m_resource_id = resource_id;
    m_resource_id_isSet = true;
}

bool OAIBusinessUserUpdateModel::is_resource_id_Set() const{
    return m_resource_id_isSet;
}

bool OAIBusinessUserUpdateModel::is_resource_id_Valid() const{
    return m_resource_id_isValid;
}

QString OAIBusinessUserUpdateModel::getRole() const {
    return m_role;
}
void OAIBusinessUserUpdateModel::setRole(const QString &role) {
    m_role = role;
    m_role_isSet = true;
}

bool OAIBusinessUserUpdateModel::is_role_Set() const{
    return m_role_isSet;
}

bool OAIBusinessUserUpdateModel::is_role_Valid() const{
    return m_role_isValid;
}

bool OAIBusinessUserUpdateModel::isSendRegistrationInvite() const {
    return m_send_registration_invite;
}
void OAIBusinessUserUpdateModel::setSendRegistrationInvite(const bool &send_registration_invite) {
    m_send_registration_invite = send_registration_invite;
    m_send_registration_invite_isSet = true;
}

bool OAIBusinessUserUpdateModel::is_send_registration_invite_Set() const{
    return m_send_registration_invite_isSet;
}

bool OAIBusinessUserUpdateModel::is_send_registration_invite_Valid() const{
    return m_send_registration_invite_isValid;
}

bool OAIBusinessUserUpdateModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_role_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_send_registration_invite_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBusinessUserUpdateModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
