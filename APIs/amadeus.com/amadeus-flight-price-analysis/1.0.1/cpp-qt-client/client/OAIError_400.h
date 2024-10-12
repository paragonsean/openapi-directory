/**
 * Flight Price Analysis API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIError_400.h
 *
 * A set of errors
 */

#ifndef OAIError_400_H
#define OAIError_400_H

#include <QJsonObject>

#include "OAIError.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIError;

class OAIError_400 : public OAIObject {
public:
    OAIError_400();
    OAIError_400(QString json);
    ~OAIError_400() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIError> getErrors() const;
    void setErrors(const QList<OAIError> &errors);
    bool is_errors_Set() const;
    bool is_errors_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIError> m_errors;
    bool m_errors_isSet;
    bool m_errors_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIError_400)

#endif // OAIError_400_H
