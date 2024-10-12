/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICreateHealthIdOptRequest.h
 *
 * 
 */

#ifndef OAICreateHealthIdOptRequest_H
#define OAICreateHealthIdOptRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateHealthIdOptRequest : public OAIObject {
public:
    OAICreateHealthIdOptRequest();
    OAICreateHealthIdOptRequest(QString json);
    ~OAICreateHealthIdOptRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAutoGeneratedBenefitId() const;
    void setAutoGeneratedBenefitId(const bool &auto_generated_benefit_id);
    bool is_auto_generated_benefit_id_Set() const;
    bool is_auto_generated_benefit_id_Valid() const;

    QString getBenefitId() const;
    void setBenefitId(const QString &benefit_id);
    bool is_benefit_id_Set() const;
    bool is_benefit_id_Valid() const;

    QString getBenefitName() const;
    void setBenefitName(const QString &benefit_name);
    bool is_benefit_name_Set() const;
    bool is_benefit_name_Valid() const;

    bool isConsentHealthId() const;
    void setConsentHealthId(const bool &consent_health_id);
    bool is_consent_health_id_Set() const;
    bool is_consent_health_id_Valid() const;

    QString getMobileNumber() const;
    void setMobileNumber(const QString &mobile_number);
    bool is_mobile_number_Set() const;
    bool is_mobile_number_Valid() const;

    QString getOtp() const;
    void setOtp(const QString &otp);
    bool is_otp_Set() const;
    bool is_otp_Valid() const;

    QString getTxnId() const;
    void setTxnId(const QString &txn_id);
    bool is_txn_id_Set() const;
    bool is_txn_id_Valid() const;

    QString getValidity() const;
    void setValidity(const QString &validity);
    bool is_validity_Set() const;
    bool is_validity_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_auto_generated_benefit_id;
    bool m_auto_generated_benefit_id_isSet;
    bool m_auto_generated_benefit_id_isValid;

    QString m_benefit_id;
    bool m_benefit_id_isSet;
    bool m_benefit_id_isValid;

    QString m_benefit_name;
    bool m_benefit_name_isSet;
    bool m_benefit_name_isValid;

    bool m_consent_health_id;
    bool m_consent_health_id_isSet;
    bool m_consent_health_id_isValid;

    QString m_mobile_number;
    bool m_mobile_number_isSet;
    bool m_mobile_number_isValid;

    QString m_otp;
    bool m_otp_isSet;
    bool m_otp_isValid;

    QString m_txn_id;
    bool m_txn_id_isSet;
    bool m_txn_id_isValid;

    QString m_validity;
    bool m_validity_isSet;
    bool m_validity_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateHealthIdOptRequest)

#endif // OAICreateHealthIdOptRequest_H
