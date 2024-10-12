/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFlightClass.h
 *
 * 
 */

#ifndef OAIFlightClass_H
#define OAIFlightClass_H

#include <QJsonObject>

#include "OAIAirportInfo.h"
#include "OAIBoardingAndSeatingPolicy.h"
#include "OAICallbackOptions.h"
#include "OAIClassTemplateInfo.h"
#include "OAIFlightHeader.h"
#include "OAIImage.h"
#include "OAIImageModuleData.h"
#include "OAIInfoModuleData.h"
#include "OAILatLongPoint.h"
#include "OAILinksModuleData.h"
#include "OAILocalizedString.h"
#include "OAIMessage.h"
#include "OAIReview.h"
#include "OAISecurityAnimation.h"
#include "OAITextModuleData.h"
#include "OAIUri.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBoardingAndSeatingPolicy;
class OAICallbackOptions;
class OAIClassTemplateInfo;
class OAIAirportInfo;
class OAIFlightHeader;
class OAIImage;
class OAIUri;
class OAIImageModuleData;
class OAIInfoModuleData;
class OAILinksModuleData;
class OAILocalizedString;
class OAILatLongPoint;
class OAIMessage;
class OAIReview;
class OAISecurityAnimation;
class OAITextModuleData;

class OAIFlightClass : public OAIObject {
public:
    OAIFlightClass();
    OAIFlightClass(QString json);
    ~OAIFlightClass() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllowMultipleUsersPerObject() const;
    void setAllowMultipleUsersPerObject(const bool &allow_multiple_users_per_object);
    bool is_allow_multiple_users_per_object_Set() const;
    bool is_allow_multiple_users_per_object_Valid() const;

    OAIBoardingAndSeatingPolicy getBoardingAndSeatingPolicy() const;
    void setBoardingAndSeatingPolicy(const OAIBoardingAndSeatingPolicy &boarding_and_seating_policy);
    bool is_boarding_and_seating_policy_Set() const;
    bool is_boarding_and_seating_policy_Valid() const;

    OAICallbackOptions getCallbackOptions() const;
    void setCallbackOptions(const OAICallbackOptions &callback_options);
    bool is_callback_options_Set() const;
    bool is_callback_options_Valid() const;

    OAIClassTemplateInfo getClassTemplateInfo() const;
    void setClassTemplateInfo(const OAIClassTemplateInfo &class_template_info);
    bool is_class_template_info_Set() const;
    bool is_class_template_info_Valid() const;

    QString getCountryCode() const;
    void setCountryCode(const QString &country_code);
    bool is_country_code_Set() const;
    bool is_country_code_Valid() const;

    OAIAirportInfo getDestination() const;
    void setDestination(const OAIAirportInfo &destination);
    bool is_destination_Set() const;
    bool is_destination_Valid() const;

    bool isEnableSmartTap() const;
    void setEnableSmartTap(const bool &enable_smart_tap);
    bool is_enable_smart_tap_Set() const;
    bool is_enable_smart_tap_Valid() const;

    OAIFlightHeader getFlightHeader() const;
    void setFlightHeader(const OAIFlightHeader &flight_header);
    bool is_flight_header_Set() const;
    bool is_flight_header_Valid() const;

    QString getFlightStatus() const;
    void setFlightStatus(const QString &flight_status);
    bool is_flight_status_Set() const;
    bool is_flight_status_Valid() const;

    OAIImage getHeroImage() const;
    void setHeroImage(const OAIImage &hero_image);
    bool is_hero_image_Set() const;
    bool is_hero_image_Valid() const;

    QString getHexBackgroundColor() const;
    void setHexBackgroundColor(const QString &hex_background_color);
    bool is_hex_background_color_Set() const;
    bool is_hex_background_color_Valid() const;

    OAIUri getHomepageUri() const;
    void setHomepageUri(const OAIUri &homepage_uri);
    bool is_homepage_uri_Set() const;
    bool is_homepage_uri_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<OAIImageModuleData> getImageModulesData() const;
    void setImageModulesData(const QList<OAIImageModuleData> &image_modules_data);
    bool is_image_modules_data_Set() const;
    bool is_image_modules_data_Valid() const;

    OAIInfoModuleData getInfoModuleData() const;
    void setInfoModuleData(const OAIInfoModuleData &info_module_data);
    bool is_info_module_data_Set() const;
    bool is_info_module_data_Valid() const;

    QString getIssuerName() const;
    void setIssuerName(const QString &issuer_name);
    bool is_issuer_name_Set() const;
    bool is_issuer_name_Valid() const;

    QString getKind() const;
    void setKind(const QString &kind);
    bool is_kind_Set() const;
    bool is_kind_Valid() const;

