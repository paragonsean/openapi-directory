/**
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITimeMachine_PointDailyStatsPrecipitationData.h
 *
 * 
 */

#ifndef OAITimeMachine_PointDailyStatsPrecipitationData_H
#define OAITimeMachine_PointDailyStatsPrecipitationData_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITimeMachine_PointDailyStatsPrecipitationData : public OAIObject {
public:
    OAITimeMachine_PointDailyStatsPrecipitationData();
    OAITimeMachine_PointDailyStatsPrecipitationData(QString json);
    ~OAITimeMachine_PointDailyStatsPrecipitationData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getAvg() const;
    void setAvg(const double &avg);
    bool is_avg_Set() const;
    bool is_avg_Valid() const;

    qint32 getProbability() const;
    void setProbability(const qint32 &probability);
    bool is_probability_Set() const;
    bool is_probability_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_avg;
    bool m_avg_isSet;
    bool m_avg_isValid;

    qint32 m_probability;
    bool m_probability_isSet;
    bool m_probability_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITimeMachine_PointDailyStatsPrecipitationData)

#endif // OAITimeMachine_PointDailyStatsPrecipitationData_H
