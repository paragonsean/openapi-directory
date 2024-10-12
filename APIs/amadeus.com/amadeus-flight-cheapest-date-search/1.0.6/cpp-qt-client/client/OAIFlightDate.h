/**
 * Flight Cheapest Date Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 1.0.6
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFlightDate.h
 *
 * 
 */

#ifndef OAIFlightDate_H
#define OAIFlightDate_H

#include <QJsonObject>

#include "OAIFlightDate_links.h"
#include "OAIPrice.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFlightDate_links;
class OAIPrice;

class OAIFlightDate : public OAIObject {
public:
    OAIFlightDate();
    OAIFlightDate(QString json);
    ~OAIFlightDate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDepartureDate() const;
    void setDepartureDate(const QString &departure_date);
    bool is_departure_date_Set() const;
    bool is_departure_date_Valid() const;

    QString getDestination() const;
    void setDestination(const QString &destination);
    bool is_destination_Set() const;
    bool is_destination_Valid() const;

    OAIFlightDate_links getLinks() const;
    void setLinks(const OAIFlightDate_links &links);
    bool is_links_Set() const;
    bool is_links_Valid() const;

    QString getOrigin() const;
    void setOrigin(const QString &origin);
    bool is_origin_Set() const;
    bool is_origin_Valid() const;

    OAIPrice getPrice() const;
    void setPrice(const OAIPrice &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QString getReturnDate() const;
    void setReturnDate(const QString &return_date);
    bool is_return_date_Set() const;
    bool is_return_date_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_departure_date;
    bool m_departure_date_isSet;
    bool m_departure_date_isValid;

    QString m_destination;
    bool m_destination_isSet;
    bool m_destination_isValid;

    OAIFlightDate_links m_links;
    bool m_links_isSet;
    bool m_links_isValid;

    QString m_origin;
    bool m_origin_isSet;
    bool m_origin_isValid;

    OAIPrice m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QString m_return_date;
    bool m_return_date_isSet;
    bool m_return_date_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFlightDate)

#endif // OAIFlightDate_H
