/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner() {
    this->initializeModel();
}

OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::~OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner() {}

void OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::getName() const {
    return m_name;
}
void OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::getValue() const {
    return m_value;
}
void OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDeploymentLocations_hostingEnvironments_inner_clusterSettings_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
