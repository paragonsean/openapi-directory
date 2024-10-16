/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDiagnosticsException.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDiagnosticsException::OAIDiagnosticsException(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDiagnosticsException::OAIDiagnosticsException() {
    this->initializeModel();
}

OAIDiagnosticsException::~OAIDiagnosticsException() {}

void OAIDiagnosticsException::initializeModel() {

    m_frames_isSet = false;
    m_frames_isValid = false;

    m_inner_exceptions_isSet = false;
    m_inner_exceptions_isValid = false;

    m_platform_isSet = false;
    m_platform_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;

    m_relevant_isSet = false;
    m_relevant_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIDiagnosticsException::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDiagnosticsException::fromJsonObject(QJsonObject json) {

    m_frames_isValid = ::OpenAPI::fromJsonValue(m_frames, json[QString("frames")]);
    m_frames_isSet = !json[QString("frames")].isNull() && m_frames_isValid;

    m_inner_exceptions_isValid = ::OpenAPI::fromJsonValue(m_inner_exceptions, json[QString("inner_exceptions")]);
    m_inner_exceptions_isSet = !json[QString("inner_exceptions")].isNull() && m_inner_exceptions_isValid;

    m_platform_isValid = ::OpenAPI::fromJsonValue(m_platform, json[QString("platform")]);
    m_platform_isSet = !json[QString("platform")].isNull() && m_platform_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;

    m_relevant_isValid = ::OpenAPI::fromJsonValue(m_relevant, json[QString("relevant")]);
    m_relevant_isSet = !json[QString("relevant")].isNull() && m_relevant_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIDiagnosticsException::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDiagnosticsException::asJsonObject() const {
    QJsonObject obj;
    if (m_frames.size() > 0) {
        obj.insert(QString("frames"), ::OpenAPI::toJsonValue(m_frames));
    }
    if (m_inner_exceptions.size() > 0) {
        obj.insert(QString("inner_exceptions"), ::OpenAPI::toJsonValue(m_inner_exceptions));
    }
    if (m_platform_isSet) {
        obj.insert(QString("platform"), ::OpenAPI::toJsonValue(m_platform));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    if (m_relevant_isSet) {
        obj.insert(QString("relevant"), ::OpenAPI::toJsonValue(m_relevant));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QList<OAIDiagnosticsException_frames_inner> OAIDiagnosticsException::getFrames() const {
    return m_frames;
}
void OAIDiagnosticsException::setFrames(const QList<OAIDiagnosticsException_frames_inner> &frames) {
    m_frames = frames;
    m_frames_isSet = true;
}

bool OAIDiagnosticsException::is_frames_Set() const{
    return m_frames_isSet;
}

bool OAIDiagnosticsException::is_frames_Valid() const{
    return m_frames_isValid;
}

QList<OAIDiagnosticsException> OAIDiagnosticsException::getInnerExceptions() const {
    return m_inner_exceptions;
}
void OAIDiagnosticsException::setInnerExceptions(const QList<OAIDiagnosticsException> &inner_exceptions) {
    m_inner_exceptions = inner_exceptions;
    m_inner_exceptions_isSet = true;
}

bool OAIDiagnosticsException::is_inner_exceptions_Set() const{
    return m_inner_exceptions_isSet;
}

bool OAIDiagnosticsException::is_inner_exceptions_Valid() const{
    return m_inner_exceptions_isValid;
}

QString OAIDiagnosticsException::getPlatform() const {
    return m_platform;
}
void OAIDiagnosticsException::setPlatform(const QString &platform) {
    m_platform = platform;
    m_platform_isSet = true;
}

bool OAIDiagnosticsException::is_platform_Set() const{
    return m_platform_isSet;
}

bool OAIDiagnosticsException::is_platform_Valid() const{
    return m_platform_isValid;
}

QString OAIDiagnosticsException::getReason() const {
    return m_reason;
}
void OAIDiagnosticsException::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIDiagnosticsException::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIDiagnosticsException::is_reason_Valid() const{
    return m_reason_isValid;
}

bool OAIDiagnosticsException::isRelevant() const {
    return m_relevant;
}
void OAIDiagnosticsException::setRelevant(const bool &relevant) {
    m_relevant = relevant;
    m_relevant_isSet = true;
}

bool OAIDiagnosticsException::is_relevant_Set() const{
    return m_relevant_isSet;
}

bool OAIDiagnosticsException::is_relevant_Valid() const{
    return m_relevant_isValid;
}

QString OAIDiagnosticsException::getType() const {
    return m_type;
}
void OAIDiagnosticsException::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIDiagnosticsException::is_type_Set() const{
    return m_type_isSet;
}

bool OAIDiagnosticsException::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIDiagnosticsException::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_frames.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_inner_exceptions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_platform_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relevant_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDiagnosticsException::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_frames_isValid && true;
}

} // namespace OpenAPI
