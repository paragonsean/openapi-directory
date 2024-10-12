/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICloudError.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICloudError::OAICloudError(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICloudError::OAICloudError() {
    this->initializeModel();
}

OAICloudError::~OAICloudError() {}

void OAICloudError::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;
}

void OAICloudError::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICloudError::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;
}

QString OAICloudError::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICloudError::asJsonObject() const {
    QJsonObject obj;
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    return obj;
}

OAICloudErrorBody OAICloudError::getError() const {
    return m_error;
}
void OAICloudError::setError(const OAICloudErrorBody &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAICloudError::is_error_Set() const{
    return m_error_isSet;
}

bool OAICloudError::is_error_Valid() const{
    return m_error_isValid;
}

bool OAICloudError::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICloudError::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
