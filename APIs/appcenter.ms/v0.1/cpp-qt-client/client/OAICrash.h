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

/*
 * OAICrash.h
 *
 * 
 */

#ifndef OAICrash_H
#define OAICrash_H

#include <QJsonObject>

#include "OAICrash_details.h"
#include "OAIStacktrace.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICrash_details;
class OAIStacktrace;

class OAICrash : public OAIObject {
public:
    OAICrash();
    OAICrash(QString json);
    ~OAICrash() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBuild() const;
    void setBuild(const QString &build);
    bool is_build_Set() const;
    bool is_build_Valid() const;

    QString getCrashId() const;
    void setCrashId(const QString &crash_id);
    bool is_crash_id_Set() const;
    bool is_crash_id_Valid() const;

    OAICrash_details getDetails() const;
    void setDetails(const OAICrash_details &details);
    bool is_details_Set() const;
    bool is_details_Valid() const;

    QString getDevice() const;
    void setDevice(const QString &device);
    bool is_device_Set() const;
    bool is_device_Valid() const;

    QString getDeviceName() const;
    void setDeviceName(const QString &device_name);
    bool is_device_name_Set() const;
    bool is_device_name_Valid() const;

    QString getDisplayId() const;
    void setDisplayId(const QString &display_id);
    bool is_display_id_Set() const;
    bool is_display_id_Valid() const;

    QString getNewCrashGroupId() const;
    void setNewCrashGroupId(const QString &new_crash_group_id);
    bool is_new_crash_group_id_Set() const;
    bool is_new_crash_group_id_Valid() const;

    QString getNewCrashId() const;
    void setNewCrashId(const QString &new_crash_id);
    bool is_new_crash_id_Set() const;
    bool is_new_crash_id_Valid() const;

    QString getOsType() const;
    void setOsType(const QString &os_type);
    bool is_os_type_Set() const;
    bool is_os_type_Valid() const;

    QString getOsVersion() const;
    void setOsVersion(const QString &os_version);
    bool is_os_version_Set() const;
    bool is_os_version_Valid() const;

    OAIStacktrace getStacktrace() const;
    void setStacktrace(const OAIStacktrace &stacktrace);
    bool is_stacktrace_Set() const;
    bool is_stacktrace_Valid() const;

    QDateTime getTimestamp() const;
    void setTimestamp(const QDateTime &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    QString getUserEmail() const;
    void setUserEmail(const QString &user_email);
    bool is_user_email_Set() const;
    bool is_user_email_Valid() const;

    QString getUserName() const;
    void setUserName(const QString &user_name);
    bool is_user_name_Set() const;
    bool is_user_name_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_build;
    bool m_build_isSet;
    bool m_build_isValid;

    QString m_crash_id;
    bool m_crash_id_isSet;
    bool m_crash_id_isValid;

    OAICrash_details m_details;
    bool m_details_isSet;
    bool m_details_isValid;

    QString m_device;
    bool m_device_isSet;
    bool m_device_isValid;

    QString m_device_name;
    bool m_device_name_isSet;
    bool m_device_name_isValid;

    QString m_display_id;
    bool m_display_id_isSet;
    bool m_display_id_isValid;

    QString m_new_crash_group_id;
    bool m_new_crash_group_id_isSet;
    bool m_new_crash_group_id_isValid;

    QString m_new_crash_id;
    bool m_new_crash_id_isSet;
    bool m_new_crash_id_isValid;

    QString m_os_type;
    bool m_os_type_isSet;
    bool m_os_type_isValid;

    QString m_os_version;
    bool m_os_version_isSet;
    bool m_os_version_isValid;

    OAIStacktrace m_stacktrace;
    bool m_stacktrace_isSet;
    bool m_stacktrace_isValid;

    QDateTime m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;

    QString m_user_email;
    bool m_user_email_isSet;
    bool m_user_email_isValid;

    QString m_user_name;
    bool m_user_name_isSet;
    bool m_user_name_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICrash)

#endif // OAICrash_H
