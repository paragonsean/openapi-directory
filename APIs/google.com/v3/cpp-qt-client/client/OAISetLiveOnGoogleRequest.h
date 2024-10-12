/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISetLiveOnGoogleRequest.h
 *
 * Request message for HotelService.SetLiveOnGoogle.
 */

#ifndef OAISetLiveOnGoogleRequest_H
#define OAISetLiveOnGoogleRequest_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISetLiveOnGoogleRequest : public OAIObject {
public:
    OAISetLiveOnGoogleRequest();
    OAISetLiveOnGoogleRequest(QString json);
    ~OAISetLiveOnGoogleRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isLiveOnGoogle() const;
    void setLiveOnGoogle(const bool &live_on_google);
    bool is_live_on_google_Set() const;
    bool is_live_on_google_Valid() const;

    QList<QString> getPartnerHotelIds() const;
    void setPartnerHotelIds(const QList<QString> &partner_hotel_ids);
    bool is_partner_hotel_ids_Set() const;
    bool is_partner_hotel_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_live_on_google;
    bool m_live_on_google_isSet;
    bool m_live_on_google_isValid;

    QList<QString> m_partner_hotel_ids;
    bool m_partner_hotel_ids_isSet;
    bool m_partner_hotel_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISetLiveOnGoogleRequest)

#endif // OAISetLiveOnGoogleRequest_H
