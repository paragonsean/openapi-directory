/**
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppointmentRescheduleModel.h
 *
 * 
 */

#ifndef OAIAppointmentRescheduleModel_H
#define OAIAppointmentRescheduleModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAppointmentRescheduleModel : public OAIObject {
public:
    OAIAppointmentRescheduleModel();
    OAIAppointmentRescheduleModel(QString json);
    ~OAIAppointmentRescheduleModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getEndDateTime() const;
    void setEndDateTime(const QDateTime &end_date_time);
    bool is_end_date_time_Set() const;
    bool is_end_date_time_Valid() const;

    QString getResourceId() const;
    void setResourceId(const QString &resource_id);
    bool is_resource_id_Set() const;
    bool is_resource_id_Valid() const;

    QString getResourceIds() const;
    void setResourceIds(const QString &resource_ids);
    bool is_resource_ids_Set() const;
    bool is_resource_ids_Valid() const;

    QString getServiceId() const;
    void setServiceId(const QString &service_id);
    bool is_service_id_Set() const;
    bool is_service_id_Valid() const;

    QDateTime getStartDateTime() const;
    void setStartDateTime(const QDateTime &start_date_time);
    bool is_start_date_time_Set() const;
    bool is_start_date_time_Valid() const;

    QString getTravelAppointmentId() const;
    void setTravelAppointmentId(const QString &travel_appointment_id);
    bool is_travel_appointment_id_Set() const;
    bool is_travel_appointment_id_Valid() const;

    qint32 getTravelTimeMins() const;
    void setTravelTimeMins(const qint32 &travel_time_mins);
    bool is_travel_time_mins_Set() const;
    bool is_travel_time_mins_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_end_date_time;
    bool m_end_date_time_isSet;
    bool m_end_date_time_isValid;

    QString m_resource_id;
    bool m_resource_id_isSet;
    bool m_resource_id_isValid;

    QString m_resource_ids;
    bool m_resource_ids_isSet;
    bool m_resource_ids_isValid;

    QString m_service_id;
    bool m_service_id_isSet;
    bool m_service_id_isValid;

    QDateTime m_start_date_time;
    bool m_start_date_time_isSet;
    bool m_start_date_time_isValid;

    QString m_travel_appointment_id;
    bool m_travel_appointment_id_isSet;
    bool m_travel_appointment_id_isValid;

    qint32 m_travel_time_mins;
    bool m_travel_time_mins_isSet;
    bool m_travel_time_mins_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppointmentRescheduleModel)

#endif // OAIAppointmentRescheduleModel_H
