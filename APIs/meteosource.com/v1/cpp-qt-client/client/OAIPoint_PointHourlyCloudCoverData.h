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
 * OAIPoint_PointHourlyCloudCoverData.h
 *
 * 
 */

#ifndef OAIPoint_PointHourlyCloudCoverData_H
#define OAIPoint_PointHourlyCloudCoverData_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPoint_PointHourlyCloudCoverData : public OAIObject {
public:
    OAIPoint_PointHourlyCloudCoverData();
    OAIPoint_PointHourlyCloudCoverData(QString json);
    ~OAIPoint_PointHourlyCloudCoverData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getHigh() const;
    void setHigh(const double &high);
    bool is_high_Set() const;
    bool is_high_Valid() const;

    double getLow() const;
    void setLow(const double &low);
    bool is_low_Set() const;
    bool is_low_Valid() const;

    double getMiddle() const;
    void setMiddle(const double &middle);
    bool is_middle_Set() const;
    bool is_middle_Valid() const;

    double getTotal() const;
    void setTotal(const double &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_high;
    bool m_high_isSet;
    bool m_high_isValid;

    double m_low;
    bool m_low_isSet;
    bool m_low_isValid;

    double m_middle;
    bool m_middle_isSet;
    bool m_middle_isValid;

    double m_total;
    bool m_total_isSet;
    bool m_total_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPoint_PointHourlyCloudCoverData)

#endif // OAIPoint_PointHourlyCloudCoverData_H
