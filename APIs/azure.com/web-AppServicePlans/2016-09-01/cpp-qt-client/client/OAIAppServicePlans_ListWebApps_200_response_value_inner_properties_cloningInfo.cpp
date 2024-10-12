/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::initializeModel() {

    m_app_settings_overrides_isSet = false;
    m_app_settings_overrides_isValid = false;

    m_clone_custom_host_names_isSet = false;
    m_clone_custom_host_names_isValid = false;

    m_clone_source_control_isSet = false;
    m_clone_source_control_isValid = false;

    m_configure_load_balancing_isSet = false;
    m_configure_load_balancing_isValid = false;

    m_correlation_id_isSet = false;
    m_correlation_id_isValid = false;

    m_hosting_environment_isSet = false;
    m_hosting_environment_isValid = false;

    m_ignore_quotas_isSet = false;
    m_ignore_quotas_isValid = false;

    m_overwrite_isSet = false;
    m_overwrite_isValid = false;

    m_source_web_app_id_isSet = false;
    m_source_web_app_id_isValid = false;

    m_traffic_manager_profile_id_isSet = false;
    m_traffic_manager_profile_id_isValid = false;

    m_traffic_manager_profile_name_isSet = false;
    m_traffic_manager_profile_name_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::fromJsonObject(QJsonObject json) {

    m_app_settings_overrides_isValid = ::OpenAPI::fromJsonValue(m_app_settings_overrides, json[QString("appSettingsOverrides")]);
    m_app_settings_overrides_isSet = !json[QString("appSettingsOverrides")].isNull() && m_app_settings_overrides_isValid;

    m_clone_custom_host_names_isValid = ::OpenAPI::fromJsonValue(m_clone_custom_host_names, json[QString("cloneCustomHostNames")]);
    m_clone_custom_host_names_isSet = !json[QString("cloneCustomHostNames")].isNull() && m_clone_custom_host_names_isValid;

    m_clone_source_control_isValid = ::OpenAPI::fromJsonValue(m_clone_source_control, json[QString("cloneSourceControl")]);
    m_clone_source_control_isSet = !json[QString("cloneSourceControl")].isNull() && m_clone_source_control_isValid;

    m_configure_load_balancing_isValid = ::OpenAPI::fromJsonValue(m_configure_load_balancing, json[QString("configureLoadBalancing")]);
    m_configure_load_balancing_isSet = !json[QString("configureLoadBalancing")].isNull() && m_configure_load_balancing_isValid;

    m_correlation_id_isValid = ::OpenAPI::fromJsonValue(m_correlation_id, json[QString("correlationId")]);
    m_correlation_id_isSet = !json[QString("correlationId")].isNull() && m_correlation_id_isValid;

    m_hosting_environment_isValid = ::OpenAPI::fromJsonValue(m_hosting_environment, json[QString("hostingEnvironment")]);
    m_hosting_environment_isSet = !json[QString("hostingEnvironment")].isNull() && m_hosting_environment_isValid;

    m_ignore_quotas_isValid = ::OpenAPI::fromJsonValue(m_ignore_quotas, json[QString("ignoreQuotas")]);
    m_ignore_quotas_isSet = !json[QString("ignoreQuotas")].isNull() && m_ignore_quotas_isValid;

    m_overwrite_isValid = ::OpenAPI::fromJsonValue(m_overwrite, json[QString("overwrite")]);
    m_overwrite_isSet = !json[QString("overwrite")].isNull() && m_overwrite_isValid;

    m_source_web_app_id_isValid = ::OpenAPI::fromJsonValue(m_source_web_app_id, json[QString("sourceWebAppId")]);
    m_source_web_app_id_isSet = !json[QString("sourceWebAppId")].isNull() && m_source_web_app_id_isValid;

    m_traffic_manager_profile_id_isValid = ::OpenAPI::fromJsonValue(m_traffic_manager_profile_id, json[QString("trafficManagerProfileId")]);
    m_traffic_manager_profile_id_isSet = !json[QString("trafficManagerProfileId")].isNull() && m_traffic_manager_profile_id_isValid;

    m_traffic_manager_profile_name_isValid = ::OpenAPI::fromJsonValue(m_traffic_manager_profile_name, json[QString("trafficManagerProfileName")]);
    m_traffic_manager_profile_name_isSet = !json[QString("trafficManagerProfileName")].isNull() && m_traffic_manager_profile_name_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_app_settings_overrides.size() > 0) {
        obj.insert(QString("appSettingsOverrides"), ::OpenAPI::toJsonValue(m_app_settings_overrides));
    }
    if (m_clone_custom_host_names_isSet) {
        obj.insert(QString("cloneCustomHostNames"), ::OpenAPI::toJsonValue(m_clone_custom_host_names));
    }
    if (m_clone_source_control_isSet) {
        obj.insert(QString("cloneSourceControl"), ::OpenAPI::toJsonValue(m_clone_source_control));
    }
    if (m_configure_load_balancing_isSet) {
        obj.insert(QString("configureLoadBalancing"), ::OpenAPI::toJsonValue(m_configure_load_balancing));
    }
    if (m_correlation_id_isSet) {
        obj.insert(QString("correlationId"), ::OpenAPI::toJsonValue(m_correlation_id));
    }
    if (m_hosting_environment_isSet) {
        obj.insert(QString("hostingEnvironment"), ::OpenAPI::toJsonValue(m_hosting_environment));
    }
    if (m_ignore_quotas_isSet) {
        obj.insert(QString("ignoreQuotas"), ::OpenAPI::toJsonValue(m_ignore_quotas));
    }
    if (m_overwrite_isSet) {
        obj.insert(QString("overwrite"), ::OpenAPI::toJsonValue(m_overwrite));
    }
    if (m_source_web_app_id_isSet) {
        obj.insert(QString("sourceWebAppId"), ::OpenAPI::toJsonValue(m_source_web_app_id));
    }
    if (m_traffic_manager_profile_id_isSet) {
        obj.insert(QString("trafficManagerProfileId"), ::OpenAPI::toJsonValue(m_traffic_manager_profile_id));
    }
    if (m_traffic_manager_profile_name_isSet) {
        obj.insert(QString("trafficManagerProfileName"), ::OpenAPI::toJsonValue(m_traffic_manager_profile_name));
    }
    return obj;
}

