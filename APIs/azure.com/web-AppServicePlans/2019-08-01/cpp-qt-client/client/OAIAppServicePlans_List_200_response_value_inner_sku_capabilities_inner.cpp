/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner() {
    this->initializeModel();
}

OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::~OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner() {}

void OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::getName() const {
    return m_name;
}
void OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::getReason() const {
    return m_reason;
}
void OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::is_reason_Valid() const{
    return m_reason_isValid;
}

QString OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::getValue() const {
    return m_value;
}
void OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
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

bool OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
