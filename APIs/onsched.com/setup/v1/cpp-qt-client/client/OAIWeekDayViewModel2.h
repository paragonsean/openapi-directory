/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWeekDayViewModel2.h
 *
 * 
 */

#ifndef OAIWeekDayViewModel2_H
#define OAIWeekDayViewModel2_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWeekDayViewModel2 : public OAIObject {
public:
    OAIWeekDayViewModel2();
    OAIWeekDayViewModel2(QString json);
    ~OAIWeekDayViewModel2() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDisplayEndTime() const;
    void setDisplayEndTime(const QString &display_end_time);
    bool is_display_end_time_Set() const;
    bool is_display_end_time_Valid() const;

    QString getDisplayStartTime() const;
    void setDisplayStartTime(const QString &display_start_time);
    bool is_display_start_time_Set() const;
    bool is_display_start_time_Valid() const;

    qint32 getEndTime() const;
    void setEndTime(const qint32 &end_time);
    bool is_end_time_Set() const;
    bool is_end_time_Valid() const;

    qint32 getStartTime() const;
    void setStartTime(const qint32 &start_time);
    bool is_start_time_Set() const;
    bool is_start_time_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_display_end_time;
    bool m_display_end_time_isSet;
    bool m_display_end_time_isValid;

    QString m_display_start_time;
    bool m_display_start_time_isSet;
    bool m_display_start_time_isValid;

    qint32 m_end_time;
    bool m_end_time_isSet;
    bool m_end_time_isValid;

    qint32 m_start_time;
    bool m_start_time_isSet;
    bool m_start_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWeekDayViewModel2)

#endif // OAIWeekDayViewModel2_H
