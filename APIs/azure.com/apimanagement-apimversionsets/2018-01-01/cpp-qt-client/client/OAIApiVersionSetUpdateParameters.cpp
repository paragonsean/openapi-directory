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

#include "OAIApiVersionSetUpdateParameters.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApiVersionSetUpdateParameters::OAIApiVersionSetUpdateParameters(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApiVersionSetUpdateParameters::OAIApiVersionSetUpdateParameters() {
    this->initializeModel();
}

OAIApiVersionSetUpdateParameters::~OAIApiVersionSetUpdateParameters() {}

void OAIApiVersionSetUpdateParameters::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIApiVersionSetUpdateParameters::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApiVersionSetUpdateParameters::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIApiVersionSetUpdateParameters::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApiVersionSetUpdateParameters::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAIApiVersionSetUpdateParametersProperties OAIApiVersionSetUpdateParameters::getProperties() const {
    return m_properties;
}
void OAIApiVersionSetUpdateParameters::setProperties(const OAIApiVersionSetUpdateParametersProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIApiVersionSetUpdateParameters::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIApiVersionSetUpdateParameters::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIApiVersionSetUpdateParameters::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApiVersionSetUpdateParameters::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
