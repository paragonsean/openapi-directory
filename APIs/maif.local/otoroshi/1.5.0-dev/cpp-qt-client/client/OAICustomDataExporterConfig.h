/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICustomDataExporterConfig.h
 *
 * 
 */

#ifndef OAICustomDataExporterConfig_H
#define OAICustomDataExporterConfig_H

#include <QJsonObject>

#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICustomDataExporterConfig : public OAIObject {
public:
    OAICustomDataExporterConfig();
    OAICustomDataExporterConfig(QString json);
    ~OAICustomDataExporterConfig() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, QString> getConfig() const;
    void setConfig(const QMap<QString, QString> &config);
    bool is_config_Set() const;
    bool is_config_Valid() const;

    QString getRef() const;
    void setRef(const QString &ref);
    bool is_ref_Set() const;
    bool is_ref_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, QString> m_config;
    bool m_config_isSet;
    bool m_config_isValid;

    QString m_ref;
    bool m_ref_isSet;
    bool m_ref_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomDataExporterConfig)

#endif // OAICustomDataExporterConfig_H
