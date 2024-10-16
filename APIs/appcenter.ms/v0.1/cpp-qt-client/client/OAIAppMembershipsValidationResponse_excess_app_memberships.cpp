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

#include "OAIAppMembershipsValidationResponse_excess_app_memberships.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppMembershipsValidationResponse_excess_app_memberships::OAIAppMembershipsValidationResponse_excess_app_memberships(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppMembershipsValidationResponse_excess_app_memberships::OAIAppMembershipsValidationResponse_excess_app_memberships() {
    this->initializeModel();
}

OAIAppMembershipsValidationResponse_excess_app_memberships::~OAIAppMembershipsValidationResponse_excess_app_memberships() {}

void OAIAppMembershipsValidationResponse_excess_app_memberships::initializeModel() {

    m_app_users_memberships_isSet = false;
    m_app_users_memberships_isValid = false;

    m_distribution_group_memberships_isSet = false;
    m_distribution_group_memberships_isValid = false;

    m_organization_admin_memberships_isSet = false;
    m_organization_admin_memberships_isValid = false;
}

void OAIAppMembershipsValidationResponse_excess_app_memberships::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppMembershipsValidationResponse_excess_app_memberships::fromJsonObject(QJsonObject json) {

    m_app_users_memberships_isValid = ::OpenAPI::fromJsonValue(m_app_users_memberships, json[QString("app_users_memberships")]);
    m_app_users_memberships_isSet = !json[QString("app_users_memberships")].isNull() && m_app_users_memberships_isValid;

    m_distribution_group_memberships_isValid = ::OpenAPI::fromJsonValue(m_distribution_group_memberships, json[QString("distribution_group_memberships")]);
    m_distribution_group_memberships_isSet = !json[QString("distribution_group_memberships")].isNull() && m_distribution_group_memberships_isValid;

    m_organization_admin_memberships_isValid = ::OpenAPI::fromJsonValue(m_organization_admin_memberships, json[QString("organization_admin_memberships")]);
    m_organization_admin_memberships_isSet = !json[QString("organization_admin_memberships")].isNull() && m_organization_admin_memberships_isValid;
}

QString OAIAppMembershipsValidationResponse_excess_app_memberships::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppMembershipsValidationResponse_excess_app_memberships::asJsonObject() const {
    QJsonObject obj;
    if (m_app_users_memberships.size() > 0) {
        obj.insert(QString("app_users_memberships"), ::OpenAPI::toJsonValue(m_app_users_memberships));
    }
    if (m_distribution_group_memberships.size() > 0) {
        obj.insert(QString("distribution_group_memberships"), ::OpenAPI::toJsonValue(m_distribution_group_memberships));
    }
    if (m_organization_admin_memberships.size() > 0) {
        obj.insert(QString("organization_admin_memberships"), ::OpenAPI::toJsonValue(m_organization_admin_memberships));
    }
    return obj;
}

QList<OAIAppMembershipsResponse_memberships_inner> OAIAppMembershipsValidationResponse_excess_app_memberships::getAppUsersMemberships() const {
    return m_app_users_memberships;
}
void OAIAppMembershipsValidationResponse_excess_app_memberships::setAppUsersMemberships(const QList<OAIAppMembershipsResponse_memberships_inner> &app_users_memberships) {
    m_app_users_memberships = app_users_memberships;
    m_app_users_memberships_isSet = true;
}

bool OAIAppMembershipsValidationResponse_excess_app_memberships::is_app_users_memberships_Set() const{
    return m_app_users_memberships_isSet;
}

bool OAIAppMembershipsValidationResponse_excess_app_memberships::is_app_users_memberships_Valid() const{
    return m_app_users_memberships_isValid;
}

QList<OAIAppMembershipsResponse_memberships_inner> OAIAppMembershipsValidationResponse_excess_app_memberships::getDistributionGroupMemberships() const {
    return m_distribution_group_memberships;
}
void OAIAppMembershipsValidationResponse_excess_app_memberships::setDistributionGroupMemberships(const QList<OAIAppMembershipsResponse_memberships_inner> &distribution_group_memberships) {
    m_distribution_group_memberships = distribution_group_memberships;
    m_distribution_group_memberships_isSet = true;
}

bool OAIAppMembershipsValidationResponse_excess_app_memberships::is_distribution_group_memberships_Set() const{
    return m_distribution_group_memberships_isSet;
}

bool OAIAppMembershipsValidationResponse_excess_app_memberships::is_distribution_group_memberships_Valid() const{
    return m_distribution_group_memberships_isValid;
}

QList<OAIAppMembershipsResponse_memberships_inner> OAIAppMembershipsValidationResponse_excess_app_memberships::getOrganizationAdminMemberships() const {
    return m_organization_admin_memberships;
}
void OAIAppMembershipsValidationResponse_excess_app_memberships::setOrganizationAdminMemberships(const QList<OAIAppMembershipsResponse_memberships_inner> &organization_admin_memberships) {
    m_organization_admin_memberships = organization_admin_memberships;
    m_organization_admin_memberships_isSet = true;
}

bool OAIAppMembershipsValidationResponse_excess_app_memberships::is_organization_admin_memberships_Set() const{
    return m_organization_admin_memberships_isSet;
}

bool OAIAppMembershipsValidationResponse_excess_app_memberships::is_organization_admin_memberships_Valid() const{
    return m_organization_admin_memberships_isValid;
}

bool OAIAppMembershipsValidationResponse_excess_app_memberships::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_users_memberships.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_distribution_group_memberships.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_organization_admin_memberships.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppMembershipsValidationResponse_excess_app_memberships::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
