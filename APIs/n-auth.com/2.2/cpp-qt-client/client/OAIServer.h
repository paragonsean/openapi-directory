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

/*
 * OAIServer.h
 *
 * 
 */

#ifndef OAIServer_H
#define OAIServer_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIServer : public OAIObject {
public:
    OAIServer();
    OAIServer(QString json);
    ~OAIServer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAccountCount() const;
    void setAccountCount(const qint32 &account_count);
    bool is_account_count_Set() const;
    bool is_account_count_Valid() const;

    QString getAppandroid() const;
    void setAppandroid(const QString &appandroid);
    bool is_appandroid_Set() const;
    bool is_appandroid_Valid() const;

    QString getAppios() const;
    void setAppios(const QString &appios);
    bool is_appios_Set() const;
    bool is_appios_Valid() const;

    QString getAppname() const;
    void setAppname(const QString &appname);
    bool is_appname_Set() const;
    bool is_appname_Valid() const;

    QString getAppurl() const;
    void setAppurl(const QString &appurl);
    bool is_appurl_Set() const;
    bool is_appurl_Valid() const;

    qint64 getLastLogin() const;
    void setLastLogin(const qint64 &last_login);
    bool is_last_login_Set() const;
    bool is_last_login_Valid() const;

    QString getLogo() const;
    void setLogo(const QString &logo);
    bool is_logo_Set() const;
    bool is_logo_Valid() const;

    qint32 getOwner() const;
    void setOwner(const qint32 &owner);
    bool is_owner_Set() const;
    bool is_owner_Valid() const;

    qint32 getPinTimeout() const;
    void setPinTimeout(const qint32 &pin_timeout);
    bool is_pin_timeout_Set() const;
    bool is_pin_timeout_Valid() const;

    qint32 getPinTransTimeout() const;
    void setPinTransTimeout(const qint32 &pin_trans_timeout);
    bool is_pin_trans_timeout_Set() const;
    bool is_pin_trans_timeout_Valid() const;

    qint32 getPingTime() const;
    void setPingTime(const qint32 &ping_time);
    bool is_ping_time_Set() const;
    bool is_ping_time_Valid() const;

    QList<QString> getServerFlags() const;
    void setServerFlags(const QList<QString> &server_flags);
    bool is_server_flags_Set() const;
    bool is_server_flags_Valid() const;

    QString getServerName() const;
    void setServerName(const QString &server_name);
    bool is_server_name_Set() const;
    bool is_server_name_Valid() const;

    QString getServerid() const;
    void setServerid(const QString &serverid);
    bool is_serverid_Set() const;
    bool is_serverid_Valid() const;

    QString getServerpk() const;
    void setServerpk(const QString &serverpk);
    bool is_serverpk_Set() const;
    bool is_serverpk_Valid() const;

    QString getSiteurl() const;
    void setSiteurl(const QString &siteurl);
    bool is_siteurl_Set() const;
    bool is_siteurl_Valid() const;

    QString getWsurl() const;
    void setWsurl(const QString &wsurl);
    bool is_wsurl_Set() const;
    bool is_wsurl_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_account_count;
    bool m_account_count_isSet;
    bool m_account_count_isValid;

    QString m_appandroid;
    bool m_appandroid_isSet;
    bool m_appandroid_isValid;

    QString m_appios;
    bool m_appios_isSet;
    bool m_appios_isValid;

    QString m_appname;
    bool m_appname_isSet;
    bool m_appname_isValid;

    QString m_appurl;
    bool m_appurl_isSet;
    bool m_appurl_isValid;

    qint64 m_last_login;
    bool m_last_login_isSet;
    bool m_last_login_isValid;

    QString m_logo;
    bool m_logo_isSet;
    bool m_logo_isValid;

    qint32 m_owner;
    bool m_owner_isSet;
    bool m_owner_isValid;

    qint32 m_pin_timeout;
    bool m_pin_timeout_isSet;
    bool m_pin_timeout_isValid;

    qint32 m_pin_trans_timeout;
    bool m_pin_trans_timeout_isSet;
    bool m_pin_trans_timeout_isValid;

    qint32 m_ping_time;
    bool m_ping_time_isSet;
    bool m_ping_time_isValid;

    QList<QString> m_server_flags;
    bool m_server_flags_isSet;
    bool m_server_flags_isValid;

    QString m_server_name;
    bool m_server_name_isSet;
    bool m_server_name_isValid;

    QString m_serverid;
    bool m_serverid_isSet;
    bool m_serverid_isValid;

    QString m_serverpk;
    bool m_serverpk_isSet;
    bool m_serverpk_isValid;

    QString m_siteurl;
    bool m_siteurl_isSet;
    bool m_siteurl_isValid;

    QString m_wsurl;
    bool m_wsurl_isSet;
    bool m_wsurl_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIServer)

#endif // OAIServer_H
