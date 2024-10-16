/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICrash_details.h
 *
 * 
 */

#ifndef OAICrash_details_H
#define OAICrash_details_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICrash_details : public OAIObject {
public:
    OAICrash_details();
    OAICrash_details(QString json);
    ~OAICrash_details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getAppStartTimestamp() const;
    void setAppStartTimestamp(const QDateTime &app_start_timestamp);
    bool is_app_start_timestamp_Set() const;
    bool is_app_start_timestamp_Valid() const;

    QString getCarrierCountry() const;
    void setCarrierCountry(const QString &carrier_country);
    bool is_carrier_country_Set() const;
    bool is_carrier_country_Valid() const;

    QString getCarrierName() const;
    void setCarrierName(const QString &carrier_name);
    bool is_carrier_name_Set() const;
    bool is_carrier_name_Valid() const;

    QString getLocale() const;
    void setLocale(const QString &locale);
    bool is_locale_Set() const;
    bool is_locale_Valid() const;

    QString getOsBuild() const;
    void setOsBuild(const QString &os_build);
    bool is_os_build_Set() const;
    bool is_os_build_Valid() const;

    bool isRooted() const;
    void setRooted(const bool &rooted);
    bool is_rooted_Set() const;
    bool is_rooted_Valid() const;

    QString getScreenSize() const;
    void setScreenSize(const QString &screen_size);
    bool is_screen_size_Set() const;
    bool is_screen_size_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_app_start_timestamp;
    bool m_app_start_timestamp_isSet;
    bool m_app_start_timestamp_isValid;

    QString m_carrier_country;
    bool m_carrier_country_isSet;
    bool m_carrier_country_isValid;

    QString m_carrier_name;
    bool m_carrier_name_isSet;
    bool m_carrier_name_isValid;

    QString m_locale;
    bool m_locale_isSet;
    bool m_locale_isValid;

    QString m_os_build;
    bool m_os_build_isSet;
    bool m_os_build_isValid;

    bool m_rooted;
    bool m_rooted_isSet;
    bool m_rooted_isValid;

    QString m_screen_size;
    bool m_screen_size_isSet;
    bool m_screen_size_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICrash_details)

#endif // OAICrash_details_H
