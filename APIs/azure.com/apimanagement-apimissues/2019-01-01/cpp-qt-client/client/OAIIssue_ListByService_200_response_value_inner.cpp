/**
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
 *
 * The version of the OpenAPI document: 2019-01-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIssue_ListByService_200_response_value_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIssue_ListByService_200_response_value_inner::OAIIssue_ListByService_200_response_value_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIssue_ListByService_200_response_value_inner::OAIIssue_ListByService_200_response_value_inner() {
    this->initializeModel();
}

OAIIssue_ListByService_200_response_value_inner::~OAIIssue_ListByService_200_response_value_inner() {}

void OAIIssue_ListByService_200_response_value_inner::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAIIssue_ListByService_200_response_value_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIssue_ListByService_200_response_value_inner::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAIIssue_ListByService_200_response_value_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIssue_ListByService_200_response_value_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

OAIIssue_ListByService_200_response_value_inner_properties OAIIssue_ListByService_200_response_value_inner::getProperties() const {
    return m_properties;
}
void OAIIssue_ListByService_200_response_value_inner::setProperties(const OAIIssue_ListByService_200_response_value_inner_properties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIIssue_ListByService_200_response_value_inner::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIIssue_ListByService_200_response_value_inner::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAIIssue_ListByService_200_response_value_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIssue_ListByService_200_response_value_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
