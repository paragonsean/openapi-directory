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

#include "OAIHybridConnectionCollection_value_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIHybridConnectionCollection_value_inner::OAIHybridConnectionCollection_value_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIHybridConnectionCollection_value_inner::OAIHybridConnectionCollection_value_inner() {
    this->initializeModel();
}

OAIHybridConnectionCollection_value_inner::~OAIHybridConnectionCollection_value_inner() {}

void OAIHybridConnectionCollection_value_inner::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIHybridConnectionCollection_value_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIHybridConnectionCollection_value_inner::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIHybridConnectionCollection_value_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIHybridConnectionCollection_value_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAIAppServicePlans_GetHybridConnection_200_response_properties OAIHybridConnectionCollection_value_inner::getProperties() const {
    return m_properties;
}
void OAIHybridConnectionCollection_value_inner::setProperties(const OAIAppServicePlans_GetHybridConnection_200_response_properties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIHybridConnectionCollection_value_inner::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIHybridConnectionCollection_value_inner::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIHybridConnectionCollection_value_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIHybridConnectionCollection_value_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
