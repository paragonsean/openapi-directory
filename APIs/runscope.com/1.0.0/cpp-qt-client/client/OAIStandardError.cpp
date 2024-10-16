/**
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStandardError.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStandardError::OAIStandardError(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStandardError::OAIStandardError() {
    this->initializeModel();
}

OAIStandardError::~OAIStandardError() {}

void OAIStandardError::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_meta_isSet = false;
    m_meta_isValid = false;
}

void OAIStandardError::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStandardError::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_meta_isValid = ::OpenAPI::fromJsonValue(m_meta, json[QString("meta")]);
    m_meta_isSet = !json[QString("meta")].isNull() && m_meta_isValid;
}

QString OAIStandardError::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStandardError::asJsonObject() const {
    QJsonObject obj;
    if (m_data_isSet) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_error.isSet()) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_meta.isSet()) {
        obj.insert(QString("meta"), ::OpenAPI::toJsonValue(m_meta));
    }
    return obj;
}

OAIObject OAIStandardError::getData() const {
    return m_data;
}
void OAIStandardError::setData(const OAIObject &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIStandardError::is_data_Set() const{
    return m_data_isSet;
}

bool OAIStandardError::is_data_Valid() const{
    return m_data_isValid;
}

OAIError400 OAIStandardError::getError() const {
    return m_error;
}
void OAIStandardError::setError(const OAIError400 &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIStandardError::is_error_Set() const{
    return m_error_isSet;
}

bool OAIStandardError::is_error_Valid() const{
    return m_error_isValid;
}

OAIMeta OAIStandardError::getMeta() const {
    return m_meta;
}
void OAIStandardError::setMeta(const OAIMeta &meta) {
    m_meta = meta;
    m_meta_isSet = true;
}

bool OAIStandardError::is_meta_Set() const{
    return m_meta_isSet;
}

bool OAIStandardError::is_meta_Valid() const{
    return m_meta_isValid;
}

bool OAIStandardError::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStandardError::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
