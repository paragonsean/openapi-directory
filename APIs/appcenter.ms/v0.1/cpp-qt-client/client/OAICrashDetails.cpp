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

#include "OAICrashDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICrashDetails::OAICrashDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICrashDetails::OAICrashDetails() {
    this->initializeModel();
}

OAICrashDetails::~OAICrashDetails() {}

void OAICrashDetails::initializeModel() {

    m_app_start_timestamp_isSet = false;
    m_app_start_timestamp_isValid = false;

    m_carrier_country_isSet = false;
    m_carrier_country_isValid = false;

    m_carrier_name_isSet = false;
    m_carrier_name_isValid = false;

    m_locale_isSet = false;
    m_locale_isValid = false;

    m_os_build_isSet = false;
    m_os_build_isValid = false;

    m_rooted_isSet = false;
    m_rooted_isValid = false;

    m_screen_size_isSet = false;
    m_screen_size_isValid = false;
}

void OAICrashDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICrashDetails::fromJsonObject(QJsonObject json) {

    m_app_start_timestamp_isValid = ::OpenAPI::fromJsonValue(m_app_start_timestamp, json[QString("app_start_timestamp")]);
    m_app_start_timestamp_isSet = !json[QString("app_start_timestamp")].isNull() && m_app_start_timestamp_isValid;

    m_carrier_country_isValid = ::OpenAPI::fromJsonValue(m_carrier_country, json[QString("carrier_country")]);
    m_carrier_country_isSet = !json[QString("carrier_country")].isNull() && m_carrier_country_isValid;

    m_carrier_name_isValid = ::OpenAPI::fromJsonValue(m_carrier_name, json[QString("carrier_name")]);
    m_carrier_name_isSet = !json[QString("carrier_name")].isNull() && m_carrier_name_isValid;

    m_locale_isValid = ::OpenAPI::fromJsonValue(m_locale, json[QString("locale")]);
    m_locale_isSet = !json[QString("locale")].isNull() && m_locale_isValid;

    m_os_build_isValid = ::OpenAPI::fromJsonValue(m_os_build, json[QString("os_build")]);
    m_os_build_isSet = !json[QString("os_build")].isNull() && m_os_build_isValid;

    m_rooted_isValid = ::OpenAPI::fromJsonValue(m_rooted, json[QString("rooted")]);
    m_rooted_isSet = !json[QString("rooted")].isNull() && m_rooted_isValid;

    m_screen_size_isValid = ::OpenAPI::fromJsonValue(m_screen_size, json[QString("screen_size")]);
    m_screen_size_isSet = !json[QString("screen_size")].isNull() && m_screen_size_isValid;
}

QString OAICrashDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICrashDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_app_start_timestamp_isSet) {
        obj.insert(QString("app_start_timestamp"), ::OpenAPI::toJsonValue(m_app_start_timestamp));
    }
    if (m_carrier_country_isSet) {
        obj.insert(QString("carrier_country"), ::OpenAPI::toJsonValue(m_carrier_country));
    }
    if (m_carrier_name_isSet) {
        obj.insert(QString("carrier_name"), ::OpenAPI::toJsonValue(m_carrier_name));
    }
    if (m_locale_isSet) {
        obj.insert(QString("locale"), ::OpenAPI::toJsonValue(m_locale));
    }
    if (m_os_build_isSet) {
        obj.insert(QString("os_build"), ::OpenAPI::toJsonValue(m_os_build));
    }
    if (m_rooted_isSet) {
        obj.insert(QString("rooted"), ::OpenAPI::toJsonValue(m_rooted));
    }
    if (m_screen_size_isSet) {
        obj.insert(QString("screen_size"), ::OpenAPI::toJsonValue(m_screen_size));
    }
    return obj;
}

QDateTime OAICrashDetails::getAppStartTimestamp() const {
    return m_app_start_timestamp;
}
void OAICrashDetails::setAppStartTimestamp(const QDateTime &app_start_timestamp) {
    m_app_start_timestamp = app_start_timestamp;
    m_app_start_timestamp_isSet = true;
}

bool OAICrashDetails::is_app_start_timestamp_Set() const{
    return m_app_start_timestamp_isSet;
}

bool OAICrashDetails::is_app_start_timestamp_Valid() const{
    return m_app_start_timestamp_isValid;
}

QString OAICrashDetails::getCarrierCountry() const {
    return m_carrier_country;
}
void OAICrashDetails::setCarrierCountry(const QString &carrier_country) {
    m_carrier_country = carrier_country;
    m_carrier_country_isSet = true;
}

bool OAICrashDetails::is_carrier_country_Set() const{
    return m_carrier_country_isSet;
}

bool OAICrashDetails::is_carrier_country_Valid() const{
    return m_carrier_country_isValid;
}

QString OAICrashDetails::getCarrierName() const {
    return m_carrier_name;
}
void OAICrashDetails::setCarrierName(const QString &carrier_name) {
    m_carrier_name = carrier_name;
    m_carrier_name_isSet = true;
}

bool OAICrashDetails::is_carrier_name_Set() const{
    return m_carrier_name_isSet;
}

bool OAICrashDetails::is_carrier_name_Valid() const{
    return m_carrier_name_isValid;
}

QString OAICrashDetails::getLocale() const {
    return m_locale;
}
void OAICrashDetails::setLocale(const QString &locale) {
    m_locale = locale;
    m_locale_isSet = true;
}

bool OAICrashDetails::is_locale_Set() const{
    return m_locale_isSet;
}

bool OAICrashDetails::is_locale_Valid() const{
    return m_locale_isValid;
}

QString OAICrashDetails::getOsBuild() const {
    return m_os_build;
}
void OAICrashDetails::setOsBuild(const QString &os_build) {
    m_os_build = os_build;
    m_os_build_isSet = true;
}

bool OAICrashDetails::is_os_build_Set() const{
    return m_os_build_isSet;
}

bool OAICrashDetails::is_os_build_Valid() const{
    return m_os_build_isValid;
}

bool OAICrashDetails::isRooted() const {
    return m_rooted;
}
void OAICrashDetails::setRooted(const bool &rooted) {
    m_rooted = rooted;
    m_rooted_isSet = true;
}

bool OAICrashDetails::is_rooted_Set() const{
    return m_rooted_isSet;
}

bool OAICrashDetails::is_rooted_Valid() const{
    return m_rooted_isValid;
}

QString OAICrashDetails::getScreenSize() const {
    return m_screen_size;
}
void OAICrashDetails::setScreenSize(const QString &screen_size) {
    m_screen_size = screen_size;
    m_screen_size_isSet = true;
}

bool OAICrashDetails::is_screen_size_Set() const{
    return m_screen_size_isSet;
}

bool OAICrashDetails::is_screen_size_Valid() const{
    return m_screen_size_isValid;
}

bool OAICrashDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_start_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_carrier_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_carrier_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_locale_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_os_build_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rooted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_screen_size_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICrashDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_locale_isValid && m_rooted_isValid && m_screen_size_isValid && true;
}

} // namespace OpenAPI
