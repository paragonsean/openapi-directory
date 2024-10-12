/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties() {
    this->initializeModel();
}

OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::~OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties() {}

void OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    return obj;
}

QString OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::getId() const {
    return m_id;
}
void OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::is_id_Set() const{
    return m_id_isSet;
}

bool OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListSiteIdentifiersAssignedToHostName_200_response_value_inner_properties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
