/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRecommendedRulesRequest.h
 *
 * 
 */

#ifndef OAIRecommendedRulesRequest_H
#define OAIRecommendedRulesRequest_H

#include <QJsonObject>

#include "OAIMicroSecGroup.h"
#include "OAITimeRange.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMicroSecGroup;
class OAITimeRange;

class OAIRecommendedRulesRequest : public OAIObject {
public:
    OAIRecommendedRulesRequest();
    OAIRecommendedRulesRequest(QString json);
    ~OAIRecommendedRulesRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIMicroSecGroup getGroup1() const;
    void setGroup1(const OAIMicroSecGroup &group_1);
    bool is_group_1_Set() const;
    bool is_group_1_Valid() const;

    OAIMicroSecGroup getGroup2() const;
    void setGroup2(const OAIMicroSecGroup &group_2);
    bool is_group_2_Set() const;
    bool is_group_2_Valid() const;

    OAITimeRange getTimeRange() const;
    void setTimeRange(const OAITimeRange &time_range);
    bool is_time_range_Set() const;
    bool is_time_range_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIMicroSecGroup m_group_1;
    bool m_group_1_isSet;
    bool m_group_1_isValid;

    OAIMicroSecGroup m_group_2;
    bool m_group_2_isSet;
    bool m_group_2_isValid;

    OAITimeRange m_time_range;
    bool m_time_range_isSet;
    bool m_time_range_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRecommendedRulesRequest)

#endif // OAIRecommendedRulesRequest_H
