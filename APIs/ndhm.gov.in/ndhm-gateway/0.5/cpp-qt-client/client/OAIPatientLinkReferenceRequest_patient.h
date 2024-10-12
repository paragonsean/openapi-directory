/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPatientLinkReferenceRequest_patient.h
 *
 * 
 */

#ifndef OAIPatientLinkReferenceRequest_patient_H
#define OAIPatientLinkReferenceRequest_patient_H

#include <QJsonObject>

#include "OAICareContext.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICareContext;

class OAIPatientLinkReferenceRequest_patient : public OAIObject {
public:
    OAIPatientLinkReferenceRequest_patient();
    OAIPatientLinkReferenceRequest_patient(QString json);
    ~OAIPatientLinkReferenceRequest_patient() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAICareContext> getCareContexts() const;
    void setCareContexts(const QList<OAICareContext> &care_contexts);
    bool is_care_contexts_Set() const;
    bool is_care_contexts_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getReferenceNumber() const;
    void setReferenceNumber(const QString &reference_number);
    bool is_reference_number_Set() const;
    bool is_reference_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAICareContext> m_care_contexts;
    bool m_care_contexts_isSet;
    bool m_care_contexts_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_reference_number;
    bool m_reference_number_isSet;
    bool m_reference_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPatientLinkReferenceRequest_patient)

#endif // OAIPatientLinkReferenceRequest_patient_H
