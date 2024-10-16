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
 * OAIAnalytics_CrashGroupOperatingSystemCounts_200_response_operating_systems_inner.h
 *
 * 
 */

#ifndef OAIAnalytics_CrashGroupOperatingSystemCounts_200_response_operating_systems_inner_H
#define OAIAnalytics_CrashGroupOperatingSystemCounts_200_response_operating_systems_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAnalytics_CrashGroupOperatingSystemCounts_200_response_operating_systems_inner : public OAIObject {
public:
    OAIAnalytics_CrashGroupOperatingSystemCounts_200_response_operating_systems_inner();
    OAIAnalytics_CrashGroupOperatingSystemCounts_200_response_operating_systems_inner(QString json);
    ~OAIAnalytics_CrashGroupOperatingSystemCounts_200_response_operating_systems_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getCrashCount() const;
    void setCrashCount(const qint64 &crash_count);
    bool is_crash_count_Set() const;
    bool is_crash_count_Valid() const;

    QString getOperatingSystemName() const;
    void setOperatingSystemName(const QString &operating_system_name);
    bool is_operating_system_name_Set() const;
    bool is_operating_system_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_crash_count;
    bool m_crash_count_isSet;
    bool m_crash_count_isValid;

    QString m_operating_system_name;
    bool m_operating_system_name_isSet;
    bool m_operating_system_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAnalytics_CrashGroupOperatingSystemCounts_200_response_operating_systems_inner)

#endif // OAIAnalytics_CrashGroupOperatingSystemCounts_200_response_operating_systems_inner_H
