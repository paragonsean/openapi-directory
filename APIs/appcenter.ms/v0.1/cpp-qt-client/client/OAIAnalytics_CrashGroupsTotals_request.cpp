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

#include "OAIAnalytics_CrashGroupsTotals_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAnalytics_CrashGroupsTotals_request::OAIAnalytics_CrashGroupsTotals_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAnalytics_CrashGroupsTotals_request::OAIAnalytics_CrashGroupsTotals_request() {
    this->initializeModel();
}

OAIAnalytics_CrashGroupsTotals_request::~OAIAnalytics_CrashGroupsTotals_request() {}

void OAIAnalytics_CrashGroupsTotals_request::initializeModel() {

    m_crash_groups_isSet = false;
    m_crash_groups_isValid = false;
}

void OAIAnalytics_CrashGroupsTotals_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAnalytics_CrashGroupsTotals_request::fromJsonObject(QJsonObject json) {

    m_crash_groups_isValid = ::OpenAPI::fromJsonValue(m_crash_groups, json[QString("crash_groups")]);
    m_crash_groups_isSet = !json[QString("crash_groups")].isNull() && m_crash_groups_isValid;
}

QString OAIAnalytics_CrashGroupsTotals_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAnalytics_CrashGroupsTotals_request::asJsonObject() const {
    QJsonObject obj;
    if (m_crash_groups.size() > 0) {
        obj.insert(QString("crash_groups"), ::OpenAPI::toJsonValue(m_crash_groups));
    }
    return obj;
}

QList<OAIAnalytics_CrashGroupsTotals_request_crash_groups_inner> OAIAnalytics_CrashGroupsTotals_request::getCrashGroups() const {
    return m_crash_groups;
}
void OAIAnalytics_CrashGroupsTotals_request::setCrashGroups(const QList<OAIAnalytics_CrashGroupsTotals_request_crash_groups_inner> &crash_groups) {
    m_crash_groups = crash_groups;
    m_crash_groups_isSet = true;
}

bool OAIAnalytics_CrashGroupsTotals_request::is_crash_groups_Set() const{
    return m_crash_groups_isSet;
}

bool OAIAnalytics_CrashGroupsTotals_request::is_crash_groups_Valid() const{
    return m_crash_groups_isValid;
}

bool OAIAnalytics_CrashGroupsTotals_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_crash_groups.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAnalytics_CrashGroupsTotals_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_crash_groups_isValid && true;
}

} // namespace OpenAPI
