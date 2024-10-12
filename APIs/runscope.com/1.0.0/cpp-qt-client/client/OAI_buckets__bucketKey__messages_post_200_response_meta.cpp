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

#include "OAI_buckets__bucketKey__messages_post_200_response_meta.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_buckets__bucketKey__messages_post_200_response_meta::OAI_buckets__bucketKey__messages_post_200_response_meta(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_buckets__bucketKey__messages_post_200_response_meta::OAI_buckets__bucketKey__messages_post_200_response_meta() {
    this->initializeModel();
}

OAI_buckets__bucketKey__messages_post_200_response_meta::~OAI_buckets__bucketKey__messages_post_200_response_meta() {}

void OAI_buckets__bucketKey__messages_post_200_response_meta::initializeModel() {

    m_error_count_isSet = false;
    m_error_count_isValid = false;

    m_succcess_count_isSet = false;
    m_succcess_count_isValid = false;

    m_warning_count_isSet = false;
    m_warning_count_isValid = false;
}

void OAI_buckets__bucketKey__messages_post_200_response_meta::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_buckets__bucketKey__messages_post_200_response_meta::fromJsonObject(QJsonObject json) {

    m_error_count_isValid = ::OpenAPI::fromJsonValue(m_error_count, json[QString("error_count")]);
    m_error_count_isSet = !json[QString("error_count")].isNull() && m_error_count_isValid;

    m_succcess_count_isValid = ::OpenAPI::fromJsonValue(m_succcess_count, json[QString("succcess_count")]);
    m_succcess_count_isSet = !json[QString("succcess_count")].isNull() && m_succcess_count_isValid;

    m_warning_count_isValid = ::OpenAPI::fromJsonValue(m_warning_count, json[QString("warning_count")]);
    m_warning_count_isSet = !json[QString("warning_count")].isNull() && m_warning_count_isValid;
}

QString OAI_buckets__bucketKey__messages_post_200_response_meta::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_buckets__bucketKey__messages_post_200_response_meta::asJsonObject() const {
    QJsonObject obj;
    if (m_error_count_isSet) {
        obj.insert(QString("error_count"), ::OpenAPI::toJsonValue(m_error_count));
    }
    if (m_succcess_count_isSet) {
        obj.insert(QString("succcess_count"), ::OpenAPI::toJsonValue(m_succcess_count));
    }
    if (m_warning_count_isSet) {
        obj.insert(QString("warning_count"), ::OpenAPI::toJsonValue(m_warning_count));
    }
    return obj;
}

qint32 OAI_buckets__bucketKey__messages_post_200_response_meta::getErrorCount() const {
    return m_error_count;
}
void OAI_buckets__bucketKey__messages_post_200_response_meta::setErrorCount(const qint32 &error_count) {
    m_error_count = error_count;
    m_error_count_isSet = true;
}

bool OAI_buckets__bucketKey__messages_post_200_response_meta::is_error_count_Set() const{
    return m_error_count_isSet;
}

bool OAI_buckets__bucketKey__messages_post_200_response_meta::is_error_count_Valid() const{
    return m_error_count_isValid;
}

qint32 OAI_buckets__bucketKey__messages_post_200_response_meta::getSucccessCount() const {
    return m_succcess_count;
}
void OAI_buckets__bucketKey__messages_post_200_response_meta::setSucccessCount(const qint32 &succcess_count) {
    m_succcess_count = succcess_count;
    m_succcess_count_isSet = true;
}

bool OAI_buckets__bucketKey__messages_post_200_response_meta::is_succcess_count_Set() const{
    return m_succcess_count_isSet;
}

bool OAI_buckets__bucketKey__messages_post_200_response_meta::is_succcess_count_Valid() const{
    return m_succcess_count_isValid;
}

qint32 OAI_buckets__bucketKey__messages_post_200_response_meta::getWarningCount() const {
    return m_warning_count;
}
void OAI_buckets__bucketKey__messages_post_200_response_meta::setWarningCount(const qint32 &warning_count) {
    m_warning_count = warning_count;
    m_warning_count_isSet = true;
}

bool OAI_buckets__bucketKey__messages_post_200_response_meta::is_warning_count_Set() const{
    return m_warning_count_isSet;
}

bool OAI_buckets__bucketKey__messages_post_200_response_meta::is_warning_count_Valid() const{
    return m_warning_count_isValid;
}

bool OAI_buckets__bucketKey__messages_post_200_response_meta::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_error_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_succcess_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_warning_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_buckets__bucketKey__messages_post_200_response_meta::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
