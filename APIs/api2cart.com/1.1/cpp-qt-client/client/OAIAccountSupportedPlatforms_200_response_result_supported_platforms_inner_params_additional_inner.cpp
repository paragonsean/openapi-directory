/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner() {
    this->initializeModel();
}

OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::~OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner() {}

void OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::getDescription() const {
    return m_description;
}
void OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::getName() const {
    return m_name;
}
void OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAccountSupportedPlatforms_200_response_result_supported_platforms_inner_params_additional_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
