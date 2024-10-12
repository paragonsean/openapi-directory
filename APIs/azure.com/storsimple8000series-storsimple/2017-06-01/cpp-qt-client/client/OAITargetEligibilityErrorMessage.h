/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITargetEligibilityErrorMessage.h
 *
 * The error/warning message due to which the device is ineligible as a failover target device.
 */

#ifndef OAITargetEligibilityErrorMessage_H
#define OAITargetEligibilityErrorMessage_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITargetEligibilityErrorMessage : public OAIObject {
public:
    OAITargetEligibilityErrorMessage();
    OAITargetEligibilityErrorMessage(QString json);
    ~OAITargetEligibilityErrorMessage() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QString getResolution() const;
    void setResolution(const QString &resolution);
    bool is_resolution_Set() const;
    bool is_resolution_Valid() const;

    QString getResultCode() const;
    void setResultCode(const QString &result_code);
    bool is_result_code_Set() const;
    bool is_result_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QString m_resolution;
    bool m_resolution_isSet;
    bool m_resolution_isValid;

    QString m_result_code;
    bool m_result_code_isSet;
    bool m_result_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITargetEligibilityErrorMessage)

#endif // OAITargetEligibilityErrorMessage_H
