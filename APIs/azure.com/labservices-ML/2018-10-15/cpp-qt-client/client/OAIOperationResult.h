/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOperationResult.h
 *
 * An Operation Result
 */

#ifndef OAIOperationResult_H
#define OAIOperationResult_H

#include <QJsonObject>

#include "OAIOperationError.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOperationError;

class OAIOperationResult : public OAIObject {
public:
    OAIOperationResult();
    OAIOperationResult(QString json);
    ~OAIOperationResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIOperationError getError() const;
    void setError(const OAIOperationError &error);
    bool is_error_Set() const;
    bool is_error_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIOperationError m_error;
    bool m_error_isSet;
    bool m_error_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOperationResult)

#endif // OAIOperationResult_H
