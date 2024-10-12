/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEndpoint_patch_users__.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEndpoint_patch_users__::OAIEndpoint_patch_users__(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEndpoint_patch_users__::OAIEndpoint_patch_users__() {
    this->initializeModel();
}

OAIEndpoint_patch_users__::~OAIEndpoint_patch_users__() {}

void OAIEndpoint_patch_users__::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAIEndpoint_patch_users__::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEndpoint_patch_users__::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAIEndpoint_patch_users__::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEndpoint_patch_users__::asJsonObject() const {
    QJsonObject obj;
    if (m_data.isSet()) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

OAIMe OAIEndpoint_patch_users__::getData() const {
    return m_data;
}
void OAIEndpoint_patch_users__::setData(const OAIMe &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIEndpoint_patch_users__::is_data_Set() const{
    return m_data_isSet;
}

bool OAIEndpoint_patch_users__::is_data_Valid() const{
    return m_data_isValid;
}

bool OAIEndpoint_patch_users__::isSuccess() const {
    return m_success;
}
void OAIEndpoint_patch_users__::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAIEndpoint_patch_users__::is_success_Set() const{
    return m_success_isSet;
}

bool OAIEndpoint_patch_users__::is_success_Valid() const{
    return m_success_isValid;
}

bool OAIEndpoint_patch_users__::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEndpoint_patch_users__::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
