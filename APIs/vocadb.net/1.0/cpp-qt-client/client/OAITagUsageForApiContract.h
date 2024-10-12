/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITagUsageForApiContract.h
 *
 * 
 */

#ifndef OAITagUsageForApiContract_H
#define OAITagUsageForApiContract_H

#include <QJsonObject>

#include "OAITagBaseContract.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITagBaseContract;

class OAITagUsageForApiContract : public OAIObject {
public:
    OAITagUsageForApiContract();
    OAITagUsageForApiContract(QString json);
    ~OAITagUsageForApiContract() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCount() const;
    void setCount(const qint32 &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    OAITagBaseContract getTag() const;
    void setTag(const OAITagBaseContract &tag);
    bool is_tag_Set() const;
    bool is_tag_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    OAITagBaseContract m_tag;
    bool m_tag_isSet;
    bool m_tag_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITagUsageForApiContract)

#endif // OAITagUsageForApiContract_H
