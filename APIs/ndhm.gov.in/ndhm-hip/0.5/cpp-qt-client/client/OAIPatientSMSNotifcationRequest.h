/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPatientSMSNotifcationRequest.h
 *
 * 
 */

#ifndef OAIPatientSMSNotifcationRequest_H
#define OAIPatientSMSNotifcationRequest_H

#include <QJsonObject>

#include "OAIPatientSMSNotifcationRequest_notification.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPatientSMSNotifcationRequest_notification;

class OAIPatientSMSNotifcationRequest : public OAIObject {
public:
    OAIPatientSMSNotifcationRequest();
    OAIPatientSMSNotifcationRequest(QString json);
    ~OAIPatientSMSNotifcationRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPatientSMSNotifcationRequest_notification getNotification() const;
    void setNotification(const OAIPatientSMSNotifcationRequest_notification &notification);
    bool is_notification_Set() const;
    bool is_notification_Valid() const;

    QString getRequestId() const;
    void setRequestId(const QString &request_id);
    bool is_request_id_Set() const;
    bool is_request_id_Valid() const;

    QDateTime getTimestamp() const;
    void setTimestamp(const QDateTime &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPatientSMSNotifcationRequest_notification m_notification;
    bool m_notification_isSet;
    bool m_notification_isValid;

    QString m_request_id;
    bool m_request_id_isSet;
    bool m_request_id_isValid;

    QDateTime m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPatientSMSNotifcationRequest)

#endif // OAIPatientSMSNotifcationRequest_H
