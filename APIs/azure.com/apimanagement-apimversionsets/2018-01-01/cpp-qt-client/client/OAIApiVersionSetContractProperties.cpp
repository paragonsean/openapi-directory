/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on the ApiVersionSet entity associated with your Azure API Management deployment. Using this entity you create and manage API Version Sets that are used to group APIs for consistent versioning.
 *
 * The version of the OpenAPI document: 2018-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApiVersionSetContractProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApiVersionSetContractProperties::OAIApiVersionSetContractProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApiVersionSetContractProperties::OAIApiVersionSetContractProperties() {
    this->initializeModel();
}

OAIApiVersionSetContractProperties::~OAIApiVersionSetContractProperties() {}

void OAIApiVersionSetContractProperties::initializeModel() {

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_versioning_scheme_isSet = false;
    m_versioning_scheme_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_version_header_name_isSet = false;
    m_version_header_name_isValid = false;

    m_version_query_name_isSet = false;
    m_version_query_name_isValid = false;
}

void OAIApiVersionSetContractProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApiVersionSetContractProperties::fromJsonObject(QJsonObject json) {

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_versioning_scheme_isValid = ::OpenAPI::fromJsonValue(m_versioning_scheme, json[QString("versioningScheme")]);
    m_versioning_scheme_isSet = !json[QString("versioningScheme")].isNull() && m_versioning_scheme_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_version_header_name_isValid = ::OpenAPI::fromJsonValue(m_version_header_name, json[QString("versionHeaderName")]);
    m_version_header_name_isSet = !json[QString("versionHeaderName")].isNull() && m_version_header_name_isValid;

    m_version_query_name_isValid = ::OpenAPI::fromJsonValue(m_version_query_name, json[QString("versionQueryName")]);
    m_version_query_name_isSet = !json[QString("versionQueryName")].isNull() && m_version_query_name_isValid;
}

QString OAIApiVersionSetContractProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApiVersionSetContractProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_versioning_scheme_isSet) {
        obj.insert(QString("versioningScheme"), ::OpenAPI::toJsonValue(m_versioning_scheme));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_version_header_name_isSet) {
        obj.insert(QString("versionHeaderName"), ::OpenAPI::toJsonValue(m_version_header_name));
    }
    if (m_version_query_name_isSet) {
        obj.insert(QString("versionQueryName"), ::OpenAPI::toJsonValue(m_version_query_name));
    }
    return obj;
}

QString OAIApiVersionSetContractProperties::getDisplayName() const {
    return m_display_name;
}
void OAIApiVersionSetContractProperties::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIApiVersionSetContractProperties::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIApiVersionSetContractProperties::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIApiVersionSetContractProperties::getVersioningScheme() const {
    return m_versioning_scheme;
}
void OAIApiVersionSetContractProperties::setVersioningScheme(const QString &versioning_scheme) {
    m_versioning_scheme = versioning_scheme;
    m_versioning_scheme_isSet = true;
}

bool OAIApiVersionSetContractProperties::is_versioning_scheme_Set() const{
    return m_versioning_scheme_isSet;
}

bool OAIApiVersionSetContractProperties::is_versioning_scheme_Valid() const{
    return m_versioning_scheme_isValid;
}

QString OAIApiVersionSetContractProperties::getDescription() const {
    return m_description;
}
void OAIApiVersionSetContractProperties::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIApiVersionSetContractProperties::is_description_Set() const{
    return m_description_isSet;
}

bool OAIApiVersionSetContractProperties::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIApiVersionSetContractProperties::getVersionHeaderName() const {
    return m_version_header_name;
}
void OAIApiVersionSetContractProperties::setVersionHeaderName(const QString &version_header_name) {
    m_version_header_name = version_header_name;
    m_version_header_name_isSet = true;
}

bool OAIApiVersionSetContractProperties::is_version_header_name_Set() const{
    return m_version_header_name_isSet;
}

bool OAIApiVersionSetContractProperties::is_version_header_name_Valid() const{
    return m_version_header_name_isValid;
}

QString OAIApiVersionSetContractProperties::getVersionQueryName() const {
    return m_version_query_name;
}
void OAIApiVersionSetContractProperties::setVersionQueryName(const QString &version_query_name) {
    m_version_query_name = version_query_name;
    m_version_query_name_isSet = true;
}

bool OAIApiVersionSetContractProperties::is_version_query_name_Set() const{
    return m_version_query_name_isSet;
}

bool OAIApiVersionSetContractProperties::is_version_query_name_Valid() const{
    return m_version_query_name_isValid;
}

bool OAIApiVersionSetContractProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_versioning_scheme_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_header_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_query_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApiVersionSetContractProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_display_name_isValid && m_versioning_scheme_isValid && true;
}

} // namespace OpenAPI
