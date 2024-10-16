/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEmployeeResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEmployeeResponse::OAIEmployeeResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEmployeeResponse::OAIEmployeeResponse() {
    this->initializeModel();
}

OAIEmployeeResponse::~OAIEmployeeResponse() {}

void OAIEmployeeResponse::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAIEmployeeResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEmployeeResponse::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAIEmployeeResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEmployeeResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_data_isSet) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

OAIObject OAIEmployeeResponse::getData() const {
    return m_data;
}
void OAIEmployeeResponse::setData(const OAIObject &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIEmployeeResponse::is_data_Set() const{
    return m_data_isSet;
}

bool OAIEmployeeResponse::is_data_Valid() const{
    return m_data_isValid;
}

bool OAIEmployeeResponse::isSuccess() const {
    return m_success;
}
void OAIEmployeeResponse::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAIEmployeeResponse::is_success_Set() const{
    return m_success_isSet;
}

bool OAIEmployeeResponse::is_success_Valid() const{
    return m_success_isValid;
}

bool OAIEmployeeResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_isSet) {
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

bool OAIEmployeeResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_data_isValid && m_success_isValid && true;
}

} // namespace OpenAPI
