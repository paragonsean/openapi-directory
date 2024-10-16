/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDataSubjectRightOperation.h
 *
 * 
 */

#ifndef OAIDataSubjectRightOperation_H
#define OAIDataSubjectRightOperation_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDataSubjectRightOperation : public OAIObject {
public:
    OAIDataSubjectRightOperation();
    OAIDataSubjectRightOperation(QString json);
    ~OAIDataSubjectRightOperation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAppId() const;
    void setAppId(const QString &app_id);
    bool is_app_id_Set() const;
    bool is_app_id_Valid() const;

    QString getContext() const;
    void setContext(const QString &context);
    bool is_context_Set() const;
    bool is_context_Valid() const;

    QString getOperationId() const;
    void setOperationId(const QString &operation_id);
    bool is_operation_id_Set() const;
    bool is_operation_id_Valid() const;

    QString getParticipant() const;
    void setParticipant(const QString &participant);
    bool is_participant_Set() const;
    bool is_participant_Valid() const;

    QString getParticipantData() const;
    void setParticipantData(const QString &participant_data);
    bool is_participant_data_Set() const;
    bool is_participant_data_Valid() const;

    QString getRequestId() const;
    void setRequestId(const QString &request_id);
    bool is_request_id_Set() const;
    bool is_request_id_Valid() const;

    QString getRequestType() const;
    void setRequestType(const QString &request_type);
    bool is_request_type_Set() const;
    bool is_request_type_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_app_id;
    bool m_app_id_isSet;
    bool m_app_id_isValid;

    QString m_context;
    bool m_context_isSet;
    bool m_context_isValid;

    QString m_operation_id;
    bool m_operation_id_isSet;
    bool m_operation_id_isValid;

    QString m_participant;
    bool m_participant_isSet;
    bool m_participant_isValid;

    QString m_participant_data;
    bool m_participant_data_isSet;
    bool m_participant_data_isValid;

    QString m_request_id;
    bool m_request_id_isSet;
    bool m_request_id_isValid;

    QString m_request_type;
    bool m_request_type_isSet;
    bool m_request_type_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDataSubjectRightOperation)

#endif // OAIDataSubjectRightOperation_H
