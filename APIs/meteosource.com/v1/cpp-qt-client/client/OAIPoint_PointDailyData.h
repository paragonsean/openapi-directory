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
 * OAIPoint_PointDailyData.h
 *
 * 
 */

#ifndef OAIPoint_PointDailyData_H
#define OAIPoint_PointDailyData_H

#include <QJsonObject>

#include "OAIHttpFileElement.h"
#include "OAIPoint_PointDailyAfternoonData.h"
#include "OAIPoint_PointDailyAllDayData.h"
#include "OAIPoint_PointDailyAstroData.h"
#include "OAIPoint_PointDailyEveningData.h"
#include "OAIPoint_PointDailyMorningData.h"
#include "OAIPoint_PointDailyStatsData.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPoint_PointDailyAfternoonData;
class OAIPoint_PointDailyAllDayData;
class OAIPoint_PointDailyAstroData;
class OAIPoint_PointDailyEveningData;
class OAIPoint_PointDailyMorningData;
class OAIPoint_PointDailyStatsData;

class OAIPoint_PointDailyData : public OAIObject {
public:
    OAIPoint_PointDailyData();
    OAIPoint_PointDailyData(QString json);
    ~OAIPoint_PointDailyData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPoint_PointDailyAfternoonData getAfternoon() const;
    void setAfternoon(const OAIPoint_PointDailyAfternoonData &afternoon);
    bool is_afternoon_Set() const;
    bool is_afternoon_Valid() const;

    OAIPoint_PointDailyAllDayData getAllDay() const;
    void setAllDay(const OAIPoint_PointDailyAllDayData &all_day);
    bool is_all_day_Set() const;
    bool is_all_day_Valid() const;

    OAIPoint_PointDailyAstroData getAstro() const;
    void setAstro(const OAIPoint_PointDailyAstroData &astro);
    bool is_astro_Set() const;
    bool is_astro_Valid() const;

    OAIHttpFileElement getDay() const;
    void setDay(const OAIHttpFileElement &day);
    bool is_day_Set() const;
    bool is_day_Valid() const;

    OAIPoint_PointDailyEveningData getEvening() const;
    void setEvening(const OAIPoint_PointDailyEveningData &evening);
    bool is_evening_Set() const;
    bool is_evening_Valid() const;

    qint32 getIcon() const;
    void setIcon(const qint32 &icon);
    bool is_icon_Set() const;
    bool is_icon_Valid() const;

    OAIPoint_PointDailyMorningData getMorning() const;
    void setMorning(const OAIPoint_PointDailyMorningData &morning);
    bool is_morning_Set() const;
    bool is_morning_Valid() const;

    qint32 getPredictability() const;
    void setPredictability(const qint32 &predictability);
    bool is_predictability_Set() const;
    bool is_predictability_Valid() const;

    OAIPoint_PointDailyStatsData getStatistics() const;
    void setStatistics(const OAIPoint_PointDailyStatsData &statistics);
    bool is_statistics_Set() const;
    bool is_statistics_Valid() const;

    QString getSummary() const;
    void setSummary(const QString &summary);
    bool is_summary_Set() const;
    bool is_summary_Valid() const;

    QString getWeather() const;
    void setWeather(const QString &weather);
    bool is_weather_Set() const;
    bool is_weather_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPoint_PointDailyAfternoonData m_afternoon;
    bool m_afternoon_isSet;
    bool m_afternoon_isValid;

    OAIPoint_PointDailyAllDayData m_all_day;
    bool m_all_day_isSet;
    bool m_all_day_isValid;

    OAIPoint_PointDailyAstroData m_astro;
    bool m_astro_isSet;
    bool m_astro_isValid;

    OAIHttpFileElement m_day;
    bool m_day_isSet;
    bool m_day_isValid;

    OAIPoint_PointDailyEveningData m_evening;
    bool m_evening_isSet;
    bool m_evening_isValid;

    qint32 m_icon;
    bool m_icon_isSet;
    bool m_icon_isValid;

    OAIPoint_PointDailyMorningData m_morning;
    bool m_morning_isSet;
    bool m_morning_isValid;

    qint32 m_predictability;
    bool m_predictability_isSet;
    bool m_predictability_isValid;

    OAIPoint_PointDailyStatsData m_statistics;
    bool m_statistics_isSet;
    bool m_statistics_isValid;

    QString m_summary;
    bool m_summary_isSet;
    bool m_summary_isValid;

    QString m_weather;
    bool m_weather_isSet;
    bool m_weather_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPoint_PointDailyData)

#endif // OAIPoint_PointDailyData_H