QMap<QString, QString> OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::getAppSettingsOverrides() const {
    return m_app_settings_overrides;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setAppSettingsOverrides(const QMap<QString, QString> &app_settings_overrides) {
    m_app_settings_overrides = app_settings_overrides;
    m_app_settings_overrides_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_app_settings_overrides_Set() const{
    return m_app_settings_overrides_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_app_settings_overrides_Valid() const{
    return m_app_settings_overrides_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::isCloneCustomHostNames() const {
    return m_clone_custom_host_names;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setCloneCustomHostNames(const bool &clone_custom_host_names) {
    m_clone_custom_host_names = clone_custom_host_names;
    m_clone_custom_host_names_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_clone_custom_host_names_Set() const{
    return m_clone_custom_host_names_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_clone_custom_host_names_Valid() const{
    return m_clone_custom_host_names_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::isCloneSourceControl() const {
    return m_clone_source_control;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setCloneSourceControl(const bool &clone_source_control) {
    m_clone_source_control = clone_source_control;
    m_clone_source_control_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_clone_source_control_Set() const{
    return m_clone_source_control_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_clone_source_control_Valid() const{
    return m_clone_source_control_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::isConfigureLoadBalancing() const {
    return m_configure_load_balancing;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setConfigureLoadBalancing(const bool &configure_load_balancing) {
    m_configure_load_balancing = configure_load_balancing;
    m_configure_load_balancing_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_configure_load_balancing_Set() const{
    return m_configure_load_balancing_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_configure_load_balancing_Valid() const{
    return m_configure_load_balancing_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::getCorrelationId() const {
    return m_correlation_id;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setCorrelationId(const QString &correlation_id) {
    m_correlation_id = correlation_id;
    m_correlation_id_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_correlation_id_Set() const{
    return m_correlation_id_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_correlation_id_Valid() const{
    return m_correlation_id_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::getHostingEnvironment() const {
    return m_hosting_environment;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setHostingEnvironment(const QString &hosting_environment) {
    m_hosting_environment = hosting_environment;
    m_hosting_environment_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_hosting_environment_Set() const{
    return m_hosting_environment_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_hosting_environment_Valid() const{
    return m_hosting_environment_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::isIgnoreQuotas() const {
    return m_ignore_quotas;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setIgnoreQuotas(const bool &ignore_quotas) {
    m_ignore_quotas = ignore_quotas;
    m_ignore_quotas_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_ignore_quotas_Set() const{
    return m_ignore_quotas_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_ignore_quotas_Valid() const{
    return m_ignore_quotas_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::isOverwrite() const {
    return m_overwrite;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setOverwrite(const bool &overwrite) {
    m_overwrite = overwrite;
    m_overwrite_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_overwrite_Set() const{
    return m_overwrite_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_overwrite_Valid() const{
    return m_overwrite_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::getSourceWebAppId() const {
    return m_source_web_app_id;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setSourceWebAppId(const QString &source_web_app_id) {
    m_source_web_app_id = source_web_app_id;
    m_source_web_app_id_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_source_web_app_id_Set() const{
    return m_source_web_app_id_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_source_web_app_id_Valid() const{
    return m_source_web_app_id_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::getTrafficManagerProfileId() const {
    return m_traffic_manager_profile_id;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setTrafficManagerProfileId(const QString &traffic_manager_profile_id) {
    m_traffic_manager_profile_id = traffic_manager_profile_id;
    m_traffic_manager_profile_id_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_traffic_manager_profile_id_Set() const{
    return m_traffic_manager_profile_id_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_traffic_manager_profile_id_Valid() const{
    return m_traffic_manager_profile_id_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::getTrafficManagerProfileName() const {
    return m_traffic_manager_profile_name;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::setTrafficManagerProfileName(const QString &traffic_manager_profile_name) {
    m_traffic_manager_profile_name = traffic_manager_profile_name;
    m_traffic_manager_profile_name_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_traffic_manager_profile_name_Set() const{
    return m_traffic_manager_profile_name_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::is_traffic_manager_profile_name_Valid() const{
    return m_traffic_manager_profile_name_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_settings_overrides.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_clone_custom_host_names_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_clone_source_control_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_configure_load_balancing_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_correlation_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hosting_environment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ignore_quotas_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_overwrite_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_web_app_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_traffic_manager_profile_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_traffic_manager_profile_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_source_web_app_id_isValid && true;
}

} // namespace OpenAPI
