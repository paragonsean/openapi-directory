/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetPublishingUser_default_response_error_details_inner.h
 *
 * Detailed errors.
 */

#ifndef OAIGetPublishingUser_default_response_error_details_inner_H
#define OAIGetPublishingUser_default_response_error_details_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetPublishingUser_default_response_error_details_inner : public OAIObject {
public:
    OAIGetPublishingUser_default_response_error_details_inner();
    OAIGetPublishingUser_default_response_error_details_inner(QString json);
    ~OAIGetPublishingUser_default_response_error_details_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QString getTarget() const;
    void setTarget(const QString &target);
    bool is_target_Set() const;
    bool is_target_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QString m_target;
    bool m_target_isSet;
    bool m_target_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetPublishingUser_default_response_error_details_inner)

#endif // OAIGetPublishingUser_default_response_error_details_inner_H
