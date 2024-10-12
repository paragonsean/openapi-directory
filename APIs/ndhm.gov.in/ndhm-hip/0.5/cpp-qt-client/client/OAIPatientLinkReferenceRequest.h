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
 * OAIPatientLinkReferenceRequest.h
 *
 * 
 */

#ifndef OAIPatientLinkReferenceRequest_H
#define OAIPatientLinkReferenceRequest_H

#include <QJsonObject>

#include "OAIPatientLinkReferenceRequest_patient.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPatientLinkReferenceRequest_patient;

class OAIPatientLinkReferenceRequest : public OAIObject {
public:
    OAIPatientLinkReferenceRequest();
    OAIPatientLinkReferenceRequest(QString json);
    ~OAIPatientLinkReferenceRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPatientLinkReferenceRequest_patient getPatient() const;
    void setPatient(const OAIPatientLinkReferenceRequest_patient &patient);
    bool is_patient_Set() const;
    bool is_patient_Valid() const;

    QString getRequestId() const;
    void setRequestId(const QString &request_id);
    bool is_request_id_Set() const;
    bool is_request_id_Valid() const;

    QDateTime getTimestamp() const;
    void setTimestamp(const QDateTime &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    QString getTransactionId() const;
    void setTransactionId(const QString &transaction_id);
    bool is_transaction_id_Set() const;
    bool is_transaction_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPatientLinkReferenceRequest_patient m_patient;
    bool m_patient_isSet;
    bool m_patient_isValid;

    QString m_request_id;
    bool m_request_id_isSet;
    bool m_request_id_isValid;

    QDateTime m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;

    QString m_transaction_id;
    bool m_transaction_id_isSet;
    bool m_transaction_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPatientLinkReferenceRequest)

#endif // OAIPatientLinkReferenceRequest_H
