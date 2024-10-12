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
 * OAIAlertProperties.h
 *
 * The properties of alert
 */

#ifndef OAIAlertProperties_H
#define OAIAlertProperties_H

#include <QJsonObject>

#include "OAIAlertErrorDetails.h"
#include "OAIAlertSource.h"
#include <QDateTime>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAlertErrorDetails;
class OAIAlertSource;

class OAIAlertProperties : public OAIObject {
public:
    OAIAlertProperties();
    OAIAlertProperties(QString json);
    ~OAIAlertProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAlertType() const;
    void setAlertType(const QString &alert_type);
    bool is_alert_type_Set() const;
    bool is_alert_type_Valid() const;

    QDateTime getAppearedAtSourceTime() const;
    void setAppearedAtSourceTime(const QDateTime &appeared_at_source_time);
    bool is_appeared_at_source_time_Set() const;
    bool is_appeared_at_source_time_Valid() const;

    QDateTime getAppearedAtTime() const;
    void setAppearedAtTime(const QDateTime &appeared_at_time);
    bool is_appeared_at_time_Set() const;
    bool is_appeared_at_time_Valid() const;

    QDateTime getClearedAtSourceTime() const;
    void setClearedAtSourceTime(const QDateTime &cleared_at_source_time);
    bool is_cleared_at_source_time_Set() const;
    bool is_cleared_at_source_time_Valid() const;

    QDateTime getClearedAtTime() const;
    void setClearedAtTime(const QDateTime &cleared_at_time);
    bool is_cleared_at_time_Set() const;
    bool is_cleared_at_time_Valid() const;

    QMap<QString, QString> getDetailedInformation() const;
    void setDetailedInformation(const QMap<QString, QString> &detailed_information);
    bool is_detailed_information_Set() const;
    bool is_detailed_information_Valid() const;

    OAIAlertErrorDetails getErrorDetails() const;
    void setErrorDetails(const OAIAlertErrorDetails &error_details);
    bool is_error_details_Set() const;
    bool is_error_details_Valid() const;

    QString getRecommendation() const;
    void setRecommendation(const QString &recommendation);
    bool is_recommendation_Set() const;
    bool is_recommendation_Valid() const;

    QString getResolutionReason() const;
    void setResolutionReason(const QString &resolution_reason);
    bool is_resolution_reason_Set() const;
    bool is_resolution_reason_Valid() const;

    QString getScope() const;
    void setScope(const QString &scope);
    bool is_scope_Set() const;
    bool is_scope_Valid() const;

    QString getSeverity() const;
    void setSeverity(const QString &severity);
    bool is_severity_Set() const;
    bool is_severity_Valid() const;

    OAIAlertSource getSource() const;
    void setSource(const OAIAlertSource &source);
    bool is_source_Set() const;
    bool is_source_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_alert_type;
    bool m_alert_type_isSet;
    bool m_alert_type_isValid;

    QDateTime m_appeared_at_source_time;
    bool m_appeared_at_source_time_isSet;
    bool m_appeared_at_source_time_isValid;

    QDateTime m_appeared_at_time;
    bool m_appeared_at_time_isSet;
    bool m_appeared_at_time_isValid;

    QDateTime m_cleared_at_source_time;
    bool m_cleared_at_source_time_isSet;
    bool m_cleared_at_source_time_isValid;

    QDateTime m_cleared_at_time;
    bool m_cleared_at_time_isSet;
    bool m_cleared_at_time_isValid;

    QMap<QString, QString> m_detailed_information;
    bool m_detailed_information_isSet;
    bool m_detailed_information_isValid;

    OAIAlertErrorDetails m_error_details;
    bool m_error_details_isSet;
    bool m_error_details_isValid;

    QString m_recommendation;
    bool m_recommendation_isSet;
    bool m_recommendation_isValid;

    QString m_resolution_reason;
    bool m_resolution_reason_isSet;
    bool m_resolution_reason_isValid;

    QString m_scope;
    bool m_scope_isSet;
    bool m_scope_isValid;

    QString m_severity;
    bool m_severity_isSet;
    bool m_severity_isValid;

    OAIAlertSource m_source;
    bool m_source_isSet;
    bool m_source_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAlertProperties)

#endif // OAIAlertProperties_H
