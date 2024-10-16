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

#include "OAIActiveCrashingAppDetails_appsWithCrashes_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActiveCrashingAppDetails_appsWithCrashes_inner::OAIActiveCrashingAppDetails_appsWithCrashes_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActiveCrashingAppDetails_appsWithCrashes_inner::OAIActiveCrashingAppDetails_appsWithCrashes_inner() {
    this->initializeModel();
}

OAIActiveCrashingAppDetails_appsWithCrashes_inner::~OAIActiveCrashingAppDetails_appsWithCrashes_inner() {}

void OAIActiveCrashingAppDetails_appsWithCrashes_inner::initializeModel() {

    m_app_id_isSet = false;
    m_app_id_isValid = false;

    m_app_version_isSet = false;
    m_app_version_isValid = false;

    m_crash_group_id_isSet = false;
    m_crash_group_id_isValid = false;
}

void OAIActiveCrashingAppDetails_appsWithCrashes_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActiveCrashingAppDetails_appsWithCrashes_inner::fromJsonObject(QJsonObject json) {

    m_app_id_isValid = ::OpenAPI::fromJsonValue(m_app_id, json[QString("appId")]);
    m_app_id_isSet = !json[QString("appId")].isNull() && m_app_id_isValid;

    m_app_version_isValid = ::OpenAPI::fromJsonValue(m_app_version, json[QString("appVersion")]);
    m_app_version_isSet = !json[QString("appVersion")].isNull() && m_app_version_isValid;

    m_crash_group_id_isValid = ::OpenAPI::fromJsonValue(m_crash_group_id, json[QString("crashGroupId")]);
    m_crash_group_id_isSet = !json[QString("crashGroupId")].isNull() && m_crash_group_id_isValid;
}

QString OAIActiveCrashingAppDetails_appsWithCrashes_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActiveCrashingAppDetails_appsWithCrashes_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_app_id_isSet) {
        obj.insert(QString("appId"), ::OpenAPI::toJsonValue(m_app_id));
    }
    if (m_app_version_isSet) {
        obj.insert(QString("appVersion"), ::OpenAPI::toJsonValue(m_app_version));
    }
    if (m_crash_group_id_isSet) {
        obj.insert(QString("crashGroupId"), ::OpenAPI::toJsonValue(m_crash_group_id));
    }
    return obj;
}

QString OAIActiveCrashingAppDetails_appsWithCrashes_inner::getAppId() const {
    return m_app_id;
}
void OAIActiveCrashingAppDetails_appsWithCrashes_inner::setAppId(const QString &app_id) {
    m_app_id = app_id;
    m_app_id_isSet = true;
}

bool OAIActiveCrashingAppDetails_appsWithCrashes_inner::is_app_id_Set() const{
    return m_app_id_isSet;
}

bool OAIActiveCrashingAppDetails_appsWithCrashes_inner::is_app_id_Valid() const{
    return m_app_id_isValid;
}

QString OAIActiveCrashingAppDetails_appsWithCrashes_inner::getAppVersion() const {
    return m_app_version;
}
void OAIActiveCrashingAppDetails_appsWithCrashes_inner::setAppVersion(const QString &app_version) {
    m_app_version = app_version;
    m_app_version_isSet = true;
}

bool OAIActiveCrashingAppDetails_appsWithCrashes_inner::is_app_version_Set() const{
    return m_app_version_isSet;
}

bool OAIActiveCrashingAppDetails_appsWithCrashes_inner::is_app_version_Valid() const{
    return m_app_version_isValid;
}

QString OAIActiveCrashingAppDetails_appsWithCrashes_inner::getCrashGroupId() const {
    return m_crash_group_id;
}
void OAIActiveCrashingAppDetails_appsWithCrashes_inner::setCrashGroupId(const QString &crash_group_id) {
    m_crash_group_id = crash_group_id;
    m_crash_group_id_isSet = true;
}

bool OAIActiveCrashingAppDetails_appsWithCrashes_inner::is_crash_group_id_Set() const{
    return m_crash_group_id_isSet;
}

bool OAIActiveCrashingAppDetails_appsWithCrashes_inner::is_crash_group_id_Valid() const{
    return m_crash_group_id_isValid;
}

bool OAIActiveCrashingAppDetails_appsWithCrashes_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_app_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_crash_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActiveCrashingAppDetails_appsWithCrashes_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
