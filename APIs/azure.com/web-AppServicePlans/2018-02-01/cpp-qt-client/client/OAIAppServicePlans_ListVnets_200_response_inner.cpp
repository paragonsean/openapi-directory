/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListVnets_200_response_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListVnets_200_response_inner::OAIAppServicePlans_ListVnets_200_response_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListVnets_200_response_inner::OAIAppServicePlans_ListVnets_200_response_inner() {
    this->initializeModel();
}

OAIAppServicePlans_ListVnets_200_response_inner::~OAIAppServicePlans_ListVnets_200_response_inner() {}

void OAIAppServicePlans_ListVnets_200_response_inner::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIAppServicePlans_ListVnets_200_response_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListVnets_200_response_inner::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIAppServicePlans_ListVnets_200_response_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListVnets_200_response_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAIAppServicePlans_ListVnets_200_response_inner_properties OAIAppServicePlans_ListVnets_200_response_inner::getProperties() const {
    return m_properties;
}
void OAIAppServicePlans_ListVnets_200_response_inner::setProperties(const OAIAppServicePlans_ListVnets_200_response_inner_properties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIAppServicePlans_ListVnets_200_response_inner::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIAppServicePlans_ListVnets_200_response_inner::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIAppServicePlans_ListVnets_200_response_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListVnets_200_response_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
