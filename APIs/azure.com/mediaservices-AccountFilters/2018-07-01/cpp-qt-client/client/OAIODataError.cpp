/**
 * Azure Media Services
 * This Swagger was generated by the API Framework.
 *
 * The version of the OpenAPI document: 2018-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIODataError.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIODataError::OAIODataError(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIODataError::OAIODataError() {
    this->initializeModel();
}

OAIODataError::~OAIODataError() {}

void OAIODataError::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;
}

void OAIODataError::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIODataError::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("target")]);
    m_target_isSet = !json[QString("target")].isNull() && m_target_isValid;
}

QString OAIODataError::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIODataError::asJsonObject() const {
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

QString OAIODataError::getCode() const {
    return m_code;
}
void OAIODataError::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIODataError::is_code_Set() const{
    return m_code_isSet;
}

bool OAIODataError::is_code_Valid() const{
    return m_code_isValid;
}

QList<OAIODataError> OAIODataError::getDetails() const {
    return m_details;
}
void OAIODataError::setDetails(const QList<OAIODataError> &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAIODataError::is_details_Set() const{
    return m_details_isSet;
}

bool OAIODataError::is_details_Valid() const{
    return m_details_isValid;
}

QString OAIODataError::getMessage() const {
    return m_message;
}
void OAIODataError::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIODataError::is_message_Set() const{
    return m_message_isSet;
}

bool OAIODataError::is_message_Valid() const{
    return m_message_isValid;
}

QString OAIODataError::getTarget() const {
    return m_target;
}
void OAIODataError::setTarget(const QString &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAIODataError::is_target_Set() const{
    return m_target_isSet;
}

bool OAIODataError::is_target_Valid() const{
    return m_target_isValid;
}

bool OAIODataError::isSet() const {
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

bool OAIODataError::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
