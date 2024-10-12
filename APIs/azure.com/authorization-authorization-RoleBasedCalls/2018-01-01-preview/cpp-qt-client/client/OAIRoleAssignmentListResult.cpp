/**
 * AuthorizationManagementClient
 * Role based access control provides you a way to apply granular level policy administration down to individual resources or resource groups. These operations enable you to manage role definitions and role assignments. A role definition describes the set of actions that can be performed on resources. A role assignment grants access to Azure Active Directory users.
 *
 * The version of the OpenAPI document: 2018-01-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRoleAssignmentListResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRoleAssignmentListResult::OAIRoleAssignmentListResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRoleAssignmentListResult::OAIRoleAssignmentListResult() {
    this->initializeModel();
}

OAIRoleAssignmentListResult::~OAIRoleAssignmentListResult() {}

void OAIRoleAssignmentListResult::initializeModel() {

    m_next_link_isSet = false;
    m_next_link_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIRoleAssignmentListResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRoleAssignmentListResult::fromJsonObject(QJsonObject json) {

    m_next_link_isValid = ::OpenAPI::fromJsonValue(m_next_link, json[QString("nextLink")]);
    m_next_link_isSet = !json[QString("nextLink")].isNull() && m_next_link_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIRoleAssignmentListResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRoleAssignmentListResult::asJsonObject() const {
    QJsonObject obj;
    if (m_next_link_isSet) {
        obj.insert(QString("nextLink"), ::OpenAPI::toJsonValue(m_next_link));
    }
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIRoleAssignmentListResult::getNextLink() const {
    return m_next_link;
}
void OAIRoleAssignmentListResult::setNextLink(const QString &next_link) {
    m_next_link = next_link;
    m_next_link_isSet = true;
}

bool OAIRoleAssignmentListResult::is_next_link_Set() const{
    return m_next_link_isSet;
}

bool OAIRoleAssignmentListResult::is_next_link_Valid() const{
    return m_next_link_isValid;
}

QList<OAIRoleAssignment> OAIRoleAssignmentListResult::getValue() const {
    return m_value;
}
void OAIRoleAssignmentListResult::setValue(const QList<OAIRoleAssignment> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIRoleAssignmentListResult::is_value_Set() const{
    return m_value_isSet;
}

bool OAIRoleAssignmentListResult::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIRoleAssignmentListResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_next_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRoleAssignmentListResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
