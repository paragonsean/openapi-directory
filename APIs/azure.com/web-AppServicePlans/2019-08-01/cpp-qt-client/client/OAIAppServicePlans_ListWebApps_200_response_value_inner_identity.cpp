/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_identity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::OAIAppServicePlans_ListWebApps_200_response_value_inner_identity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::OAIAppServicePlans_ListWebApps_200_response_value_inner_identity() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::~OAIAppServicePlans_ListWebApps_200_response_value_inner_identity() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::initializeModel() {

    m_principal_id_isSet = false;
    m_principal_id_isValid = false;

    m_tenant_id_isSet = false;
    m_tenant_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_user_assigned_identities_isSet = false;
    m_user_assigned_identities_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::fromJsonObject(QJsonObject json) {

    m_principal_id_isValid = ::OpenAPI::fromJsonValue(m_principal_id, json[QString("principalId")]);
    m_principal_id_isSet = !json[QString("principalId")].isNull() && m_principal_id_isValid;

    m_tenant_id_isValid = ::OpenAPI::fromJsonValue(m_tenant_id, json[QString("tenantId")]);
    m_tenant_id_isSet = !json[QString("tenantId")].isNull() && m_tenant_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_user_assigned_identities_isValid = ::OpenAPI::fromJsonValue(m_user_assigned_identities, json[QString("userAssignedIdentities")]);
    m_user_assigned_identities_isSet = !json[QString("userAssignedIdentities")].isNull() && m_user_assigned_identities_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::asJsonObject() const {
    QJsonObject obj;
    if (m_principal_id_isSet) {
        obj.insert(QString("principalId"), ::OpenAPI::toJsonValue(m_principal_id));
    }
    if (m_tenant_id_isSet) {
        obj.insert(QString("tenantId"), ::OpenAPI::toJsonValue(m_tenant_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_user_assigned_identities.size() > 0) {
        obj.insert(QString("userAssignedIdentities"), ::OpenAPI::toJsonValue(m_user_assigned_identities));
    }
    return obj;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::getPrincipalId() const {
    return m_principal_id;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::setPrincipalId(const QString &principal_id) {
    m_principal_id = principal_id;
    m_principal_id_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::is_principal_id_Set() const{
    return m_principal_id_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::is_principal_id_Valid() const{
    return m_principal_id_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::getTenantId() const {
    return m_tenant_id;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::setTenantId(const QString &tenant_id) {
    m_tenant_id = tenant_id;
    m_tenant_id_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::is_tenant_id_Set() const{
    return m_tenant_id_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::is_tenant_id_Valid() const{
    return m_tenant_id_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::getType() const {
    return m_type;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::is_type_Valid() const{
    return m_type_isValid;
}

QMap<QString, OAIAppServicePlans_ListWebApps_200_response_value_inner_identity_userAssignedIdentities_value> OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::getUserAssignedIdentities() const {
    return m_user_assigned_identities;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::setUserAssignedIdentities(const QMap<QString, OAIAppServicePlans_ListWebApps_200_response_value_inner_identity_userAssignedIdentities_value> &user_assigned_identities) {
    m_user_assigned_identities = user_assigned_identities;
    m_user_assigned_identities_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::is_user_assigned_identities_Set() const{
    return m_user_assigned_identities_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::is_user_assigned_identities_Valid() const{
    return m_user_assigned_identities_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_principal_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tenant_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_assigned_identities.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_identity::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