    QString getLanguageOverride() const;
    void setLanguageOverride(const QString &language_override);
    bool is_language_override_Set() const;
    bool is_language_override_Valid() const;

    OAILinksModuleData getLinksModuleData() const;
    void setLinksModuleData(const OAILinksModuleData &links_module_data);
    bool is_links_module_data_Set() const;
    bool is_links_module_data_Valid() const;

    QString getLocalBoardingDateTime() const;
    void setLocalBoardingDateTime(const QString &local_boarding_date_time);
    bool is_local_boarding_date_time_Set() const;
    bool is_local_boarding_date_time_Valid() const;

    QString getLocalEstimatedOrActualArrivalDateTime() const;
    void setLocalEstimatedOrActualArrivalDateTime(const QString &local_estimated_or_actual_arrival_date_time);
    bool is_local_estimated_or_actual_arrival_date_time_Set() const;
    bool is_local_estimated_or_actual_arrival_date_time_Valid() const;

    QString getLocalEstimatedOrActualDepartureDateTime() const;
    void setLocalEstimatedOrActualDepartureDateTime(const QString &local_estimated_or_actual_departure_date_time);
    bool is_local_estimated_or_actual_departure_date_time_Set() const;
    bool is_local_estimated_or_actual_departure_date_time_Valid() const;

    QString getLocalGateClosingDateTime() const;
    void setLocalGateClosingDateTime(const QString &local_gate_closing_date_time);
    bool is_local_gate_closing_date_time_Set() const;
    bool is_local_gate_closing_date_time_Valid() const;

    QString getLocalScheduledArrivalDateTime() const;
    void setLocalScheduledArrivalDateTime(const QString &local_scheduled_arrival_date_time);
    bool is_local_scheduled_arrival_date_time_Set() const;
    bool is_local_scheduled_arrival_date_time_Valid() const;

    QString getLocalScheduledDepartureDateTime() const;
    void setLocalScheduledDepartureDateTime(const QString &local_scheduled_departure_date_time);
    bool is_local_scheduled_departure_date_time_Set() const;
    bool is_local_scheduled_departure_date_time_Valid() const;

    OAILocalizedString getLocalizedIssuerName() const;
    void setLocalizedIssuerName(const OAILocalizedString &localized_issuer_name);
    bool is_localized_issuer_name_Set() const;
    bool is_localized_issuer_name_Valid() const;

    QList<OAILatLongPoint> getLocations() const;
    void setLocations(const QList<OAILatLongPoint> &locations);
    bool is_locations_Set() const;
    bool is_locations_Valid() const;

    QList<OAIMessage> getMessages() const;
    void setMessages(const QList<OAIMessage> &messages);
    bool is_messages_Set() const;
    bool is_messages_Valid() const;

    QString getMultipleDevicesAndHoldersAllowedStatus() const;
    void setMultipleDevicesAndHoldersAllowedStatus(const QString &multiple_devices_and_holders_allowed_status);
    bool is_multiple_devices_and_holders_allowed_status_Set() const;
    bool is_multiple_devices_and_holders_allowed_status_Valid() const;

    OAIAirportInfo getOrigin() const;
    void setOrigin(const OAIAirportInfo &origin);
    bool is_origin_Set() const;
    bool is_origin_Valid() const;

    QList<QString> getRedemptionIssuers() const;
    void setRedemptionIssuers(const QList<QString> &redemption_issuers);
    bool is_redemption_issuers_Set() const;
    bool is_redemption_issuers_Valid() const;

    OAIReview getReview() const;
    void setReview(const OAIReview &review);
    bool is_review_Set() const;
    bool is_review_Valid() const;

    QString getReviewStatus() const;
    void setReviewStatus(const QString &review_status);
    bool is_review_status_Set() const;
    bool is_review_status_Valid() const;

    OAISecurityAnimation getSecurityAnimation() const;
    void setSecurityAnimation(const OAISecurityAnimation &security_animation);
    bool is_security_animation_Set() const;
    bool is_security_animation_Valid() const;

    QList<OAITextModuleData> getTextModulesData() const;
    void setTextModulesData(const QList<OAITextModuleData> &text_modules_data);
    bool is_text_modules_data_Set() const;
    bool is_text_modules_data_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    QString getViewUnlockRequirement() const;
    void setViewUnlockRequirement(const QString &view_unlock_requirement);
    bool is_view_unlock_requirement_Set() const;
    bool is_view_unlock_requirement_Valid() const;

    OAIImage getWordMark() const;
    void setWordMark(const OAIImage &word_mark);
    bool is_word_mark_Set() const;
    bool is_word_mark_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_allow_multiple_users_per_object;
    bool m_allow_multiple_users_per_object_isSet;
    bool m_allow_multiple_users_per_object_isValid;

