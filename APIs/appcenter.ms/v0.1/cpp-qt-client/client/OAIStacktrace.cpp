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

#include "OAIStacktrace.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStacktrace::OAIStacktrace(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStacktrace::OAIStacktrace() {
    this->initializeModel();
}

OAIStacktrace::~OAIStacktrace() {}

void OAIStacktrace::initializeModel() {

    m_exception_isSet = false;
    m_exception_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;

    m_threads_isSet = false;
    m_threads_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIStacktrace::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStacktrace::fromJsonObject(QJsonObject json) {

    m_exception_isValid = ::OpenAPI::fromJsonValue(m_exception, json[QString("exception")]);
    m_exception_isSet = !json[QString("exception")].isNull() && m_exception_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;

    m_threads_isValid = ::OpenAPI::fromJsonValue(m_threads, json[QString("threads")]);
    m_threads_isSet = !json[QString("threads")].isNull() && m_threads_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAIStacktrace::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStacktrace::asJsonObject() const {
    QJsonObject obj;
    if (m_exception.isSet()) {
        obj.insert(QString("exception"), ::OpenAPI::toJsonValue(m_exception));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    if (m_threads.size() > 0) {
        obj.insert(QString("threads"), ::OpenAPI::toJsonValue(m_threads));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

OAIException OAIStacktrace::getException() const {
    return m_exception;
}
void OAIStacktrace::setException(const OAIException &exception) {
    m_exception = exception;
    m_exception_isSet = true;
}

bool OAIStacktrace::is_exception_Set() const{
    return m_exception_isSet;
}

bool OAIStacktrace::is_exception_Valid() const{
    return m_exception_isValid;
}

QString OAIStacktrace::getReason() const {
    return m_reason;
}
void OAIStacktrace::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIStacktrace::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIStacktrace::is_reason_Valid() const{
    return m_reason_isValid;
}

QList<OAIThread> OAIStacktrace::getThreads() const {
    return m_threads;
}
void OAIStacktrace::setThreads(const QList<OAIThread> &threads) {
    m_threads = threads;
    m_threads_isSet = true;
}

bool OAIStacktrace::is_threads_Set() const{
    return m_threads_isSet;
}

bool OAIStacktrace::is_threads_Valid() const{
    return m_threads_isValid;
}

QString OAIStacktrace::getTitle() const {
    return m_title;
}
void OAIStacktrace::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIStacktrace::is_title_Set() const{
    return m_title_isSet;
}

bool OAIStacktrace::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIStacktrace::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_exception.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_threads.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStacktrace::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
