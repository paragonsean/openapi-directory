/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAutoData.h
 *
 * &#x60;data&#x60; property allows you to specify the data stored in the QR Code.
 */

#ifndef OAIAutoData_H
#define OAIAutoData_H

#include <QJsonObject>

#include "OAIBcc.h"
#include "OAICc.h"
#include "OAICell_Phone.h"
#include "OAIContactData.h"
#include "OAICryptoPaymentData.h"
#include "OAICryptocurrency.h"
#include "OAIEmail.h"
#include "OAIEmailData.h"
#include "OAIFax.h"
#include "OAIGeolocationData.h"
#include "OAIGeolocationUriFormat.h"
#include "OAIHome_Phone.h"
#include "OAIPhoneData.h"
#include "OAIPhoto.h"
#include "OAISMSData.h"
#include "OAITitle.h"
#include "OAITo_1.h"
#include "OAIUrl.h"
#include "OAIVideophone.h"
#include "OAIWiFiData.h"
#include "OAIWiFiSecurity.h"
#include "OAIWork_Phone.h"
#include <QDate>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAutoData : public OAIObject {
public:
    OAIAutoData();
    OAIAutoData(QString json);
    ~OAIAutoData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isHidden() const;
    void setHidden(const bool &hidden);
    bool is_hidden_Set() const;
    bool is_hidden_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    OAIWiFiSecurity getSecurity() const;
    void setSecurity(const OAIWiFiSecurity &security);
    bool is_security_Set() const;
    bool is_security_Valid() const;

    QString getSsid() const;
    void setSsid(const QString &ssid);
    bool is_ssid_Set() const;
    bool is_ssid_Valid() const;

    OAIBcc getBcc() const;
    void setBcc(const OAIBcc &bcc);
    bool is_bcc_Set() const;
    bool is_bcc_Valid() const;

    QString getBody() const;
    void setBody(const QString &body);
    bool is_body_Set() const;
    bool is_body_Valid() const;

    OAICc getCc() const;
    void setCc(const OAICc &cc);
    bool is_cc_Set() const;
    bool is_cc_Valid() const;

    QString getSubject() const;
    void setSubject(const QString &subject);
    bool is_subject_Set() const;
    bool is_subject_Valid() const;

    OAITo_1 getTo() const;
    void setTo(const OAITo_1 &to);
    bool is_to_Set() const;
    bool is_to_Valid() const;

    QDate getBirthday() const;
    void setBirthday(const QDate &birthday);
    bool is_birthday_Set() const;
    bool is_birthday_Valid() const;

    OAICell_Phone getCellPhone() const;
    void setCellPhone(const OAICell_Phone &cell_phone);
    bool is_cell_phone_Set() const;
    bool is_cell_phone_Valid() const;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    OAIEmail getEmail() const;
    void setEmail(const OAIEmail &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getEncoding() const;
    void setEncoding(const QString &encoding);
    bool is_encoding_Set() const;
    bool is_encoding_Valid() const;

    OAIFax getFax() const;
    void setFax(const OAIFax &fax);
    bool is_fax_Set() const;
    bool is_fax_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    OAIHome_Phone getHomePhone() const;
    void setHomePhone(const OAIHome_Phone &home_phone);
    bool is_home_phone_Set() const;
    bool is_home_phone_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    double getLatitude() const;
    void setLatitude(const double &latitude);
    bool is_latitude_Set() const;
    bool is_latitude_Valid() const;

    double getLongitude() const;
    void setLongitude(const double &longitude);
    bool is_longitude_Set() const;
    bool is_longitude_Valid() const;

    QString getMemo() const;
    void setMemo(const QString &memo);
    bool is_memo_Set() const;
    bool is_memo_Valid() const;

    QString getNickname() const;
    void setNickname(const QString &nickname);
    bool is_nickname_Set() const;
    bool is_nickname_Valid() const;

    QString getOrganization() const;
    void setOrganization(const QString &organization);
    bool is_organization_Set() const;
    bool is_organization_Valid() const;

    QString getPhone() const;
    void setPhone(const QString &phone);
    bool is_phone_Set() const;
    bool is_phone_Valid() const;

    OAIPhoto getPhoto() const;
    void setPhoto(const OAIPhoto &photo);
    bool is_photo_Set() const;
    bool is_photo_Valid() const;

    QString getPoBox() const;
    void setPoBox(const QString &po_box);
    bool is_po_box_Set() const;
    bool is_po_box_Valid() const;

    QString getRegion() const;
    void setRegion(const QString &region);
    bool is_region_Set() const;
    bool is_region_Valid() const;

    QDate getRevision() const;
    void setRevision(const QDate &revision);
    bool is_revision_Set() const;
    bool is_revision_Valid() const;

    QString getSource() const;
    void setSource(const QString &source);
    bool is_source_Set() const;
    bool is_source_Valid() const;

    QString getStreet() const;
    void setStreet(const QString &street);
    bool is_street_Set() const;
    bool is_street_Valid() const;

    OAITitle getTitle() const;
    void setTitle(const OAITitle &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    OAIUrl getUrl() const;
    void setUrl(const OAIUrl &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    OAIVideophone getVideophone() const;
    void setVideophone(const OAIVideophone &videophone);
    bool is_videophone_Set() const;
    bool is_videophone_Valid() const;

    OAIWork_Phone getWorkPhone() const;
    void setWorkPhone(const OAIWork_Phone &work_phone);
    bool is_work_phone_Set() const;
    bool is_work_phone_Valid() const;

    QString getZipCode() const;
    void setZipCode(const QString &zip_code);
    bool is_zip_code_Set() const;
    bool is_zip_code_Valid() const;

    QString getHouseNumber() const;
    void setHouseNumber(const QString &house_number);
    bool is_house_number_Set() const;
    bool is_house_number_Valid() const;

    QString getPrefecture() const;
    void setPrefecture(const QString &prefecture);
    bool is_prefecture_Set() const;
    bool is_prefecture_Valid() const;

    QString getReading() const;
    void setReading(const QString &reading);
    bool is_reading_Set() const;
    bool is_reading_Valid() const;

    QString getRoomNumber() const;
    void setRoomNumber(const QString &room_number);
    bool is_room_number_Set() const;
    bool is_room_number_Valid() const;

    QString getAddress() const;
    void setAddress(const QString &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    double getAmount() const;
    void setAmount(const double &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    OAICryptocurrency getCurrency() const;
    void setCurrency(const OAICryptocurrency &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    QString getLabel() const;
    void setLabel(const QString &label);
    bool is_label_Set() const;
    bool is_label_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    OAIGeolocationUriFormat getFormat() const;
    void setFormat(const OAIGeolocationUriFormat &format);
    bool is_format_Set() const;
    bool is_format_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_hidden;
    bool m_hidden_isSet;
    bool m_hidden_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    OAIWiFiSecurity m_security;
    bool m_security_isSet;
    bool m_security_isValid;

    QString m_ssid;
    bool m_ssid_isSet;
    bool m_ssid_isValid;

    OAIBcc m_bcc;
    bool m_bcc_isSet;
    bool m_bcc_isValid;

    QString m_body;
    bool m_body_isSet;
    bool m_body_isValid;

    OAICc m_cc;
    bool m_cc_isSet;
    bool m_cc_isValid;

    QString m_subject;
    bool m_subject_isSet;
    bool m_subject_isValid;

    OAITo_1 m_to;
    bool m_to_isSet;
    bool m_to_isValid;

    QDate m_birthday;
    bool m_birthday_isSet;
    bool m_birthday_isValid;

    OAICell_Phone m_cell_phone;
    bool m_cell_phone_isSet;
    bool m_cell_phone_isValid;

    QString m_city;
    bool m_city_isSet;
    bool m_city_isValid;

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    OAIEmail m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_encoding;
    bool m_encoding_isSet;
    bool m_encoding_isValid;

    OAIFax m_fax;
    bool m_fax_isSet;
    bool m_fax_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    OAIHome_Phone m_home_phone;
    bool m_home_phone_isSet;
    bool m_home_phone_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    double m_latitude;
    bool m_latitude_isSet;
    bool m_latitude_isValid;

    double m_longitude;
    bool m_longitude_isSet;
    bool m_longitude_isValid;

    QString m_memo;
    bool m_memo_isSet;
    bool m_memo_isValid;

    QString m_nickname;
    bool m_nickname_isSet;
    bool m_nickname_isValid;

    QString m_organization;
    bool m_organization_isSet;
    bool m_organization_isValid;

    QString m_phone;
    bool m_phone_isSet;
    bool m_phone_isValid;

    OAIPhoto m_photo;
    bool m_photo_isSet;
    bool m_photo_isValid;

    QString m_po_box;
    bool m_po_box_isSet;
    bool m_po_box_isValid;

    QString m_region;
    bool m_region_isSet;
    bool m_region_isValid;

    QDate m_revision;
    bool m_revision_isSet;
    bool m_revision_isValid;

    QString m_source;
    bool m_source_isSet;
    bool m_source_isValid;

    QString m_street;
    bool m_street_isSet;
    bool m_street_isValid;

    OAITitle m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    OAIUrl m_url;
    bool m_url_isSet;
    bool m_url_isValid;

    OAIVideophone m_videophone;
    bool m_videophone_isSet;
    bool m_videophone_isValid;

    OAIWork_Phone m_work_phone;
    bool m_work_phone_isSet;
    bool m_work_phone_isValid;

    QString m_zip_code;
    bool m_zip_code_isSet;
    bool m_zip_code_isValid;

    QString m_house_number;
    bool m_house_number_isSet;
    bool m_house_number_isValid;

    QString m_prefecture;
    bool m_prefecture_isSet;
    bool m_prefecture_isValid;

    QString m_reading;
    bool m_reading_isSet;
    bool m_reading_isValid;

    QString m_room_number;
    bool m_room_number_isSet;
    bool m_room_number_isValid;

    QString m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    double m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    OAICryptocurrency m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    QString m_label;
    bool m_label_isSet;
    bool m_label_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    OAIGeolocationUriFormat m_format;
    bool m_format_isSet;
    bool m_format_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAutoData)

#endif // OAIAutoData_H
