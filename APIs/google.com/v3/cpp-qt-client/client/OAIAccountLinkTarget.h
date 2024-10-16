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
 * OAIAccountLinkTarget.h
 *
 * Defines whether all properties or a subset of properties in the Hotel Center account can be managed with the linked Google Ads account. If a subset, the specific properties are specified.
 */

#ifndef OAIAccountLinkTarget_H
#define OAIAccountLinkTarget_H

#include <QJsonObject>

#include "OAIHotelList.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIHotelList;

class OAIAccountLinkTarget : public OAIObject {
public:
    OAIAccountLinkTarget();
    OAIAccountLinkTarget(QString json);
    ~OAIAccountLinkTarget() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllHotels() const;
    void setAllHotels(const bool &all_hotels);
    bool is_all_hotels_Set() const;
    bool is_all_hotels_Valid() const;

    OAIHotelList getHotelList() const;
    void setHotelList(const OAIHotelList &hotel_list);
    bool is_hotel_list_Set() const;
    bool is_hotel_list_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_all_hotels;
    bool m_all_hotels_isSet;
    bool m_all_hotels_isValid;

    OAIHotelList m_hotel_list;
    bool m_hotel_list_isSet;
    bool m_hotel_list_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAccountLinkTarget)

#endif // OAIAccountLinkTarget_H
