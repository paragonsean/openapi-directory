/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOutputDateInfo.h
 *
 * 
 */

#ifndef OAIOutputDateInfo_H
#define OAIOutputDateInfo_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIOutputDateInfo : public OAIObject {
public:
    OAIOutputDateInfo();
    OAIOutputDateInfo(QString json);
    ~OAIOutputDateInfo() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getDayOfWeek() const;
    void setDayOfWeek(const double &day_of_week);
    bool is_day_of_week_Set() const;
    bool is_day_of_week_Valid() const;

    double getDayOfYear() const;
    void setDayOfYear(const double &day_of_year);
    bool is_day_of_year_Set() const;
    bool is_day_of_year_Valid() const;

    double getMinutesInDay() const;
    void setMinutesInDay(const double &minutes_in_day);
    bool is_minutes_in_day_Set() const;
    bool is_minutes_in_day_Valid() const;

    double getSecondsInDay() const;
    void setSecondsInDay(const double &seconds_in_day);
    bool is_seconds_in_day_Set() const;
    bool is_seconds_in_day_Valid() const;

    double getTicks() const;
    void setTicks(const double &ticks);
    bool is_ticks_Set() const;
    bool is_ticks_Valid() const;

    double getWeekOfYear() const;
    void setWeekOfYear(const double &week_of_year);
    bool is_week_of_year_Set() const;
    bool is_week_of_year_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_day_of_week;
    bool m_day_of_week_isSet;
    bool m_day_of_week_isValid;

    double m_day_of_year;
    bool m_day_of_year_isSet;
    bool m_day_of_year_isValid;

    double m_minutes_in_day;
    bool m_minutes_in_day_isSet;
    bool m_minutes_in_day_isValid;

    double m_seconds_in_day;
    bool m_seconds_in_day_isSet;
    bool m_seconds_in_day_isValid;

    double m_ticks;
    bool m_ticks_isSet;
    bool m_ticks_isValid;

    double m_week_of_year;
    bool m_week_of_year_isSet;
    bool m_week_of_year_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOutputDateInfo)

#endif // OAIOutputDateInfo_H
