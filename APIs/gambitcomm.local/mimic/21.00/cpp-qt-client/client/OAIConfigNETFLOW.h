/**
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIConfigNETFLOW.h
 *
 * 
 */

#ifndef OAIConfigNETFLOW_H
#define OAIConfigNETFLOW_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIConfigNETFLOW : public OAIObject {
public:
    OAIConfigNETFLOW();
    OAIConfigNETFLOW(QString json);
    ~OAIConfigNETFLOW() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getBundleflowsets() const;
    void setBundleflowsets(const qint32 &bundleflowsets);
    bool is_bundleflowsets_Set() const;
    bool is_bundleflowsets_Valid() const;

    QString getCollector() const;
    void setCollector(const QString &collector);
    bool is_collector_Set() const;
    bool is_collector_Valid() const;

    qint32 getCollectorport() const;
    void setCollectorport(const qint32 &collectorport);
    bool is_collectorport_Set() const;
    bool is_collectorport_Valid() const;

    QString getFilename() const;
    void setFilename(const QString &filename);
    bool is_filename_Set() const;
    bool is_filename_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_bundleflowsets;
    bool m_bundleflowsets_isSet;
    bool m_bundleflowsets_isValid;

    QString m_collector;
    bool m_collector_isSet;
    bool m_collector_isValid;

    qint32 m_collectorport;
    bool m_collectorport_isSet;
    bool m_collectorport_isValid;

    QString m_filename;
    bool m_filename_isSet;
    bool m_filename_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConfigNETFLOW)

#endif // OAIConfigNETFLOW_H
