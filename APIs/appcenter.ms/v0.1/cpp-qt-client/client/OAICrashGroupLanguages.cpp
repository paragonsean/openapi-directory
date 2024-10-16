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

#include "OAICrashGroupLanguages.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICrashGroupLanguages::OAICrashGroupLanguages(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICrashGroupLanguages::OAICrashGroupLanguages() {
    this->initializeModel();
}

OAICrashGroupLanguages::~OAICrashGroupLanguages() {}

void OAICrashGroupLanguages::initializeModel() {

    m_crash_count_isSet = false;
    m_crash_count_isValid = false;

    m_languages_isSet = false;
    m_languages_isValid = false;
}

void OAICrashGroupLanguages::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICrashGroupLanguages::fromJsonObject(QJsonObject json) {

    m_crash_count_isValid = ::OpenAPI::fromJsonValue(m_crash_count, json[QString("crash_count")]);
    m_crash_count_isSet = !json[QString("crash_count")].isNull() && m_crash_count_isValid;

    m_languages_isValid = ::OpenAPI::fromJsonValue(m_languages, json[QString("languages")]);
    m_languages_isSet = !json[QString("languages")].isNull() && m_languages_isValid;
}

QString OAICrashGroupLanguages::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICrashGroupLanguages::asJsonObject() const {
    QJsonObject obj;
    if (m_crash_count_isSet) {
        obj.insert(QString("crash_count"), ::OpenAPI::toJsonValue(m_crash_count));
    }
    if (m_languages.size() > 0) {
        obj.insert(QString("languages"), ::OpenAPI::toJsonValue(m_languages));
    }
    return obj;
}

qint64 OAICrashGroupLanguages::getCrashCount() const {
    return m_crash_count;
}
void OAICrashGroupLanguages::setCrashCount(const qint64 &crash_count) {
    m_crash_count = crash_count;
    m_crash_count_isSet = true;
}

bool OAICrashGroupLanguages::is_crash_count_Set() const{
    return m_crash_count_isSet;
}

bool OAICrashGroupLanguages::is_crash_count_Valid() const{
    return m_crash_count_isValid;
}

QList<OAICrashGroupLanguages_languages_inner> OAICrashGroupLanguages::getLanguages() const {
    return m_languages;
}
void OAICrashGroupLanguages::setLanguages(const QList<OAICrashGroupLanguages_languages_inner> &languages) {
    m_languages = languages;
    m_languages_isSet = true;
}

bool OAICrashGroupLanguages::is_languages_Set() const{
    return m_languages_isSet;
}

bool OAICrashGroupLanguages::is_languages_Valid() const{
    return m_languages_isValid;
}

bool OAICrashGroupLanguages::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_crash_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_languages.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICrashGroupLanguages::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
