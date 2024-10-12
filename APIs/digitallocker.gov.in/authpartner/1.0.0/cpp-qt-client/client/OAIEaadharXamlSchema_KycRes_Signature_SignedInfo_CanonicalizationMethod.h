/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod.h
 *
 * 
 */

#ifndef OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod_H
#define OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod : public OAIObject {
public:
    OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod();
    OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod(QString json);
    ~OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAlgorithm() const;
    void setAlgorithm(const QString &algorithm);
    bool is_algorithm_Set() const;
    bool is_algorithm_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_algorithm;
    bool m_algorithm_isSet;
    bool m_algorithm_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod)

#endif // OAIEaadharXamlSchema_KycRes_Signature_SignedInfo_CanonicalizationMethod_H
