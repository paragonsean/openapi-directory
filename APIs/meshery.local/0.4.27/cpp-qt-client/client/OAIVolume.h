/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIVolume.h
 *
 * Volume volume
 */

#ifndef OAIVolume_H
#define OAIVolume_H

#include <QJsonObject>

#include "OAIObject.h"
#include "OAIVolumeUsageData.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIVolumeUsageData;

class OAIVolume : public OAIObject {
public:
    OAIVolume();
    OAIVolume(QString json);
    ~OAIVolume() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getDriver() const;
    void setDriver(const QString &driver);
    bool is_driver_Set() const;
    bool is_driver_Valid() const;

    QMap<QString, QString> getLabels() const;
    void setLabels(const QMap<QString, QString> &labels);
    bool is_labels_Set() const;
    bool is_labels_Valid() const;

    QString getMountpoint() const;
    void setMountpoint(const QString &mountpoint);
    bool is_mountpoint_Set() const;
    bool is_mountpoint_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QMap<QString, QString> getOptions() const;
    void setOptions(const QMap<QString, QString> &options);
    bool is_options_Set() const;
    bool is_options_Valid() const;

    QString getScope() const;
    void setScope(const QString &scope);
    bool is_scope_Set() const;
    bool is_scope_Valid() const;

    QMap<QString, OAIObject> getStatus() const;
    void setStatus(const QMap<QString, OAIObject> &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    OAIVolumeUsageData getUsageData() const;
    void setUsageData(const OAIVolumeUsageData &usage_data);
    bool is_usage_data_Set() const;
    bool is_usage_data_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_driver;
    bool m_driver_isSet;
    bool m_driver_isValid;

    QMap<QString, QString> m_labels;
    bool m_labels_isSet;
    bool m_labels_isValid;

    QString m_mountpoint;
    bool m_mountpoint_isSet;
    bool m_mountpoint_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QMap<QString, QString> m_options;
    bool m_options_isSet;
    bool m_options_isValid;

    QString m_scope;
    bool m_scope_isSet;
    bool m_scope_isValid;

    QMap<QString, OAIObject> m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    OAIVolumeUsageData m_usage_data;
    bool m_usage_data_isSet;
    bool m_usage_data_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVolume)

#endif // OAIVolume_H
