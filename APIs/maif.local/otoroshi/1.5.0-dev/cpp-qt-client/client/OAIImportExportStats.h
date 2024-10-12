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
 * OAIImportExportStats.h
 *
 * Global stats for the current Otoroshi instances
 */

#ifndef OAIImportExportStats_H
#define OAIImportExportStats_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIImportExportStats : public OAIObject {
public:
    OAIImportExportStats();
    OAIImportExportStats(QString json);
    ~OAIImportExportStats() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getCalls() const;
    void setCalls(const qint64 &calls);
    bool is_calls_Set() const;
    bool is_calls_Valid() const;

    qint64 getDataIn() const;
    void setDataIn(const qint64 &data_in);
    bool is_data_in_Set() const;
    bool is_data_in_Valid() const;

    qint64 getDataOut() const;
    void setDataOut(const qint64 &data_out);
    bool is_data_out_Set() const;
    bool is_data_out_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_calls;
    bool m_calls_isSet;
    bool m_calls_isValid;

    qint64 m_data_in;
    bool m_data_in_isSet;
    bool m_data_in_isValid;

    qint64 m_data_out;
    bool m_data_out_isSet;
    bool m_data_out_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImportExportStats)

#endif // OAIImportExportStats_H
