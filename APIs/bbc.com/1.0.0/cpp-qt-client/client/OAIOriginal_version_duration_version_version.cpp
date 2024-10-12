/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOriginal_version_duration_version_version.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOriginal_version_duration_version_version::OAIOriginal_version_duration_version_version(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOriginal_version_duration_version_version::OAIOriginal_version_duration_version_version() {
    this->initializeModel();
}

OAIOriginal_version_duration_version_version::~OAIOriginal_version_duration_version_version() {}

void OAIOriginal_version_duration_version_version::initializeModel() {

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_href_isSet = false;
    m_href_isValid = false;

    m_pid_isSet = false;
    m_pid_isValid = false;
}

void OAIOriginal_version_duration_version_version::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOriginal_version_duration_version_version::fromJsonObject(QJsonObject json) {

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_href_isValid = ::OpenAPI::fromJsonValue(m_href, json[QString("href")]);
    m_href_isSet = !json[QString("href")].isNull() && m_href_isValid;

    m_pid_isValid = ::OpenAPI::fromJsonValue(m_pid, json[QString("pid")]);
    m_pid_isSet = !json[QString("pid")].isNull() && m_pid_isValid;
}

QString OAIOriginal_version_duration_version_version::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOriginal_version_duration_version_version::asJsonObject() const {
    QJsonObject obj;
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_href_isSet) {
        obj.insert(QString("href"), ::OpenAPI::toJsonValue(m_href));
    }
    if (m_pid_isSet) {
        obj.insert(QString("pid"), ::OpenAPI::toJsonValue(m_pid));
    }
    return obj;
}

QString OAIOriginal_version_duration_version_version::getDuration() const {
    return m_duration;
}
void OAIOriginal_version_duration_version_version::setDuration(const QString &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIOriginal_version_duration_version_version::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIOriginal_version_duration_version_version::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAIOriginal_version_duration_version_version::getHref() const {
    return m_href;
}
void OAIOriginal_version_duration_version_version::setHref(const QString &href) {
    m_href = href;
    m_href_isSet = true;
}

bool OAIOriginal_version_duration_version_version::is_href_Set() const{
    return m_href_isSet;
}

bool OAIOriginal_version_duration_version_version::is_href_Valid() const{
    return m_href_isValid;
}

QString OAIOriginal_version_duration_version_version::getPid() const {
    return m_pid;
}
void OAIOriginal_version_duration_version_version::setPid(const QString &pid) {
    m_pid = pid;
    m_pid_isSet = true;
}

bool OAIOriginal_version_duration_version_version::is_pid_Set() const{
    return m_pid_isSet;
}

bool OAIOriginal_version_duration_version_version::is_pid_Valid() const{
    return m_pid_isValid;
}

bool OAIOriginal_version_duration_version_version::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_href_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOriginal_version_duration_version_version::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_href_isValid && m_pid_isValid && true;
}

} // namespace OpenAPI
