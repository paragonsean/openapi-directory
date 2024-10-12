/**
 * import.io
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIReport.h
 *
 * 
 */

#ifndef OAIReport_H
#define OAIReport_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIReport : public OAIObject {
public:
    OAIReport();
    OAIReport(QString json);
    ~OAIReport() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getConfigId() const;
    void setConfigId(const QString &config_id);
    bool is_config_id_Set() const;
    bool is_config_id_Valid() const;

    QString getGuid() const;
    void setGuid(const QString &guid);
    bool is_guid_Set() const;
    bool is_guid_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    bool isPublished() const;
    void setPublished(const bool &published);
    bool is_published_Set() const;
    bool is_published_Valid() const;

    QString getReportId() const;
    void setReportId(const QString &report_id);
    bool is_report_id_Set() const;
    bool is_report_id_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    OAIObject getSummary() const;
    void setSummary(const OAIObject &summary);
    bool is_summary_Set() const;
    bool is_summary_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_config_id;
    bool m_config_id_isSet;
    bool m_config_id_isValid;

    QString m_guid;
    bool m_guid_isSet;
    bool m_guid_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    bool m_published;
    bool m_published_isSet;
    bool m_published_isValid;

    QString m_report_id;
    bool m_report_id_isSet;
    bool m_report_id_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    OAIObject m_summary;
    bool m_summary_isSet;
    bool m_summary_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIReport)

#endif // OAIReport_H
