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

#include "OAIPrivateCreateStoreRequest_intune_details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPrivateCreateStoreRequest_intune_details::OAIPrivateCreateStoreRequest_intune_details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPrivateCreateStoreRequest_intune_details::OAIPrivateCreateStoreRequest_intune_details() {
    this->initializeModel();
}

OAIPrivateCreateStoreRequest_intune_details::~OAIPrivateCreateStoreRequest_intune_details() {}

void OAIPrivateCreateStoreRequest_intune_details::initializeModel() {

    m_app_category_isSet = false;
    m_app_category_isValid = false;

    m_target_audience_isSet = false;
    m_target_audience_isValid = false;

    m_tenant_id_isSet = false;
    m_tenant_id_isValid = false;
}

void OAIPrivateCreateStoreRequest_intune_details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPrivateCreateStoreRequest_intune_details::fromJsonObject(QJsonObject json) {

    m_app_category_isValid = ::OpenAPI::fromJsonValue(m_app_category, json[QString("app_category")]);
    m_app_category_isSet = !json[QString("app_category")].isNull() && m_app_category_isValid;

    m_target_audience_isValid = ::OpenAPI::fromJsonValue(m_target_audience, json[QString("target_audience")]);
    m_target_audience_isSet = !json[QString("target_audience")].isNull() && m_target_audience_isValid;

    m_tenant_id_isValid = ::OpenAPI::fromJsonValue(m_tenant_id, json[QString("tenant_id")]);
    m_tenant_id_isSet = !json[QString("tenant_id")].isNull() && m_tenant_id_isValid;
}

QString OAIPrivateCreateStoreRequest_intune_details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPrivateCreateStoreRequest_intune_details::asJsonObject() const {
    QJsonObject obj;
    if (m_app_category.isSet()) {
        obj.insert(QString("app_category"), ::OpenAPI::toJsonValue(m_app_category));
    }
    if (m_target_audience.isSet()) {
        obj.insert(QString("target_audience"), ::OpenAPI::toJsonValue(m_target_audience));
    }
    if (m_tenant_id_isSet) {
        obj.insert(QString("tenant_id"), ::OpenAPI::toJsonValue(m_tenant_id));
    }
    return obj;
}

OAIStores_create_request_intune_details_app_category OAIPrivateCreateStoreRequest_intune_details::getAppCategory() const {
    return m_app_category;
}
void OAIPrivateCreateStoreRequest_intune_details::setAppCategory(const OAIStores_create_request_intune_details_app_category &app_category) {
    m_app_category = app_category;
    m_app_category_isSet = true;
}

bool OAIPrivateCreateStoreRequest_intune_details::is_app_category_Set() const{
    return m_app_category_isSet;
}

bool OAIPrivateCreateStoreRequest_intune_details::is_app_category_Valid() const{
    return m_app_category_isValid;
}

OAIStores_create_request_intune_details_target_audience OAIPrivateCreateStoreRequest_intune_details::getTargetAudience() const {
    return m_target_audience;
}
void OAIPrivateCreateStoreRequest_intune_details::setTargetAudience(const OAIStores_create_request_intune_details_target_audience &target_audience) {
    m_target_audience = target_audience;
    m_target_audience_isSet = true;
}

bool OAIPrivateCreateStoreRequest_intune_details::is_target_audience_Set() const{
    return m_target_audience_isSet;
}

bool OAIPrivateCreateStoreRequest_intune_details::is_target_audience_Valid() const{
    return m_target_audience_isValid;
}

QString OAIPrivateCreateStoreRequest_intune_details::getTenantId() const {
    return m_tenant_id;
}
void OAIPrivateCreateStoreRequest_intune_details::setTenantId(const QString &tenant_id) {
    m_tenant_id = tenant_id;
    m_tenant_id_isSet = true;
}

bool OAIPrivateCreateStoreRequest_intune_details::is_tenant_id_Set() const{
    return m_tenant_id_isSet;
}

bool OAIPrivateCreateStoreRequest_intune_details::is_tenant_id_Valid() const{
    return m_tenant_id_isValid;
}

bool OAIPrivateCreateStoreRequest_intune_details::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_category.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_audience.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tenant_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPrivateCreateStoreRequest_intune_details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
