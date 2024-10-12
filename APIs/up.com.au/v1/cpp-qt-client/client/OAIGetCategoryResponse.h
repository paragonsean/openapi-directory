/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetCategoryResponse.h
 *
 * Successful response to get a single category and its ancestry. 
 */

#ifndef OAIGetCategoryResponse_H
#define OAIGetCategoryResponse_H

#include <QJsonObject>

#include "OAICategoryResource.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICategoryResource;

class OAIGetCategoryResponse : public OAIObject {
public:
    OAIGetCategoryResponse();
    OAIGetCategoryResponse(QString json);
    ~OAIGetCategoryResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICategoryResource getData() const;
    void setData(const OAICategoryResource &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICategoryResource m_data;
    bool m_data_isSet;
    bool m_data_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetCategoryResponse)

#endif // OAIGetCategoryResponse_H
