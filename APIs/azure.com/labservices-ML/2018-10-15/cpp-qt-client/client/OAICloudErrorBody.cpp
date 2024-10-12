/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICloudErrorBody.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICloudErrorBody::OAICloudErrorBody(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICloudErrorBody::OAICloudErrorBody() {
    this->initializeModel();
}

OAICloudErrorBody::~OAICloudErrorBody() {}

void OAICloudErrorBody::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;
}

void OAICloudErrorBody::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICloudErrorBody::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("target")]);
    m_target_isSet = !json[QString("target")].isNull() && m_target_isValid;
}

QString OAICloudErrorBody::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICloudErrorBody::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_details.size() > 0) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_target_isSet) {
        obj.insert(QString("target"), ::OpenAPI::toJsonValue(m_target));
    }
    return obj;
}

QString OAICloudErrorBody::getCode() const {
    return m_code;
}
void OAICloudErrorBody::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAICloudErrorBody::is_code_Set() const{
    return m_code_isSet;
}

bool OAICloudErrorBody::is_code_Valid() const{
    return m_code_isValid;
}

QList<OAICloudErrorBody> OAICloudErrorBody::getDetails() const {
    return m_details;
}
void OAICloudErrorBody::setDetails(const QList<OAICloudErrorBody> &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAICloudErrorBody::is_details_Set() const{
    return m_details_isSet;
}

bool OAICloudErrorBody::is_details_Valid() const{
    return m_details_isValid;
}

QString OAICloudErrorBody::getMessage() const {
    return m_message;
}
void OAICloudErrorBody::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAICloudErrorBody::is_message_Set() const{
    return m_message_isSet;
}

bool OAICloudErrorBody::is_message_Valid() const{
    return m_message_isValid;
}

QString OAICloudErrorBody::getTarget() const {
    return m_target;
}
void OAICloudErrorBody::setTarget(const QString &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAICloudErrorBody::is_target_Set() const{
    return m_target_isSet;
}

bool OAICloudErrorBody::is_target_Valid() const{
    return m_target_isValid;
}

bool OAICloudErrorBody::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_details.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICloudErrorBody::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
