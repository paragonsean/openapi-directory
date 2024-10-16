/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIMultiSharedRulesResult.h
 *
 * 
 */

#ifndef OAIMultiSharedRulesResult_H
#define OAIMultiSharedRulesResult_H

#include <QJsonObject>

#include "OAISharedRules.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISharedRules;

class OAIMultiSharedRulesResult : public OAIObject {
public:
    OAIMultiSharedRulesResult();
    OAIMultiSharedRulesResult(QString json);
    ~OAIMultiSharedRulesResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAISharedRules> getResult() const;
    void setResult(const QList<OAISharedRules> &result);
    bool is_result_Set() const;
    bool is_result_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAISharedRules> m_result;
    bool m_result_isSet;
    bool m_result_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMultiSharedRulesResult)

#endif // OAIMultiSharedRulesResult_H
