/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAddSmsVerificationRequest.h
 *
 * 
 */

#ifndef OAIAddSmsVerificationRequest_H
#define OAIAddSmsVerificationRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAddSmsVerificationRequest : public OAIObject {
public:
    OAIAddSmsVerificationRequest();
    OAIAddSmsVerificationRequest(QString json);
    ~OAIAddSmsVerificationRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getSms() const;
    void setSms(const QString &sms);
    bool is_sms_Set() const;
    bool is_sms_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_sms;
    bool m_sms_isSet;
    bool m_sms_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAddSmsVerificationRequest)

#endif // OAIAddSmsVerificationRequest_H
