/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIErrorMessage.h
 *
 * 
 */

#ifndef OAIErrorMessage_H
#define OAIErrorMessage_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIErrorMessage : public OAIObject {
public:
    OAIErrorMessage();
    OAIErrorMessage(QString json);
    ~OAIErrorMessage() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getCode() const;
    void setCode(const qint64 &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIErrorMessage)

#endif // OAIErrorMessage_H
