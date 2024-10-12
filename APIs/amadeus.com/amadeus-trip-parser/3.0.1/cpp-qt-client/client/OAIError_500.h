/**
 * Trip Parser
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 3.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIError_500.h
 *
 * 
 */

#ifndef OAIError_500_H
#define OAIError_500_H

#include <QJsonObject>

#include "OAIIssue.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIssue;

class OAIError_500 : public OAIObject {
public:
    OAIError_500();
    OAIError_500(QString json);
    ~OAIError_500() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIIssue> getErrors() const;
    void setErrors(const QList<OAIIssue> &errors);
    bool is_errors_Set() const;
    bool is_errors_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIIssue> m_errors;
    bool m_errors_isSet;
    bool m_errors_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIError_500)

#endif // OAIError_500_H
