/**
 * Azure SQL Database
 * Provides create, read, update and delete functionality for Azure SQL Database resources including recommendations and operations.
 *
 * The version of the OpenAPI document: 2014-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIElasticPoolDatabaseActivityProperties.h
 *
 * Represents the properties of an elastic pool database activity.
 */

#ifndef OAIElasticPoolDatabaseActivityProperties_H
#define OAIElasticPoolDatabaseActivityProperties_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIElasticPoolDatabaseActivityProperties : public OAIObject {
public:
    OAIElasticPoolDatabaseActivityProperties();
    OAIElasticPoolDatabaseActivityProperties(QString json);
    ~OAIElasticPoolDatabaseActivityProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCurrentElasticPoolName() const;
    void setCurrentElasticPoolName(const QString &current_elastic_pool_name);
    bool is_current_elastic_pool_name_Set() const;
    bool is_current_elastic_pool_name_Valid() const;

    QString getCurrentServiceObjective() const;
    void setCurrentServiceObjective(const QString &current_service_objective);
    bool is_current_service_objective_Set() const;
    bool is_current_service_objective_Valid() const;

    QString getDatabaseName() const;
    void setDatabaseName(const QString &database_name);
    bool is_database_name_Set() const;
    bool is_database_name_Valid() const;

    QDateTime getEndTime() const;
    void setEndTime(const QDateTime &end_time);
    bool is_end_time_Set() const;
    bool is_end_time_Valid() const;

    qint32 getErrorCode() const;
    void setErrorCode(const qint32 &error_code);
    bool is_error_code_Set() const;
    bool is_error_code_Valid() const;

    QString getErrorMessage() const;
    void setErrorMessage(const QString &error_message);
    bool is_error_message_Set() const;
    bool is_error_message_Valid() const;

    qint32 getErrorSeverity() const;
    void setErrorSeverity(const qint32 &error_severity);
    bool is_error_severity_Set() const;
    bool is_error_severity_Valid() const;

    QString getOperation() const;
    void setOperation(const QString &operation);
    bool is_operation_Set() const;
    bool is_operation_Valid() const;

    QString getOperationId() const;
    void setOperationId(const QString &operation_id);
    bool is_operation_id_Set() const;
    bool is_operation_id_Valid() const;

    qint32 getPercentComplete() const;
    void setPercentComplete(const qint32 &percent_complete);
    bool is_percent_complete_Set() const;
    bool is_percent_complete_Valid() const;

    QString getRequestedElasticPoolName() const;
    void setRequestedElasticPoolName(const QString &requested_elastic_pool_name);
    bool is_requested_elastic_pool_name_Set() const;
    bool is_requested_elastic_pool_name_Valid() const;

    QString getRequestedServiceObjective() const;
    void setRequestedServiceObjective(const QString &requested_service_objective);
    bool is_requested_service_objective_Set() const;
    bool is_requested_service_objective_Valid() const;

    QString getServerName() const;
    void setServerName(const QString &server_name);
    bool is_server_name_Set() const;
    bool is_server_name_Valid() const;

    QDateTime getStartTime() const;
    void setStartTime(const QDateTime &start_time);
    bool is_start_time_Set() const;
    bool is_start_time_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_current_elastic_pool_name;
    bool m_current_elastic_pool_name_isSet;
    bool m_current_elastic_pool_name_isValid;

    QString m_current_service_objective;
    bool m_current_service_objective_isSet;
    bool m_current_service_objective_isValid;

    QString m_database_name;
    bool m_database_name_isSet;
    bool m_database_name_isValid;

    QDateTime m_end_time;
    bool m_end_time_isSet;
    bool m_end_time_isValid;

    qint32 m_error_code;
    bool m_error_code_isSet;
    bool m_error_code_isValid;

    QString m_error_message;
    bool m_error_message_isSet;
    bool m_error_message_isValid;

    qint32 m_error_severity;
    bool m_error_severity_isSet;
    bool m_error_severity_isValid;

    QString m_operation;
    bool m_operation_isSet;
    bool m_operation_isValid;

    QString m_operation_id;
    bool m_operation_id_isSet;
    bool m_operation_id_isValid;

    qint32 m_percent_complete;
    bool m_percent_complete_isSet;
    bool m_percent_complete_isValid;

    QString m_requested_elastic_pool_name;
    bool m_requested_elastic_pool_name_isSet;
    bool m_requested_elastic_pool_name_isValid;

    QString m_requested_service_objective;
    bool m_requested_service_objective_isSet;
    bool m_requested_service_objective_isValid;

    QString m_server_name;
    bool m_server_name_isSet;
    bool m_server_name_isValid;

    QDateTime m_start_time;
    bool m_start_time_isSet;
    bool m_start_time_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIElasticPoolDatabaseActivityProperties)

#endif // OAIElasticPoolDatabaseActivityProperties_H
