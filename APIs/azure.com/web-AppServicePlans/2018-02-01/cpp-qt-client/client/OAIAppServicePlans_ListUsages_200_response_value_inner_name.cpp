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

#include "OAIAppServicePlans_ListUsages_200_response_value_inner_name.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListUsages_200_response_value_inner_name::OAIAppServicePlans_ListUsages_200_response_value_inner_name(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListUsages_200_response_value_inner_name::OAIAppServicePlans_ListUsages_200_response_value_inner_name() {
    this->initializeModel();
}

OAIAppServicePlans_ListUsages_200_response_value_inner_name::~OAIAppServicePlans_ListUsages_200_response_value_inner_name() {}

void OAIAppServicePlans_ListUsages_200_response_value_inner_name::initializeModel() {

    m_localized_value_isSet = false;
    m_localized_value_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIAppServicePlans_ListUsages_200_response_value_inner_name::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListUsages_200_response_value_inner_name::fromJsonObject(QJsonObject json) {

    m_localized_value_isValid = ::OpenAPI::fromJsonValue(m_localized_value, json[QString("localizedValue")]);
    m_localized_value_isSet = !json[QString("localizedValue")].isNull() && m_localized_value_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIAppServicePlans_ListUsages_200_response_value_inner_name::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListUsages_200_response_value_inner_name::asJsonObject() const {
    QJsonObject obj;
    if (m_localized_value_isSet) {
        obj.insert(QString("localizedValue"), ::OpenAPI::toJsonValue(m_localized_value));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIAppServicePlans_ListUsages_200_response_value_inner_name::getLocalizedValue() const {
    return m_localized_value;
}
void OAIAppServicePlans_ListUsages_200_response_value_inner_name::setLocalizedValue(const QString &localized_value) {
    m_localized_value = localized_value;
    m_localized_value_isSet = true;
}

bool OAIAppServicePlans_ListUsages_200_response_value_inner_name::is_localized_value_Set() const{
    return m_localized_value_isSet;
}

bool OAIAppServicePlans_ListUsages_200_response_value_inner_name::is_localized_value_Valid() const{
    return m_localized_value_isValid;
}

QString OAIAppServicePlans_ListUsages_200_response_value_inner_name::getValue() const {
    return m_value;
}
void OAIAppServicePlans_ListUsages_200_response_value_inner_name::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIAppServicePlans_ListUsages_200_response_value_inner_name::is_value_Set() const{
    return m_value_isSet;
}

bool OAIAppServicePlans_ListUsages_200_response_value_inner_name::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIAppServicePlans_ListUsages_200_response_value_inner_name::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_localized_value_isSet) {
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

bool OAIAppServicePlans_ListUsages_200_response_value_inner_name::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
