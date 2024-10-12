/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITimeSettingsProperties.h
 *
 * The properties of time settings of a device.
 */

#ifndef OAITimeSettingsProperties_H
#define OAITimeSettingsProperties_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITimeSettingsProperties : public OAIObject {
public:
    OAITimeSettingsProperties();
    OAITimeSettingsProperties(QString json);
    ~OAITimeSettingsProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getPrimaryTimeServer() const;
    void setPrimaryTimeServer(const QString &primary_time_server);
    bool is_primary_time_server_Set() const;
    bool is_primary_time_server_Valid() const;

    QList<QString> getSecondaryTimeServer() const;
    void setSecondaryTimeServer(const QList<QString> &secondary_time_server);
    bool is_secondary_time_server_Set() const;
    bool is_secondary_time_server_Valid() const;

    QString getTimeZone() const;
    void setTimeZone(const QString &time_zone);
    bool is_time_zone_Set() const;
    bool is_time_zone_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_primary_time_server;
    bool m_primary_time_server_isSet;
    bool m_primary_time_server_isValid;

    QList<QString> m_secondary_time_server;
    bool m_secondary_time_server_isSet;
    bool m_secondary_time_server_isValid;

    QString m_time_zone;
    bool m_time_zone_isSet;
    bool m_time_zone_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITimeSettingsProperties)

#endif // OAITimeSettingsProperties_H
