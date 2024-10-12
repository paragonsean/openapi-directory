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
 * OAIPatientAuthConfirmResponse_auth.h
 *
 * depending on the purpose of auth, as specified in /auth/init, the response may include the following    1. LINK - only returns **accessToken**   2. KYC - only returns **patient**   3. KYC_AND_LINK - returns both **accessToken** and **patient** 
 */

#ifndef OAIPatientAuthConfirmResponse_auth_H
#define OAIPatientAuthConfirmResponse_auth_H

#include <QJsonObject>

#include "OAIAccessTokenValidity.h"
#include "OAIPatientDemographicResponse.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPatientDemographicResponse;
class OAIAccessTokenValidity;

class OAIPatientAuthConfirmResponse_auth : public OAIObject {
public:
    OAIPatientAuthConfirmResponse_auth();
    OAIPatientAuthConfirmResponse_auth(QString json);
    ~OAIPatientAuthConfirmResponse_auth() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccessToken() const;
    void setAccessToken(const QString &access_token);
    bool is_access_token_Set() const;
    bool is_access_token_Valid() const;

    OAIPatientDemographicResponse getPatient() const;
    void setPatient(const OAIPatientDemographicResponse &patient);
    bool is_patient_Set() const;
    bool is_patient_Valid() const;

    OAIAccessTokenValidity getValidity() const;
    void setValidity(const OAIAccessTokenValidity &validity);
    bool is_validity_Set() const;
    bool is_validity_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_access_token;
    bool m_access_token_isSet;
    bool m_access_token_isValid;

    OAIPatientDemographicResponse m_patient;
    bool m_patient_isSet;
    bool m_patient_isValid;

    OAIAccessTokenValidity m_validity;
    bool m_validity_isSet;
    bool m_validity_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPatientAuthConfirmResponse_auth)

#endif // OAIPatientAuthConfirmResponse_auth_H
