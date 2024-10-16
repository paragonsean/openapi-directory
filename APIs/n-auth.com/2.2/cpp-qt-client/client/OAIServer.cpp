/**
 * nextAuth API
 * API for the nextAuth server
 *
 * The version of the OpenAPI document: 2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIServer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIServer::OAIServer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIServer::OAIServer() {
    this->initializeModel();
}

OAIServer::~OAIServer() {}

void OAIServer::initializeModel() {

    m_account_count_isSet = false;
    m_account_count_isValid = false;

    m_appandroid_isSet = false;
    m_appandroid_isValid = false;

    m_appios_isSet = false;
    m_appios_isValid = false;

    m_appname_isSet = false;
    m_appname_isValid = false;

    m_appurl_isSet = false;
    m_appurl_isValid = false;

    m_last_login_isSet = false;
    m_last_login_isValid = false;

    m_logo_isSet = false;
    m_logo_isValid = false;

    m_owner_isSet = false;
    m_owner_isValid = false;

    m_pin_timeout_isSet = false;
    m_pin_timeout_isValid = false;

    m_pin_trans_timeout_isSet = false;
    m_pin_trans_timeout_isValid = false;

    m_ping_time_isSet = false;
    m_ping_time_isValid = false;

    m_server_flags_isSet = false;
    m_server_flags_isValid = false;

    m_server_name_isSet = false;
    m_server_name_isValid = false;

    m_serverid_isSet = false;
    m_serverid_isValid = false;

    m_serverpk_isSet = false;
    m_serverpk_isValid = false;

    m_siteurl_isSet = false;
    m_siteurl_isValid = false;

    m_wsurl_isSet = false;
    m_wsurl_isValid = false;
}

void OAIServer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIServer::fromJsonObject(QJsonObject json) {

    m_account_count_isValid = ::OpenAPI::fromJsonValue(m_account_count, json[QString("accountCount")]);
    m_account_count_isSet = !json[QString("accountCount")].isNull() && m_account_count_isValid;

    m_appandroid_isValid = ::OpenAPI::fromJsonValue(m_appandroid, json[QString("appandroid")]);
    m_appandroid_isSet = !json[QString("appandroid")].isNull() && m_appandroid_isValid;

    m_appios_isValid = ::OpenAPI::fromJsonValue(m_appios, json[QString("appios")]);
    m_appios_isSet = !json[QString("appios")].isNull() && m_appios_isValid;

    m_appname_isValid = ::OpenAPI::fromJsonValue(m_appname, json[QString("appname")]);
    m_appname_isSet = !json[QString("appname")].isNull() && m_appname_isValid;

    m_appurl_isValid = ::OpenAPI::fromJsonValue(m_appurl, json[QString("appurl")]);
    m_appurl_isSet = !json[QString("appurl")].isNull() && m_appurl_isValid;

    m_last_login_isValid = ::OpenAPI::fromJsonValue(m_last_login, json[QString("lastLogin")]);
    m_last_login_isSet = !json[QString("lastLogin")].isNull() && m_last_login_isValid;

    m_logo_isValid = ::OpenAPI::fromJsonValue(m_logo, json[QString("logo")]);
    m_logo_isSet = !json[QString("logo")].isNull() && m_logo_isValid;

    m_owner_isValid = ::OpenAPI::fromJsonValue(m_owner, json[QString("owner")]);
    m_owner_isSet = !json[QString("owner")].isNull() && m_owner_isValid;

    m_pin_timeout_isValid = ::OpenAPI::fromJsonValue(m_pin_timeout, json[QString("pinTimeout")]);
    m_pin_timeout_isSet = !json[QString("pinTimeout")].isNull() && m_pin_timeout_isValid;

    m_pin_trans_timeout_isValid = ::OpenAPI::fromJsonValue(m_pin_trans_timeout, json[QString("pinTransTimeout")]);
    m_pin_trans_timeout_isSet = !json[QString("pinTransTimeout")].isNull() && m_pin_trans_timeout_isValid;

    m_ping_time_isValid = ::OpenAPI::fromJsonValue(m_ping_time, json[QString("pingTime")]);
    m_ping_time_isSet = !json[QString("pingTime")].isNull() && m_ping_time_isValid;

    m_server_flags_isValid = ::OpenAPI::fromJsonValue(m_server_flags, json[QString("serverFlags")]);
    m_server_flags_isSet = !json[QString("serverFlags")].isNull() && m_server_flags_isValid;

    m_server_name_isValid = ::OpenAPI::fromJsonValue(m_server_name, json[QString("serverName")]);
    m_server_name_isSet = !json[QString("serverName")].isNull() && m_server_name_isValid;

    m_serverid_isValid = ::OpenAPI::fromJsonValue(m_serverid, json[QString("serverid")]);
    m_serverid_isSet = !json[QString("serverid")].isNull() && m_serverid_isValid;

    m_serverpk_isValid = ::OpenAPI::fromJsonValue(m_serverpk, json[QString("serverpk")]);
    m_serverpk_isSet = !json[QString("serverpk")].isNull() && m_serverpk_isValid;

    m_siteurl_isValid = ::OpenAPI::fromJsonValue(m_siteurl, json[QString("siteurl")]);
    m_siteurl_isSet = !json[QString("siteurl")].isNull() && m_siteurl_isValid;

    m_wsurl_isValid = ::OpenAPI::fromJsonValue(m_wsurl, json[QString("wsurl")]);
    m_wsurl_isSet = !json[QString("wsurl")].isNull() && m_wsurl_isValid;
}

QString OAIServer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIServer::asJsonObject() const {
    QJsonObject obj;
    if (m_account_count_isSet) {
        obj.insert(QString("accountCount"), ::OpenAPI::toJsonValue(m_account_count));
    }
    if (m_appandroid_isSet) {
        obj.insert(QString("appandroid"), ::OpenAPI::toJsonValue(m_appandroid));
    }
    if (m_appios_isSet) {
        obj.insert(QString("appios"), ::OpenAPI::toJsonValue(m_appios));
    }
    if (m_appname_isSet) {
        obj.insert(QString("appname"), ::OpenAPI::toJsonValue(m_appname));
    }
    if (m_appurl_isSet) {
        obj.insert(QString("appurl"), ::OpenAPI::toJsonValue(m_appurl));
    }
    if (m_last_login_isSet) {
        obj.insert(QString("lastLogin"), ::OpenAPI::toJsonValue(m_last_login));
    }
    if (m_logo_isSet) {
        obj.insert(QString("logo"), ::OpenAPI::toJsonValue(m_logo));
    }
    if (m_owner_isSet) {
        obj.insert(QString("owner"), ::OpenAPI::toJsonValue(m_owner));
    }
    if (m_pin_timeout_isSet) {
        obj.insert(QString("pinTimeout"), ::OpenAPI::toJsonValue(m_pin_timeout));
    }
    if (m_pin_trans_timeout_isSet) {
        obj.insert(QString("pinTransTimeout"), ::OpenAPI::toJsonValue(m_pin_trans_timeout));
    }
    if (m_ping_time_isSet) {
        obj.insert(QString("pingTime"), ::OpenAPI::toJsonValue(m_ping_time));
    }
    if (m_server_flags.size() > 0) {
        obj.insert(QString("serverFlags"), ::OpenAPI::toJsonValue(m_server_flags));
    }
    if (m_server_name_isSet) {
        obj.insert(QString("serverName"), ::OpenAPI::toJsonValue(m_server_name));
    }
    if (m_serverid_isSet) {
        obj.insert(QString("serverid"), ::OpenAPI::toJsonValue(m_serverid));
    }
    if (m_serverpk_isSet) {
        obj.insert(QString("serverpk"), ::OpenAPI::toJsonValue(m_serverpk));
    }
    if (m_siteurl_isSet) {
        obj.insert(QString("siteurl"), ::OpenAPI::toJsonValue(m_siteurl));
    }
    if (m_wsurl_isSet) {
        obj.insert(QString("wsurl"), ::OpenAPI::toJsonValue(m_wsurl));
    }
    return obj;
}

qint32 OAIServer::getAccountCount() const {
    return m_account_count;
}
void OAIServer::setAccountCount(const qint32 &account_count) {
    m_account_count = account_count;
    m_account_count_isSet = true;
}

bool OAIServer::is_account_count_Set() const{
    return m_account_count_isSet;
}

bool OAIServer::is_account_count_Valid() const{
    return m_account_count_isValid;
}

QString OAIServer::getAppandroid() const {
    return m_appandroid;
}
void OAIServer::setAppandroid(const QString &appandroid) {
    m_appandroid = appandroid;
    m_appandroid_isSet = true;
}

bool OAIServer::is_appandroid_Set() const{
    return m_appandroid_isSet;
}

bool OAIServer::is_appandroid_Valid() const{
    return m_appandroid_isValid;
}

QString OAIServer::getAppios() const {
    return m_appios;
}
void OAIServer::setAppios(const QString &appios) {
    m_appios = appios;
    m_appios_isSet = true;
}

bool OAIServer::is_appios_Set() const{
    return m_appios_isSet;
}

bool OAIServer::is_appios_Valid() const{
    return m_appios_isValid;
}

QString OAIServer::getAppname() const {
    return m_appname;
}
void OAIServer::setAppname(const QString &appname) {
    m_appname = appname;
    m_appname_isSet = true;
}

bool OAIServer::is_appname_Set() const{
    return m_appname_isSet;
}

bool OAIServer::is_appname_Valid() const{
    return m_appname_isValid;
}

QString OAIServer::getAppurl() const {
    return m_appurl;
}
void OAIServer::setAppurl(const QString &appurl) {
    m_appurl = appurl;
    m_appurl_isSet = true;
}

bool OAIServer::is_appurl_Set() const{
    return m_appurl_isSet;
}

bool OAIServer::is_appurl_Valid() const{
    return m_appurl_isValid;
}

qint64 OAIServer::getLastLogin() const {
    return m_last_login;
}
void OAIServer::setLastLogin(const qint64 &last_login) {
    m_last_login = last_login;
    m_last_login_isSet = true;
}

bool OAIServer::is_last_login_Set() const{
    return m_last_login_isSet;
}

bool OAIServer::is_last_login_Valid() const{
    return m_last_login_isValid;
}

QString OAIServer::getLogo() const {
    return m_logo;
}
void OAIServer::setLogo(const QString &logo) {
    m_logo = logo;
    m_logo_isSet = true;
}

bool OAIServer::is_logo_Set() const{
    return m_logo_isSet;
}

bool OAIServer::is_logo_Valid() const{
    return m_logo_isValid;
}

qint32 OAIServer::getOwner() const {
    return m_owner;
}
void OAIServer::setOwner(const qint32 &owner) {
    m_owner = owner;
    m_owner_isSet = true;
}

bool OAIServer::is_owner_Set() const{
    return m_owner_isSet;
}

bool OAIServer::is_owner_Valid() const{
    return m_owner_isValid;
}

qint32 OAIServer::getPinTimeout() const {
    return m_pin_timeout;
}
void OAIServer::setPinTimeout(const qint32 &pin_timeout) {
    m_pin_timeout = pin_timeout;
    m_pin_timeout_isSet = true;
}

bool OAIServer::is_pin_timeout_Set() const{
    return m_pin_timeout_isSet;
}

bool OAIServer::is_pin_timeout_Valid() const{
    return m_pin_timeout_isValid;
}

qint32 OAIServer::getPinTransTimeout() const {
    return m_pin_trans_timeout;
}
void OAIServer::setPinTransTimeout(const qint32 &pin_trans_timeout) {
    m_pin_trans_timeout = pin_trans_timeout;
    m_pin_trans_timeout_isSet = true;
}

bool OAIServer::is_pin_trans_timeout_Set() const{
    return m_pin_trans_timeout_isSet;
}

bool OAIServer::is_pin_trans_timeout_Valid() const{
    return m_pin_trans_timeout_isValid;
}

qint32 OAIServer::getPingTime() const {
    return m_ping_time;
}
void OAIServer::setPingTime(const qint32 &ping_time) {
    m_ping_time = ping_time;
    m_ping_time_isSet = true;
}

bool OAIServer::is_ping_time_Set() const{
    return m_ping_time_isSet;
}

bool OAIServer::is_ping_time_Valid() const{
    return m_ping_time_isValid;
}

QList<QString> OAIServer::getServerFlags() const {
    return m_server_flags;
}
void OAIServer::setServerFlags(const QList<QString> &server_flags) {
    m_server_flags = server_flags;
    m_server_flags_isSet = true;
}

bool OAIServer::is_server_flags_Set() const{
    return m_server_flags_isSet;
}

bool OAIServer::is_server_flags_Valid() const{
    return m_server_flags_isValid;
}

QString OAIServer::getServerName() const {
    return m_server_name;
}
void OAIServer::setServerName(const QString &server_name) {
    m_server_name = server_name;
    m_server_name_isSet = true;
}

bool OAIServer::is_server_name_Set() const{
    return m_server_name_isSet;
}

bool OAIServer::is_server_name_Valid() const{
    return m_server_name_isValid;
}

QString OAIServer::getServerid() const {
    return m_serverid;
}
void OAIServer::setServerid(const QString &serverid) {
    m_serverid = serverid;
    m_serverid_isSet = true;
}

bool OAIServer::is_serverid_Set() const{
    return m_serverid_isSet;
}

bool OAIServer::is_serverid_Valid() const{
    return m_serverid_isValid;
}

QString OAIServer::getServerpk() const {
    return m_serverpk;
}
void OAIServer::setServerpk(const QString &serverpk) {
    m_serverpk = serverpk;
    m_serverpk_isSet = true;
}

bool OAIServer::is_serverpk_Set() const{
    return m_serverpk_isSet;
}

bool OAIServer::is_serverpk_Valid() const{
    return m_serverpk_isValid;
}

QString OAIServer::getSiteurl() const {
    return m_siteurl;
}
void OAIServer::setSiteurl(const QString &siteurl) {
    m_siteurl = siteurl;
    m_siteurl_isSet = true;
}

bool OAIServer::is_siteurl_Set() const{
    return m_siteurl_isSet;
}

bool OAIServer::is_siteurl_Valid() const{
    return m_siteurl_isValid;
}

QString OAIServer::getWsurl() const {
    return m_wsurl;
}
void OAIServer::setWsurl(const QString &wsurl) {
    m_wsurl = wsurl;
    m_wsurl_isSet = true;
}

bool OAIServer::is_wsurl_Set() const{
    return m_wsurl_isSet;
}

bool OAIServer::is_wsurl_Valid() const{
    return m_wsurl_isValid;
}

bool OAIServer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_appandroid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_appios_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_appname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_appurl_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_login_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_logo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pin_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pin_trans_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ping_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_flags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_serverid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_serverpk_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_siteurl_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wsurl_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIServer::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_logo_isValid && m_pin_timeout_isValid && m_pin_trans_timeout_isValid && m_ping_time_isValid && m_server_flags_isValid && m_server_name_isValid && m_serverid_isValid && m_serverpk_isValid && true;
}

} // namespace OpenAPI
