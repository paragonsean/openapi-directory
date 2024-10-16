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
 * OAIActiveCrashingAppDetails_appsWithCrashes_inner.h
 *
 * 
 */

#ifndef OAIActiveCrashingAppDetails_appsWithCrashes_inner_H
#define OAIActiveCrashingAppDetails_appsWithCrashes_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIActiveCrashingAppDetails_appsWithCrashes_inner : public OAIObject {
public:
    OAIActiveCrashingAppDetails_appsWithCrashes_inner();
    OAIActiveCrashingAppDetails_appsWithCrashes_inner(QString json);
    ~OAIActiveCrashingAppDetails_appsWithCrashes_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAppId() const;
    void setAppId(const QString &app_id);
    bool is_app_id_Set() const;
    bool is_app_id_Valid() const;

    QString getAppVersion() const;
    void setAppVersion(const QString &app_version);
    bool is_app_version_Set() const;
    bool is_app_version_Valid() const;

    QString getCrashGroupId() const;
    void setCrashGroupId(const QString &crash_group_id);
    bool is_crash_group_id_Set() const;
    bool is_crash_group_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_app_id;
    bool m_app_id_isSet;
    bool m_app_id_isValid;

    QString m_app_version;
    bool m_app_version_isSet;
    bool m_app_version_isValid;

    QString m_crash_group_id;
    bool m_crash_group_id_isSet;
    bool m_crash_group_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIActiveCrashingAppDetails_appsWithCrashes_inner)

#endif // OAIActiveCrashingAppDetails_appsWithCrashes_inner_H
