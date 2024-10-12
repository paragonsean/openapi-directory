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

#include "OAI_buckets__bucketKey__messages_post_200_response_data_inner_error.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::OAI_buckets__bucketKey__messages_post_200_response_data_inner_error(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::OAI_buckets__bucketKey__messages_post_200_response_data_inner_error() {
    this->initializeModel();
}

OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::~OAI_buckets__bucketKey__messages_post_200_response_data_inner_error() {}

void OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_more_info_isSet = false;
    m_more_info_isValid = false;
}

void OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_more_info_isValid = ::OpenAPI::fromJsonValue(m_more_info, json[QString("more_info")]);
    m_more_info_isSet = !json[QString("more_info")].isNull() && m_more_info_isValid;
}

QString OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_more_info_isSet) {
        obj.insert(QString("more_info"), ::OpenAPI::toJsonValue(m_more_info));
    }
    return obj;
}

qint32 OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::getCode() const {
    return m_code;
}
void OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::setCode(const qint32 &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::is_code_Set() const{
    return m_code_isSet;
}

bool OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::is_code_Valid() const{
    return m_code_isValid;
}

QString OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::getMessage() const {
    return m_message;
}
void OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::is_message_Set() const{
    return m_message_isSet;
}

bool OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::is_message_Valid() const{
    return m_message_isValid;
}

QString OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::getMoreInfo() const {
    return m_more_info;
}
void OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::setMoreInfo(const QString &more_info) {
    m_more_info = more_info;
    m_more_info_isSet = true;
}

bool OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::is_more_info_Set() const{
    return m_more_info_isSet;
}

bool OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::is_more_info_Valid() const{
    return m_more_info_isValid;
}

bool OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_more_info_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_buckets__bucketKey__messages_post_200_response_data_inner_error::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
