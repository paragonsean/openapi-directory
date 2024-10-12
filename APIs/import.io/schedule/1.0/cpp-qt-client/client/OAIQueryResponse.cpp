/**
 * import.io
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQueryResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQueryResponse::OAIQueryResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQueryResponse::OAIQueryResponse() {
    this->initializeModel();
}

OAIQueryResponse::~OAIQueryResponse() {}

void OAIQueryResponse::initializeModel() {

    m_error_isSet = false;
    m_error_isValid = false;

    m_exception_type_isSet = false;
    m_exception_type_isValid = false;

    m_extractor_data_isSet = false;
    m_extractor_data_isValid = false;

    m_page_data_isSet = false;
    m_page_data_isValid = false;

    m_runtime_config_id_isSet = false;
    m_runtime_config_id_isValid = false;

    m_sequence_number_isSet = false;
    m_sequence_number_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIQueryResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQueryResponse::fromJsonObject(QJsonObject json) {

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_exception_type_isValid = ::OpenAPI::fromJsonValue(m_exception_type, json[QString("exceptionType")]);
    m_exception_type_isSet = !json[QString("exceptionType")].isNull() && m_exception_type_isValid;

    m_extractor_data_isValid = ::OpenAPI::fromJsonValue(m_extractor_data, json[QString("extractorData")]);
    m_extractor_data_isSet = !json[QString("extractorData")].isNull() && m_extractor_data_isValid;

    m_page_data_isValid = ::OpenAPI::fromJsonValue(m_page_data, json[QString("pageData")]);
    m_page_data_isSet = !json[QString("pageData")].isNull() && m_page_data_isValid;

    m_runtime_config_id_isValid = ::OpenAPI::fromJsonValue(m_runtime_config_id, json[QString("runtimeConfigId")]);
    m_runtime_config_id_isSet = !json[QString("runtimeConfigId")].isNull() && m_runtime_config_id_isValid;

    m_sequence_number_isValid = ::OpenAPI::fromJsonValue(m_sequence_number, json[QString("sequenceNumber")]);
    m_sequence_number_isSet = !json[QString("sequenceNumber")].isNull() && m_sequence_number_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAIQueryResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQueryResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_exception_type_isSet) {
        obj.insert(QString("exceptionType"), ::OpenAPI::toJsonValue(m_exception_type));
    }
    if (m_extractor_data_isSet) {
        obj.insert(QString("extractorData"), ::OpenAPI::toJsonValue(m_extractor_data));
    }
    if (m_page_data_isSet) {
        obj.insert(QString("pageData"), ::OpenAPI::toJsonValue(m_page_data));
    }
    if (m_runtime_config_id_isSet) {
        obj.insert(QString("runtimeConfigId"), ::OpenAPI::toJsonValue(m_runtime_config_id));
    }
    if (m_sequence_number_isSet) {
        obj.insert(QString("sequenceNumber"), ::OpenAPI::toJsonValue(m_sequence_number));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

QString OAIQueryResponse::getError() const {
    return m_error;
}
void OAIQueryResponse::setError(const QString &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIQueryResponse::is_error_Set() const{
    return m_error_isSet;
}

bool OAIQueryResponse::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIQueryResponse::getExceptionType() const {
    return m_exception_type;
}
void OAIQueryResponse::setExceptionType(const QString &exception_type) {
    m_exception_type = exception_type;
    m_exception_type_isSet = true;
}

bool OAIQueryResponse::is_exception_type_Set() const{
    return m_exception_type_isSet;
}

bool OAIQueryResponse::is_exception_type_Valid() const{
    return m_exception_type_isValid;
}

OAIObject OAIQueryResponse::getExtractorData() const {
    return m_extractor_data;
}
void OAIQueryResponse::setExtractorData(const OAIObject &extractor_data) {
    m_extractor_data = extractor_data;
    m_extractor_data_isSet = true;
}

bool OAIQueryResponse::is_extractor_data_Set() const{
    return m_extractor_data_isSet;
}

bool OAIQueryResponse::is_extractor_data_Valid() const{
    return m_extractor_data_isValid;
}

OAIObject OAIQueryResponse::getPageData() const {
    return m_page_data;
}
void OAIQueryResponse::setPageData(const OAIObject &page_data) {
    m_page_data = page_data;
    m_page_data_isSet = true;
}

bool OAIQueryResponse::is_page_data_Set() const{
    return m_page_data_isSet;
}

bool OAIQueryResponse::is_page_data_Valid() const{
    return m_page_data_isValid;
}

QString OAIQueryResponse::getRuntimeConfigId() const {
    return m_runtime_config_id;
}
void OAIQueryResponse::setRuntimeConfigId(const QString &runtime_config_id) {
    m_runtime_config_id = runtime_config_id;
    m_runtime_config_id_isSet = true;
}

bool OAIQueryResponse::is_runtime_config_id_Set() const{
    return m_runtime_config_id_isSet;
}

bool OAIQueryResponse::is_runtime_config_id_Valid() const{
    return m_runtime_config_id_isValid;
}

qint32 OAIQueryResponse::getSequenceNumber() const {
    return m_sequence_number;
}
void OAIQueryResponse::setSequenceNumber(const qint32 &sequence_number) {
    m_sequence_number = sequence_number;
    m_sequence_number_isSet = true;
}

bool OAIQueryResponse::is_sequence_number_Set() const{
    return m_sequence_number_isSet;
}

bool OAIQueryResponse::is_sequence_number_Valid() const{
    return m_sequence_number_isValid;
}

qint64 OAIQueryResponse::getTimestamp() const {
    return m_timestamp;
}
void OAIQueryResponse::setTimestamp(const qint64 &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAIQueryResponse::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAIQueryResponse::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

QString OAIQueryResponse::getUrl() const {
    return m_url;
}
void OAIQueryResponse::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIQueryResponse::is_url_Set() const{
    return m_url_isSet;
}

bool OAIQueryResponse::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIQueryResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exception_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extractor_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_runtime_config_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sequence_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQueryResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
