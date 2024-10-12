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

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner() {
    this->initializeModel();
}

OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner() {}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::initializeModel() {

    m_physical_path_isSet = false;
    m_physical_path_isValid = false;

    m_preload_enabled_isSet = false;
    m_preload_enabled_isValid = false;

    m_virtual_directories_isSet = false;
    m_virtual_directories_isValid = false;

    m_virtual_path_isSet = false;
    m_virtual_path_isValid = false;
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::fromJsonObject(QJsonObject json) {

    m_physical_path_isValid = ::OpenAPI::fromJsonValue(m_physical_path, json[QString("physicalPath")]);
    m_physical_path_isSet = !json[QString("physicalPath")].isNull() && m_physical_path_isValid;

    m_preload_enabled_isValid = ::OpenAPI::fromJsonValue(m_preload_enabled, json[QString("preloadEnabled")]);
    m_preload_enabled_isSet = !json[QString("preloadEnabled")].isNull() && m_preload_enabled_isValid;

    m_virtual_directories_isValid = ::OpenAPI::fromJsonValue(m_virtual_directories, json[QString("virtualDirectories")]);
    m_virtual_directories_isSet = !json[QString("virtualDirectories")].isNull() && m_virtual_directories_isValid;

    m_virtual_path_isValid = ::OpenAPI::fromJsonValue(m_virtual_path, json[QString("virtualPath")]);
    m_virtual_path_isSet = !json[QString("virtualPath")].isNull() && m_virtual_path_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_physical_path_isSet) {
        obj.insert(QString("physicalPath"), ::OpenAPI::toJsonValue(m_physical_path));
    }
    if (m_preload_enabled_isSet) {
        obj.insert(QString("preloadEnabled"), ::OpenAPI::toJsonValue(m_preload_enabled));
    }
    if (m_virtual_directories.size() > 0) {
        obj.insert(QString("virtualDirectories"), ::OpenAPI::toJsonValue(m_virtual_directories));
    }
    if (m_virtual_path_isSet) {
        obj.insert(QString("virtualPath"), ::OpenAPI::toJsonValue(m_virtual_path));
    }
    return obj;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::getPhysicalPath() const {
    return m_physical_path;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::setPhysicalPath(const QString &physical_path) {
    m_physical_path = physical_path;
    m_physical_path_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::is_physical_path_Set() const{
    return m_physical_path_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::is_physical_path_Valid() const{
    return m_physical_path_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::isPreloadEnabled() const {
    return m_preload_enabled;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::setPreloadEnabled(const bool &preload_enabled) {
    m_preload_enabled = preload_enabled;
    m_preload_enabled_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::is_preload_enabled_Set() const{
    return m_preload_enabled_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::is_preload_enabled_Valid() const{
    return m_preload_enabled_isValid;
}

QList<OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner_virtualDirectories_inner> OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::getVirtualDirectories() const {
    return m_virtual_directories;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::setVirtualDirectories(const QList<OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner_virtualDirectories_inner> &virtual_directories) {
    m_virtual_directories = virtual_directories;
    m_virtual_directories_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::is_virtual_directories_Set() const{
    return m_virtual_directories_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::is_virtual_directories_Valid() const{
    return m_virtual_directories_isValid;
}

QString OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::getVirtualPath() const {
    return m_virtual_path;
}
void OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::setVirtualPath(const QString &virtual_path) {
    m_virtual_path = virtual_path;
    m_virtual_path_isSet = true;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::is_virtual_path_Set() const{
    return m_virtual_path_isSet;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::is_virtual_path_Valid() const{
    return m_virtual_path_isValid;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_physical_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_preload_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_virtual_directories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_virtual_path_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
