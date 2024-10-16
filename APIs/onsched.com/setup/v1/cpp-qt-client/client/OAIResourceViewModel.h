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
 * OAIResourceViewModel.h
 *
 * 
 */

#ifndef OAIResourceViewModel_H
#define OAIResourceViewModel_H

#include <QJsonObject>

#include "OAIAddressViewModel.h"
#include "OAIContactViewModel.h"
#include "OAICustomFieldInputModel.h"
#include "OAIPhoneViewModel.h"
#include "OAIResourceHoursViewModel.h"
#include "OAIResourceOptionsInputModel.h"
#include "OAIResourceServiceViewModel.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddressViewModel;
class OAIResourceHoursViewModel;
class OAIContactViewModel;
class OAICustomFieldInputModel;
class OAIResourceOptionsInputModel;
class OAIPhoneViewModel;
class OAIResourceServiceViewModel;

class OAIResourceViewModel : public OAIObject {
public:
    OAIResourceViewModel();
    OAIResourceViewModel(QString json);
    ~OAIResourceViewModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAddressViewModel getAddress() const;
    void setAddress(const OAIAddressViewModel &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    OAIResourceHoursViewModel getAvailability() const;
    void setAvailability(const OAIResourceHoursViewModel &availability);
    bool is_availability_Set() const;
    bool is_availability_Valid() const;

    QString getBioLink() const;
    void setBioLink(const QString &bio_link);
    bool is_bio_link_Set() const;
    bool is_bio_link_Valid() const;

    qint32 getBookingNotification() const;
    void setBookingNotification(const qint32 &booking_notification);
    bool is_booking_notification_Set() const;
    bool is_booking_notification_Valid() const;

    qint32 getCalendarAvailability() const;
    void setCalendarAvailability(const qint32 &calendar_availability);
    bool is_calendar_availability_Set() const;
    bool is_calendar_availability_Valid() const;

    OAIContactViewModel getContact() const;
    void setContact(const OAIContactViewModel &contact);
    bool is_contact_Set() const;
    bool is_contact_Valid() const;

    OAICustomFieldInputModel getCustomFields() const;
    void setCustomFields(const OAICustomFieldInputModel &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    bool isDeletedStatus() const;
    void setDeletedStatus(const bool &deleted_status);
    bool is_deleted_status_Set() const;
    bool is_deleted_status_Valid() const;

    QDateTime getDeletedTime() const;
    void setDeletedTime(const QDateTime &deleted_time);
    bool is_deleted_time_Set() const;
    bool is_deleted_time_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QDateTime getEffectiveDate() const;
    void setEffectiveDate(const QDateTime &effective_date);
    bool is_effective_date_Set() const;
    bool is_effective_date_Valid() const;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getGender() const;
    void setGender(const QString &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

    QString getGoogleCalendarAuthUrl() const;
    void setGoogleCalendarAuthUrl(const QString &google_calendar_auth_url);
    bool is_google_calendar_auth_url_Set() const;
    bool is_google_calendar_auth_url_Valid() const;

    bool isGoogleCalendarAuthorized() const;
    void setGoogleCalendarAuthorized(const bool &google_calendar_authorized);
    bool is_google_calendar_authorized_Set() const;
    bool is_google_calendar_authorized_Valid() const;

    QString getGoogleCalendarId() const;
    void setGoogleCalendarId(const QString &google_calendar_id);
    bool is_google_calendar_id_Set() const;
    bool is_google_calendar_id_Valid() const;

    qint32 getGroupId() const;
    void setGroupId(const qint32 &group_id);
    bool is_group_id_Set() const;
    bool is_group_id_Valid() const;

    double getHourly() const;
    void setHourly(const double &hourly);
    bool is_hourly_Set() const;
    bool is_hourly_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIgnoreBusinessHours() const;
    void setIgnoreBusinessHours(const bool &ignore_business_hours);
    bool is_ignore_business_hours_Set() const;
    bool is_ignore_business_hours_Valid() const;

    QString getImageUrl() const;
    void setImageUrl(const QString &image_url);
    bool is_image_url_Set() const;
    bool is_image_url_Valid() const;

    QString getLocationId() const;
    void setLocationId(const QString &location_id);
    bool is_location_id_Set() const;
    bool is_location_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getNotificationType() const;
    void setNotificationType(const qint32 &notification_type);
    bool is_notification_type_Set() const;
    bool is_notification_type_Valid() const;

    QString getObject() const;
    void setObject(const QString &object);
    bool is_object_Set() const;
    bool is_object_Valid() const;

    OAIResourceOptionsInputModel getOptions() const;
    void setOptions(const OAIResourceOptionsInputModel &options);
    bool is_options_Set() const;
    bool is_options_Valid() const;

    QString getOutlookCalendarAuthUrl() const;
    void setOutlookCalendarAuthUrl(const QString &outlook_calendar_auth_url);
    bool is_outlook_calendar_auth_url_Set() const;
    bool is_outlook_calendar_auth_url_Valid() const;

    bool isOutlookCalendarAuthorized() const;
    void setOutlookCalendarAuthorized(const bool &outlook_calendar_authorized);
    bool is_outlook_calendar_authorized_Set() const;
    bool is_outlook_calendar_authorized_Valid() const;

    QString getOutlookCalendarId() const;
    void setOutlookCalendarId(const QString &outlook_calendar_id);
    bool is_outlook_calendar_id_Set() const;
    bool is_outlook_calendar_id_Valid() const;

    OAIPhoneViewModel getPhone() const;
    void setPhone(const OAIPhoneViewModel &phone);
    bool is_phone_Set() const;
    bool is_phone_Valid() const;

    bool isRecurringAvailability() const;
    void setRecurringAvailability(const bool &recurring_availability);
    bool is_recurring_availability_Set() const;
    bool is_recurring_availability_Valid() const;

    QList<OAIResourceServiceViewModel> getServices() const;
    void setServices(const QList<OAIResourceServiceViewModel> &services);
    bool is_services_Set() const;
    bool is_services_Valid() const;

    QString getSkypeName() const;
    void setSkypeName(const QString &skype_name);
    bool is_skype_name_Set() const;
    bool is_skype_name_Valid() const;

    qint32 getSortKey() const;
    void setSortKey(const qint32 &sort_key);
    bool is_sort_key_Set() const;
    bool is_sort_key_Valid() const;

    QString getTimezoneIana() const;
    void setTimezoneIana(const QString &timezone_iana);
    bool is_timezone_iana_Set() const;
    bool is_timezone_iana_Valid() const;

    QString getTimezoneId() const;
    void setTimezoneId(const QString &timezone_id);
    bool is_timezone_id_Set() const;
    bool is_timezone_id_Valid() const;

    qint32 getTimezoneOffset() const;
    void setTimezoneOffset(const qint32 &timezone_offset);
    bool is_timezone_offset_Set() const;
    bool is_timezone_offset_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAddressViewModel m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    OAIResourceHoursViewModel m_availability;
    bool m_availability_isSet;
    bool m_availability_isValid;

    QString m_bio_link;
    bool m_bio_link_isSet;
    bool m_bio_link_isValid;

    qint32 m_booking_notification;
    bool m_booking_notification_isSet;
    bool m_booking_notification_isValid;

    qint32 m_calendar_availability;
    bool m_calendar_availability_isSet;
    bool m_calendar_availability_isValid;

    OAIContactViewModel m_contact;
    bool m_contact_isSet;
    bool m_contact_isValid;

    OAICustomFieldInputModel m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    bool m_deleted_status;
    bool m_deleted_status_isSet;
    bool m_deleted_status_isValid;

    QDateTime m_deleted_time;
    bool m_deleted_time_isSet;
    bool m_deleted_time_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QDateTime m_effective_date;
    bool m_effective_date_isSet;
    bool m_effective_date_isValid;

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    QString m_google_calendar_auth_url;
    bool m_google_calendar_auth_url_isSet;
    bool m_google_calendar_auth_url_isValid;

    bool m_google_calendar_authorized;
    bool m_google_calendar_authorized_isSet;
    bool m_google_calendar_authorized_isValid;

    QString m_google_calendar_id;
    bool m_google_calendar_id_isSet;
    bool m_google_calendar_id_isValid;

    qint32 m_group_id;
    bool m_group_id_isSet;
    bool m_group_id_isValid;

    double m_hourly;
    bool m_hourly_isSet;
    bool m_hourly_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_ignore_business_hours;
    bool m_ignore_business_hours_isSet;
    bool m_ignore_business_hours_isValid;

    QString m_image_url;
    bool m_image_url_isSet;
    bool m_image_url_isValid;

    QString m_location_id;
    bool m_location_id_isSet;
    bool m_location_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_notification_type;
    bool m_notification_type_isSet;
    bool m_notification_type_isValid;

    QString m_object;
    bool m_object_isSet;
    bool m_object_isValid;

    OAIResourceOptionsInputModel m_options;
    bool m_options_isSet;
    bool m_options_isValid;

    QString m_outlook_calendar_auth_url;
    bool m_outlook_calendar_auth_url_isSet;
    bool m_outlook_calendar_auth_url_isValid;

    bool m_outlook_calendar_authorized;
    bool m_outlook_calendar_authorized_isSet;
    bool m_outlook_calendar_authorized_isValid;

    QString m_outlook_calendar_id;
    bool m_outlook_calendar_id_isSet;
    bool m_outlook_calendar_id_isValid;

    OAIPhoneViewModel m_phone;
    bool m_phone_isSet;
    bool m_phone_isValid;

    bool m_recurring_availability;
    bool m_recurring_availability_isSet;
    bool m_recurring_availability_isValid;

    QList<OAIResourceServiceViewModel> m_services;
    bool m_services_isSet;
    bool m_services_isValid;

    QString m_skype_name;
    bool m_skype_name_isSet;
    bool m_skype_name_isValid;

    qint32 m_sort_key;
    bool m_sort_key_isSet;
    bool m_sort_key_isValid;

    QString m_timezone_iana;
    bool m_timezone_iana_isSet;
    bool m_timezone_iana_isValid;

    QString m_timezone_id;
    bool m_timezone_id_isSet;
    bool m_timezone_id_isValid;

    qint32 m_timezone_offset;
    bool m_timezone_offset_isSet;
    bool m_timezone_offset_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIResourceViewModel)

#endif // OAIResourceViewModel_H
