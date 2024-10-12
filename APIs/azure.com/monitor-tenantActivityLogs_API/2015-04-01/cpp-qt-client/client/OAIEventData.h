/**
 * MonitorManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEventData.h
 *
 * The Azure event log entries are of type EventData
 */

#ifndef OAIEventData_H
#define OAIEventData_H

#include <QJsonObject>

#include "OAIHttpRequestInfo.h"
#include "OAILocalizableString.h"
#include "OAISenderAuthorization.h"
#include <QDateTime>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISenderAuthorization;
class OAILocalizableString;
class OAIHttpRequestInfo;

class OAIEventData : public OAIObject {
public:
    OAIEventData();
    OAIEventData(QString json);
    ~OAIEventData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAISenderAuthorization getAuthorization() const;
    void setAuthorization(const OAISenderAuthorization &authorization);
    bool is_authorization_Set() const;
    bool is_authorization_Valid() const;

    QString getCaller() const;
    void setCaller(const QString &caller);
    bool is_caller_Set() const;
    bool is_caller_Valid() const;

    OAILocalizableString getCategory() const;
    void setCategory(const OAILocalizableString &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    QMap<QString, QString> getClaims() const;
    void setClaims(const QMap<QString, QString> &claims);
    bool is_claims_Set() const;
    bool is_claims_Valid() const;

    QString getCorrelationId() const;
    void setCorrelationId(const QString &correlation_id);
    bool is_correlation_id_Set() const;
    bool is_correlation_id_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getEventDataId() const;
    void setEventDataId(const QString &event_data_id);
    bool is_event_data_id_Set() const;
    bool is_event_data_id_Valid() const;

    OAILocalizableString getEventName() const;
    void setEventName(const OAILocalizableString &event_name);
    bool is_event_name_Set() const;
    bool is_event_name_Valid() const;

    QDateTime getEventTimestamp() const;
    void setEventTimestamp(const QDateTime &event_timestamp);
    bool is_event_timestamp_Set() const;
    bool is_event_timestamp_Valid() const;

    OAIHttpRequestInfo getHttpRequest() const;
    void setHttpRequest(const OAIHttpRequestInfo &http_request);
    bool is_http_request_Set() const;
    bool is_http_request_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLevel() const;
    void setLevel(const QString &level);
    bool is_level_Set() const;
    bool is_level_Valid() const;

    QString getOperationId() const;
    void setOperationId(const QString &operation_id);
    bool is_operation_id_Set() const;
    bool is_operation_id_Valid() const;

    OAILocalizableString getOperationName() const;
    void setOperationName(const OAILocalizableString &operation_name);
    bool is_operation_name_Set() const;
    bool is_operation_name_Valid() const;

    QMap<QString, QString> getProperties() const;
    void setProperties(const QMap<QString, QString> &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getResourceGroupName() const;
    void setResourceGroupName(const QString &resource_group_name);
    bool is_resource_group_name_Set() const;
    bool is_resource_group_name_Valid() const;

    QString getResourceId() const;
    void setResourceId(const QString &resource_id);
    bool is_resource_id_Set() const;
    bool is_resource_id_Valid() const;

    OAILocalizableString getResourceProviderName() const;
    void setResourceProviderName(const OAILocalizableString &resource_provider_name);
    bool is_resource_provider_name_Set() const;
    bool is_resource_provider_name_Valid() const;

    OAILocalizableString getResourceType() const;
    void setResourceType(const OAILocalizableString &resource_type);
    bool is_resource_type_Set() const;
    bool is_resource_type_Valid() const;

    OAILocalizableString getStatus() const;
    void setStatus(const OAILocalizableString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    OAILocalizableString getSubStatus() const;
    void setSubStatus(const OAILocalizableString &sub_status);
    bool is_sub_status_Set() const;
    bool is_sub_status_Valid() const;

    QDateTime getSubmissionTimestamp() const;
    void setSubmissionTimestamp(const QDateTime &submission_timestamp);
    bool is_submission_timestamp_Set() const;
    bool is_submission_timestamp_Valid() const;

    QString getSubscriptionId() const;
    void setSubscriptionId(const QString &subscription_id);
    bool is_subscription_id_Set() const;
    bool is_subscription_id_Valid() const;

    QString getTenantId() const;
    void setTenantId(const QString &tenant_id);
    bool is_tenant_id_Set() const;
    bool is_tenant_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAISenderAuthorization m_authorization;
    bool m_authorization_isSet;
    bool m_authorization_isValid;

    QString m_caller;
    bool m_caller_isSet;
    bool m_caller_isValid;

    OAILocalizableString m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    QMap<QString, QString> m_claims;
    bool m_claims_isSet;
    bool m_claims_isValid;

    QString m_correlation_id;
    bool m_correlation_id_isSet;
    bool m_correlation_id_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_event_data_id;
    bool m_event_data_id_isSet;
    bool m_event_data_id_isValid;

    OAILocalizableString m_event_name;
    bool m_event_name_isSet;
    bool m_event_name_isValid;

    QDateTime m_event_timestamp;
    bool m_event_timestamp_isSet;
    bool m_event_timestamp_isValid;

    OAIHttpRequestInfo m_http_request;
    bool m_http_request_isSet;
    bool m_http_request_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_level;
    bool m_level_isSet;
    bool m_level_isValid;

    QString m_operation_id;
    bool m_operation_id_isSet;
    bool m_operation_id_isValid;

    OAILocalizableString m_operation_name;
    bool m_operation_name_isSet;
    bool m_operation_name_isValid;

    QMap<QString, QString> m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_resource_group_name;
    bool m_resource_group_name_isSet;
    bool m_resource_group_name_isValid;

    QString m_resource_id;
    bool m_resource_id_isSet;
    bool m_resource_id_isValid;

    OAILocalizableString m_resource_provider_name;
    bool m_resource_provider_name_isSet;
    bool m_resource_provider_name_isValid;

    OAILocalizableString m_resource_type;
    bool m_resource_type_isSet;
    bool m_resource_type_isValid;

    OAILocalizableString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    OAILocalizableString m_sub_status;
    bool m_sub_status_isSet;
    bool m_sub_status_isValid;

    QDateTime m_submission_timestamp;
    bool m_submission_timestamp_isSet;
    bool m_submission_timestamp_isValid;

    QString m_subscription_id;
    bool m_subscription_id_isSet;
    bool m_subscription_id_isValid;

    QString m_tenant_id;
    bool m_tenant_id_isSet;
    bool m_tenant_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEventData)

#endif // OAIEventData_H
