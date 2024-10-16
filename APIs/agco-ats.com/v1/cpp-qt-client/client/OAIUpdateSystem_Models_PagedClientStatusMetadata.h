/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateSystem_Models_PagedClientStatusMetadata.h
 *
 * 
 */

#ifndef OAIUpdateSystem_Models_PagedClientStatusMetadata_H
#define OAIUpdateSystem_Models_PagedClientStatusMetadata_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateSystem_Models_PagedClientStatusMetadata : public OAIObject {
public:
    OAIUpdateSystem_Models_PagedClientStatusMetadata();
    OAIUpdateSystem_Models_PagedClientStatusMetadata(QString json);
    ~OAIUpdateSystem_Models_PagedClientStatusMetadata() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getLimit() const;
    void setLimit(const qint32 &limit);
    bool is_limit_Set() const;
    bool is_limit_Valid() const;

    qint32 getOffset() const;
    void setOffset(const qint32 &offset);
    bool is_offset_Set() const;
    bool is_offset_Valid() const;

    QString getReportResultExpected() const;
    void setReportResultExpected(const QString &report_result_expected);
    bool is_report_result_expected_Set() const;
    bool is_report_result_expected_Valid() const;

    QString getReportResultLabel() const;
    void setReportResultLabel(const QString &report_result_label);
    bool is_report_result_label_Set() const;
    bool is_report_result_label_Valid() const;

    QString getReportValueLabel() const;
    void setReportValueLabel(const QString &report_value_label);
    bool is_report_value_label_Set() const;
    bool is_report_value_label_Valid() const;

    qint32 getTotalCount() const;
    void setTotalCount(const qint32 &total_count);
    bool is_total_count_Set() const;
    bool is_total_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_limit;
    bool m_limit_isSet;
    bool m_limit_isValid;

    qint32 m_offset;
    bool m_offset_isSet;
    bool m_offset_isValid;

    QString m_report_result_expected;
    bool m_report_result_expected_isSet;
    bool m_report_result_expected_isValid;

    QString m_report_result_label;
    bool m_report_result_label_isSet;
    bool m_report_result_label_isValid;

    QString m_report_value_label;
    bool m_report_value_label_isSet;
    bool m_report_value_label_isValid;

    qint32 m_total_count;
    bool m_total_count_isSet;
    bool m_total_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateSystem_Models_PagedClientStatusMetadata)

#endif // OAIUpdateSystem_Models_PagedClientStatusMetadata_H
