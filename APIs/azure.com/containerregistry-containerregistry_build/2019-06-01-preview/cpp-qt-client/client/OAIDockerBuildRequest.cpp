/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDockerBuildRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDockerBuildRequest::OAIDockerBuildRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDockerBuildRequest::OAIDockerBuildRequest() {
    this->initializeModel();
}

OAIDockerBuildRequest::~OAIDockerBuildRequest() {}

void OAIDockerBuildRequest::initializeModel() {

    m_agent_configuration_isSet = false;
    m_agent_configuration_isValid = false;

    m_arguments_isSet = false;
    m_arguments_isValid = false;

    m_credentials_isSet = false;
    m_credentials_isValid = false;

    m_docker_file_path_isSet = false;
    m_docker_file_path_isValid = false;

    m_image_names_isSet = false;
    m_image_names_isValid = false;

    m_is_push_enabled_isSet = false;
    m_is_push_enabled_isValid = false;

    m_no_cache_isSet = false;
    m_no_cache_isValid = false;

    m_platform_isSet = false;
    m_platform_isValid = false;

    m_source_location_isSet = false;
    m_source_location_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;

    m_timeout_isSet = false;
    m_timeout_isValid = false;

    m_is_archive_enabled_isSet = false;
    m_is_archive_enabled_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIDockerBuildRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDockerBuildRequest::fromJsonObject(QJsonObject json) {

    m_agent_configuration_isValid = ::OpenAPI::fromJsonValue(m_agent_configuration, json[QString("agentConfiguration")]);
    m_agent_configuration_isSet = !json[QString("agentConfiguration")].isNull() && m_agent_configuration_isValid;

    m_arguments_isValid = ::OpenAPI::fromJsonValue(m_arguments, json[QString("arguments")]);
    m_arguments_isSet = !json[QString("arguments")].isNull() && m_arguments_isValid;

    m_credentials_isValid = ::OpenAPI::fromJsonValue(m_credentials, json[QString("credentials")]);
    m_credentials_isSet = !json[QString("credentials")].isNull() && m_credentials_isValid;

    m_docker_file_path_isValid = ::OpenAPI::fromJsonValue(m_docker_file_path, json[QString("dockerFilePath")]);
    m_docker_file_path_isSet = !json[QString("dockerFilePath")].isNull() && m_docker_file_path_isValid;

    m_image_names_isValid = ::OpenAPI::fromJsonValue(m_image_names, json[QString("imageNames")]);
    m_image_names_isSet = !json[QString("imageNames")].isNull() && m_image_names_isValid;

    m_is_push_enabled_isValid = ::OpenAPI::fromJsonValue(m_is_push_enabled, json[QString("isPushEnabled")]);
    m_is_push_enabled_isSet = !json[QString("isPushEnabled")].isNull() && m_is_push_enabled_isValid;

    m_no_cache_isValid = ::OpenAPI::fromJsonValue(m_no_cache, json[QString("noCache")]);
    m_no_cache_isSet = !json[QString("noCache")].isNull() && m_no_cache_isValid;

    m_platform_isValid = ::OpenAPI::fromJsonValue(m_platform, json[QString("platform")]);
    m_platform_isSet = !json[QString("platform")].isNull() && m_platform_isValid;

    m_source_location_isValid = ::OpenAPI::fromJsonValue(m_source_location, json[QString("sourceLocation")]);
    m_source_location_isSet = !json[QString("sourceLocation")].isNull() && m_source_location_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("target")]);
    m_target_isSet = !json[QString("target")].isNull() && m_target_isValid;

    m_timeout_isValid = ::OpenAPI::fromJsonValue(m_timeout, json[QString("timeout")]);
    m_timeout_isSet = !json[QString("timeout")].isNull() && m_timeout_isValid;

    m_is_archive_enabled_isValid = ::OpenAPI::fromJsonValue(m_is_archive_enabled, json[QString("isArchiveEnabled")]);
    m_is_archive_enabled_isSet = !json[QString("isArchiveEnabled")].isNull() && m_is_archive_enabled_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIDockerBuildRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDockerBuildRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_agent_configuration.isSet()) {
        obj.insert(QString("agentConfiguration"), ::OpenAPI::toJsonValue(m_agent_configuration));
    }
    if (m_arguments.size() > 0) {
        obj.insert(QString("arguments"), ::OpenAPI::toJsonValue(m_arguments));
    }
    if (m_credentials.isSet()) {
        obj.insert(QString("credentials"), ::OpenAPI::toJsonValue(m_credentials));
    }
    if (m_docker_file_path_isSet) {
        obj.insert(QString("dockerFilePath"), ::OpenAPI::toJsonValue(m_docker_file_path));
    }
    if (m_image_names.size() > 0) {
        obj.insert(QString("imageNames"), ::OpenAPI::toJsonValue(m_image_names));
    }
    if (m_is_push_enabled_isSet) {
        obj.insert(QString("isPushEnabled"), ::OpenAPI::toJsonValue(m_is_push_enabled));
    }
    if (m_no_cache_isSet) {
        obj.insert(QString("noCache"), ::OpenAPI::toJsonValue(m_no_cache));
    }
    if (m_platform.isSet()) {
        obj.insert(QString("platform"), ::OpenAPI::toJsonValue(m_platform));
    }
    if (m_source_location_isSet) {
        obj.insert(QString("sourceLocation"), ::OpenAPI::toJsonValue(m_source_location));
    }
    if (m_target_isSet) {
        obj.insert(QString("target"), ::OpenAPI::toJsonValue(m_target));
    }
    if (m_timeout_isSet) {
        obj.insert(QString("timeout"), ::OpenAPI::toJsonValue(m_timeout));
    }
    if (m_is_archive_enabled_isSet) {
        obj.insert(QString("isArchiveEnabled"), ::OpenAPI::toJsonValue(m_is_archive_enabled));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIAgentProperties OAIDockerBuildRequest::getAgentConfiguration() const {
    return m_agent_configuration;
}
void OAIDockerBuildRequest::setAgentConfiguration(const OAIAgentProperties &agent_configuration) {
    m_agent_configuration = agent_configuration;
    m_agent_configuration_isSet = true;
}

bool OAIDockerBuildRequest::is_agent_configuration_Set() const{
    return m_agent_configuration_isSet;
}

bool OAIDockerBuildRequest::is_agent_configuration_Valid() const{
    return m_agent_configuration_isValid;
}

QList<OAIArgument> OAIDockerBuildRequest::getArguments() const {
    return m_arguments;
}
void OAIDockerBuildRequest::setArguments(const QList<OAIArgument> &arguments) {
    m_arguments = arguments;
    m_arguments_isSet = true;
}

bool OAIDockerBuildRequest::is_arguments_Set() const{
    return m_arguments_isSet;
}

bool OAIDockerBuildRequest::is_arguments_Valid() const{
    return m_arguments_isValid;
}

OAICredentials OAIDockerBuildRequest::getCredentials() const {
    return m_credentials;
}
void OAIDockerBuildRequest::setCredentials(const OAICredentials &credentials) {
    m_credentials = credentials;
    m_credentials_isSet = true;
}

bool OAIDockerBuildRequest::is_credentials_Set() const{
    return m_credentials_isSet;
}

bool OAIDockerBuildRequest::is_credentials_Valid() const{
    return m_credentials_isValid;
}

QString OAIDockerBuildRequest::getDockerFilePath() const {
    return m_docker_file_path;
}
void OAIDockerBuildRequest::setDockerFilePath(const QString &docker_file_path) {
    m_docker_file_path = docker_file_path;
    m_docker_file_path_isSet = true;
}

bool OAIDockerBuildRequest::is_docker_file_path_Set() const{
    return m_docker_file_path_isSet;
}

bool OAIDockerBuildRequest::is_docker_file_path_Valid() const{
    return m_docker_file_path_isValid;
}

QList<QString> OAIDockerBuildRequest::getImageNames() const {
    return m_image_names;
}
void OAIDockerBuildRequest::setImageNames(const QList<QString> &image_names) {
    m_image_names = image_names;
    m_image_names_isSet = true;
}

bool OAIDockerBuildRequest::is_image_names_Set() const{
    return m_image_names_isSet;
}

bool OAIDockerBuildRequest::is_image_names_Valid() const{
    return m_image_names_isValid;
}

bool OAIDockerBuildRequest::isIsPushEnabled() const {
    return m_is_push_enabled;
}
void OAIDockerBuildRequest::setIsPushEnabled(const bool &is_push_enabled) {
    m_is_push_enabled = is_push_enabled;
    m_is_push_enabled_isSet = true;
}

bool OAIDockerBuildRequest::is_is_push_enabled_Set() const{
    return m_is_push_enabled_isSet;
}

bool OAIDockerBuildRequest::is_is_push_enabled_Valid() const{
    return m_is_push_enabled_isValid;
}

bool OAIDockerBuildRequest::isNoCache() const {
    return m_no_cache;
}
void OAIDockerBuildRequest::setNoCache(const bool &no_cache) {
    m_no_cache = no_cache;
    m_no_cache_isSet = true;
}

bool OAIDockerBuildRequest::is_no_cache_Set() const{
    return m_no_cache_isSet;
}

bool OAIDockerBuildRequest::is_no_cache_Valid() const{
    return m_no_cache_isValid;
}

OAIPlatformProperties OAIDockerBuildRequest::getPlatform() const {
    return m_platform;
}
void OAIDockerBuildRequest::setPlatform(const OAIPlatformProperties &platform) {
    m_platform = platform;
    m_platform_isSet = true;
}

bool OAIDockerBuildRequest::is_platform_Set() const{
    return m_platform_isSet;
}

bool OAIDockerBuildRequest::is_platform_Valid() const{
    return m_platform_isValid;
}

QString OAIDockerBuildRequest::getSourceLocation() const {
    return m_source_location;
}
void OAIDockerBuildRequest::setSourceLocation(const QString &source_location) {
    m_source_location = source_location;
    m_source_location_isSet = true;
}

bool OAIDockerBuildRequest::is_source_location_Set() const{
    return m_source_location_isSet;
}

bool OAIDockerBuildRequest::is_source_location_Valid() const{
    return m_source_location_isValid;
}

QString OAIDockerBuildRequest::getTarget() const {
    return m_target;
}
void OAIDockerBuildRequest::setTarget(const QString &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAIDockerBuildRequest::is_target_Set() const{
    return m_target_isSet;
}

bool OAIDockerBuildRequest::is_target_Valid() const{
    return m_target_isValid;
}

qint32 OAIDockerBuildRequest::getTimeout() const {
    return m_timeout;
}
void OAIDockerBuildRequest::setTimeout(const qint32 &timeout) {
    m_timeout = timeout;
    m_timeout_isSet = true;
}

bool OAIDockerBuildRequest::is_timeout_Set() const{
    return m_timeout_isSet;
}

bool OAIDockerBuildRequest::is_timeout_Valid() const{
    return m_timeout_isValid;
}

bool OAIDockerBuildRequest::isIsArchiveEnabled() const {
    return m_is_archive_enabled;
}
void OAIDockerBuildRequest::setIsArchiveEnabled(const bool &is_archive_enabled) {
    m_is_archive_enabled = is_archive_enabled;
    m_is_archive_enabled_isSet = true;
}

bool OAIDockerBuildRequest::is_is_archive_enabled_Set() const{
    return m_is_archive_enabled_isSet;
}

bool OAIDockerBuildRequest::is_is_archive_enabled_Valid() const{
    return m_is_archive_enabled_isValid;
}

QString OAIDockerBuildRequest::getType() const {
    return m_type;
}
void OAIDockerBuildRequest::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIDockerBuildRequest::is_type_Set() const{
    return m_type_isSet;
}

bool OAIDockerBuildRequest::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIDockerBuildRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_agent_configuration.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_arguments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_credentials.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_docker_file_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_names.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_push_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_no_cache_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_platform.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_archive_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDockerBuildRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_docker_file_path_isValid && m_platform_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
