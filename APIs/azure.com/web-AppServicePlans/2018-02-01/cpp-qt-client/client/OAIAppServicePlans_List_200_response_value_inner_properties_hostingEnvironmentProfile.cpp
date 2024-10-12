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

#include "OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile() {
    this->initializeModel();
}

OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::~OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile() {}

void OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::getId() const {
    return m_id;
}
void OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::getName() const {
    return m_name;
}
void OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::getType() const {
    return m_type;
}
void OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

bool OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