    OAIBoardingAndSeatingPolicy m_boarding_and_seating_policy;
    bool m_boarding_and_seating_policy_isSet;
    bool m_boarding_and_seating_policy_isValid;

    OAICallbackOptions m_callback_options;
    bool m_callback_options_isSet;
    bool m_callback_options_isValid;

    OAIClassTemplateInfo m_class_template_info;
    bool m_class_template_info_isSet;
    bool m_class_template_info_isValid;

    QString m_country_code;
    bool m_country_code_isSet;
    bool m_country_code_isValid;

    OAIAirportInfo m_destination;
    bool m_destination_isSet;
    bool m_destination_isValid;

    bool m_enable_smart_tap;
    bool m_enable_smart_tap_isSet;
    bool m_enable_smart_tap_isValid;

    OAIFlightHeader m_flight_header;
    bool m_flight_header_isSet;
    bool m_flight_header_isValid;

    QString m_flight_status;
    bool m_flight_status_isSet;
    bool m_flight_status_isValid;

    OAIImage m_hero_image;
    bool m_hero_image_isSet;
    bool m_hero_image_isValid;

    QString m_hex_background_color;
    bool m_hex_background_color_isSet;
    bool m_hex_background_color_isValid;

    OAIUri m_homepage_uri;
    bool m_homepage_uri_isSet;
    bool m_homepage_uri_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<OAIImageModuleData> m_image_modules_data;
    bool m_image_modules_data_isSet;
    bool m_image_modules_data_isValid;

    OAIInfoModuleData m_info_module_data;
    bool m_info_module_data_isSet;
    bool m_info_module_data_isValid;

    QString m_issuer_name;
    bool m_issuer_name_isSet;
    bool m_issuer_name_isValid;

    QString m_kind;
    bool m_kind_isSet;
    bool m_kind_isValid;

    QString m_language_override;
    bool m_language_override_isSet;
    bool m_language_override_isValid;

    OAILinksModuleData m_links_module_data;
    bool m_links_module_data_isSet;
    bool m_links_module_data_isValid;

    QString m_local_boarding_date_time;
    bool m_local_boarding_date_time_isSet;
    bool m_local_boarding_date_time_isValid;

    QString m_local_estimated_or_actual_arrival_date_time;
    bool m_local_estimated_or_actual_arrival_date_time_isSet;
    bool m_local_estimated_or_actual_arrival_date_time_isValid;

    QString m_local_estimated_or_actual_departure_date_time;
    bool m_local_estimated_or_actual_departure_date_time_isSet;
    bool m_local_estimated_or_actual_departure_date_time_isValid;

    QString m_local_gate_closing_date_time;
    bool m_local_gate_closing_date_time_isSet;
    bool m_local_gate_closing_date_time_isValid;

    QString m_local_scheduled_arrival_date_time;
    bool m_local_scheduled_arrival_date_time_isSet;
    bool m_local_scheduled_arrival_date_time_isValid;

    QString m_local_scheduled_departure_date_time;
    bool m_local_scheduled_departure_date_time_isSet;
    bool m_local_scheduled_departure_date_time_isValid;

    OAILocalizedString m_localized_issuer_name;
    bool m_localized_issuer_name_isSet;
    bool m_localized_issuer_name_isValid;

    QList<OAILatLongPoint> m_locations;
    bool m_locations_isSet;
    bool m_locations_isValid;

    QList<OAIMessage> m_messages;
    bool m_messages_isSet;
    bool m_messages_isValid;

    QString m_multiple_devices_and_holders_allowed_status;
    bool m_multiple_devices_and_holders_allowed_status_isSet;
    bool m_multiple_devices_and_holders_allowed_status_isValid;

    OAIAirportInfo m_origin;
    bool m_origin_isSet;
    bool m_origin_isValid;

    QList<QString> m_redemption_issuers;
    bool m_redemption_issuers_isSet;
    bool m_redemption_issuers_isValid;

    OAIReview m_review;
    bool m_review_isSet;
    bool m_review_isValid;

    QString m_review_status;
    bool m_review_status_isSet;
    bool m_review_status_isValid;

    OAISecurityAnimation m_security_animation;
    bool m_security_animation_isSet;
    bool m_security_animation_isValid;

    QList<OAITextModuleData> m_text_modules_data;
    bool m_text_modules_data_isSet;
    bool m_text_modules_data_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;

    QString m_view_unlock_requirement;
    bool m_view_unlock_requirement_isSet;
    bool m_view_unlock_requirement_isValid;

    OAIImage m_word_mark;
    bool m_word_mark_isSet;
    bool m_word_mark_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFlightClass)

#endif // OAIFlightClass_H
