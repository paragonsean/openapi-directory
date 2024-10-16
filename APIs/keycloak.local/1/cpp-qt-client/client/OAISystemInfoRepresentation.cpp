/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISystemInfoRepresentation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISystemInfoRepresentation::OAISystemInfoRepresentation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISystemInfoRepresentation::OAISystemInfoRepresentation() {
    this->initializeModel();
}

OAISystemInfoRepresentation::~OAISystemInfoRepresentation() {}

void OAISystemInfoRepresentation::initializeModel() {

    m_file_encoding_isSet = false;
    m_file_encoding_isValid = false;

    m_java_home_isSet = false;
    m_java_home_isValid = false;

    m_java_runtime_isSet = false;
    m_java_runtime_isValid = false;

    m_java_vendor_isSet = false;
    m_java_vendor_isValid = false;

    m_java_version_isSet = false;
    m_java_version_isValid = false;

    m_java_vm_isSet = false;
    m_java_vm_isValid = false;

    m_java_vm_version_isSet = false;
    m_java_vm_version_isValid = false;

    m_os_architecture_isSet = false;
    m_os_architecture_isValid = false;

    m_os_name_isSet = false;
    m_os_name_isValid = false;

    m_os_version_isSet = false;
    m_os_version_isValid = false;

    m_server_time_isSet = false;
    m_server_time_isValid = false;

    m_uptime_isSet = false;
    m_uptime_isValid = false;

    m_uptime_millis_isSet = false;
    m_uptime_millis_isValid = false;

    m_user_dir_isSet = false;
    m_user_dir_isValid = false;

    m_user_locale_isSet = false;
    m_user_locale_isValid = false;

    m_user_name_isSet = false;
    m_user_name_isValid = false;

    m_user_timezone_isSet = false;
    m_user_timezone_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAISystemInfoRepresentation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISystemInfoRepresentation::fromJsonObject(QJsonObject json) {

    m_file_encoding_isValid = ::OpenAPI::fromJsonValue(m_file_encoding, json[QString("fileEncoding")]);
    m_file_encoding_isSet = !json[QString("fileEncoding")].isNull() && m_file_encoding_isValid;

    m_java_home_isValid = ::OpenAPI::fromJsonValue(m_java_home, json[QString("javaHome")]);
    m_java_home_isSet = !json[QString("javaHome")].isNull() && m_java_home_isValid;

    m_java_runtime_isValid = ::OpenAPI::fromJsonValue(m_java_runtime, json[QString("javaRuntime")]);
    m_java_runtime_isSet = !json[QString("javaRuntime")].isNull() && m_java_runtime_isValid;

    m_java_vendor_isValid = ::OpenAPI::fromJsonValue(m_java_vendor, json[QString("javaVendor")]);
    m_java_vendor_isSet = !json[QString("javaVendor")].isNull() && m_java_vendor_isValid;

    m_java_version_isValid = ::OpenAPI::fromJsonValue(m_java_version, json[QString("javaVersion")]);
    m_java_version_isSet = !json[QString("javaVersion")].isNull() && m_java_version_isValid;

    m_java_vm_isValid = ::OpenAPI::fromJsonValue(m_java_vm, json[QString("javaVm")]);
    m_java_vm_isSet = !json[QString("javaVm")].isNull() && m_java_vm_isValid;

    m_java_vm_version_isValid = ::OpenAPI::fromJsonValue(m_java_vm_version, json[QString("javaVmVersion")]);
    m_java_vm_version_isSet = !json[QString("javaVmVersion")].isNull() && m_java_vm_version_isValid;

    m_os_architecture_isValid = ::OpenAPI::fromJsonValue(m_os_architecture, json[QString("osArchitecture")]);
    m_os_architecture_isSet = !json[QString("osArchitecture")].isNull() && m_os_architecture_isValid;

    m_os_name_isValid = ::OpenAPI::fromJsonValue(m_os_name, json[QString("osName")]);
    m_os_name_isSet = !json[QString("osName")].isNull() && m_os_name_isValid;

    m_os_version_isValid = ::OpenAPI::fromJsonValue(m_os_version, json[QString("osVersion")]);
    m_os_version_isSet = !json[QString("osVersion")].isNull() && m_os_version_isValid;

    m_server_time_isValid = ::OpenAPI::fromJsonValue(m_server_time, json[QString("serverTime")]);
    m_server_time_isSet = !json[QString("serverTime")].isNull() && m_server_time_isValid;

    m_uptime_isValid = ::OpenAPI::fromJsonValue(m_uptime, json[QString("uptime")]);
    m_uptime_isSet = !json[QString("uptime")].isNull() && m_uptime_isValid;

    m_uptime_millis_isValid = ::OpenAPI::fromJsonValue(m_uptime_millis, json[QString("uptimeMillis")]);
    m_uptime_millis_isSet = !json[QString("uptimeMillis")].isNull() && m_uptime_millis_isValid;

    m_user_dir_isValid = ::OpenAPI::fromJsonValue(m_user_dir, json[QString("userDir")]);
    m_user_dir_isSet = !json[QString("userDir")].isNull() && m_user_dir_isValid;

    m_user_locale_isValid = ::OpenAPI::fromJsonValue(m_user_locale, json[QString("userLocale")]);
    m_user_locale_isSet = !json[QString("userLocale")].isNull() && m_user_locale_isValid;

    m_user_name_isValid = ::OpenAPI::fromJsonValue(m_user_name, json[QString("userName")]);
    m_user_name_isSet = !json[QString("userName")].isNull() && m_user_name_isValid;

    m_user_timezone_isValid = ::OpenAPI::fromJsonValue(m_user_timezone, json[QString("userTimezone")]);
    m_user_timezone_isSet = !json[QString("userTimezone")].isNull() && m_user_timezone_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAISystemInfoRepresentation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISystemInfoRepresentation::asJsonObject() const {
    QJsonObject obj;
    if (m_file_encoding_isSet) {
        obj.insert(QString("fileEncoding"), ::OpenAPI::toJsonValue(m_file_encoding));
    }
    if (m_java_home_isSet) {
        obj.insert(QString("javaHome"), ::OpenAPI::toJsonValue(m_java_home));
    }
    if (m_java_runtime_isSet) {
        obj.insert(QString("javaRuntime"), ::OpenAPI::toJsonValue(m_java_runtime));
    }
    if (m_java_vendor_isSet) {
        obj.insert(QString("javaVendor"), ::OpenAPI::toJsonValue(m_java_vendor));
    }
    if (m_java_version_isSet) {
        obj.insert(QString("javaVersion"), ::OpenAPI::toJsonValue(m_java_version));
    }
    if (m_java_vm_isSet) {
        obj.insert(QString("javaVm"), ::OpenAPI::toJsonValue(m_java_vm));
    }
    if (m_java_vm_version_isSet) {
        obj.insert(QString("javaVmVersion"), ::OpenAPI::toJsonValue(m_java_vm_version));
    }
    if (m_os_architecture_isSet) {
        obj.insert(QString("osArchitecture"), ::OpenAPI::toJsonValue(m_os_architecture));
    }
    if (m_os_name_isSet) {
        obj.insert(QString("osName"), ::OpenAPI::toJsonValue(m_os_name));
    }
    if (m_os_version_isSet) {
        obj.insert(QString("osVersion"), ::OpenAPI::toJsonValue(m_os_version));
    }
    if (m_server_time_isSet) {
        obj.insert(QString("serverTime"), ::OpenAPI::toJsonValue(m_server_time));
    }
    if (m_uptime_isSet) {
        obj.insert(QString("uptime"), ::OpenAPI::toJsonValue(m_uptime));
    }
    if (m_uptime_millis_isSet) {
        obj.insert(QString("uptimeMillis"), ::OpenAPI::toJsonValue(m_uptime_millis));
    }
    if (m_user_dir_isSet) {
        obj.insert(QString("userDir"), ::OpenAPI::toJsonValue(m_user_dir));
    }
    if (m_user_locale_isSet) {
        obj.insert(QString("userLocale"), ::OpenAPI::toJsonValue(m_user_locale));
    }
    if (m_user_name_isSet) {
        obj.insert(QString("userName"), ::OpenAPI::toJsonValue(m_user_name));
    }
    if (m_user_timezone_isSet) {
        obj.insert(QString("userTimezone"), ::OpenAPI::toJsonValue(m_user_timezone));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QString OAISystemInfoRepresentation::getFileEncoding() const {
    return m_file_encoding;
}
void OAISystemInfoRepresentation::setFileEncoding(const QString &file_encoding) {
    m_file_encoding = file_encoding;
    m_file_encoding_isSet = true;
}

bool OAISystemInfoRepresentation::is_file_encoding_Set() const{
    return m_file_encoding_isSet;
}

bool OAISystemInfoRepresentation::is_file_encoding_Valid() const{
    return m_file_encoding_isValid;
}

QString OAISystemInfoRepresentation::getJavaHome() const {
    return m_java_home;
}
void OAISystemInfoRepresentation::setJavaHome(const QString &java_home) {
    m_java_home = java_home;
    m_java_home_isSet = true;
}

bool OAISystemInfoRepresentation::is_java_home_Set() const{
    return m_java_home_isSet;
}

bool OAISystemInfoRepresentation::is_java_home_Valid() const{
    return m_java_home_isValid;
}

QString OAISystemInfoRepresentation::getJavaRuntime() const {
    return m_java_runtime;
}
void OAISystemInfoRepresentation::setJavaRuntime(const QString &java_runtime) {
    m_java_runtime = java_runtime;
    m_java_runtime_isSet = true;
}

bool OAISystemInfoRepresentation::is_java_runtime_Set() const{
    return m_java_runtime_isSet;
}

bool OAISystemInfoRepresentation::is_java_runtime_Valid() const{
    return m_java_runtime_isValid;
}

QString OAISystemInfoRepresentation::getJavaVendor() const {
    return m_java_vendor;
}
void OAISystemInfoRepresentation::setJavaVendor(const QString &java_vendor) {
    m_java_vendor = java_vendor;
    m_java_vendor_isSet = true;
}

bool OAISystemInfoRepresentation::is_java_vendor_Set() const{
    return m_java_vendor_isSet;
}

bool OAISystemInfoRepresentation::is_java_vendor_Valid() const{
    return m_java_vendor_isValid;
}

QString OAISystemInfoRepresentation::getJavaVersion() const {
    return m_java_version;
}
void OAISystemInfoRepresentation::setJavaVersion(const QString &java_version) {
    m_java_version = java_version;
    m_java_version_isSet = true;
}

bool OAISystemInfoRepresentation::is_java_version_Set() const{
    return m_java_version_isSet;
}

bool OAISystemInfoRepresentation::is_java_version_Valid() const{
    return m_java_version_isValid;
}

QString OAISystemInfoRepresentation::getJavaVm() const {
    return m_java_vm;
}
void OAISystemInfoRepresentation::setJavaVm(const QString &java_vm) {
    m_java_vm = java_vm;
    m_java_vm_isSet = true;
}

bool OAISystemInfoRepresentation::is_java_vm_Set() const{
    return m_java_vm_isSet;
}

bool OAISystemInfoRepresentation::is_java_vm_Valid() const{
    return m_java_vm_isValid;
}

QString OAISystemInfoRepresentation::getJavaVmVersion() const {
    return m_java_vm_version;
}
void OAISystemInfoRepresentation::setJavaVmVersion(const QString &java_vm_version) {
    m_java_vm_version = java_vm_version;
    m_java_vm_version_isSet = true;
}

bool OAISystemInfoRepresentation::is_java_vm_version_Set() const{
    return m_java_vm_version_isSet;
}

bool OAISystemInfoRepresentation::is_java_vm_version_Valid() const{
    return m_java_vm_version_isValid;
}

QString OAISystemInfoRepresentation::getOsArchitecture() const {
    return m_os_architecture;
}
void OAISystemInfoRepresentation::setOsArchitecture(const QString &os_architecture) {
    m_os_architecture = os_architecture;
    m_os_architecture_isSet = true;
}

bool OAISystemInfoRepresentation::is_os_architecture_Set() const{
    return m_os_architecture_isSet;
}

bool OAISystemInfoRepresentation::is_os_architecture_Valid() const{
    return m_os_architecture_isValid;
}

QString OAISystemInfoRepresentation::getOsName() const {
    return m_os_name;
}
void OAISystemInfoRepresentation::setOsName(const QString &os_name) {
    m_os_name = os_name;
    m_os_name_isSet = true;
}

bool OAISystemInfoRepresentation::is_os_name_Set() const{
    return m_os_name_isSet;
}

bool OAISystemInfoRepresentation::is_os_name_Valid() const{
    return m_os_name_isValid;
}

QString OAISystemInfoRepresentation::getOsVersion() const {
    return m_os_version;
}
void OAISystemInfoRepresentation::setOsVersion(const QString &os_version) {
    m_os_version = os_version;
    m_os_version_isSet = true;
}

bool OAISystemInfoRepresentation::is_os_version_Set() const{
    return m_os_version_isSet;
}

bool OAISystemInfoRepresentation::is_os_version_Valid() const{
    return m_os_version_isValid;
}

QString OAISystemInfoRepresentation::getServerTime() const {
    return m_server_time;
}
void OAISystemInfoRepresentation::setServerTime(const QString &server_time) {
    m_server_time = server_time;
    m_server_time_isSet = true;
}

bool OAISystemInfoRepresentation::is_server_time_Set() const{
    return m_server_time_isSet;
}

bool OAISystemInfoRepresentation::is_server_time_Valid() const{
    return m_server_time_isValid;
}

QString OAISystemInfoRepresentation::getUptime() const {
    return m_uptime;
}
void OAISystemInfoRepresentation::setUptime(const QString &uptime) {
    m_uptime = uptime;
    m_uptime_isSet = true;
}

bool OAISystemInfoRepresentation::is_uptime_Set() const{
    return m_uptime_isSet;
}

bool OAISystemInfoRepresentation::is_uptime_Valid() const{
    return m_uptime_isValid;
}

qint64 OAISystemInfoRepresentation::getUptimeMillis() const {
    return m_uptime_millis;
}
void OAISystemInfoRepresentation::setUptimeMillis(const qint64 &uptime_millis) {
    m_uptime_millis = uptime_millis;
    m_uptime_millis_isSet = true;
}

bool OAISystemInfoRepresentation::is_uptime_millis_Set() const{
    return m_uptime_millis_isSet;
}

bool OAISystemInfoRepresentation::is_uptime_millis_Valid() const{
    return m_uptime_millis_isValid;
}

QString OAISystemInfoRepresentation::getUserDir() const {
    return m_user_dir;
}
void OAISystemInfoRepresentation::setUserDir(const QString &user_dir) {
    m_user_dir = user_dir;
    m_user_dir_isSet = true;
}

bool OAISystemInfoRepresentation::is_user_dir_Set() const{
    return m_user_dir_isSet;
}

bool OAISystemInfoRepresentation::is_user_dir_Valid() const{
    return m_user_dir_isValid;
}

QString OAISystemInfoRepresentation::getUserLocale() const {
    return m_user_locale;
}
void OAISystemInfoRepresentation::setUserLocale(const QString &user_locale) {
    m_user_locale = user_locale;
    m_user_locale_isSet = true;
}

bool OAISystemInfoRepresentation::is_user_locale_Set() const{
    return m_user_locale_isSet;
}

bool OAISystemInfoRepresentation::is_user_locale_Valid() const{
    return m_user_locale_isValid;
}

QString OAISystemInfoRepresentation::getUserName() const {
    return m_user_name;
}
void OAISystemInfoRepresentation::setUserName(const QString &user_name) {
    m_user_name = user_name;
    m_user_name_isSet = true;
}

bool OAISystemInfoRepresentation::is_user_name_Set() const{
    return m_user_name_isSet;
}

bool OAISystemInfoRepresentation::is_user_name_Valid() const{
    return m_user_name_isValid;
}

QString OAISystemInfoRepresentation::getUserTimezone() const {
    return m_user_timezone;
}
void OAISystemInfoRepresentation::setUserTimezone(const QString &user_timezone) {
    m_user_timezone = user_timezone;
    m_user_timezone_isSet = true;
}

bool OAISystemInfoRepresentation::is_user_timezone_Set() const{
    return m_user_timezone_isSet;
}

bool OAISystemInfoRepresentation::is_user_timezone_Valid() const{
    return m_user_timezone_isValid;
}

QString OAISystemInfoRepresentation::getVersion() const {
    return m_version;
}
void OAISystemInfoRepresentation::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAISystemInfoRepresentation::is_version_Set() const{
    return m_version_isSet;
}

bool OAISystemInfoRepresentation::is_version_Valid() const{
    return m_version_isValid;
}

bool OAISystemInfoRepresentation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_file_encoding_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_java_home_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_java_runtime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_java_vendor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_java_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_java_vm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_java_vm_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_os_architecture_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_os_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_os_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uptime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uptime_millis_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_dir_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_locale_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_timezone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISystemInfoRepresentation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
